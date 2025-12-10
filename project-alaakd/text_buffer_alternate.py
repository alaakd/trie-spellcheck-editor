from __future__ import annotations

import itertools
from dataclasses import dataclass, field
from typing import TypeVar, Optional, Iterator
from trie import Trie, PUNCTUATION


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

all_links: dict[int, DoubleLink] = {}


@dataclass
class DoubleLink[T]:
    element: T
    next: Optional[DoubleLink[T]] = None
    prev: Optional[DoubleLink[T]] = None

    def __post_init__(self):
        global all_links
        all_links[id(self)] = self

    def __str__(self):
        if self.element.char == '\0':
            return "EOF"
        return str(self.element.char)


class TextBufferException(Exception):
    """Raised when there is a buffer error."""


class TextBuffer:
    """Store the buffers characters in a doubly-linked chain/list.
    ... simplified, cannot add or delete characters,
    ... BUT you can read in an initial text
    """

    EOF = DoubleLink(Character("\0"))

    def __init__(self, initial_text: str = None):
        self.head = TextBuffer.EOF
        self.point = self.head
        self.trie = Trie()

    def initialize_text(self, initial_text: str = None):
        nodes = [DoubleLink(Character(a)) for a in initial_text] + [TextBuffer.EOF]
        for a,b in itertools.pairwise(nodes):
            a.next = b
            b.prev = a
        self.point = nodes[-1]
        self.head = nodes[0]

    def __iter__(self) -> Iterator[tuple[Character, bool, bool]]:
        current = self.head

        while True:
            yield current.element, self.point == current, False
            if current.next is None:
                break
            current = current.next

    def insert_at_point(self, c: Character):
        """Insert character in front of point"""

    def delete_at_point(self):
        """Delete character in front of point"""

    def backward_char(self):
        """Move point back by one space"""

        if self.point.prev is None:
            return

        self.point = self.point.prev

    def forward_char(self):
        """Move forward by one point"""

        if self.point.next is None:
            return

        self.point = self.point.next

    def set_mark(self):
        """set the mark (for deletion purposes)"""

    def kill_region(self):
        """remove all nodes within mark"""


