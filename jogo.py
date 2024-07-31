# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import gerador
import random

pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# ----- Gera tela principal
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Gerador')

# ----- Inicia estruturas de dados
game = True

# ----- Inicia assets
numeros_gerados = gerador.gera_numeros()
font = pygame.font.SysFont(None, 48)

resultado = numeros_gerados[0]
resultado_str = font.render(str(resultado), True, (1, 1, 1))
numeros_gerados.remove(resultado)

quadrado_1 = random.choice(numeros_gerados)
quadrado_1_str = font.render(str(quadrado_1), True, (1, 1, 1))
numeros_gerados.remove(quadrado_1)

quadrado_2 = random.choice(numeros_gerados)
quadrado_2_str = font.render(str(quadrado_2), True, (1, 1, 1))
numeros_gerados.remove(quadrado_2)

quadrado_3 = random.choice(numeros_gerados)
quadrado_3_str = font.render(str(quadrado_3), True, (1, 1, 1))

# ===== Loop principal =====
while game:
    # ----- Trata eventos
    for event in pygame.event.get():
        local_mouse = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (local_mouse[0]>= 350 and local_mouse[0] <= 450) and (local_mouse[1]> 300 and local_mouse[1] < 400):
                print(str(quadrado_1))
            elif (local_mouse[0]>= 350 and local_mouse[0] <= 450) and (local_mouse[1]> 400 and local_mouse[1] < 500):
                print(str(quadrado_2))
            elif (local_mouse[0]>= 350 and local_mouse[0] <= 450) and (local_mouse[1]> 500 and local_mouse[1] < 600):
                print(str(quadrado_3))

        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

    # ----- Gera saídas
    window.fill((255, 255, 255))  # Preenche com a cor branca
    pygame.draw.rect(window, (243, 43, 59), pygame.Rect(350, 300, 100, 100))
    pygame.draw.rect(window, (111, 255, 9), pygame.Rect(350, 400, 100, 100))
    pygame.draw.rect(window, (4,75,255), pygame.Rect(350, 500, 100, 100))
    window.blit(resultado_str, (15, 15))
    window.blit(quadrado_1_str, (385, 334))
    window.blit(quadrado_2_str, (385, 434))
    window.blit(quadrado_3_str, (385, 534))
    pygame.display.flip()

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados