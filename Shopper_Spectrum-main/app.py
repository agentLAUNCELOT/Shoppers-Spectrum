"""Launch the application stored in the nested project directory."""

from pathlib import Path
import runpy


PROJECT_APP = Path(__file__).resolve().parent / "Shopper_Spectrum-main" / "app.py"

if not PROJECT_APP.is_file():
    raise FileNotFoundError(
        f"Application entry point not found: {PROJECT_APP}. "
        "Make sure the Shopper_Spectrum-main folder is present."
    )

runpy.run_path(str(PROJECT_APP), run_name="__main__")
