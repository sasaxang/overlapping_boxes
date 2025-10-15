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
top_box_index = 1  # Controls which box is drawn last (on top)


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
        color = (0, 150, 0) if valid else (200, 0, 0)
        line = f"{label1} {symbol} {label2}    ({val1} {symbol} {val2})"
        line_y = HEIGHT - 100 + i * 22
        line_surface = condition_font.render(line, True, (0, 0, 0))
        screen.blit(line_surface, (10, line_y))
        pygame.draw.circle(screen, color, (350, line_y + 8), 7)


# --- Main Loop ---
running = True
while running:
    screen.fill((255, 255, 255))
    draw_axes()

    # Logical box references (fixed)
    box1 = next(b for b in boxes if b["number"] == "1")
    box2 = next(b for b in boxes if b["number"] == "2")

    # Draw overlap first
    rect1 = pygame.Rect(box1["x"], box1["y"], box1["w"], box1["h"])
    rect2 = pygame.Rect(box2["x"], box2["y"], box2["w"], box2["h"])
    overlap_rect = rect1.clip(rect2)

    if overlap_rect.width > 0 and overlap_rect.height > 0:
        overlap_surface = pygame.Surface((overlap_rect.width, overlap_rect.height), pygame.SRCALPHA)
        pygame.draw.rect(overlap_surface, (128, 0, 128, 180), overlap_surface.get_rect(), 0)
        screen.blit(overlap_surface, overlap_rect.topleft)

    # Draw boxes (bottom first, then top)
    for i in [1 - top_box_index, top_box_index]:
        box = boxes[i]
        box_surface = pygame.Surface((box["w"], box["h"]), pygame.SRCALPHA)
        pygame.draw.rect(box_surface, box["color"] + (150,), box_surface.get_rect(), 0)
        pygame.draw.rect(box_surface, box["color"], box_surface.get_rect(), 2)
        screen.blit(box_surface, (box["x"], box["y"]))
        screen.blit(big_font.render(box["number"], True, (0, 0, 0)),
                    (box["x"] + box["w"] // 2 - 10, box["y"] + box["h"] // 2 - 18))
        screen.blit(font.render(f"X{box['number']}_u,Y{box['number']}_u", True, (0, 0, 0)),
                    (box["x"] - 5, box["y"] - 15))
        screen.blit(font.render(f"X{box['number']}_l,Y{box['number']}_l", True, (0, 0, 0)),
                    (box["x"] + box["w"] - 60, box["y"] + box["h"] + 5))
        draw_guides(box["x"], box["y"])
        draw_guides(box["x"] + box["w"], box["y"] + box["h"])

    draw_conditions(box1, box2)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = event.pos
            for i in reversed(range(len(boxes))):
                box = boxes[i]
                if box["x"] < mx < box["x"] + box["w"] and box["y"] < my < box["y"] + box["h"]:
                    dragging = i
                    offset_x = mx - box["x"]
                    offset_y = my - box["y"]
                    top_box_index = i  # Update visual layering
                    break

        elif event.type == pygame.MOUSEBUTTONUP:
            dragging = None

        elif event.type == pygame.MOUSEMOTION and dragging is not None:
            mx, my = event.pos
            boxes[dragging]["x"] = mx - offset_x
            boxes[dragging]["y"] = my - offset_y

pygame.quit()
