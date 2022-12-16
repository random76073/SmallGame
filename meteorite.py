import pygame
import random
import threading
import time
pygame.init()
class Meteorite:
	total = []
	frequent = 0
	path = ''
	size = ()
	window_size = ()
	def __init__(self, path=path, size=size):
		self.img = pygame.transform.scale(pygame.image.load(path), size)
		self.x = 0
		self.y = 0
		self.rect = self.img.get_rect()

	@classmethod
	def add(cls):
		cls.total.append(cls())

	@classmethod
	def generate(cls, event: threading.Event, ThreadList: dict, passScoreList: list[threading.Event()], item: int = None):
		while True:
			if (item is not None and passScoreList[item].is_set()) or item is None:
				cls.add()
				time.sleep(cls.frequent)
			else:
				ThreadList[cls].passEvent.wait()
			if not event.is_set():
				ThreadList[cls].pauseEvent.wait()

	def collide(self, host):
		if self.rect.colliderect(host.determine_rect):
			return 1
		else:
			return 0

	@classmethod
	def collideDetermine(cls, host):
		for total in cls.total:
			if total.collide(host):
				return 1
		return 0

	def draw(self, screen):
		screen.blit(self.img, (self.x, self.y))

	def move(self, direction=(0, 0, 0, 7)): # [left, right, front, down]
		self.x -= direction[0] - direction[1]
		self.y -= direction[2] - direction[3]
		self.rect.topleft = (self.x, self.y)

	def get_xy(self):
		return self.x, self.y

	@classmethod
	def clear(cls):
		score = 0
		for total in cls.total:
			xy = total.get_xy()
			if not (0 <= xy[0] <= cls.window_size[0] and 0 <= xy[1] <= cls.window_size[1]):
				cls.total.remove(total)
				score += 1
		return score

	@classmethod
	def clearAll(cls):
		cls.total.clear()

	@classmethod
	def set_frequent(cls, value):
		cls.frequent = value

class Meteorite1(Meteorite):
	total = []
	frequent = 0.02
	def __init__(self):
		super().__init__(super().path, super().size)
		self.x = random.randint(0, 938)


class Meteorite2_1(Meteorite):
	total = []
	frequent = 0.3
	def __init__(self):
		super().__init__(super().path, super().size)
		self.x = random.randint(480, 938)

	def move(self, direction: tuple[float, float, float, float] = (7, 0, 0, 4)):
		super().move(direction)


class Meteorite2_2(Meteorite):
	total = []
	frequent = 0.3
	def __init__(self):
		super().__init__(super().path, super().size)
		self.y = random.randint(0, 270)

	def move(self, direction: tuple[float, float, float, float] = (0, 7, 0, 4)):
		super().move(direction)

class Meteorite2_3(Meteorite):
	total = []
	frequent = 0.3
	def __init__(self):
		super().__init__(super().path, super().size)
		self.x = 960
		self.y = random.randint(0, 540)

	def move(self, direction: tuple[float, float, float, float] = (7, 0, 0, 0)):
		super().move(direction)

class Meteorite3(Meteorite):
	total = []
	frequent = 0.3
	def __init__(self):
		super().__init__(super().path, super().size)
		self.x = random.randint(0, 960)
		self.y = 540
		self.ay = 1.03
		self.direction = [0, 0, 1.1, 0]

	def move(self, direction: tuple[float, float, float, float] = (0, 0, 1.1, 0)):
		super().move(self.direction)
		self.direction[2] *= self.ay

class Meteorite4_1(Meteorite):
	total = []
	frequent = 0.1
	def __init__(self):
		super().__init__(super().path, super().size)
		self.direction = (0, random.randint(3, 7), 0, random.randint(3, 7))

	def move(self, direction=(0, 0, 0, 7)):
		super().move(self.direction)

class Meteorite4_2(Meteorite):
	total = []
	frequent = 0.1
	def __init__(self):
		super().__init__(super().path, super().size)
		self.x = 938
		self.direction = (random.randint(3, 7), 0, 0, random.randint(3, 7))

	def move(self, direction=(0, 0, 0, 7)):
		super().move(self.direction)

class Meteorite5(Meteorite):
	total = []
	frequent = 0.1
	def __init__(self):
		super().__init__(super().path, super().size)
		self.x = super().window_size[0] // 2
		self.y = super().window_size[1] // 2
		self.direction = (0, random.randint(-5, 5), 0, random.randint(-5, 5))
	def move(self, direction=(0, 0, 0, 0)):
		super().move(self.direction)


thread = {}
class MeteoriteThread(threading.Thread):
	def __init__(self, target, args: tuple, pauseEvent, passEvent):
		super().__init__(target=target, args=args)
		self.pauseEvent = pauseEvent
		self.passEvent = passEvent


def addClass(i, is_game: threading.Event, passScoreList: list, threadict: dict, item):
	if i not in thread:
		if item is not None:
			threadict[i] = MeteoriteThread(i.generate,
									(is_game, thread, passScoreList, item), is_game, passScoreList[item])
		else:
			threadict[i] = MeteoriteThread(i.generate,
									(is_game, thread, passScoreList, item), is_game, None)
		threadict[i].daemon = True
		threadict[i].start()

	return i




