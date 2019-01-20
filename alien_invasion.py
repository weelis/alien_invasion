#coding=GBK

import sys

import pygame

from settings import Settings

from ship import Ship

def run_game():
    """��ʼ����Ϸ������һ����Ļ����"""
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
    (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    # ����һ�ҷɴ�
    ship = Ship(screen)
    
    #���ñ���ɫ
    bg_color = (230, 230, 230)
    
    #��ʼ��Ϸ����ѭ��
    while True:
        
        """���Ӽ��̺����ʱ��"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        """ÿ��ѭ��ʱ���ػ���Ļ"""
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        """��������Ƶ���Ļ�ɼ�"""
        pygame.display.flip()
        
run_game()
