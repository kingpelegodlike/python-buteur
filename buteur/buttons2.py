import sys
import pygame
import pygame.gfxdraw

pygame.init()
screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()
buttons = pygame.sprite.Group()
class Button(pygame.sprite.Sprite):
    def __init__(self, position, text, size,
        colors="white on blue",
        hover_colors="red on green",
        style=1, borderc=(255,255,255),
        command=lambda: print("No command activated for this button")):
        # the hover_colors attribute needs to be fixed
        super().__init__()
        self.text = text
        self.command = command
        # --- colors ---
        self.colors = colors
        self.original_colors = colors
        self.foreground, self.background = self.colors.split(" on ")
        if hover_colors == "red on green":
            self.hover_colors = f"{self.background} on {self.foreground}"
        else:
            self.hover_colors = hover_colors
        self.style = style
        self.borderc = borderc # for the style2
        # font
        self.font = pygame.font.SysFont("Arial", size)
        self.render()
        self.xaxis, self.yaxis, self.width , self.height = self.text_render.get_rect()
        self.xaxis, self.yaxis = position
        self.rect = pygame.Rect(self.xaxis, self.yaxis, self.width, self.height)
        self.position = position
        self.pressed = 1
        buttons.add(self)

    def render(self):
        self.text_render = self.font.render(self.text, 1, self.foreground)
        self.image = self.text_render

    def update(self):
        self.foreground, self.background = self.colors.split(" on ")
        if self.style == 0:
            self.draw_button0()
        elif self.style == 1:
            self.draw_button1()
        elif self.style == 2:
            self.draw_button2()
        self.hover()
        self.click()

    def draw_button0(self):
        ''' a linear border '''
        pygame.draw.rect(screen, self.background, (self.xaxis, self.yaxis, self.width , self.height))
        pygame.gfxdraw.rectangle(screen, (self.xaxis, self.yaxis, self.width , self.height), (211,211,211))

    def draw_button1(self):
        ''' draws 4 lines around the button and the background '''
        # horizontal up
        pygame.draw.line(screen, (150, 150, 150), (self.xaxis, self.yaxis), (self.xaxis + self.width , self.yaxis), 5)
        pygame.draw.line(screen, (150, 150, 150), (self.xaxis, self.yaxis - 2), (self.xaxis, self.yaxis + self.height), 5)
        # horizontal down
        pygame.draw.line(screen, (50, 50, 50), (self.xaxis, self.yaxis + self.height), (self.xaxis + self.width , self.yaxis + self.height), 5)
        pygame.draw.line(screen, (50, 50, 50), (self.xaxis + self.width , self.yaxis + self.height), [self.xaxis + self.width , self.yaxis], 5)
        # background of the button
        pygame.draw.rect(screen, self.background, (self.xaxis, self.yaxis, self.width , self.height))

    def draw_button2(self):
        ''' a linear border '''
        pygame.draw.rect(screen, self.background, (self.xaxis, self.yaxis, self.width , self.height))
        pygame.gfxdraw.rectangle(screen, (self.xaxis, self.yaxis, self.width , self.height), self.borderc)

    def hover(self):
        ''' checks if the mouse is over the button and changes the color if it is true '''
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            # you can change the colors when the pointer is on the button if you want
            if self.style != 0:
                self.colors = self.hover_colors
            # pygame.mouse.set_cursor(*pygame.cursors.diamond)
        else:
            self.colors = self.original_colors

        self.render()

    def click(self):
        ''' checks if you click on the button and makes the call to the action just one time'''
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0] and self.pressed == 1 and self.style != 0:
                print("Execunting code for button '" + self.text + "'")
                self.command()
                self.pressed = 0
            if pygame.mouse.get_pressed() == (0,0,0):
                self.pressed = 1




# FUNCTIONS for the buttons on click
# I used this convention ... on_+text of the button

def on_click():
    print("Ciao bello")

def on_run():
    print("Ciao bello questo è RUN")

def on_save():
    print("This is Save")

def buttons_def():
    Button((300, 300), "Click me now", 55, "black on white", command=on_click)
    Button((10, 100), "Run the program", 40, "black on red", command=on_run)
    Button((10, 170), "Save this file", 36, "red on yellow", hover_colors="blue on orange", style=2, borderc=(255,255,0), command=on_save)

# ======================= this code is just for example, start the program from the main file
# in the main folder, I mean, you can also use this file only, but I prefer from the main file
# 29.8.2021

if __name__ == '__main__':
    pygame.init()
    # game_on = 0
    def loop():
        # BUTTONS ISTANCES
        game_on = 1
        buttons_def()
        while True:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    game_on = 0
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        game_on = 0
            if game_on:
                buttons.update()
                buttons.draw(screen)
            else:
                pygame.quit()
                sys.exit()
            buttons.draw(screen)
            clock.tick(60)
            pygame.display.update()
        pygame.quit()




    loop()
