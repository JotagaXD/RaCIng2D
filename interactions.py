import pygame

def no_control(player, oil_sprites):  # função que sinaliza a colisão do carrinho com o sprite do oleo
    if pygame.sprite.spritecollide(player, oil_sprites, False, pygame.sprite.collide_mask):
        return True
    else:
        return False

def slow(player, slow_sprites):   # função que sinaliza a colisão do carrinho com o sprite do slow
    if pygame.sprite.spritecollide(player, slow_sprites, False, pygame.sprite.collide_mask):
        return True
    else:
        return False

def difficult(lapse):  # função que aumentará a dificuldade do jogo em função do tempo
    return int(lapse*(9/10))
