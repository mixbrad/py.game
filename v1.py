# ----- Importa e inicia pacotes
import pygame
import random

#definição de variaveis pro jogo
pygame.init()
relogio= pygame.time.Clock()
fps=60
fonte= pygame.font.Font("freesansbold.ttf", 30)
clock= pygame.time.Clock()
active= False
pontuacao= 0

#definição das cores
branco=(255,255,255)
preto=(0,0,0)
cinza=(128,128,128) 
vermelho=(255,0,0)
laranja=(255,128,0)
verde=(0,255,0)
azul=(0,0,255)
roxo=(138,43,226)
amarelo=(255,255,0)
rosa=(255,105,180)
cores=[vermelho, laranja, amarelo, verde, azul, roxo, rosa ]

def criar_tabuleiro_aleatorio():
    tabuleiro_aleatorio= []
    linhas= random.randint(6, 10)
    for i in range(linhas):
        linha= []
        for j in range(7):
            linha.append(random.randint(1, 7))
        tabuleiro_aleatorio.append(linha)
    return tabuleiro_aleatorio

#definição da tela e da fonte
altura= 770
largura= 500
tela= pygame.display.set_mode((largura, altura))
#tabuleiro= [[7,7,7,7,7],[6,6,6,6,6],[5,5,5,5,5],[4,4,4,4,4],[3,3,3,3,3],[2,2,2,2,2],[1,1,1,1,1]]
tabuleiro=[ ]
criar_novo= True
def desenhar_tabuleiro(tabuleiro):
    tabuleiro_alvos=[]
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro[i])):
            if tabuleiro[i][j]>0: 
                alvos= pygame.draw.rect(tela, cores[(tabuleiro[i][j])-1], [j*100, i*40, 98, 38], 0, 3)
                pygame.draw.rect(tela, preto, [j*100, i*40, 98, 38], 3, 3)
                limite_alto= pygame.rect.Rect((j*100, i*40), (98, 1))
                limite_baixo= pygame.rect.Rect((j*100, (i*40)+37), (98, 1))
                esquerda= pygame.rect.Rect((j*100, i*40), (37, 1))
                direita= pygame.rect.Rect(((j*100)+97 , i*40), (37, 1)) 
                tabuleiro_alvos.append([limite_alto, limite_baixo, esquerda, direita, (i, j)])
    return tabuleiro_alvos


#definicão das variáveis do jogador e da bola
jogador_x= 190
bola_x= largura/2
bola_y= altura-30
movimento_bola_x= 0
movimento_bola_y= 0
velocidade_bola_x= 5
velocidade_bola_y= 5
velocidade_jogador= 10
movimento_jogador= 0

run= True
while run:
    tela.fill(cinza)
    relogio.tick(fps)
    if criar_novo:
        tabuleiro= criar_tabuleiro_aleatorio()
        criar_novo= False
    alvos= desenhar_tabuleiro(tabuleiro)
    jogador= pygame.draw.rect(tela, preto, [jogador_x, altura-20, 120, 15], 0, 3)
    pygame.draw.rect(tela, branco, [jogador_x +5, altura-18, 110, 11], 3, 3)
    bola= pygame.draw.circle(tela, branco, (bola_x, bola_y), 10)
    pygame.draw.circle(tela, preto, (bola_x, bola_y), 10, 3)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run= False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not active:
                active= True 
                movimento_bola_y= -1
                movimento_bola_x= random.choice ([-1, 1])
                pontuacao= 0
            if event.key == pygame.K_RIGHT and active:
                movimento_jogador= 1
            if event.key == pygame.K_LEFT and active:
                movimento_jogador= -1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                movimento_jogador= 0
            if event.key == pygame.K_LEFT:
                movimento_jogador= 0

    #delimitação para a bola não sair do tabuleiro
    if bola_x <= 10 or bola_x >= largura-10:
        movimento_bola_x*= -1

    for i in range(len(alvos)):
        if bola.colliderect(alvos[i][0]) or bola.colliderect(alvos[i][1]):
            movimento_bola_y*= -1
            tabuleiro[alvos[i][4][0]][alvos[i][4][1]]-= 1
            pontuacao+=1
        if (bola.colliderect(alvos[i][2]) and movimento_bola_x == 1) or (bola.colliderect(alvos[i][3])  and movimento_bola_x == -1):
            movimento_bola_x *= -1
            tabuleiro[alvos[i][4][0]][alvos[i][4][1]]-= 1
            pontuacao+=1

    #delimitação para a bola não passar pelo jogador
    if bola.colliderect(jogador):
        if movimento_jogador== movimento_bola_x:
            velocidade_bola_x+=1
        elif movimento_jogador == -movimento_bola_x and velocidade_bola_x > 1:
            velocidade_bola_x -=1
        elif movimento_jogador == -movimento_bola_x and velocidade_bola_x == 1:
            movimento_bola_x *=1

        movimento_bola_y*= -1

    #movimento da bola
    bola_y+= movimento_bola_y* velocidade_bola_y
    bola_x+= movimento_bola_x* velocidade_bola_x

    if bola_y <= 10:
        movimento_bola_y= 10
        movimento_bola_y*= -1

    if bola_y >= altura -10 or len(alvos)== 0:
        active= False
        jogador_x= 190
        bola_x= largura/2
        bola_y= altura-30
        movimento_bola_x= 0
        movimento_bola_y= 0
        velocidade_bola_x= 5
        velocidade_bola_y= 5
        velocidade_jogador= 10
        movimento_jogador= 0
        criar_novo= True
    
    
    #movimento do jogador sem sair da tela
    jogador_x+=movimento_jogador* velocidade_jogador
    if jogador_x <= 0:
        jogador_x= 0
    if jogador_x >= largura-120:
        jogador_x= largura-120
    
   
    pontuacao_texto= fonte.render(f'Pontuação: {pontuacao}', True, branco)
    tela.blit(pontuacao_texto, (12, 7))

    if not active:
        texto_incio= fonte.render("Pressione ESPACO para iniciar", True, branco)
        tela.blit(texto_incio, (25, 400))
    
    pygame.display.flip()
pygame.quit()
