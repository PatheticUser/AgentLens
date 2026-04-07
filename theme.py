"""
AgentLens Theme Configuration
Centralized styling, colors, and Nerd Font icons for a cohesive TUI experience.
"""

from rich.style import Style
from rich.color import Color
from rich.console import Console

# ═══════════════════════════════════════════════════════════════════════════════
# COLOR PALETTE
# ═══════════════════════════════════════════════════════════════════════════════

class Colors:
    """Centralized color palette for consistent theming."""
    # Primary accent colors
    CYAN = "cyan"
    BLUE = "blue"
    MAGENTA = "magenta"
    GREEN = "green"
    YELLOW = "yellow"
    RED = "red"

    # Bright variants (for emphasis)
    BRIGHT_CYAN = "bright_cyan"
    BRIGHT_BLUE = "bright_blue"
    BRIGHT_MAGENTA = "bright_magenta"
    BRIGHT_GREEN = "bright_green"
    BRIGHT_YELLOW = "bright_yellow"
    BRIGHT_RED = "bright_red"

    # Neutrals
    WHITE = "white"
    DIM = "dim white"
    BLACK = "black"

    # Semantic colors
    SUCCESS = "bright_green"
    ERROR = "bright_red"
    WARNING = "bright_yellow"
    INFO = "bright_cyan"

    # Gradient-like accent pairs (alternating)
    ACCENT_PAIRS = [
        ("bright_cyan", "cyan"),
        ("bright_blue", "blue"),
        ("bright_magenta", "magenta"),
        ("bright_green", "green"),
    ]


# ═══════════════════════════════════════════════════════════════════════════════
# NERD FONT ICONS (Requires Nerd Font installation)
# ═══════════════════════════════════════════════════════════════════════════════

class Icons:
    """Nerd Font icons for visual enhancement."""
    # ── Application ──
    APP = ""  # Robot/AI icon
    LENS = ""  # Magnifying glass
    SEARCH = ""  # Search icon

    # ── Status Indicators ──
    SUCCESS = ""  # Checkmark
    ERROR = ""  # X mark
    WARNING = ""  # Warning triangle
    INFO = ""  # Info icon
    LOADING = ""  # Hourglass/spinner
    SYNC = ""  # Sync/refresh
    ONLINE = ""  # Green circle
    OFFLINE = ""  # Red circle/empty
    CONNECTED = ""  # Link connected

    # ── Models & AI ──
    MODEL = ""  # Model/brain
    ROBOT = ""  # Robot face
    NEURAL = ""  # Neural network
    CHIPS = ""  # Chips/processor
    CPU = ""  # CPU

    # ── Parameters & Specs ──
    PARAMS = ""  # Parameters/settings
    SIZE = ""  # Size/scale
    TOOLS = ""  # Tools/wrench
    FEATURES = ""  # Star/features
    SPEED = ""  # Speed/fast

    # ── Cloud & Deployment ──
    CLOUD = ""  # Cloud icon
    SERVER = ""  # Server
    DOWNLOAD = ""  # Download
    UPLOAD = ""  # Upload
    LOCAL = ""  # Local/folder

    # ── Navigation & Actions ──
    QUIT = ""  # Quit/exit
    ENTER = ""  # Enter/return
    ARROW_RIGHT = ""  # Arrow right
    ARROW_LEFT = ""  # Arrow left
    BULLET = ""  # Bullet point
    CHEVRON = ""  # Chevron

    # ── Decorative ──
    SPARKLE = ""  # Sparkle/star
    GEM = ""  # Gem/diamond
    FIRE = ""  # Fire/hot
    BOOK = ""  # Book/docs
    LIGHTBULB = ""  # Lightbulb/idea

    # ── Box Drawing ──
    CORNER_TL = ""
    CORNER_TR = ""
    CORNER_BL = ""
    CORNER_BR = ""
    HORIZONTAL = "─"
    VERTICAL = "│"
    HORIZONTAL_BOLD = "━"
    VERTICAL_BOLD = "┃"


# ═══════════════════════════════════════════════════════════════════════════════
# RICH STYLES
# ═══════════════════════════════════════════════════════════════════════════════

