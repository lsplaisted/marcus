# Copilot Instructions for M.A.R.C.U.S.

## Project Overview

M.A.R.C.U.S. (Menu Activated Robot Code Usage System) is a LEGO SPIKE Prime robot program for FLL (FIRST LEGO League) competitions, written in Python using the [Pybricks](https://pybricks.com/) library. All code runs directly on the SPIKE Prime hub — there is no standard Python runtime, no filesystem, and no `pip install`.

## Setup

```sh
uv sync
```

This installs `pybricks` stubs for type-checking only. Code is deployed to the hub via the Pybricks firmware and the BlocklyPy VS Code extension, not executed locally.

## Architecture

The repo has two layers:

- **Root** — team-specific files that change each season: `main_program.py`, `robot.py`, `program1.py`, `program2.py`, etc.
- **`marcus/` subfolder** — reusable MARCUS infrastructure: menu system, button input, utilities, images. These rarely need editing.

**Entry point:** `main_program.py` — registers mission programs and launches the menu.

**Menu system (`marcus/menu.py`):** A hub-button-driven selector with two modes:
- **Mode 0 (Programs):** Left/Right to pick a numbered mission, Center (or force sensor) to run it. After the last program runs, `celebrate.Run` plays automatically.
- **Mode 1 (Utilities):** Bluetooth button toggles into utility mode (clean wheels, battery check, celebrate, straight demo). Same Left/Right/Center navigation.

Center button stops a running sub-program (via `SystemExit` catch). Center+Bluetooth stops the entire system. The `run_program` helper in `menu.py` handles stop-button switching, motor cleanup, and button release.

**Button input (`marcus/buttons.py`):** `ButtonInput` class providing edge detection (`just_pressed`), hold detection (`is_held`), and `wait_until_released`. Optionally merges a force sensor press as a Center button press.

**Robot config (`robot.py`):** Single `Robot` class that initializes the hub, 4 motors (left/right wheels + left/right attachments), a `DriveBase`, and an optional `ForceSensor`. Update `TIRE_DIAMETER`, `AXLE_TRACK`, motor ports/directions, and `FORCE_SENSOR_PORT` here when the physical robot changes.

**Unified run signature:** All programs and utilities use `Run(drive_base: DriveBase, left_attachment: Motor, right_attachment: Motor, hub: PrimeHub)`.

**`marcus/images.py`:** 5×5 LED matrix sprites as `pybricks.tools.Matrix` constants (UPPER_SNAKE_CASE).

## Conventions

- Function names use `PascalCase` (e.g., `Run`, `Rescale`). Constants use `UPPER_SNAKE_CASE`.
- Every program/utility file includes `if __name__ == "__main__":` so it can run standalone on the hub for testing without the menu.
- To add a new mission program: create `programN.py` at root with a `Run(drive_base, left_attachment, right_attachment, hub)` function, import it in `main_program.py`, and add it to the `programs` list.
- To add a new utility: create the file in `marcus/` with the same `Run` signature and add it to the `utilities` list in `marcus/menu.py`.
- Files inside `marcus/` use `from marcus.X import Y` for sibling imports. They import `robot` directly since it's at the root.
- Distances are in millimeters, angles in degrees (Pybricks conventions).
- Gyro is off by default in the menu; individual programs should call `drive_base.use_gyro(True)` if they need it.
