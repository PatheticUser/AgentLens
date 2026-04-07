import json
import random
from tavily import TavilyClient

TAVILY_KEYS_PATH = "/home/Rameez/Code/AgentLens/tavily_api_keys.json"

def get_tavily_keys() -> list[str]:
    """Reads keys from the local file."""
    try:
        with open(TAVILY_KEYS_PATH, "r") as f:
            return json.load(f)
    except Exception:
        return []

def search_tavily(query: str) -> str:
    """
    Performs research using Tavily. Rotates keys if one fails or exceeds limits.
    Returns a string of the most relevant search results as context.
    """
    keys = get_tavily_keys()
    if not keys:
        return "No Tavily API keys found for research."

    random.shuffle(keys)  # Starting with a random key for distribution
    
    for key in keys:
        try:
            client = TavilyClient(api_key=key)
            # Fetch up-to-date benchmarks and LLM pricing data
            search_query = f"top 10 best llm models for {query} 2026 benchmarks pricing"
            response = client.search(query=search_query, search_depth="advanced", max_results=10)
            
            # Formatting results as a research context string
            context = []
            for result in response.get('results', []):
                snippet = f"Source: {result.get('url', 'Unknown')}\nContent: {result.get('content', 'No content available.')}\n"
                context.append(snippet)
            
            return "\n".join(context) if context else "No research results found."
            
        except Exception as e:
            # If rate limit or error, try the next key
            # Error checking: usually contains '429' for rate limits
            if "429" in str(e):
                continue
            else:
                # Other types of errors (invalid key, etc.), try next
                continue
                
    return "All research keys exhausted or failed."
