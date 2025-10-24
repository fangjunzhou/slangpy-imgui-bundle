from typing import Unpack
from reactivex.subject import BehaviorSubject
from slangpy_imgui_bundle.app import App
from slangpy_imgui_bundle.example.imgui_demo_window import ImGuiDemoWindow
from slangpy_imgui_bundle.render_targets.dockspace import Dockspace, DockspaceArgs
from slangpy_imgui_bundle.render_targets.menu import (
    Menu,
    MenuItem,
)


class ExampleDockspaceArgs(DockspaceArgs):
    demo_window_opened: BehaviorSubject[bool]


class ExampleDockspace(Dockspace):
    def __init__(self, **kwargs: Unpack[ExampleDockspaceArgs]) -> None:
        super().__init__(**kwargs)
        self._menu_items = [
            Menu(
                device=self.device,
                name="Views",
                chilren=[
                    MenuItem(
                        device=self.device,
                        name="ImGui Demo Window",
                        open=kwargs["demo_window_opened"],
                        on_open_changed=lambda opened: kwargs[
                            "demo_window_opened"
                        ].on_next(opened),
                    )
                ],
            )
        ]


class ExampleApp(App):
    _demo_window_opened: BehaviorSubject[bool] = BehaviorSubject(True)

    def __init__(self) -> None:
        super().__init__([])

        self._render_targets = [
            ImGuiDemoWindow(
                device=self.device,
                open=self._demo_window_opened,
                on_close=lambda: self._demo_window_opened.on_next(False),
            )
        ]

        self._dockspace = ExampleDockspace(
            device=self.device,
            window_size=self._curr_window_size,
            demo_window_opened=self._demo_window_opened,
        )
