from reactivex.subject import BehaviorSubject
from slangpy_imgui_bundle.app import App
from slangpy_imgui_bundle.example.imgui_demo_window import ImGuiDemoWindow
from slangpy_imgui_bundle.render_targets.window import WindowContext


class ExampleApp(App):
    demo_window_opened: BehaviorSubject[bool] = BehaviorSubject(True)

    def __init__(self) -> None:
        super().__init__([])

        self._render_targets = [
            ImGuiDemoWindow(
                WindowContext(
                    device=self.device,
                    open=self.demo_window_opened,
                    on_close=lambda: self.demo_window_opened.on_next(False),
                )
            )
        ]
