import pygame
from pygame.draw import *
from random import randint, sample
pygame.init()

FPS = 200
screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
x = 100
y = 100
r = 50
dx = 1
dy =1
dxcool = 1
dycool = 1
last_ticks = 0
inp = True
clock = pygame.time.Clock()
finished = False
A = []
n = 0
circles = [(x, y, r, dx, dy)]
coolcircles = [(x, y, r, dxcool, dycool)]
name = ""
down = False


while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

        elif event.type == pygame.MOUSEBUTTONDOWN:
            A = pygame.mouse.get_pos()
            x1 = A[0]
            y1 = A[1]
            for i in range(len(circles)):
                xc, yc, rc = circles[i][:3]
                if ((x1-xc)**2 + (y1-yc)**2)**0.5 <= r:
                    del circles[i]
                    n+=1
                    break
                else:
                    pass
            for j in range(len(coolcircles)):
                xc, yc, rc = coolcircles[j][:3]
                if ((x1 - xc) ** 2 + (y1 - yc) ** 2) ** 0.5 <= r:
                    del coolcircles[j]
                    n += abs(1*dxcool)
                    break
                else:
                    pass

    cur_ticks = pygame.time.get_ticks()

    if cur_ticks - last_ticks >= 3000:
        dycool += randint(1, 10) * 0.1 * (dycool / abs(dycool))
        dxcool += randint(1, 10) * 0.1 * (dxcool / abs(dxcool))
        dxcool *= sample([-1, 1], 1)[0]
        dycool *= sample([-1, 1], 1)[0]
        circles.append([100, 200, 50, dx, dy])
        coolcircles.append([100, 200, 20, dxcool, dycool])
        last_ticks = cur_ticks


    for i in range(len(circles)):
        xi, yi, ri, dxi, dyi = circles[i]
        xi += dxi
        yi += dyi
        circle(screen, COLORS[0], (xi, yi), ri)
        if xi >= 1150 or xi < 50:
            v = dxi**2 + dyi**2
            dxi = randint(1, int(v**0.5 * 100) - 1) * 0.01 * (abs(dxi) / dxi) * -1
            dyi = (v - dxi**2)**0.5 * (abs(dyi) / dyi)
        if yi >= 850 or yi < 50:
            v = dxi**2 + dyi**2
            dyi = randint(1, int(v ** 0.5 * 100) - 1) * 0.01 * (abs(dyi) / dyi) * -1
            dxi = (v - dyi ** 2) ** 0.5 * (abs(dxi) / dxi)
        circles[i] = [xi, yi, ri, dxi, dyi]

    for i in range(len(coolcircles)):
        xi, yi, ri, dxi, dyi = coolcircles[i]
        xi += dxi
        yi += dyi
        circle(screen, COLORS[2], (xi, yi), ri)
        if xi >= 1150 or xi < 50:
            v = dxi**2 + dyi**2
            dxi = randint(1, int(v**0.5 * 100) - 1) * 0.01 * (abs(dxi) / dxi) * -1
            dyi = (v - dxi**2)**0.5 * (abs(dyi) / dyi)
        if yi >= 850 or yi < 50:
            v = dxi**2 + dyi**2
            dyi = randint(1, int(v ** 0.5 * 100) - 1) * 0.01 * (abs(dyi) / dyi) * -1
            dxi = (v - dyi ** 2) ** 0.5 * (abs(dxi) / dxi)
        coolcircles[i] = [xi, yi, ri, dxi, dyi]

    text = pygame.font.Font(None, 100).render('Счёт:' + str(n),
                                                  True, (255, 255, 255))
    screen.blit(text, (80, 300))
    pygame.display.update()
    screen.fill(BLACK)
pygame.quit()
