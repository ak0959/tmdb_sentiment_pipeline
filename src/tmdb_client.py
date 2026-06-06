import os
import aiohttp
import asyncio
from typing import Dict, List, Optional
from dotenv import load_dotenv

class TMDBClient:
    """Production-grade asynchronous client for interacting with the TMDb API."""
    
    def __init__(self):
        # Locate the .env file relative to this source file if running from root
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        load_dotenv(os.path.join(base_dir, ".env"))
        
        self.api_key = os.getenv("TMDB_API_KEY")
        # Maintain api.tmdb.org to ensure ISP block bypass
        self.base_url = "https://api.tmdb.org/3"
        
        if not self.api_key:
            raise ValueError("Initialization Failed: TMDB_API_KEY is missing from environment.")

    def _get_default_params(self) -> Dict[str, str]:
        return {"api_key": self.api_key, "language": "en-US"}

    async def search_movie(self, query: str) -> List[Dict]:
        """Searches for a movie by its title string and returns candidate matches."""
        url = f"{self.base_url}/search/movie"
        params = self._get_default_params()
        params["query"] = query
        
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(url, params=params, timeout=5) as response:
                    if response.status == 200:
                        data = await response.json()
                        return data.get("results", [])
                    return []
            except Exception:
                return []

    async def get_movie_metadata(self, movie_id: int) -> Optional[Dict]:
        """Fetches and builds core metadata, crew, and cast in a single parallel operation."""
        params = self._get_default_params()
        
        async with aiohttp.ClientSession() as session:
            details_task = session.get(f"{self.base_url}/movie/{movie_id}", params=params, timeout=5)
            credits_task = session.get(f"{self.base_url}/movie/{movie_id}/credits", params=params, timeout=5)
            
            responses = await asyncio.gather(details_task, credits_task, return_exceptions=True)
            
            # Handle details response
            if isinstance(responses[0], Exception) or responses[0].status != 200:
                return None
            details_data = await responses[0].json()
            
            # Handle credits response
            credits_data = {}
            if not isinstance(responses[1], Exception) and responses[1].status == 200:
                credits_data = await responses[1].json()
                
            # Parse Cast (Top 4 billed)
            cast_list = credits_data.get("cast", [])
            top_4_actors = [actor.get("name") for actor in cast_list[:4]]
            
            # Parse Crew (Director and DP)
            crew_list = credits_data.get("crew", [])
            director = None
            cinematographer = None
            for member in crew_list:
                job = member.get("job")
                if job == "Director":
                    director = member.get("name")
                elif job in ["Director of Photography", "Cinematographer"]:
                    cinematographer = member.get("name")
            
            poster_path = details_data.get("poster_path")
            
            return {
                "id": movie_id,
                "title": details_data.get("title"),
                "release_date": details_data.get("release_date"),
                "overview": details_data.get("overview"),
                "poster_url": f"https://image.tmdb.org/t/p/w500{poster_path}" if poster_path else None,
                "director": director,
                "cinematographer": cinematographer,
                "cast": top_4_actors
            }

    async def get_movie_reviews(self, movie_id: int, page: int = 1) -> List[Dict]:
        """Streams and extracts review objects from the movie reviews endpoint."""
        url = f"{self.base_url}/movie/{movie_id}/reviews"
        params = self._get_default_params()
        params["page"] = str(page)
        
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(url, params=params, timeout=5) as response:
                    if response.status == 200:
                        data = await response.json()
                        cleaned_reviews = []
                        for item in data.get("results", []):
                            cleaned_reviews.append({
                                "author": item.get("author"),
                                "content": item.get("content"),
                                "rating": item.get("author_details", {}).get("rating")
                            })
                        return cleaned_reviews
                    return []
            except Exception:
                return []