class Styles:
    """Pre-defined Rich Style objects for consistent styling."""
    # Headers
    HEADER_TITLE = Style(color=Colors.BRIGHT_CYAN, bold=True)
    HEADER_SUBTITLE = Style(color=Colors.WHITE, italic=True, dim=True)

    # Prompts
    PROMPT_LABEL = Style(color=Colors.BRIGHT_GREEN, bold=True)
    PROMPT_HINT = Style(color=Colors.WHITE, dim=True)

    # Cards
    CARD_TITLE = Style(color=Colors.BRIGHT_CYAN, bold=True)
    CARD_BODY = Style(color=Colors.WHITE)
    CARD_LABEL = Style(color=Colors.CYAN, bold=True)

    # Tables
    TABLE_HEADER = Style(color=Colors.BRIGHT_GREEN, bold=True)
    TABLE_ROW = Style(color=Colors.WHITE)
    TABLE_ALT_ROW = Style(color=Colors.WHITE, dim=True)

    # Status
    STATUS_LOADING = Style(color=Colors.BRIGHT_MAGENTA, bold=True)
    STATUS_SUCCESS = Style(color=Colors.SUCCESS, bold=True)
    STATUS_ERROR = Style(color=Colors.ERROR, bold=True)

    # Accents (alternating)
    ACCENT_PRIMARY = Style(color=Colors.BRIGHT_CYAN, bold=True)
    ACCENT_SECONDARY = Style(color=Colors.BRIGHT_BLUE, bold=True)


# ═══════════════════════════════════════════════════════════════════════════════
# ASCII ART LOGOS
# ═══════════════════════════════════════════════════════════════════════════════

LOGO = """
[cyan]    ___              _      _     [bright_cyan]    [cyan]
[cyan]   /   \            | |    | |    [bright_cyan] ___ [cyan] ___  ___ _ __
[cyan]  / /\ \   __ _  ___| | __ | |    [bright_cyan]/ __|[cyan]/ _ \/ __| '__|
[cyan] / /  \ \ / _` |/ __| |/ / | |____[bright_cyan]| (__ [cyan]  __/ (__| |
[cyan]/_/    \_\__,_|____|_/___| |______[bright_cyan]\___|[cyan]\___|\___|_|
[white]                  by Rameez
"""

LOGO_MINI = "[bright_cyan]󰚩 [bold white]Agent[bright_cyan]Lens[/]"


# ═══════════════════════════════════════════════════════════════════════════════
# UI MESSAGES
# ═══════════════════════════════════════════════════════════════════════════════

class Messages:
    """Pre-defined messages and labels."""
    WELCOME = "Enter an agentic topic to initiate deep model research."
    EXAMPLE = f"{Icons.LIGHTBULB} Try: [italic cyan]'I need a coding agent'[/] or [italic cyan]'Customer support system'[/]"
    SEARCH_PROMPT = f"{Icons.SEARCH} [bold bright_green]Search Query[/]"
    SEARCH_HINT = "[dim](or 'q' to quit, 'h' for help)[/]"
    LOADING = f"{Icons.SYNC} [bold bright_magenta]Synthesizing Deep Research...[/]"
    LOADING_DETAIL = f"{Icons.LOADING} Consulting Tavily + Ollama for insights"
    RESULTS_HEADER = f"{Icons.GEM} [bold bright_magenta]Agentic Discoveries[/]"
    LOCAL_HEADER = f"{Icons.LOCAL} [bold bright_green]Connected Ollama Model Library[/]"
    NO_RESULTS = f"{Icons.WARNING} No discoveries found. Try a broader query."
    GOODBYE = f"{Icons.QUIT} [bold bright_magenta]Exiting AgentLens. Goodbye![/]"
    HELP = f"{Icons.BOOK} [bold bright_cyan]Help & Shortcuts[/]"


# ═══════════════════════════════════════════════════════════════════════════════
# UTILITY FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════════════

def get_accent_color(index: int) -> tuple[str, str]:
    """Get alternating accent colors based on index."""
    pair = Colors.ACCENT_PAIRS[index % len(Colors.ACCENT_PAIRS)]
    return pair


def make_gradient_bar(width: int = 60, colors: list[str] = None) -> str:
    """Create a gradient-like progress bar using multiple colors."""
    if colors is None:
        colors = [Colors.BRIGHT_CYAN, Colors.BRIGHT_BLUE, Colors.BRIGHT_MAGENTA, Colors.BRIGHT_GREEN]
    segment_width = width // len(colors)
    bar = ""
    for color in colors:
        bar += f"[{color}]{'━' * segment_width}[/]"
    return bar


# ═══════════════════════════════════════════════════════════════════════════════
# GLOBAL CONSOLE INSTANCE
# ═══════════════════════════════════════════════════════════════════════════════

console = Console()