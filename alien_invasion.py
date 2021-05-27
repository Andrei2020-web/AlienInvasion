import sys
import pygame
from settings import Settings


class AlienInvasion():
    """Класс для управления ресурсами и поведением игры."""

    def __init__(self):
        """Инициализирует игру и создаёт игровые ресурсы."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                               self.settings.screen_height))
        pygame.display.set_caption("Инопланетное вторжение")
        """Назначение цвета фона"""
        self.bg_color = self.settings.bg_color

    def run_game(self):
        """Запуск основного цикла игры."""
        while True:
            """Отслеживание событи клавиатуры и мыши."""
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            """При каждом проходе цикла перерисовывается икран."""
            self.screen.fill(self.bg_color)
            """Отобажение последнего прорисованного экрана."""
            pygame.display.flip()


if __name__ == '__main__':
    """Создаём экземпляр и стартуем игру."""
    ai = AlienInvasion()
    ai.run_game()
