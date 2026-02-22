import pygame
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, LINE_WIDTH
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
  
  # ROTATES PLAYER
  def rotate(self, dt):
    self.rotation += PLAYER_TURN_SPEED * dt

  # MOVES PLAYER
  def move(self, dt):
    # Start with unit vector pointing straight up
    unit_vector = pygame.Vector2(0, 1)
    # Rotate unit vector so it's pointing in the same direction as the player
    rotated_vector = unit_vector.rotate(self.rotation)
    # Multiply vector by player speed and delta time to calculate length player should move during this frame
    rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
    # Adds this vector to player, making them move.
    self.position += rotated_with_speed_vector
  
  # UPDATES PLAYER (adds player input via keyboard)
  def update(self, dt):
    keys = pygame.key.get_pressed()

    # Rotate player left when pressing "A"
    if keys[pygame.K_a]:
      self.rotate(-(dt))
    # Rotate player right when pressing "D"
    if keys[pygame.K_d]:
      self.rotate(dt)
    # Move player in direction it's facing when pressing "W"
    if keys[pygame.K_w]:
      self.move(dt)
    # Move player in opposite direction it's facing when pressing "S"
    if keys[pygame.K_s]:
      self.move(-(dt))