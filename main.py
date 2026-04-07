import time
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich import box
from rich.prompt import Prompt
from rich.align import Align
from rich.style import Style

from config import APP_TITLE, APP_TAGLINE, APP_DESCRIPTION
from ollama_utils import get_local_models, get_ollama_status
from agent_core import get_agentic_models_from_cloud

console = Console()

def print_header():
    title_text = Text(f"󰚩 {APP_TITLE}", style="bold bright_cyan", justify="center")
    title_text.append(f"\n{APP_TAGLINE}", style="italic dim white")
    
    panel = Panel(
        title_text,
        border_style="bright_blue",
        box=box.DOUBLE_EDGE,
        padding=(1, 4)
    )
    console.print(Align.center(panel))
    
def print_welcome():
    console.print(f"\n[white]{APP_DESCRIPTION}[/]\n", justify="center")
    console.print("[dim white]Enter an agentic topic to initiate deep model research.[/]", justify="center")
    console.print("[italic bright_magenta]Example:[/] [italic cyan]'I need a coding agent'[/] [dim]or[/] [italic cyan]'Customer support system'[/]\n", justify="center")

def run_cli():
    console.clear()
    print_header()
    print_welcome()
    
    while True:
        try:
            query = Prompt.ask("\n[bold bright_green]󰭻 Search Query[/] [dim](or 'q' to quit)[/]")
        except (EOFError, KeyboardInterrupt):
            break
            
        if query.lower() == 'q':
            break
            
        if not query.strip():
            continue

        # Animated Status Banner
        with console.status("[bold bright_cyan]󰛓 Synthesizing Deep Research (Tavily + Ollama)...[/]", spinner="bouncingBar", spinner_style="bright_magenta"):
            cloud_results = get_agentic_models_from_cloud(query)
            local_models = get_local_models()
            
        console.print(f"\n[bold bright_magenta]󰅟 Agentic Discoveries for:[/] [bold white]{query}[/]")
        console.print("[dim bright_blue]" + "━" * 80 + "[/]")

        if not cloud_results:
            console.print("[bright_red]No discoveries found. Try a broader query.[/]\n")
        else:
            for i, model in enumerate(cloud_results, 1):
                # We use alternating accents based on odd/even to make scanning models easier
                accent = "bright_cyan" if i % 2 != 0 else "bright_blue"
                
                card = Text()
                card.append(f"󰚩 {model.get('Model Name', 'Unknown')}\n", style=f"bold {accent}")
                card.append(f"{model.get('Description', 'N/A')}\n\n", style="white")
                
                card.append(f"󱜚 Params:   ", style=f"bold {accent}")
                card.append(f"{model.get('Parameters', 'N/A')}\n", style="white")
                
                card.append(f"󰈙 Features: ", style=f"bold {accent}")
                card.append(f"{model.get('Key Features', 'N/A')}\n", style="white")
                
                card.append(f"󱔁 Tooling:  ", style=f"bold {accent}")
                card.append(f"{model.get('Tool/Function Calling', 'N/A')}", style="white")
                
                console.print(Panel(card, border_style=accent, box=box.ROUNDED, padding=(1, 2)))
                
        # Local library table
        console.print("\n[bold bright_green]󰗀 Connected Ollama Model Library[/]")
        table = Table(box=box.ROUNDED, show_header=True, header_style="bold bright_green", border_style="dim green")
        table.add_column("Model Artifact", style="bold white")
        table.add_column("Params", justify="center", style="bright_yellow")
        table.add_column("Deployment Tier", justify="center")
        
        if not local_models:
            table.add_row("[dim white]No local models found[/]", "-", "-")
        else:
            for model in local_models[:10]:
                name = model['Model Name']
                is_cloud_tier = ":cloud" in name.lower()
                tier = "[bold bright_cyan]󰐊 Cloud SOTA[/]" if is_cloud_tier else "[dim white]󰄬 Standard[/]"
                table.add_row(name, model['Parameters'], tier)
                
        console.print(table)
        console.print("[dim]" + "─" * 80 + "[/]")

    console.print("\n[bold bright_magenta]󰩈 Exiting AgentLens. Goodbye![/]")

def main():
    run_cli()

if __name__ == "__main__":
    main()
