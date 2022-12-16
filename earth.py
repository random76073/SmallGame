import pygame

pygame.init()
class Earth:
	def __init__(self, path: str, start_pos: tuple[int, int], limit: int, window_size: tuple[int, int], a_in: float, a_de: float, size, rect_size:tuple[int, int]):
		self.x,  self.y = start_pos
		self.start_pos = start_pos
		self.size = size
		self.img = pygame.transform.scale(pygame.image.load(path), self.size)
		self.ax = 0
		self.ay = 0
		self.direction = [0, 0, 0, 0] # [left, right, front, down]
		self.rect = self.img.get_rect()
		self.determine_rect = pygame.Rect(self.x + (self.size[0] - rect_size[0]) / 2, self.y + (self.size[1] - rect_size[1]) / 2, *rect_size)
		self.limit = limit
		self.limit_size = window_size
		self.a_in = a_in
		self.a_de = a_de

	def process(self):
		if -self.limit < self.ax < self.limit:
			if self.direction[0] == 1:
				self.ax -= self.a_in
			if self.direction[1] == 1:
				self.ax += self.a_in
		if self.direction[0] + self.direction[1] == 0:
			self.ax /= self.a_de
		if (0 >= self.x and self.ax < 0) or self.x + self.ax < 0 or (self.x >= self.limit_size[0] - self.size[0] and 0 < self.ax) or self.x + self.ax > self.limit_size[0] - self.size[0]:
			self.ax = 0
		self.x += self.ax
		if -self.limit < self.ay < self.limit:
			if self.direction[2] == 1:
				self.ay += self.a_in
			if self.direction[3] == 1:
				self.ay -= self.a_in
		if self.direction[2] + self.direction[3] == 0:
			self.ay /= self.a_de
		if (0 >= self.y and self.ay > 0) or self.y - self.ay < 0 or (self.y >= self.limit_size[1] - self.size[1] and 0 > self.ay) or self.y - self.ay > self.limit_size[1] - self.size[1]:
			self.ay = 0
		self.y -= self.ay

		self.rect.topleft = (self.x, self.y)
		self.determine_rect.topleft = (self.x + 11, self.y + 11)

	def change_direction(self, index, value):
		self.direction[index] = value

	def draw(self, screen):
		screen.blit(self.img, (self.x, self.y))

	def place(self, pos: tuple[int, int]):
		self.x = pos[0]
		self.y = pos[1]
		self.ax = 0
		self.ay = 0
		self.direction = [0, 0, 0, 0]
