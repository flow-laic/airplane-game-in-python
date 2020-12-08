import pygame

"""
pygame.Rect是一个比较特殊的类，内部只是封装了一些数字计算
不执行pygame.init()方法同样能够直接使用

左上角为原点位置
"""

hero_rect = pygame.Rect(100, 500, 120, 125)

print("英雄的原点 %d %d" % (hero_rect.x, hero_rect.y))
print("英雄的尺寸 %d %d" % (hero_rect.width, hero_rect.height))
print("%d %d" % hero_rect.size)
