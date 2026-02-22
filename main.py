import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from player import Player

def main():
  print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
  print(f"Screen width: {SCREEN_WIDTH}")
  print(f"Screen height: {SCREEN_HEIGHT}")
  # INITIALIZE GAME AND SCREEN
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  # INITIALIZE GAME CLOCK
  clock = pygame.time.Clock()
  dt = 0
  # INSTANTIATE PLAYER (in middle of screen)
  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

  # THE GAME LOOP
  while True:
    # LOG
    log_state()
    
    for event in pygame.event.get():
      # If game window close button is clicked, window closes and exits out of game loop.
      if event.type == pygame.QUIT:
        return
    
    # Fills screen with color black.
    screen.fill("black")
    # Re-render player on screen.
    player.draw(screen)
    # Refreshes screen.
    pygame.display.flip()
    # Pause game loop until 1/60th of a second has passed.
    dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
