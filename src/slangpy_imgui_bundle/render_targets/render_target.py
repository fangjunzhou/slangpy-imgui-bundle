"""
A slangpy imgui render target that will be rendered every frame.
"""

import slangpy as spy
from dataclasses import dataclass


@dataclass
class RenderContext:
    device: spy.Device


class RenderTarget:
    """A render target base class for slangpy imgui applications.

    :param device: The slangpy device setup by the application.
    """

    def __init__(self, context: RenderContext) -> None:
        self.device = context.device

    def render(self, time: float, delta_time: float) -> None:
        """Called every frame to render the target.

        :param time: Current time in seconds.
        :param delta_time: Time elapsed since last frame in seconds.
        """
        pass
