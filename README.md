# NexusScout

**NexusScout** is a premium, terminal-based AI exploration and discovery tool. Built to assist developers and researchers, it bridges the gap between current state-of-the-art models and your specific engineering workflows by conducting live research and synthesizing highly accurate model recommendations.

![NexusScout TUI](https://img.shields.io/badge/Interface-CLI_TUI-bright_cyan?style=for-the-badge&logoColor=white) 
![Ollama Support](https://img.shields.io/badge/Engine-Ollama-bright_green?style=for-the-badge&logo=ollama&logoColor=white)
![Tavily API](https://img.shields.io/badge/Research-Tavily-bright_magenta?style=for-the-badge&logoColor=white)

---

## Features

- **Tavily Research Integration (`tavily_utils.py`)**: Initiates a real-time web scrape to pull SOTA SWEBENCH metrics, price drops, and context window updates before evaluating SOTA agent viability.
- **Local Analytics Synthesis (`agent_core.py`)**: Discards generic ChatGPT responses by strictly utilizing your local privacy-first Ollama LLM to synthesize data into hard, factual outputs.
- **Enforced Model Yield**: For every search, NexusScout is prompt-engineered to guarantee at least **7 diverse model recommendations** (from Frontier models to Open-source self-hostable powerhouses), formatted flawlessly.
- **Premium TUI UI (`theme.py` & `main.py`)**: Uses high-performance rendering from `rich` to provide animated components, dynamic color styling, and exclusive Nerd Font icons in a layout that elegantly supports terminal scrolling output.

---

## Installation & Setup

NexusScout relies on strict dependency management via [`uv`](https://docs.astral.sh/uv/) for maximum startup performance.

### Prerequisites
1. **Ollama**: Needs to be installed and running a high-capability model locally (e.g., `qwen3.5:cloud` or `llama3-70b`).
2. **uv**: Recommended python package manager.
3. **Nerd Font**: You MUST use a [Nerd Font](https://www.nerdfonts.com/) patched font in your terminal for the UI to display icons accurately (e.g., *MesloLGS NF*, *FiraCode Nerd Font*).

### Quickstart

1. **Clone & Enter Repository**
   ```bash
   git clone https://github.com/YourUsername/NexusScout.git
   cd NexusScout
   ```

2. **Add API Keys**
   We utilize automatic key-rotation. Add as many free-tier Tavily keys as you have to ensure uninterrupted research access.
   Edit the file `tavily_api_keys.json`:
   ```json
   [
     "tvly-YourKey1",
     "tvly-YourKey2"
   ]
   ```

3. **Install Dependencies & Run**
   Using `uv`, you don't even have to activate the environment manually:
   ```bash
   uv run python main.py
   ```

---

## Basic Usage

1. Start the tool (`uv run python main.py`).
2. Enter your discovery query, for example: `"Best models for processing multi-step complex system refactoring"`.
3. Wait for the `Synthesizing Deep Research` progress indicator to finish.
4. NexusScout will print a beautiful, scrollable dashboard with 7 curated AI models suitable for your exact use case, alongside a table of your existing local library.

---
*Created by [Rameez]. Proudly open-source.*
