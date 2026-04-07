import json
import ollama
from pydantic import BaseModel, Field
from config import OLLAMA_HOST
from tavily_utils import search_tavily
from rich.console import Console

console = Console()

class ModelInfo(BaseModel):
    model_name: str = Field(description="Official name and version")
    description: str = Field(description="Summary of strengths for this specific task")
    parameters: str = Field(description="Size in billions (e.g., 8B, 70B, etc. or N/A)")
    key_features: str = Field(description="Key strengths, benchmarks, or reasoning capabilities")
    tool_calling: str = Field(description="Support for parallel tool or function execution")

class ModelsResponse(BaseModel):
    models: list[ModelInfo]

def get_agentic_models_from_cloud(query: str) -> list[dict]:
    """
    Performs deep research using Tavily, then compiles a top model recommendation list
    using the best local Ollama engine (e.g., qwen3.5:cloud).
    """
    # 1. Start Web Research
    research_context = search_tavily(query)

    # 2. Compile system prompt with research data
    system_prompt = (
        "You are 'AgentLens', a Senior AI Research & Discovery Engineer. "
        "Your task is to perform an exhaustive evaluation of models for the user's specific query. "
        "Use the provided Research Context for latest benchmarks and pricing. "
        "CRITICAL REQUIREMENT: You MUST recommend EXACTLY 7 distinct models. NOT 1, NOT 3, but EXACTLY 7. "
        "Provide a diverse range: include at least 2 frontier models, 3 open-source models, and 2 task-specific niche models. "
        "\n\n--- RESEARCH CONTEXT ---\n"
        f"{research_context}\n"
        "--- END RESEARCH CONTEXT ---\n\n"
        "Output MUST be a raw JSON object matching this schema exactly. "
        "Your JSON MUST contain exactly 7 items in the 'models' array:\n"
        "{\n"
        "  'models': [\n"
        "    { 'model_name': '...', 'description': '...', 'parameters': '...', 'key_features': '...', 'tool_calling': '...' },\n"
        "    { 'model_name': '...', 'description': '...', 'parameters': '...', 'key_features': '...', 'tool_calling': '...' },\n"
        "    { 'model_name': '...', 'description': '...', 'parameters': '...', 'key_features': '...', 'tool_calling': '...' },\n"
        "    { 'model_name': '...', 'description': '...', 'parameters': '...', 'key_features': '...', 'tool_calling': '...' },\n"
        "    { 'model_name': '...', 'description': '...', 'parameters': '...', 'key_features': '...', 'tool_calling': '...' },\n"
        "    { 'model_name': '...', 'description': '...', 'parameters': '...', 'key_features': '...', 'tool_calling': '...' },\n"
        "    { 'model_name': '...', 'description': '...', 'parameters': '...', 'key_features': '...', 'tool_calling': '...' }\n"
        "  ]\n"
        "}"
    )

    # 3. Choose Local Discovery Engine
    try:
        client = ollama.Client(host=OLLAMA_HOST)
        models_list = client.list()
        available_models = models_list.get('models', []) if isinstance(models_list, dict) else models_list.models
        
        # Engine choice strategy
        engine_options = ["qwen3.5:cloud", "deepseek-v3.1:671b-cloud", "nemotron-3-super:cloud"]
        engine_model = available_models[0].model if not isinstance(available_models[0], dict) else available_models[0]['name']
        for opt in engine_options:
            if any((m.model == opt if not isinstance(m, dict) else m['name'] == opt) for m in available_models):
                engine_model = opt
                break

        response = client.chat(
            model=engine_model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Discover top 7 models for: {query}"}
            ],
            format="json"
        )
        
        raw_content = response['message']['content']
        data = json.loads(raw_content)
        
        # Format the result list for UI component
        results = []
        for m in data.get("models", []):
            results.append({
                "Model Name": m.get("model_name", "Unknown"),
                "Description": m.get("description", "Not provided"),
                "Parameters": m.get("parameters", "N/A"),
                "Key Features": m.get("key_features", "N/A"),
                "Tool/Function Calling": m.get("tool_calling", "N/A")
            })
        return results

    except Exception as e:
        return [{
            "Model Name": "Discovery Error",
            "Description": f"Failed to perform research discovery: {str(e)}",
            "Parameters": "!",
            "Key Features": "!",
            "Tool/Function Calling": "!"
        }]
