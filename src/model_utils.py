import os
import joblib
import logging
import warnings
from typing import Dict, Any
from transformers import pipeline

# Suppress system/HuggingFace clutter cleanly
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "True"
warnings.filterwarnings("ignore", category=UserWarning, module="huggingface_hub")
logging.getLogger("transformers").setLevel(logging.ERROR)
logging.getLogger("huggingface_hub").setLevel(logging.ERROR)

class ModelInferencePlatform:
    """Unified interface managing classical baselines, legacy binary anchors, and custom local Transformers."""
    
    def __init__(self):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        
        # Paths to local artifacts
        self.baseline_path = os.path.join(base_dir, "models", "baseline_3class.pkl")
        self.transformer_3class_path = os.path.join(base_dir, "models", "transformer_3class")
        
        # Engine anchors
        self.baseline_model = None
        self.legacy_hf_pipeline = None
        self.transformer_3class_pipeline = None
        
        # Remote repository address for Engine 2
        self.legacy_repo = "amitkadia79/movie-sentiment-distilbert"

    def load_baseline_engine(self) -> bool:
        """Loads the local serialized classical machine learning pipeline."""
        if not os.path.exists(self.baseline_path):
            return False
        try:
            self.baseline_model = joblib.load(self.baseline_path)
            return True
        except Exception:
            return False

    def load_legacy_hf_engine(self) -> bool:
        """Pulls and instantiates your fine-tuned binary model directly from Hugging Face."""
        try:
            self.legacy_hf_pipeline = pipeline(
                "sentiment-analysis", 
                model=self.legacy_repo,
                tokenizer=self.legacy_repo,
                token=False
            )
            return True
        except Exception:
            return False

    def load_transformer_3class_engine(self) -> bool:
        """Loads the newly fine-tuned custom 3-class transformer from local artifacts folder."""
        if not os.path.exists(self.transformer_3class_path):
            return False
        try:
            self.transformer_3class_pipeline = pipeline(
                "sentiment-analysis",
                model=self.transformer_3class_path,
                tokenizer=self.transformer_3class_path
            )
            return True
        except Exception:
            return False

    def predict_baseline(self, clean_text: str) -> Dict[str, Any]:
        """Runs inference via Engine 1 (3-Class Baseline)."""
        if not self.baseline_model:
            raise RuntimeError("Engine 1 is not loaded.")
        
        label_map = {0: "Negative", 1: "Neutral", 2: "Positive"}
        pred_class = int(self.baseline_model.predict([clean_text])[0])
        probabilities = self.baseline_model.predict_proba([clean_text])[0]
        
        return {
            "engine": "Engine 1 (Traditional Baseline)",
            "label": label_map[pred_class],
            "confidence": float(probabilities[pred_class])
        }

    def predict_legacy_hf(self, clean_text: str) -> Dict[str, Any]:
        """Runs inference via Engine 2 (Binary Legacy Anchor)."""
        if not self.legacy_hf_pipeline:
            raise RuntimeError("Engine 2 is not loaded.")
        
        result = self.legacy_hf_pipeline(clean_text[:512])[0]
        return {
            "engine": "Engine 2 (Binary Legacy Anchor)",
            "label": result["label"],
            "confidence": float(result["score"])
        }

    def predict_transformer_3class(self, clean_text: str) -> Dict[str, Any]:
        """Runs inference via Engine 3 (Our Custom Fine-Tuned 3-Class Transformer)."""
        if not self.transformer_3class_pipeline:
            raise RuntimeError("Engine 3 is not loaded.")
        
        result = self.transformer_3class_pipeline(clean_text[:512])[0]
        
        # Native Hugging Face output tags to clean string targets
        tag_map = {"LABEL_0": "Negative", "LABEL_1": "Neutral", "LABEL_2": "Positive"}
        resolved_label = tag_map.get(result["label"], "Unknown")
        
        return {
            "engine": "Engine 3 (3-Class Fine-Tuned DistilBERT)",
            "label": resolved_label,
            "confidence": float(result["score"])
        }