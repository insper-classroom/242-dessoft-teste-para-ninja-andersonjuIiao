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
cor_quadrado_1 = (243, 43, 59)
posicao_1 = (385, 284)
numeros_gerados.remove(quadrado_1)

quadrado_2 = random.choice(numeros_gerados)
quadrado_2_str = font.render(str(quadrado_2), True, (1, 1, 1))
cor_quadrado_2 = (111, 255, 9)
posicao_2 = (385, 384)
numeros_gerados.remove(quadrado_2)

quadrado_3 = random.choice(numeros_gerados)
quadrado_3_str = font.render(str(quadrado_3), True, (1, 1, 1))
cor_quadrado_3 = (4,75,255)
posicao_3 = (385, 484)

# ===== Loop principal =====
while game:

    # ----- Trata eventos
    for event in pygame.event.get():
        local_mouse = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (local_mouse[0]>= 350 and local_mouse[0] <= 450) and (local_mouse[1]> 250 and local_mouse[1] < 350):
                valor = quadrado_2 + quadrado_3
                if valor == resultado:
                    cor_quadrado_1 = (255, 255, 255)
                    posicao_1 = (350, 284)
                    quadrado_1_str = font.render("Certo!", True, (78, 255, 32))
                else:
                    cor_quadrado_1 = (255, 255, 255)
                    posicao_1 = (350, 284)
                    quadrado_1_str = font.render("Errado!", True, (255, 0, 0))
            elif (local_mouse[0]>= 350 and local_mouse[0] <= 450) and (local_mouse[1]> 350 and local_mouse[1] < 450):
                valor = quadrado_1 + quadrado_3
                if valor == resultado:
                    cor_quadrado_2 = (255, 255, 255)
                    posicao_2 = (350, 384)
                    quadrado_2_str = font.render("Certo!", True, (78, 255, 32))
                else:
                    cor_quadrado_2 = (255, 255, 255)
                    posicao_2 = (350, 384)
                    quadrado_2_str = font.render("Errado!", True, (255, 0, 0))
            elif (local_mouse[0]>= 350 and local_mouse[0] <= 450) and (local_mouse[1]> 450 and local_mouse[1] < 550):
                valor = quadrado_1 + quadrado_2
                if valor == resultado:
                    cor_quadrado_3 = (255, 255, 255)
                    posicao_3 = (350, 484)
                    quadrado_3_str = font.render("Certo!", True, (78, 255, 32))
                else:
                    cor_quadrado_3 = (255, 255, 255)
                    posicao_3 = (350, 484)
                    quadrado_3_str = font.render("Errado!", True, (255, 0, 0))

        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

    # ----- Gera saídas
    window.fill((255, 255, 255))  # Preenche com a cor branca
    pygame.draw.rect(window, cor_quadrado_1, pygame.Rect(350, 250, 100, 100))
    pygame.draw.rect(window, cor_quadrado_2, pygame.Rect(350, 350, 100, 100))
    pygame.draw.rect(window, cor_quadrado_3, pygame.Rect(350, 450, 100, 100))
    pygame.draw.rect(window, (203, 207, 205), pygame.Rect(0, 550, 800, 100))
    window.blit(resultado_str, (15, 15))
    window.blit(quadrado_1_str, posicao_1)
    window.blit(quadrado_2_str, posicao_2)
    window.blit(quadrado_3_str, posicao_3)
    pygame.display.flip()

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados