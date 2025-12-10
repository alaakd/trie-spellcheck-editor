from __future__ import annotations

from dataclasses import dataclass, field
from typing import TypeVar, Optional


# ============================================================================
# Color
# ============================================================================

@dataclass
class Color:
    r: int
    g: int
    b: int
  
    def __str__(self) -> str:
        if not hasattr(self, "s"):
            self.s = f"rgb({self.r},{self.g},{self.b})"
        return self.s

    def __eq__(self, other: Color) -> bool:
        return self.r == other.r and self.g == other.g and self.b == other.b

    def __hash__(self) -> int:
        return hash((self.r, self.g, self.b))
    
    def from_hex(s: str) -> Color:
        r = int(s[1:3], 16)
        g = int(s[3:5], 16)
        b = int(s[5:7], 16)
        return Color(r, g, b)


NO_COLOR = Color(-1, -1, -1)
REGULAR = Color(255, 255, 255)
CURSOR = Color(128, 128, 128)
REGION = Color(0, 255, 0)

# ============================================================================
# Character
# ============================================================================
    
@dataclass
class Character:
    char: str
    fg_color: Color = field(default_factory=lambda: REGULAR)
    bg_color: Color = field(default_factory=lambda: NO_COLOR)


# ============================================================================
# Text Buffer
# ============================================================================

T = TypeVar("T")

@dataclass
class DoubleLink[T]:
    element: T
    next: Optional[DoubleLink[T]] = None
    prev: Optional[DoubleLink[T]] = None


class TextBufferException(Exception):
    """Raised when there is a buffer error."""

    
class TextBuffer:
    """Store the buffers characters in a doubly-linked chain/list."""

raise Exception("Replace this file with your text_buffer.py from Assginment 6")
