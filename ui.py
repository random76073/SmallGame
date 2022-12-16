import pygame
import pickle as pk
pygame.init()


class Button:
	def __init__(self, topleft: tuple[float, float], command, text: pygame.surface.Surface, bgcolor=(0, 0, 0), args=None, rect=None):
		self.pos = topleft
		self.function = command
		self.args = args
		self.text = text
		self.bgcolor = bgcolor
		self.touch_mouse = False
		if not rect:
			self.rect = self.text.get_rect()
			self.rect.topleft = self.pos
		else:
			self.rect = rect
		self.surface = pygame.Surface(self.rect.size)
		self.surface.fill(self.bgcolor)

	def draw(self, screen: pygame.Surface):
		screen.blit(self.surface, self.pos)
		screen.blit(self.text, self.rect)

	def click(self, mousex, mousey):
		if self.rect.collidepoint(mousex, mousey):
			try:
				return self.function(*self.args)
			except TypeError:
				return self.function()


def save(score):
	try:
		with open('score.dat', 'rb') as file:
			scoreRecord = pk.load(file)
		with open('score.dat', 'wb+') as file:
			pk.dump(scoreRecord + str(score) + '\n', file, 1)
	except (EOFError, FileNotFoundError):
		with open('score.dat', 'wb') as file:
			scoreRecord = ''
			pk.dump(str(score) + '\n', file, 1)

	finally:
		return scoreRecord + str(score)

def remain(scoreRecord):
	scoreList = sorted([int(i) for i in scoreRecord], reverse=True)
	highest_score = scoreList[0]
	scoreRecord = str(highest_score)
	with open('score.dat', 'wb') as fil:
		pk.dump(scoreRecord + '\n', fil, 1)
	return highest_score

class Panel:
	def __init__(self, font: pygame.font.Font, color, pos, is_alpha: bool = False):
		self.font = font
		self.color = color
		self.pos = pos
		self.is_alpha = is_alpha

	def draw(self, screen, text: str):
		text = self.font.render(text, True, self.color)
		if self.is_alpha:
			text = text.convert_alpha()
		screen.blit(text, self.pos)



