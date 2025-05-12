from recursos.funcoes import limparTela, aguardarTempo
import pygame
pygame.init()
largura = 800
altura = 600
fps = pygame.time.Clock()
dimensao = (largura, altura)
tela = pygame.display.set_mode(dimensao)
pygame.display.set_caption("Iron Man Marcão")
branco = (255, 255, 255)
preto = (0, 0, 0)
fundoStart = pygame.image.load("assets/fundoStart.jpg")
fundoJogo = pygame.image.load("assets/fundoJogo.png")
fonteMenu = pygame.font.SysFont("comicsans", 18)

def jogar():
    ironMan = pygame.image.load("assets/iron.png")
    posicaoXIron = 300
    posicaoYIron = 300
    movimentoXIron = 0
    movimentoYIron = 0
    while True:
        eventos = pygame.event.get()
        for evento in eventos:
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    movimentoYIron =  movimentoYIron - 10 
                elif evento.key == pygame.K_DOWN:
                    movimentoYIron =  movimentoYIron + 10
                elif evento.key == pygame.K_LEFT:
                    movimentoXIron =  movimentoXIron - 10
                elif evento.key == pygame.K_RIGHT:
                    movimentoXIron = movimentoXIron + 10
            elif evento.type == pygame.KEYUP:
                movimentoXIron = 0
                movimentoYIron = 0
                
        tela.fill(branco)
        tela.blit(fundoJogo, (0, 0) )


        posicaoXIron = posicaoXIron + movimentoXIron
        posicaoYIron = posicaoYIron + movimentoYIron    
        
        if posicaoXIron >= 800:
            posicaoXIron = 799
        if posicaoXIron <= 0:
            posicaoXIron = 1

        if posicaoYIron >= 550:
            posicaoYIron = 549
        if posicaoYIron <= 5:
            posicaoYIron = 6


    
        tela.blit(ironMan, (posicaoXIron,posicaoYIron) )
        
        
        pygame.display.update()
        fps.tick(60)

def start():
    while True:
        eventos = pygame.event.get()
        for evento in eventos:
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif evento.type == pygame.MOUSEBUTTONUP:
                if quitButton.collidepoint(evento.pos):
                    pygame.quit()
                    quit()
                if startButton.collidepoint(evento.pos):
                    jogar()
                
        tela.fill(branco)
        tela.blit(fundoStart, (0, 0) )
        
        startButton = pygame.draw.rect(tela, branco, (10, 10, 150, 40), border_radius=20)
        startText = fonteMenu.render("Iniciar Jogo", True, preto)
        tela.blit(startText, (25,12))      
        
        quitButton = pygame.draw.rect(tela, branco, (10, 60, 150, 40), border_radius=20)
        quitText = fonteMenu.render("Sair do Jogo", True, preto)
        tela.blit(quitText, (25,62))      
        
        pygame.display.update()
        fps.tick(60)


start()