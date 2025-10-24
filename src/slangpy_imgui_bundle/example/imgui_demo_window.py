from imgui_bundle import imgui
from slangpy_imgui_bundle.render_targets.window import Window


class ImGuiDemoWindow(Window):
    name: str = "ImGui Demo Window"
    size_min: tuple[float, float] = (800, 600)

    def render_window(self, time: float, delta_time: float, open: bool | None) -> bool:
        return imgui.show_demo_window(open) == True
