class Settings():
    """Класс для хранения всех настроек игры."""

    def __init__(self):
        """Инициализирует статические настройки игры."""
        """Параметры экрана"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        """Параметры снаряда"""
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        """Настройки пришельцев"""
        self.fleet_drop_speed = 10

        """Настройки корабля"""
        self.ship_limit = 3

        """Темп ускорения игры."""
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Инициализирует настройки, изменяющиеся в ходе игры."""
        self.ship_speed = 1.5
        self.bullet_speed = 1.5
        self.alien_speed = 1.0

        # fleet_direction = 1 - движение вправо, -1 - движение влево.
        self.fleet_direction = 1

    def increase_speed(self):
        """Увеличивает настройки скорости."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
