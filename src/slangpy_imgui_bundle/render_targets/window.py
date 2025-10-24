"""
A module defining a basic window render target for slangpy imgui applications.
"""

from dataclasses import dataclass
from typing import Callable, Tuple
from imgui_bundle import imgui, imgui_ctx
from reactivex import Observable
from slangpy_imgui_bundle.render_targets.render_target import (
    RenderContext,
    RenderTarget,
)


@dataclass
class WindowContext(RenderContext):
    open: Observable[bool]
    on_close: Callable[[], None]


class Window(RenderTarget):
    name: str = "Window"
    size: Tuple[int, int] = (400, 300)
    size_min: Tuple[float, float] = (200, 150)
    size_max: Tuple[float, float] = (imgui.FLT_MAX, imgui.FLT_MAX)
    window_flags: int = imgui.WindowFlags_.none.value

    _open: bool

    def __init__(self, context: WindowContext) -> None:
        super().__init__(context)

        def update_open(open: bool) -> None:
            self._open = open

        context.open.subscribe(update_open)
        self.on_close = context.on_close

    def render_window(self, time: float, delta_time: float) -> bool:
        """Render the contents of the window.

        :param time: Current time in seconds.
        :param delta_time: Time elapsed since last frame in seconds.
        :param open: Whether the window is open.
        """
        return True

    def render(self, time: float, delta_time: float) -> None:
        if self._open:
            imgui.set_next_window_size(self.size, imgui.Cond_.once.value)
            imgui.set_next_window_size_constraints(self.size_min, self.size_max)
            if not self.render_window(time, delta_time):
                self.on_close()
