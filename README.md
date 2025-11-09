Box Overlap with Axes & Conditions
This project is a simple interactive visualization built with Pygame. It demonstrates how two rectangular boxes can overlap on a 2D plane, while also showing the logical conditions that determine their relative positions.

Features
Two draggable boxes (blue and red) displayed on a coordinate plane.

Real-time overlap detection between the boxes.

Visual guides for box coordinates (x and y).

Display of logical conditions (<, >, =) comparing box edges.

Highlighted overlap area when boxes intersect.

Dynamic layering: the last clicked box is drawn on top.

Requirements
Python 3.x

Pygame library

Install Pygame with:

bash
pip install pygame
How It Works
The program initializes an 800x500 window with axes drawn from the origin (0,0).

Two boxes are defined with position, size, and color.

The overlap between the boxes is calculated using pygame.Rect.clip.

Logical conditions are evaluated:

X1_u < X2_l

X1_l > X2_u

Y1_u < Y2_l

Y1_l > Y2_u

These conditions are displayed at the bottom of the screen with indicators showing whether they are valid.

Users can click and drag boxes to move them around, updating overlap and conditions in real time.

Controls
Click and drag a box to move it.

The last clicked box will be drawn on top.

Close the window to quit the program.

Code Structure
draw_axes(): Draws coordinate axes and origin label.

draw_guides(x, y): Draws guide lines for box corners.

compare(a, b, expected): Compares values with expected relation.

draw_conditions(b1, b2): Displays logical conditions between box edges.

Main loop:

Handles drawing, overlap detection, and user input events.

Updates box positions when dragged.

Example Use Case
This project can be used as a teaching aid for:

Understanding rectangle overlap logic.

Visualizing coordinate systems.

Learning Pygame basics such as rendering, event handling, and collision detection.
