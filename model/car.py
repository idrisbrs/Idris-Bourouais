import pygame
import math
from constants import (
    CAR_ACCELERATION, CAR_WIDTH, CAR_HEIGHT, TILE_SIZE, CAR_ROTATION
)


class Car:

    def __init__(self, start_col: int, start_row: int,color: tuple[int, int, int] = (255, 0, 0)):
        self.x = start_col * TILE_SIZE + TILE_SIZE // 2
        self.y = start_row * TILE_SIZE + TILE_SIZE // 2
        self.speed: float = 0.0
        self.angle: float = 0.0
        self.color = color
        self.sprite = self.build_sprite()

    def accelerate(self) -> None:
        self.speed += CAR_ACCELERATION

    def brake(self) -> None:
        if self.speed > 0:
            self.speed = max(0.0, self.speed - CAR_ACCELERATION * 2)
        elif self.speed < 0:
            self.speed = min(0.0, self.speed + CAR_ACCELERATION * 2)
                

    def reverse(self) ->None:
        self.speed -= CAR_ACCELERATION
    def turn_left(self) -> None:
        self.angle -= CAR_ROTATION

    def turn_right(self) -> None:
        self.angle += CAR_ROTATION

    def update_position(self) -> None:
        rad = math.radians(self.angle)
        self.x += -math.sin(rad) * self.speed
        self.y += math.cos(rad) * self.speed

    def build_sprite(self) -> pygame.Surface:
        surf = pygame.Surface((CAR_WIDTH, CAR_HEIGHT), pygame.SRCALPHA)
        pygame.draw.rect(surf, self.color, (0, 0, CAR_WIDTH,CAR_HEIGHT), border_radius=5)
        return surf

    def get_rotated_sprite(self) -> tuple[pygame.Surface, pygame.Rect]:
        rotated = pygame.transform.rotate(self.sprite, -self.angle)
        rect = rotated.get_rect(center=(int(self.x), int(self.y)))
        return rotated, rect
