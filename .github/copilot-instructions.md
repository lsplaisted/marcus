# Copilot Instructions for M.A.R.C.U.S.

## Project Overview

M.A.R.C.U.S. (Menu Activated Robot Code Usage System) is a LEGO SPIKE Prime robot program for FLL (FIRST LEGO League) competitions, written in Python using the [Pybricks](https://pybricks.com/) library. All code runs directly on the SPIKE Prime hub — there is no standard Python runtime, no filesystem, and no `pip install`.

## Setup

```sh
cd code
uv sync
```

This installs `pybricks` stubs for type-checking only. Code is deployed to the hub via the Pybricks firmware and VS Code extension, not executed locally.

## Architecture

The `code/` folder has two layers:

- **Top level** — team-specific files that change each season: `main_program.py`, `robot.py`, `program1.py`, `program2.py`, etc.
- **`marcus/` subfolder** — reusable MARCUS infrastructure: menu system, utilities, images. These rarely need editing.

**Entry point:** `main_program.py` — registers mission programs and launches the menu.

**Menu system (`marcus/menu.py`):** A hub-button-driven selector with two modes:
- **Mode 0 (Programs):** Left/Right to pick a numbered mission, Center to run it. After the last program runs, `celebrate.Run` plays automatically.
- **Mode 1 (Utilities):** Bluetooth button toggles into utility mode (clean wheels, battery check, celebrate, straight demo). Same Left/Right/Center navigation.

Center button stops a running sub-program (via `SystemExit` catch). Center+Bluetooth stops the entire system.

**Robot config (`robot.py`):** Single `Robot` class that initializes the hub, 4 motors (left/right wheels + left/right attachments), and a `DriveBase`. Update `TIRE_DIAMETER`, `AXLE_TRACK`, and motor ports/directions here when the physical robot changes.

**Two types of run functions:**
- **Mission programs** (`program1.py`, `program2.py`, ...): Signature is `Run(drive_base, left_attachment, right_attachment)`. These are autonomous FLL mission runs. Live in `code/` top level.
- **Utilities** (`marcus/cleanwheels.py`, `marcus/battery.py`, `marcus/celebrate.py`, `marcus/straightdemo.py`): Signature is `Run(robot)` — receives the full `Robot` instance.

**`marcus/images.py`:** 5×5 LED matrix sprites as `pybricks.tools.Matrix` constants (UPPER_SNAKE_CASE).

## Conventions

- Function names use `PascalCase` (e.g., `Run`, `Rescale`). Constants use `UPPER_SNAKE_CASE`.
- Every program/utility file includes `if __name__ == "__main__":` so it can run standalone on the hub for testing without the menu.
- To add a new mission program: create `programN.py` in `code/` with a `Run(drive_base, left_attachment, right_attachment)` function, import it in `main_program.py`, and add it to the `programs` dict.
- To add a new utility: create the file in `marcus/` with a `Run(robot)` function and add it to the `utilities` dict in `marcus/menu.py`.
- Files inside `marcus/` import siblings as `marcus.module` (e.g., `import marcus.images as images`). They import `robot` directly since it's in the parent `code/` directory.
- Distances are in millimeters, angles in degrees (Pybricks conventions).
- Gyro is off by default in the menu; individual programs should call `drive_base.use_gyro(True)` if they need it.
- Subfolder package support in Pybricks has historically been unreliable. If imports break on the hub, the fallback is to flatten everything back to `code/`.
