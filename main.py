import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mario Animation")
grey_color = (128, 128, 128)

# Load Mario's sprites
walk_sprites = [pygame.image.load("assets/walk/walk1.jpeg")]
run_sprites = [pygame.image.load("assets/run/run1.jpeg"), pygame.image.load("assets/run/run2.jpeg"), pygame.image.load("assets/run/run3.jpeg"), pygame.image.load("assets/run/run4.jpeg")]
jump_sprites = [pygame.image.load("assets/jump/jump1.jpeg"), pygame.image.load("assets/jump/jump2.jpeg"), pygame.image.load("assets/jump/jump3.jpeg"), pygame.image.load("assets/jump/jump4.jpeg")]

# Set initial position and jump variables
x, y = 100, 300
initial_x, initial_y = x, y  # Armazenar a posição inicial
speed = 5

# Set initial animation and frame index
current_animation = walk_sprites
frame_index = 0
animation_speed = 10
counter = 0

# Function to handle events
def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

# Function to update Mario's position
def update_position(keys):
    global x, y, current_animation, initial_x, initial_y
    if keys[pygame.K_RIGHT]:
        x += speed
        current_animation = run_sprites
    elif keys[pygame.K_LEFT]:
        x -= speed
        current_animation = run_sprites
    else:
        current_animation = walk_sprites

    if keys[pygame.K_UP]:
        current_animation = jump_sprites
        # Simular um pequeno deslocamento no eixo y
        y -= 10

    if not keys[pygame.K_UP] and y < initial_y:
        y += 10  # Retornar à posição inicial se a tecla de seta para cima não estiver pressionada

# Função para atualizar o quadro da animação
def update_animation_frame():
    global frame_index, counter
    counter += 1
    if current_animation and len(current_animation) > 0:
        frame_index = (frame_index + 1) % len(current_animation)  # Usando operação de módulo

# Função para desenhar na tela
def draw_screen():
    screen.fill(grey_color)
    if current_animation and len(current_animation) > 0:
        screen.blit(current_animation[frame_index], (x, y))
    pygame.display.flip()

clock = pygame.time.Clock()

while True:
    handle_events()
    keys = pygame.key.get_pressed()
    update_position(keys)
    update_animation_frame()
    draw_screen()
    clock.tick(5)
