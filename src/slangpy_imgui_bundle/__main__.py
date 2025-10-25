import logging
import asyncio
from slangpy_imgui_bundle.example.app import ExampleApp

if __name__ == "__main__":
    # Enable debug logging
    logging.basicConfig(level=logging.DEBUG)

    app = ExampleApp()
    asyncio.run(app.run())
