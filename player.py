import pygame
from constants import PLAYER_RADIUS, LINE_WIDTH
from circleshape import CircleShape

# CREATES PLAYER AS CIRCLE (physically as a hitbox)
class Player(CircleShape):
  def __init__(self, x, y):
    super().__init__(x, y, PLAYER_RADIUS)

    self.rotation = 0
  
  # CALCULATES POINTS OF TRIANGLE (for drawing of triangle)
  def triangle(self):
    forward = pygame.Vector2(0, 1).rotate(self.rotation)
    right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
    a = self.position + forward * self.radius
    b = self.position - forward * self.radius - right
    c = self.position - forward * self.radius + right
    return [a, b, c]

  # DRAWS PLAYER (as triangle on screen)
  def draw(self, screen):
    pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)