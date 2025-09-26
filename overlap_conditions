import pygame

pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Box Overlap with Axes & Conditions")
font = pygame.font.SysFont("monospace", 14)
big_font = pygame.font.SysFont("sans", 36, bold=True)
condition_font = pygame.font.SysFont("sans", 16)

# Box data
boxes = [
    {"x": 100, "y": 100, "w": 150, "h": 100, "color": (0, 0, 255), "number": "1"},  # Blue
    {"x": 350, "y": 200, "w": 150, "h": 100, "color": (255, 0, 0), "number": "2"}  # Red
]

dragging = None
offset_x = offset_y = 0


def draw_axes():
    pygame.draw.line(screen, (150, 150, 150), (0, 0), (WIDTH, 0), 1)
    pygame.draw.line(screen, (150, 150, 150), (0, 0), (0, HEIGHT), 1)
    screen.blit(font.render("(0,0)", True, (150, 150, 150)), (5, 5))


def draw_guides(x, y):
    pygame.draw.line(screen, (180, 180, 180), (x, y), (x, 0), 1)
    pygame.draw.line(screen, (180, 180, 180), (x, y), (0, y), 1)
    screen.blit(font.render(f"x={x}", True, (100, 100, 100)), (x + 2, 5))
    screen.blit(font.render(f"y={y}", True, (100, 100, 100)), (2, y - 15))


def compare(a, b, expected):
    if expected == '<':
        symbol = '<' if a < b else '>' if a > b else '='
        return symbol, a < b
    if expected == '>':
        symbol = '>' if a > b else '<' if a < b else '='
        return symbol, a > b
    return '=', False


def draw_conditions(b1, b2):
    x1_u, x1_l = b1["x"], b1["x"] + b1["w"]
    y1_u, y1_l = b1["y"], b1["y"] + b1["h"]
    x2_u, x2_l = b2["x"], b2["x"] + b2["w"]
    y2_u, y2_l = b2["y"], b2["y"] + b2["h"]

    conditions = [
        ("X1_u", x1_u, "<", "X2_l", x2_l),
        ("X1_l", x1_l, ">", "X2_u", x2_u),
        ("Y1_u", y1_u, "<", "Y2_l", y2_l),
        ("Y1_l", y1_l, ">", "Y2_u", y2_u)
    ]

    for i, (label1, val1, op, label2, val2) in enumerate(conditions):
        symbol, valid = compare(val1, val2, op)

        if valid:
            color = (0, 150, 0)  # Green for true
        else:
            color = (200, 0, 0)  # Red for false

        line = f"{label1} {symbol} {label2}    ({val1} {symbol} {val2})"
        line_y = HEIGHT - 100 + i * 22

        line_surface = condition_font.render(line, True, (0, 0, 0))
        screen.blit(line_surface, (10, line_y))

        center_x = 350
        center_y = line_y + 8
        radius = 7

        pygame.draw.circle(screen, color, (center_x, center_y), radius)


# --- Main Loop ---
running = True
while running:
    screen.fill((255, 255, 255))
    draw_axes()

    # --- Draw Overlap First (before individual boxes) ---
    rect1 = pygame.Rect(boxes[0]["x"], boxes[0]["y"], boxes[0]["w"], boxes[0]["h"])
    rect2 = pygame.Rect(boxes[1]["x"], boxes[1]["y"], boxes[1]["w"], boxes[1]["h"])

    overlap_rect = rect1.clip(rect2)  # Get the intersection rectangle

    if overlap_rect.width > 0 and overlap_rect.height > 0:
        # Create a semi-transparent surface for the overlap
        overlap_surface = pygame.Surface((overlap_rect.width, overlap_rect.height), pygame.SRCALPHA)
        # Use a distinct color for the overlap, e.g., purple from mixing red and blue
        overlap_color = (128, 0, 128, 180)  # R, G, B, Alpha (180 out of 255 for transparency)
        pygame.draw.rect(overlap_surface, overlap_color, overlap_surface.get_rect(), 0)
        screen.blit(overlap_surface, overlap_rect.topleft)

    # --- Draw Transparent Boxes and their Numbers/Labels ---
    for i, box in enumerate(boxes):
        # Create a new Surface for each box with SRCALPHA flag for transparency
        box_surface = pygame.Surface((box["w"], box["h"]), pygame.SRCALPHA)

        # Define transparency level (0-255, 255 is opaque)
        alpha_level = 150  # Example: 150 out of 255, so it's quite transparent

        # Fill the box surface with its color and transparency
        box_color_with_alpha = box["color"] + (alpha_level,)
        pygame.draw.rect(box_surface, box_color_with_alpha, box_surface.get_rect(), 0)  # Fill
        pygame.draw.rect(box_surface, box["color"], box_surface.get_rect(), 2)  # Border (opaque)

        # Blit the box surface onto the main screen
        screen.blit(box_surface, (box["x"], box["y"]))

        # Draw box number and corner labels (these remain opaque)
        screen.blit(big_font.render(box["number"], True, (0, 0, 0)),
                    (box["x"] + box["w"] // 2 - 10, box["y"] + box["h"] // 2 - 18))
        screen.blit(font.render(f"X{i + 1}_u,Y{i + 1}_u", True, (0, 0, 0)), (box["x"] - 5, box["y"] - 15))
        screen.blit(font.render(f"X{i + 1}_l,Y{i + 1}_l", True, (0, 0, 0)),
                    (box["x"] + box["w"] - 60, box["y"] + box["h"] + 5))

        draw_guides(box["x"], box["y"])
        draw_guides(box["x"] + box["w"], box["y"] + box["h"])

    draw_conditions(boxes[0], boxes[1])

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = event.pos
            # Iterate boxes in reverse order so that clicking on an overlapping box
            # selects the one on top for dragging.
            for i in reversed(range(len(boxes))):
                box = boxes[i]
                rx, ry, rw, rh = box["x"], box["y"], box["w"], box["h"]

                if rx < mx < rx + rw and ry < my < ry + rh:
                    dragging = i
                    offset_x = mx - rx
                    offset_y = my - ry
                    # Bring the dragged box to the front (visual layer)
                    # This ensures the dragged box is always drawn last (on top)
                    boxes.append(boxes.pop(i))
                    break

        elif event.type == pygame.MOUSEBUTTONUP:
            dragging = None

        elif event.type == pygame.MOUSEMOTION:
            mx, my = event.pos

            if dragging is not None:
                boxes[dragging]["x"] = mx - offset_x
                boxes[dragging]["y"] = my - offset_y

pygame.quit()
