import pygame
import random
import math
import sys

# 初始化pygame
pygame.init()

# 设置窗口
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("樱花雨")

# 颜色定义
PINK = (255, 192, 203)
LIGHT_PINK = (255, 182, 193)
WHITE = (255, 255, 255)
BACKGROUND = (240, 240, 250)

# 樱花花瓣类
class Petal:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(-50, -10)
        self.size = random.randint(2, 5)
        self.speed = random.uniform(1, 3)
        self.angle = 0
        self.rotation_speed = random.uniform(0.01, 0.05)
        self.max_rotation = random.uniform(0.5, 2)
        self.swing = random.uniform(0.5, 2)
        self.swing_speed = random.uniform(0.01, 0.03)
        self.color = random.choice([PINK, LIGHT_PINK, WHITE])
        
    def fall(self):
        self.y += self.speed
        self.angle += self.rotation_speed
        self.x += math.sin(self.y * self.swing_speed) * self.swing
        
        # 如果花瓣落到底部，重新从顶部开始
        if self.y > HEIGHT:
            self.y = random.randint(-50, -10)
            self.x = random.randint(0, WIDTH)
            
    def draw(self):
        # 绘制旋转的花瓣（简化版，实际可以用图片更美观）
        points = []
        for i in range(5):
            angle = self.angle + i * math.pi * 2 / 5
            points.append((
                self.x + math.cos(angle) * self.size,
                self.y + math.sin(angle) * self.size
            ))
        pygame.draw.polygon(screen, self.color, points)

# 创建樱花花瓣
petals = [Petal() for _ in range(150)]

# 添加地面樱花堆积效果
ground_petals = []
for _ in range(50):
    ground_petals.append((
        random.randint(0, WIDTH),
        random.randint(HEIGHT - 20, HEIGHT),
        random.randint(2, 5),
        random.choice([PINK, LIGHT_PINK, WHITE])
    ))

# 主循环
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # 填充背景色
    screen.fill(BACKGROUND)
    
    # 绘制地面堆积的樱花
    for petal in ground_petals:
        x, y, size, color = petal
        pygame.draw.circle(screen, color, (x, y), size)
    
    # 更新和绘制飘落的樱花
    for petal in petals:
        petal.fall()
        petal.draw()
    
    # 随机添加新的地面樱花（模拟堆积效果）
    if random.random() < 0.02:
        ground_petals.append((
            random.randint(0, WIDTH),
            HEIGHT - 10,
            random.randint(2, 5),
            random.choice([PINK, LIGHT_PINK, WHITE])
        ))
        # 保持地面樱花数量不超过100
        if len(ground_petals) > 100:
            ground_petals.pop(0)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()