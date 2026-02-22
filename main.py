import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state

def main():
  print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
  print(f"Screen width: {SCREEN_WIDTH}")
  print(f"Screen height: {SCREEN_HEIGHT}")
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

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
    # Refreshes screen.
    pygame.display.flip()

if __name__ == "__main__":
    main()
