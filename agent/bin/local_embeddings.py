"""
Custom Embedding Function for ChromaDB
Uses LM Studio's OpenAI-compatible API for local embeddings
"""

import requests
import os
from typing import Optional

class LMStudioEmbeddings:
    """
    ChromaDB-compatible embedding function using LM Studio.
    
    LM Studio serves an OpenAI-compatible API at http://localhost:1234
    by default. Configure with your preferred model (Nemotron Nano, etc.)
    """
    
    def __init__(
        self,
        api_base: str = "http://localhost:1234/v1",
        model: str = "nomic-embed-text",  # Default, can be overridden
        embedding_dimensions: int = 768  # Adjust based on your model
    ):
        self.api_base = api_base.rstrip('/')
        self.model = model
        self.dimensions = embedding_dimensions
        
    def __call__(self, texts: list[str]) -> list[list[float]]:
        """
        Generate embeddings for a list of texts.
        
        Args:
            texts: List of text strings to embed
            
        Returns:
            List of embedding vectors
        """
        headers = {"Content-Type": "application/json"}
        
        # Prepare request in OpenAI format
        payload = {
            "input": texts,
            "model": self.model
        }
        
        try:
            response = requests.post(
                f"{self.api_base}/embeddings",
                headers=headers,
                json=payload,
                timeout=60
            )
            response.raise_for_status()
            
            result = response.json()
            return [item["embedding"] for item in result["data"]]
            
        except requests.exceptions.ConnectionError:
            raise RuntimeError(
                f"Could not connect to LM Studio at {self.api_base}. "
                "Make sure LM Studio is running with the server enabled."
            )
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"LM Studio API error: {e}")


# Default instance for ChromaDB
def get_embedding_function():
    """Factory function for ChromaDB embedding configuration."""
    return LMStudioEmbeddings()
