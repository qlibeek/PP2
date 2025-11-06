import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    radius = 15
    x = 0
    y = 0
    mode = 'blue'          # blue|red|green или 'eraser' внутри drawLineBetween
    tool = 'free'          # НОВОЕ: 'free'|'eraser'|'rect'|'circle'
    points = []
    shapes = []            # НОВОЕ: список зафиксированных фигур
    drawing_shape = False  # НОВОЕ: тянем ли фигуру сейчас
    shape_start = None     # НОВОЕ: стартовая точка фигуры
    
    while True:
        
        pressed = pygame.key.get_pressed()
        alt_held  = pressed[pygame.K_LALT]  or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            # закрытие окна/горячие клавиши выхода
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held: return
                if event.key == pygame.K_F4 and alt_held: return
                if event.key == pygame.K_ESCAPE: return
            
                # выбор цвета (как было)
                if event.key == pygame.K_r:   mode = 'red'
                elif event.key == pygame.K_g: mode = 'green'
                elif event.key == pygame.K_b: mode = 'blue'
                
                # НОВОЕ: выбор инструмента
                elif event.key == pygame.K_d: tool = 'free'
                elif event.key == pygame.K_e: tool = 'eraser'
                elif event.key == pygame.K_t: tool = 'rect'
                elif event.key == pygame.K_c: tool = 'circle'
            
            # мышь
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:   # LMB — толще
                    radius = min(200, radius + 1)
                elif event.button == 3: # RMB — тоньше
                    radius = max(1, radius - 1)
                
                # НОВОЕ: старт фигуры по ЛКМ
                if event.button == 1 and tool in ('rect','circle'):
                    drawing_shape = True
                    shape_start = event.pos
            
            if event.type == pygame.MOUSEBUTTONUP:
                # НОВОЕ: фиксируем фигуру на ЛКМ
                if event.button == 1 and drawing_shape and shape_start and tool in ('rect','circle'):
                    x0, y0 = shape_start
                    x1, y1 = event.pos
                    # вычисляем итоговый цвет из mode
                    if mode == 'blue':   col = (0, 0, 255)
                    elif mode == 'red':  col = (255, 0, 0)
                    elif mode == 'green':col = (0, 255, 0)
                    else:                col = (0, 0, 255)
                    if tool == 'rect':
                        rect = (min(x0,x1), min(y0,y1), abs(x1-x0), abs(y1-y0))
                        shapes.append(('rect', rect, col))
                    else:
                        import math
                        r = int(math.hypot(x1-x0, y1-y0))
                        shapes.append(('circle', (x0, y0, r), col))
                    drawing_shape = False
                    shape_start = None
            
            if event.type == pygame.MOUSEMOTION:
                # исходная логика: копим точки — только для free/eraser и когда не тянем фигуру
                if not drawing_shape and tool in ('free','eraser'):
                    position = event.pos
                    points = points + [position]
                    points = points[-256:]
        
        # фон
        screen.fill((0, 0, 0))
        
        # НОВОЕ: отрисовать уже зафиксированные фигуры
        for kind, data, col in shapes:
            if kind == 'rect':
                pygame.draw.rect(screen, col, pygame.Rect(*data), 0)
            else:
                cx, cy, rr = data
                pygame.draw.circle(screen, col, (cx, cy), rr, 0)
        
        # НОВОЕ: превью тянущейся фигуры (контур)
        if drawing_shape and shape_start and tool in ('rect','circle'):
            x0, y0 = shape_start
            x1, y1 = pygame.mouse.get_pos()
            if mode == 'blue':   col = (0, 0, 255)
            elif mode == 'red':  col = (255, 0, 0)
            elif mode == 'green':col = (0, 255, 0)
            else:                col = (0, 0, 255)
            if tool == 'rect':
                rect = pygame.Rect(min(x0,x1), min(y0,y1), abs(x1-x0), abs(y1-y0))
                pygame.draw.rect(screen, col, rect, 2)
            else:
                import math
                r = int(math.hypot(x1-x0, y1-y0))
                pygame.draw.circle(screen, col, (x0, y0), r, 2)
        
        # draw all points (исходная часть) — с учётом ластика
        i = 0
        while i < len(points) - 1:
            cm = 'eraser' if tool == 'eraser' else mode
            drawLineBetween(screen, i, points[i], points[i + 1], radius, cm)
            i += 1
        
        pygame.display.flip()
        clock.tick(60)

def drawLineBetween(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    
    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    elif color_mode == 'eraser':      # НОВОЕ: «цвет» ластика — чёрный фон
        color = (0, 0, 0)
    
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy)) or 1  # защита от деления на ноль
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

main()
