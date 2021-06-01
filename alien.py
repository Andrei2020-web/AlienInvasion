from select import select

import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Класс, представляющий одного пришельца."""

    def __init__(self, ai_game):
        """Инициализирует пришельца и задаёт его начальную позицию."""
        super().__init__()
        self.screen = ai_game.screen

        """Загрузка изображения пришельца и назначение атрибута rect."""
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        """Каждый новый пишелец появляется в левом верхнм углу экрана."""
        self.rect.x = self.rect.x = self.rect.width
        self.rect.y = self.rect.x = self.rect.height

        """Сохранение точной горизонтальной позиции пришельца."""
        self.x = float(self.rect.x)

