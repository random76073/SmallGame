import xml.etree.ElementTree as Et
from ui import *
from bg import *
from earth import *
from meteorite import *
dom = Et.parse('info.xml')
data = dom.getroot()
for a in data:
	for b in a:
		if b.tag == 'name':
			name = b.text
		if b.tag == 'fps':
			fps = int(b.text)
		if b.tag == 'version':
			version = b.text
		if b.tag == 'game':
			for c in b:
				if c.tag == 'music':
					for d in c:
						if d.tag == 'path':
							music_path = d.text
						if d.tag == 'volume':
							volume = float(d.text)
				if c.tag == 'windows':
					for d in c:
						if d.tag == 'size':
							window_size = tuple((int(i) for i in d.text.split(', ')))
				if c.tag == 'background':
					for d in c:
						bg = Background(tuple(d.text.split(', ')), window_size)
				if c.tag == 'earth':
					earth = Earth(c.find('path').text, tuple((int(i) for i in c.find('start_pos').text.split(', '))), int(c.find('limit').text), window_size, float(c.find('a_in').text), float(c.find('a_de').text), tuple((int(i) for i in c.find('size').text.split(', '))), tuple((int(i) for i in c.find('rect_size').text.split(', '))))
				if c.tag == 'meteorite':
					Meteorite.size = tuple((int(i) for i in c.find('size').text.split(', ')))
					Meteorite.path = c.find('path').text
					Meteorite.window_size = window_size
		if b.tag == 'ui':
			for c in b:
				if c.tag == 'font':
					for d in c:
						if d.tag == 'simhei':
							simheiFont1 = pygame.font.Font(d.find('path').text, tuple((int(i) for i in d.find('size').text.split(', ')))[0])
							simheiFont2 = pygame.font.Font(d.find('path').text, tuple((int(i) for i in d.find('size').text.split(', ')))[1])
						if d.tag == 'FCS':
							FCSFont1 = pygame.font.Font(d.find('path').text, tuple((int(i) for i in d.find('size').text.split(', ')))[0])
							FCSFont2 = pygame.font.Font(d.find('path').text, tuple((int(i) for i in d.find('size').text.split(', ')))[1])
						if d.tag == 'square':
							SquareFont1 = pygame.font.Font(d.find('path').text, tuple((int(i) for i in d.find('size').text.split(', ')))[0])

				if c.tag == 'text_surface':
					for d in c:
						if d.tag == 'pauseText':
							pauseText1 = simheiFont2.render(d.find('_1').find('text').text, True, tuple((int(i) for i in d.find('_1').find('f_color').text.split(', '))), tuple((int(i) for i in d.find('_1').find('bg_color').text.split(', '))))
							pauseText2 = simheiFont1.render(d.find('_2').find('text').text, True, tuple((int(i) for i in d.find('_2').find('f_color').text.split(', '))), tuple((int(i) for i in d.find('_2').find('bg_color').text.split(', '))))
							pauseText1Pos = tuple((int(i) for i in d.find('_1').find('pos').text.split(', ')))
							pauseText2Pos = tuple((int(i) for i in d.find('_2').find('pos').text.split(', ')))
						if d.tag == 'remainText':
							remainText = simheiFont1.render(d.find('text').text, True, tuple((int(i) for i in d.find('f_color').text.split(', '))), tuple((int(i) for i in d.find('bg_color').text.split(', '))))
						if d.tag == 'restartText':
							restartText = simheiFont1.render(d.find('text').text, True, tuple((int(i) for i in d.find('f_color').text.split(', '))), tuple((int(i) for i in d.find('bg_color').text.split(', '))))
						if d.tag == 'scoreRecordText':
							SRT_f_color = tuple((int(i) for i in d.find('f_color').text.split(', ')))
							SRT_bg_color = tuple((int(i) for i in d.find('bg_color').text.split(', ')))
				if c.tag == 'panel':
					for d in c:
						if d.tag == 'scorePanel':
							scorePanel = Panel(FCSFont1, tuple((int(i) for i in d.find('color').text.split(', '))), tuple((int(i) for i in d.find('pos').text.split(', '))))
							scorePanelText = d.find('text').text
						if d.tag == 'fpsPanel':
							fpsPanel = Panel(FCSFont2, tuple((int(i) for i in d.find('color').text.split(', '))), tuple((int(i) for i in d.find('pos').text.split(', '))), True)
							fpsPanelText = d.find('text').text
						if d.tag == 'versionPanel':
							versionPanel = Panel(FCSFont2, tuple((int(i) for i in d.find('color').text.split(', '))), tuple((int(i) for i in d.find('pos').text.split(', '))), True)
							versionPanelText = d.find('text').text
						if d.tag == 'volumePanel':
							volumePanel = Panel(FCSFont2, tuple((int(i) for i in d.find('color').text.split(', '))), tuple((int(i) for i in d.find('pos').text.split(', '))), True)
							volumePanelText = d.find('text').text
						if d.tag == 'timePanel':
							timePanel = Panel(SquareFont1, tuple((int(i) for i in d.find('color').text.split(', '))), tuple((int(i) for i in d.find('pos').text.split(', '))))
							timePanelText = d.find('text').text
				if c.tag == 'backdrop':
					for d in c:
						if d.tag == 'pauseBackdrop':
							screen = pygame.display.set_mode(window_size)
							pauseBackdrop = pygame.Surface(tuple((int(i) for i in d.find('size').text.split(', ')))).convert_alpha()
							pauseBackdrop.fill(tuple((int(i) for i in d.find('color').text.split(', '))))
							pauseBackdropPos = tuple((int(i) for i in d.find('pos').text.split(', ')))
						if d.tag == 'finishBackdrop':
							finishBackdrop = pygame.Surface(tuple((int(i) for i in d.find('size').text.split(', '))))
							finishBackdrop.fill(tuple((int(i) for i in d.find('color').text.split(', '))))
							finishBackdropPos = tuple((int(i) for i in d.find('pos').text.split(', ')))
				if c.tag == 'button':
					for d in c:
						if d.tag == 'RestartButton':
							RestartButton_bgcolor = tuple((int(i) for i in d.find('bgcolor').text.split(', ')))
							RestartButton_topleft = tuple((int(i) for i in d.find('topleft').text.split(', ')))
						if d.tag == 'RemainHighestScoreButton':
							RemainHighestScoreButton_bgcolor = tuple((int(i) for i in d.find('bgcolor').text.split(', ')))
							RemainHighestScoreButton_topleft = tuple((int(i) for i in d.find('topleft').text.split(', ')))
pygame.init()
clock = pygame.time.Clock()
pygame.mixer.init()
pygame.display.set_caption(name)
game = 1
fullscreen = 0
paused = 0

pauseWindow = pygame.rect.Rect((280, 170), (400, 200))
pygame.mixer.music.load(music_path)
pygame.mixer.music.set_volume(volume)
is_game = threading.Event()
passScoreList = [threading.Event() for i in range(4)]
def restart():
	return 1
meteoriteList = []
