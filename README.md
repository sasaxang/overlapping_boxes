# Pygame Box Overlap with AABB Conditions Visualizer

This Pygame application provides an interactive visualization of 2D Axis-Aligned Bounding Box (AABB) overlap and the fundamental conditions used to detect it. Drag two boxes around the screen and observe in real-time how their overlap is calculated and how the underlying collision detection conditions change.

## Table of Contents

-   [Features](#features)
-   [Installation](#installation)
-   [How to Run](#how-to-run)
-   [Usage](#usage)
-   [Understanding AABB Overlap Conditions](#understanding-aabb-overlap-conditions)
-   [Screenshot](#screenshot)
-   [License](#license)

## Features

*   **Interactive Boxes:** Two draggable boxes (Blue Box 1 and Red Box 2) that can be moved anywhere on the screen.
*   **Real-time Overlap:** A purple translucent area highlights the exact region where the two boxes overlap.
*   **AABB Condition Display:** Four key conditions for AABB collision detection are displayed at the bottom left, showing their current values and truthiness.
*   **Visual Feedback:** Green/red circles indicate whether each overlap condition is currently `True` or `False`.
*   **Coordinate Guides:** X and Y axes, along with guide lines and coordinate labels for the corners of each box, help in understanding their positions.
*   **Dynamic Layering:** The box you are currently dragging will automatically be drawn on top.

## Installation

1.  **Python:** Ensure you have Python 3.x installed.
2.  **Pygame:** Install the Pygame library using pip:
    ```bash
    pip install pygame
    ```

## How to Run

1.  Save the provided code into a file named, for example, `aabb_overlap_visualizer.py`.
2.  Open a terminal or command prompt.
3.  Navigate to the directory where you saved the file.
4.  Run the script:
    ```bash
    python aabb_overlap_visualizer.py
    ```

## Usage

Once the application starts:

1.  You will see two colored boxes (Blue Box 1 and Red Box 2) and a coordinate system.
2.  **Click and Drag:** Use your mouse to click on either box and drag it around the screen.
3.  **Observe Overlap:** As the boxes move and intersect, a purple translucent rectangle will appear, indicating their overlap.
4.  **Monitor Conditions:** At the bottom left of the window, you'll see four conditions listed, for example: `X1_u < X2_l`.
    *   The values next to the condition (`(val1 symbol val2)`) show the current numerical comparison.
    *   A **green circle** next to a condition means it evaluates to `True`.
    *   A **red circle** means it evaluates to `False`.
5.  **Understand Corners:** The labels `X1_u,Y1_u`, `X1_l,Y1_l`, etc., denote the "upper-left" (minimum x, minimum y) and "lower-right" (maximum x, maximum y) corners of each box.

## Understanding AABB Overlap Conditions

The core of 2D AABB (Axis-Aligned Bounding Box) collision detection often relies on checking if the boxes are *not* overlapping. If they are not overlapping, then they must be separated along either the X-axis or the Y-axis.

The four conditions displayed in this visualizer are a common way to express this:

Let `b1` be Box 1 (blue) and `b2` be Box 2 (red).
`X_u` refers to the **min X** coordinate (left edge).
`X_l` refers to the **max X** coordinate (right edge).
`Y_u` refers to the **min Y** coordinate (top edge).
`Y_l` refers to the **max Y** coordinate (bottom edge).

1.  `X1_u < X2_l` (Box 1's left edge is to the left of Box 2's right edge)
    *   If this is `False`, Box 1 is entirely to the right of Box 2.
2.  `X1_l > X2_u` (Box 1's right edge is to the right of Box 2's left edge)
    *   If this is `False`, Box 1 is entirely to the left of Box 2.
3.  `Y1_u < Y2_l` (Box 1's top edge is above Box 2's bottom edge)
    *   If this is `False`, Box 1 is entirely below Box 2.
4.  `Y1_l > Y2_u` (Box 1's bottom edge is below Box 2's top edge)
    *   If this is `False`, Box 1 is entirely above Box 2.

**Key Principle:**
The two boxes **overlap if and only if ALL FOUR conditions are TRUE**.
If *any one* of these conditions is `False`, the boxes are not overlapping.

Observe how the purple overlap area appears/disappears precisely when all four circles turn green/red together.

## Screenshot

![Screenshot of AABB Conditions Visualizer](AABB_Conditions_Visualizer_screenshot.png)

## License

This project is open-source and available under the MIT License. Feel free to use, modify, and distribute it for educational or personal purposes.
