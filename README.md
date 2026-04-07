# 󰭻 AgentLens

**AI-Powered LLM Discovery Assistant for Agentic AI Workflows**

AgentLens is a terminal-based (TUI) discovery tool for Large Language Models. It specifically evaluates models for autonomous agent architectures, focusing on reasoning, multi-step planning, and tool-calling capabilities.

## 󰀦 Key Features

- **󰅟 Cloud Discovery:** Uses OpenAI's Responses API (with structured outputs) to fetch real-time model recommendations.
- **󰗀 Local Benchmarks:** Integrates with **Ollama** to verify local capabilities and compare them with cloud SOTA.
- **󰐋 Dynamic TUI:** built with `rich`, featuring Nerd Font icons, a live dashboard, and card-based model breakdowns.
- **󰈙 Model Comparison:** Side-by-side analysis of parameters, key features, and native tool-calling support.

## 󱐥 Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Rameez/AgentLens.git
    cd AgentLens
    ```

2.  **Install dependencies using `uv`:**
    ```bash
    uv sync
    ```

3.  **Configure environment:** Create a `.env` file with your OpenAI API key:
    ```
    OPENAI_API_KEY=sk-...
    OLLAMA_HOST=http://localhost:11434
    ```

## 󰀄 Usage

Run the TUI application directly:
```bash
uv run python main.py
```

## 󱔁 Tech Stack

- **Core Logic:** Python 3.10+
- **Package Management:** [uv](https://github.com/astral-sh/uv)
- **TUI Framework:** [rich](https://github.com/Textualize/rich)
- **Cloud Models:** OpenAI gpt-4o (structured outputs)
- **Local Models:** Ollama API
- **Data Handling:** Pandas & Pydantic
