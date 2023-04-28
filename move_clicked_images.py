import pygame

# --- constants ---

RED = (213, 43, 67)

# --- classes ---

class Item(pygame.sprite.Sprite):

    def __init__(self, image, x, y):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect(x=x, y=y)

    def update(self, rel):
        self.rect.move_ip(rel)

# --- main ---

pygame.init()
screen = pygame.display.set_mode((800,600))

items = pygame.sprite.Group(
    Item("base_2.png", 150, 50),
    Item("base_2.png", 400, 50), 
    Item("base_2.png", 150, 300),
    Item("base_2.png", 400, 300),
)

dragged = pygame.sprite.Group()

# --- mainloop ---

clock = pygame.time.Clock()
game_exit = False

while not game_exit:

    # - events -
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            dragged.add(x for x in items if x.rect.collidepoint(event.pos))          
        elif event.type == pygame.MOUSEBUTTONUP:
            dragged.empty()
        elif event.type == pygame.MOUSEMOTION:
            dragged.update(event.rel)

    # - draws -            
    screen.fill(RED)
    items.draw(screen)
    pygame.display.update()

    # - FPS -
    clock.tick(30)

# --- end ---

pygame.quit() 