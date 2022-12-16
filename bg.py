import pygame

pygame.init()
class Background:
	def __init__(self, path: tuple, window_size: tuple):
		self.img = [pygame.transform.scale(pygame.image.load(i), window_size) for i in path]
		self.costume = 0
		self.rect = self.img[self.costume].get_rect()

	def draw(self, screen):
		screen.blit(self.img[self.costume], self.rect)

	def next_bg(self):
		self.costume += 1
		if self.costume > len(self.img) - 1:
			self.costume = 0

	def set_bg(self, costume):
		self.costume = costume
