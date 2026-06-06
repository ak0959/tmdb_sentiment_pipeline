import re
from typing import Dict, Union

class TextPreprocessor:
    """Production-grade text preprocessing and label engineering pipeline for NLP analytics."""
    
    def __init__(self):
        # Pre-compile regex patterns with explicit string literal quotes
        self.html_pattern = re.compile(r'<[^>]+>')
        self.whitespace_pattern = re.compile(r'\s+')

    def clean_text(self, text: str) -> str:
        """Applies deterministic cleaning steps to raw input text string."""
        if not isinstance(text, str):
            return ""
        
        # Remove HTML tags
        text = self.html_pattern.sub(" ", text)
        
        # Normalize whitespace and strip boundaries
        text = self.whitespace_pattern.sub(" ", text).strip()
        
        return text.lower()

    def map_tmdb_rating_to_3class(self, rating: Union[int, float, None]) -> int:
        """
        Maps a 10-point scale numeric rating to a 3-class system.
        0: Negative (1-4)
        1: Neutral (5-6)
        2: Positive (7-10)
        -1: Missing / Unrated
        """
        if rating is None:
            return -1
        
        try:
            rating_val = float(rating)
            if 1.0 <= rating_val <= 4.0:
                return 0
            elif 5.0 <= rating_val <= 6.0:
                return 1
            elif 7.0 <= rating_val <= 10.0:
                return 2
            else:
                return -1
        except (ValueError, TypeError):
            return -1