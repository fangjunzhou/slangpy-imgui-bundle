from dataclasses import dataclass
from typing import Callable

from reactivex import Observable
from slangpy_imgui_bundle.render_targets.render_target import (
    RenderContext,
    RenderTarget,
)


@dataclass
class MenuContext(RenderContext):
    open: Observable[bool]
    on_open_changed: Callable[[bool], None]


class MenuItem(RenderTarget):
    def __init__(self, context: RenderContext) -> None:
        super().__init__(context)
