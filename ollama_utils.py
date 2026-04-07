import ollama
from rich.console import Console
from config import OLLAMA_HOST

console = Console()

def get_local_models() -> list[dict]:
    """
    Fetches the list of locally available models from the Ollama API.
    Handles different library versions and missing metadata.
    """
    try:
        client = ollama.Client(host=OLLAMA_HOST)
        response = client.list()
        
        # Handle both dict and object responses
        models_raw = response.get("models", []) if isinstance(response, dict) else response.models
        
        models = []
        for model in models_raw:
            # Handle both dict and object models
            name = model.get("name", "Unknown") if isinstance(model, dict) else model.model
            details = model.get("details", {}) if isinstance(model, dict) else model.details
            
            # Use getattr for object-based details
            if hasattr(details, "__dict__") or not isinstance(details, dict):
                p_size = getattr(details, 'parameter_size', "N/A")
                family = getattr(details, 'family', "N/A")
                quant = getattr(details, 'quantization_level', "N/A")
                fmt = getattr(details, 'format', "N/A")
            else:
                p_size = details.get("parameter_size", "N/A")
                family = details.get("family", "N/A")
                quant = details.get("quantization_level", "N/A")
                fmt = details.get("format", "N/A")

            models.append({
                "Model Name": name,
                "Description": f"Local model ({fmt}). served via Ollama.",
                "Parameters": p_size or "Unknown",
                "Key Features": f"Architecture: {family}, Quantization: {quant}",
                "Tool/Function Calling": "Determined by architecture"
            })
        return models
    except Exception as e:
        return []

def is_ollama_running() -> bool:
    """
    Checks if the Ollama service is running and accessible.
    """
    try:
        client = ollama.Client(host=OLLAMA_HOST)
        client.list()
        return True
    except Exception:
        return False

def get_ollama_status() -> tuple[bool, str]:
    """Returns connectivity status and a nice string with an icon."""
    if is_ollama_running():
        return True, "[bold green]●[/] [green]Ollama Connected[/]"
    return False, "[bold red]○[/] [red]Ollama Offline[/]"
