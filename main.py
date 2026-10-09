import pygame

pygame.init()
screen = pygame.display.set_mode((1000,1000))

font=pygame.font.SysFont("Arial",128)

def renderText(message:str) -> pygame.Surface:
    return font.render(message,True,(255,255,255))


text=renderText("Hello World !")

screen.blit(text,(0,0))
pygame.display.flip()
pygame.time.wait(5000)