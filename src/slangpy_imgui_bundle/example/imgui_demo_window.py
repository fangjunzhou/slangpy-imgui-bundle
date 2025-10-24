from imgui_bundle import imgui
from slangpy_imgui_bundle.render_targets.window import Window


class ImGuiDemoWindow(Window):
    name: str = "ImGui Demo Window"

    def render_window(self, time: float, delta_time: float) -> bool:
        return imgui.show_demo_window(True) == True
