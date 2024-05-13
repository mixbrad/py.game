# ----- Importa e inicia pacotes
import pygame
import random

pygame.init()
relogio= pygame.time.Clock()
fps=60


#definição das cores
branco=(255,255,255)
preto=(0,0,0)
cinza=(128,128,128) 
vermelho=(255,0,0)
laranja=(255,128,0)
verde=(0,255,0)
azul=(0,0,255)
roxo=(238,130,238)
amarelo=(255,255,0)
rosa=(255,192,203)
cores=[vermelho, laranja, amarelo, verde, azul, roxo, rosa ]

#definição da tela e da fonte
altura= 770
largura= 500
screen= pygame.display.set_mode((largura, altura))
fonte= pygame.font.Font("freesansbold.ttf", 30)
clock= pygame.time.Clock()


#definicão das variáveis do jogador e da bola
jogador_x= 190
bola_x= largura/2
bola_y= altura-30
tabuleiro= [[5,5,5,5,5],[4,4,4,4,4],[3,3,3,3,3],[2,2,2,2,2],[1,1,1,1,1]]

def desenhar_tabuleiro(tabuleiro):
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro[i])):
            pygame.draw.rect(screen, cores[(tabuleiro[i][j])-1], [j*100, i*40, 98, 38])

run= True
while run:
    screen.fill(cinza)
    relogio.tick(fps)
    desenhar_tabuleiro(tabuleiro)
    jogador= pygame.draw.rect(screen, preto, [jogador_x, altura-20, 120, 15], 0, 3)
    bola= pygame.draw.circle(screen, branco, (bola_x, bola_y), 10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run= False
    
    pygame.display.flip()
pygame.quit()
