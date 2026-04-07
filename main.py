"""
AgentLens - AI-Powered LLM Discovery Assistant
Enhanced TUI with Rich and Nerd Fonts
"""

import time
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich import box
from rich.prompt import Prompt
from rich.align import Align
from rich.layout import Layout
from rich.columns import Columns
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn
from rich.live import Live
from rich.rule import Rule

from theme import (
    Colors, Icons, Styles, Messages, LOGO, LOGO_MINI,
    get_accent_color, make_gradient_bar, console
)
from config import APP_TITLE, APP_TAGLINE, APP_DESCRIPTION
from ollama_utils import get_local_models, get_ollama_status
from agent_core import get_agentic_models_from_cloud


# ═══════════════════════════════════════════════════════════════════════════════
# HEADER & BANNER COMPONENTS
# ═══════════════════════════════════════════════════════════════════════════════

def create_header() -> Panel:
    """Create an elegant header panel with logo and branding."""
    header_content = Text(justify="center")
    header_content.append(f"{Icons.APP} ", style="bold bright_cyan")
    header_content.append(f"{APP_TITLE}\n", style="bold bright_white")
    header_content.append(f"{APP_TAGLINE}", style="italic dim white")

    return Panel(
        header_content,
        border_style="bright_cyan",
        box=box.HEAVY_EDGE,
        padding=(1, 4),
        title=f"[bold bright_magenta]{Icons.SPARKLE} AI Model Discovery {Icons.SPARKLE}[/]",
        title_align="c"
    )


def create_status_bar() -> Panel:
    """Create a status bar showing connection status."""
    ollama_ok, ollama_status = get_ollama_status()

    status_line = Text()
    status_line.append(f"{Icons.CONNECTED} ", style="bright_cyan")
    status_line.append("Status: ", style="dim white")

    if ollama_ok:
        status_line.append(f"{Icons.ONLINE} ", style="bright_green")
        status_line.append("Ollama Connected", style="bold bright_green")
    else:
        status_line.append(f"{Icons.OFFLINE} ", style="bright_red")
        status_line.append("Ollama Offline", style="bold bright_red")

    return Panel(
        status_line,
        border_style="bright_green" if ollama_ok else "bright_red",
        box=box.ROUNDED,
        padding=(0, 2)
    )


def create_help_panel() -> Panel:
    """Create a help panel showing keyboard shortcuts."""
    shortcuts = Text()
    shortcuts.append(f"  {Icons.ENTER} ", style="bright_cyan")
    shortcuts.append("Enter    ", style="bold white")
    shortcuts.append("Submit query\n", style="dim white")

    shortcuts.append(f"  {Icons.QUIT} ", style="bright_cyan")
    shortcuts.append("q/Q      ", style="bold white")
    shortcuts.append("Quit application\n", style="dim white")

    shortcuts.append(f"  {Icons.BOOK} ", style="bright_cyan")
    shortcuts.append("h/H      ", style="bold white")
    shortcuts.append("Show this help\n", style="dim white")

    shortcuts.append(f"  {Icons.QUIT} ", style="bright_cyan")
    shortcuts.append("Ctrl+C   ", style="bold white")
    shortcuts.append("Force exit", style="dim white")

    return Panel(
        shortcuts,
        title=f"[bold bright_magenta]{Icons.BOOK} Quick Commands[/]",
        border_style="bright_magenta",
        box=box.ROUNDED,
        padding=(1, 2)
    )


def create_welcome_banner():
    """Display welcome message with instructions."""
    console.print()
    console.print(Align.center(
        Panel(
            f"[white]{APP_DESCRIPTION}[/]\n\n"
            f"[dim]{Messages.WELCOME}[/]\n\n"
            f"{Messages.EXAMPLE}",
            border_style="dim cyan",
            box=box.ROUNDED,
            padding=(1, 3),
            title=f"[bold cyan]{Icons.LIGHTBULB} Getting Started[/]"
        )
    ))


# ═══════════════════════════════════════════════════════════════════════════════
# MODEL DISPLAY COMPONENTS
# ═══════════════════════════════════════════════════════════════════════════════

def create_model_card(model: dict, index: int) -> Panel:
    """Create a visually appealing model information card."""
    accent_bright, accent_dim = get_accent_color(index)
    icon = Icons.MODEL if index % 2 == 0 else Icons.ROBOT

    content = Text()

    # Title with icon
    content.append(f"{icon} ", style=f"bold {accent_bright}")
    content.append(f"{model.get('Model Name', 'Unknown')}\n", style=f"bold {accent_bright}")

    # Description
    content.append(f"{model.get('Description', 'N/A')}\n\n", style="white")

    # Parameters
    content.append(f"{Icons.PARAMS} ", style=f"{accent_bright}")
    content.append("Parameters: ", style=f"bold {accent_dim}")
    content.append(f"{model.get('Parameters', 'N/A')}\n", style="white")

    # Features
    content.append(f"{Icons.FEATURES} ", style=f"{accent_bright}")
    content.append("Features:   ", style=f"bold {accent_dim}")
    content.append(f"{model.get('Key Features', 'N/A')}\n", style="white")

    # Tool Calling
    tool_calling = model.get('Tool/Function Calling', 'N/A')
    tool_icon = Icons.TOOLS if "yes" in tool_calling.lower() or "supports" in tool_calling.lower() else Icons.WARNING
    content.append(f"{tool_icon} ", style=f"{accent_bright}")
    content.append("Tooling:    ", style=f"bold {accent_dim}")
    content.append(f"{tool_calling}", style="white")

    return Panel(
        content,
        border_style=accent_bright,
        box=box.ROUNDED,
        padding=(1, 2),
        title=f"[dim]{Icons.SPARKLE}[/] [bold white]Result #{index}[/] [dim]{Icons.SPARKLE}[/]",
        title_align="l"
    )


def create_models_table(models: list[dict]) -> Table:
    """Create a styled table for local models."""
    table = Table(
        box=box.HEAVY_HEAD,
        show_header=True,
        header_style="bold bright_green",
        border_style="bright_green",
        row_styles=["white", "dim white"],
        title=f"\n{Icons.LOCAL} Local Model Library",
        title_style="bold bright_green"
    )

    table.add_column(
        f"{Icons.MODEL} Model Artifact",
        style="bold white",
        no_wrap=True
    )
    table.add_column(
        f"{Icons.SIZE} Parameters",
        justify="center",
        style="bright_yellow"
    )
    table.add_column(
        f"{Icons.CLOUD} Deployment Tier",
        justify="center"
    )

    if not models:
        table.add_row(
            f"[dim]{Icons.WARNING} No local models found[/]",
            "[dim]--[/]",
            "[dim]--[/]"
        )
    else:
        for model in models[:10]:
            name = model['Model Name']
            params = model['Parameters']

            # Determine tier with visual indicator
            if ":cloud" in name.lower():
                tier = f"[bold bright_cyan]{Icons.CLOUD} Cloud SOTA[/]"
            elif any(x in name.lower() for x in ["7b", "8b", "9b"]):
                tier = f"[bold bright_green]{Icons.SPEED} Edge Ready[/]"
            else:
                tier = f"[dim white]{Icons.LOCAL} Standard[/]"

            table.add_row(name, params, tier)

    return table


# ═══════════════════════════════════════════════════════════════════════════════
# ANIMATION & LOADING COMPONENTS
# ═══════════════════════════════════════════════════════════════════════════════

def show_loading_animation():
    """Display an animated loading state with progress indicators."""
    spinner_frames = [
        f"{Icons.SYNC} ",
        f"{Icons.LOADING} ",
        f"{Icons.NEURAL} ",
        f"{Icons.CPU} ",
    ]

    tasks = [
        ("Querying Tavily Search API...", "bright_cyan"),
        ("Analyzing model capabilities...", "bright_blue"),
        ("Fetching local Ollama models...", "bright_magenta"),
        ("Synthesizing recommendations...", "bright_green"),
    ]

    with Progress(
        SpinnerColumn("bouncingBar", style="bright_magenta"),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(bar_width=40, style="bright_cyan", complete_style="bright_green"),
        console=console,
        transient=True
    ) as progress:
        task_ids = []
        for desc, color in tasks:
            task_id = progress.add_task(f"[{color}]{desc}[/]", total=100)
            task_ids.append(task_id)

        # Simulate progress for visual effect
        for i, task_id in enumerate(task_ids):
            for _ in range(10):
                progress.advance(task_id, 10)
                time.sleep(0.05)


# ═══════════════════════════════════════════════════════════════════════════════
# MAIN CLI INTERFACE
# ═══════════════════════════════════════════════════════════════════════════════

def print_header():
    """Print the main header with logo."""
    console.print()
    console.print(Align.center(create_header()))


def print_status_bar():
    """Print the status bar."""
    console.print(Align.center(create_status_bar()))


def print_help():
    """Display the help panel."""
    console.clear()
    print_header()
    console.print()
    console.print(Align.center(create_help_panel()))
    console.print()
    console.print(Align.center("[dim]Press Enter to continue...[/]"))
    Prompt.ask("", default="")


def run_cli():
    """Main CLI loop with enhanced TUI."""
    console.clear()

    # Initial header
    print_header()
    print_status_bar()
    create_welcome_banner()

    # Keyboard shortcuts hint
    console.print(Align.center(
        f"[dim]{Icons.CHEVRON} Press 'h' for help, 'q' to quit[/]"
    ))

    while True:
        try:
            console.print()
            prompt_text = f"{Icons.SEARCH} [bold bright_green]Search Query[/] [dim](or 'q' to quit, 'h' for help)[/]"
            query = Prompt.ask(f"\n{prompt_text}")
        except (EOFError, KeyboardInterrupt):
            console.print()
            break

        query = query.strip().lower()

        # Handle special commands
        if query == 'q':
            break
        if query == 'h':
            print_help()
            console.clear()
            print_header()
            print_status_bar()
            create_welcome_banner()
            continue
        if not query:
            continue

        # Loading animation
        console.print()
        with console.status(
            f"[bold bright_magenta]{Icons.SYNC}  Synthesizing Deep Research (Tavily + Ollama)...[/]",
            spinner="bouncingBar",
            spinner_style="bright_magenta"
        ):
            cloud_results = get_agentic_models_from_cloud(query)
            local_models = get_local_models()

        # Results section header
        console.print()
        console.print(Rule(
            f"[bold bright_magenta]{Icons.GEM}  Agentic Discoveries for: [bold white]{query}[/]",
            style="bright_magenta"
        ))

        if not cloud_results:
            console.print()
            console.print(Align.center(
                Panel(
                    f"[dim]{Icons.WARNING}[/] [yellow]No discoveries found.\n\nTry a broader query or different keywords.[/]",
                    border_style="yellow",
                    box=box.ROUNDED,
                    padding=(1, 3)
                )
            ))
        else:
            # Display model cards
            console.print()
            for i, model in enumerate(cloud_results, 1):
                console.print(create_model_card(model, i))

        # Local models table
        console.print()
        console.print(Rule(
            f"[bold bright_green]{Icons.LOCAL}  Connected Ollama Model Library[/]",
            style="bright_green"
        ))
        console.print()
        console.print(create_models_table(local_models))

        # Footer separator
        console.print()
        console.print(Rule(style="dim"))

    # Exit message
    console.print()
    console.print(Align.center(
        Panel(
            f"{Icons.QUIT} [bold bright_magenta]Thanks for using AgentLens![/]\n\n"
            f"[dim]Happy model hunting! {Icons.SPARKLE}[/]",
            border_style="bright_magenta",
            box=box.ROUNDED,
            padding=(1, 4)
        )
    ))
    console.print()


def main():
    run_cli()


if __name__ == "__main__":
    main()