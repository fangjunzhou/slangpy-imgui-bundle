from imgui_bundle import imgui, implot3d
from slangpy_imgui_bundle.render_targets.window import Window


class ImGuiDemoWindow(Window):
    size_min: tuple[float, float] = (800, 600)

    def render_window(self, time: float, delta_time: float, open: bool | None) -> bool:
        return imgui.show_demo_window(open) == True


class ImPlot3DDemoWindow(Window):
    size_min: tuple[float, float] = (800, 600)

    def render_window(self, time: float, delta_time: float, open: bool | None) -> bool:
        implot3d.show_demo_window()
        return True
