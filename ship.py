#coding=GBK

import pygame

class Ship():
    def __init__(self, screen):
        """��ʼ���ɴ����������ʼλ��"""
        self.screen = screen
        
        """���طɴ�ͼ�񲢻�ȡ����Ӿ���"""
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        #��ÿ���·ɴ�������Ļ�ײ�����
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
    def blitme(self):
        """��ָ��λ�û��Ʒɴ�"""
        self.screen.blit(self.image, self.rect)
        
