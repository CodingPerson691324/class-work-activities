import pygame

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 700, 700

display_surface = pygame,display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption('ading background and images')

background_image = pygame.transform.scale(
    pygame.image.load('fruitbowl.jpg').convert(),
    (SCREEN_WIDTH, SCREEN_HEIGHT)
)

apple_image = pygame.transform.scale(
    pygame.image.load('the shiny apple.webp').convert_alpha(),
    (300,300)
)

apple_rect = apple_image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 150))

text = pygame.font.Font(None, 36).render('This is The Shiny Apple',True, pygame.Color('red'))

text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 150))