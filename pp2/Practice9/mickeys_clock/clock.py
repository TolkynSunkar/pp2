import pygame
import datetime

class MickeyClock:
    def __init__(self, screen, center):
        self.screen = screen
        self.center = center

        self.hand = pygame.image.load("images/mickey_hand.png")
        self.hand = pygame.transform.scale(self.hand, (150, 30))

    def draw(self):
        now = datetime.datetime.now()

        seconds = now.second
        minutes = now.minute

        sec_angle = - (seconds / 60) * 360
        min_angle = - (minutes / 60) * 360

        sec_hand = pygame.transform.rotate(self.hand, sec_angle)
        min_hand = pygame.transform.rotate(self.hand, min_angle)

        sec_rect = sec_hand.get_rect(center=self.center)
        min_rect = min_hand.get_rect(center=self.center)

        self.screen.blit(min_hand, min_rect)
        self.screen.blit(sec_hand, sec_rect)