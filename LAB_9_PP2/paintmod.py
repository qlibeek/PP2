import pygame, sys, math
pygame.init()

W, H = 640, 480
screen = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 20)

# настройки
radius = 15
mode = 'blue'              # текущий цвет
tool = 'free'              # текущий инструмент

strokes = []               # свободные линии
current = None             # текущая линия
shapes = []                # фигуры: dict {tool, start, end, color}
drawing = False
drawing_shape = False
shape_start = None         # точка начала фигуры


def color_from_mode(m):
    if m == 'blue':  return (0, 0, 255)
    if m == 'red':   return (255, 0, 0)
    return (0, 255, 0)


def draw_line(surface, a, b, w, col):
    # толстая линия как набор кругов
    dx, dy = b[0] - a[0], b[1] - a[1]
    steps = max(abs(dx), abs(dy)) or 1
    for i in range(steps + 1):
        t = i / steps
        x = int(a[0] + dx * t)
        y = int(a[1] + dy * t)
        pygame.draw.circle(surface, col, (x, y), w)


def draw_shape(surface, tool, start, end, color, outline=False):
    # одна функция для всех фигур
    x0, y0 = start
    x1, y1 = end
    w = 2 if outline else 0

    if tool == 'rect':
        r = pygame.Rect(min(x0, x1), min(y0, y1), abs(x1 - x0), abs(y1 - y0))
        pygame.draw.rect(surface, color, r, w)

    elif tool == 'circle':
        r = int(math.hypot(x1 - x0, y1 - y0))
        pygame.draw.circle(surface, color, (x0, y0), r, w)

    elif tool == 'square':
        dx, dy = x1 - x0, y1 - y0
        side = max(abs(dx), abs(dy))
        left = x0 if dx >= 0 else x0 - side
        top = y0 if dy >= 0 else y0 - side
        r = pygame.Rect(left, top, side, side)
        pygame.draw.rect(surface, color, r, w)

    elif tool == 'tri_right':
        # прямоугольный треугольник
        p1 = (x0, y0)
        p2 = (x1, y0)
        p3 = (x0, y1)
        pygame.draw.polygon(surface, color, [p1, p2, p3], w)

    elif tool == 'tri_eq':
        # равносторонний треугольник
        left, right = min(x0, x1), max(x0, x1)
        bottom = max(y0, y1)
        side = max(1, right - left)
        cx = (left + right) / 2
        h = side * math.sqrt(3) / 2
        top_y = bottom - h
        p1 = (left, bottom)
        p2 = (right, bottom)
        p3 = (cx, top_y)
        pygame.draw.polygon(surface, color, [p1, p2, p3], w)

    elif tool == 'rhombus':
        # ромб
        left, right = min(x0, x1), max(x0, x1)
        top, bottom = min(y0, y1), max(y0, y1)
        cx, cy = (left + right) / 2, (top + bottom) / 2
        pts = [(cx, top), (right, cy), (cx, bottom), (left, cy)]
        pygame.draw.polygon(surface, color, pts, w)


while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit(); sys.exit()

        if e.type == pygame.KEYDOWN:
            pressed = pygame.key.get_pressed()
            if e.key == pygame.K_w and pressed[pygame.K_LCTRL]: pygame.quit(); sys.exit()
            if e.key == pygame.K_ESCAPE: pygame.quit(); sys.exit()

            # цвет
            if   e.key == pygame.K_r: mode = 'red'
            elif e.key == pygame.K_g: mode = 'green'
            elif e.key == pygame.K_b: mode = 'blue'

            # инструменты
            elif e.key == pygame.K_d: tool = 'free'
            elif e.key == pygame.K_e: tool = 'eraser'
            elif e.key == pygame.K_t: tool = 'rect'
            elif e.key == pygame.K_c: tool = 'circle'
            elif e.key == pygame.K_1: tool = 'square'
            elif e.key == pygame.K_2: tool = 'tri_right'
            elif e.key == pygame.K_3: tool = 'tri_eq'
            elif e.key == pygame.K_4: tool = 'rhombus'

            # очистка
            elif e.key == pygame.K_x:
                strokes.clear()
                shapes.clear()

        if e.type == pygame.MOUSEBUTTONDOWN:
            if e.button == 1:
                radius = min(200, radius + 1)
                if tool in ('free', 'eraser'):
                    drawing = True
                    col = (0, 0, 0) if tool == 'eraser' else color_from_mode(mode)
                    current = {'pts': [e.pos], 'col': col, 'w': radius}
                else:
                    drawing_shape = True
                    shape_start = e.pos
            elif e.button == 3:
                radius = max(1, radius - 1)

        if e.type == pygame.MOUSEMOTION and drawing and current:
            current['pts'].append(e.pos)

        if e.type == pygame.MOUSEBUTTONUP and e.button == 1:
            if drawing and current:
                strokes.append(current)
                current = None
                drawing = False
            if drawing_shape and shape_start and tool not in ('free', 'eraser'):
                shapes.append({
                    'tool': tool,
                    'start': shape_start,
                    'end': e.pos,
                    'color': color_from_mode(mode)
                })
                drawing_shape = False
                shape_start = None

    # рисуем
    screen.fill((0, 0, 0))

# линии (включая ластик)
    for st in strokes:
        pts = st['pts']
        for i in range(len(pts) - 1):
            draw_line(screen, pts[i], pts[i + 1], st['w'], st['col'])

# текущая линия
    if current:
        pts = current['pts']
        for i in range(len(pts) - 1):
            draw_line(screen, pts[i], pts[i + 1], current['w'], current['col'])

# готовые фигуры — поверх всего
    for s in shapes:
        draw_shape(screen, s['tool'], s['start'], s['end'], s['color'], outline=False)

    # превью фигуры тоже рисуем после всего
    if drawing_shape and shape_start:
        draw_shape(screen, tool, shape_start, pygame.mouse.get_pos(),
                   color_from_mode(mode), outline=True)


    # подсказка
    txt = f"Tool:{tool} Color:{mode} Size:{radius}  R/G/B D/E T/C 1-□ 2-⊿ 3-△ 4-◇ X-clear"
    screen.blit(font.render(txt, True, (200, 200, 200)), (6, 6))

    pygame.display.flip()
    clock.tick(60)