# -*- coding: utf-8 -*-
# !usr/bin/python
from parse import *
from sys import exit
while True:
	pygame.mixer.music.play(loops=-1)
	score = 0
	ScoreRecord = 0
	for i in thread.keys(): # concern it
		i.clearAll()
	for i in passScoreList:
		i.clear()
	meteoriteList = [addClass(Meteorite1, is_game, passScoreList, thread, None)]
	is_game.set()
	meteoriteList[0].set_frequent(0.02)
	bg.set_bg(0)
	earth.place(earth.start_pos)
	timer = 0
	while game:
		while not paused:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					exit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_w:
						earth.change_direction(2, 1)
					if event.key == pygame.K_s:
						earth.change_direction(3, 1)
					if event.key == pygame.K_a:
						earth.change_direction(0, 1)
					if event.key == pygame.K_d:
						earth.change_direction(1, 1)

					if event.key == pygame.K_SPACE or event.key == pygame.K_PAUSE:
						paused = 1

					if event.key == pygame.K_KP_PLUS:
						if volume < 1:
							volume += 0.1
							pygame.mixer.music.set_volume(volume)
					if event.key == pygame.K_KP_MINUS:
						if volume > 0:
							volume -= 0.1
							pygame.mixer.music.set_volume(volume)
				if event.type == pygame.KEYUP:
					if event.key == pygame.K_w:
						earth.change_direction(2, 0)
					if event.key == pygame.K_s:
						earth.change_direction(3, 0)
					if event.key == pygame.K_a:
						earth.change_direction(0, 0)
					if event.key == pygame.K_d:
						earth.change_direction(1, 0)
			if score >= 400 and not passScoreList[0].is_set():
				bg.next_bg()
				passScoreList[0].set()
				meteoriteList.append(addClass(Meteorite2_1, is_game, passScoreList, thread, 0))
				meteoriteList.append(addClass(Meteorite2_2, is_game, passScoreList, thread, 0))
				meteoriteList.append(addClass(Meteorite2_3, is_game, passScoreList, thread, 0))
				meteoriteList[0].set_frequent(0.1)
			if score >= 700 and not passScoreList[1].is_set():
				bg.next_bg()
				passScoreList[1].set()
				meteoriteList.append(addClass(Meteorite3, is_game, passScoreList, thread, 1))
			if score >= 900 and not passScoreList[2].is_set():
				bg.next_bg()
				passScoreList[2].set()
				meteoriteList.append(addClass(Meteorite4_1, is_game, passScoreList, thread, 2))
				meteoriteList.append(addClass(Meteorite4_2, is_game, passScoreList, thread, 2))
				meteoriteList[4].set_frequent(0.2)
				meteoriteList[3].set_frequent(0.5)
				meteoriteList[2].set_frequent(0.5)
				meteoriteList[1].set_frequent(0.5)
			if score >= 1200 and not passScoreList[3].is_set():
				bg.next_bg()
				passScoreList[3].set()
				meteoriteList.append(addClass(Meteorite5, is_game, passScoreList, thread, 3))
				meteoriteList[0].set_frequent(0.05)
				meteoriteList[4].set_frequent(0.5)
				meteoriteList[3].set_frequent(1)
				meteoriteList[2].set_frequent(1)
				meteoriteList[1].set_frequent(1)
			bg.draw(screen)
			earth.process()
			earth.draw(screen)
			for i in meteoriteList:
				score += i.clear()
				for total in i.total:
					total.move()
					total.draw(screen)
				if i.collideDetermine(earth):
					game = 0
					break
			else:
				scorePanel.draw(screen, scorePanelText.format(score))
				fpsPanel.draw(screen, fpsPanelText % clock.get_fps())
				versionPanel.draw(screen, versionPanelText + version)
				volumePanel.draw(screen, volumePanelText + str(int(volume * 100)))
				timePanel.draw(screen, timePanelText % timer)
				pygame.display.update()
				clock.tick(fps)
				timer += clock.get_time() / 1000
				continue
			break
		screen.blit(pauseBackdrop, pauseBackdropPos)
		pygame.mixer.music.pause()
		is_game.clear()
		while paused:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					exit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_SPACE or event.key == pygame.K_PAUSE:
						paused = 0

					if event.key == pygame.K_KP_PLUS:
						if volume < 1:
							volume += 0.1
							pygame.mixer.music.set_volume(volume)
					if event.key == pygame.K_KP_MINUS:
						if volume > 0:
							volume -= 0.1
							pygame.mixer.music.set_volume(volume)
			pygame.draw.rect(screen, (0, 0, 64), pauseWindow)
			screen.blit(pauseText1, pauseText1Pos)
			screen.blit(pauseText2, pauseText2Pos)
			pygame.display.update()
			clock.tick(fps)
		pygame.mixer.music.unpause()
		is_game.set()
	is_game.clear()
	pygame.mixer.music.stop()
	ScoreRecord = save(score).split('\n')
	scoreRecordText = []
	for i in ScoreRecord:
		scoreRecordText.append(simheiFont1.render(i, True, SRT_f_color, SRT_bg_color))
	RemainHighestScoreButton = Button(text=remainText, command=remain, args=(ScoreRecord,), topleft=RemainHighestScoreButton_topleft,
									  bgcolor=RemainHighestScoreButton_bgcolor)
	RestartButton = Button(text=restartText, topleft=RestartButton_topleft, bgcolor=RestartButton_bgcolor, command=restart)
	while not game:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if RemainHighestScoreButton.click(*pygame.mouse.get_pos()):
					scoreRecordText = [simheiFont1.render(str(RemainHighestScoreButton.click(*pygame.mouse.get_pos())),
														 True, SRT_f_color, SRT_bg_color)]
				if RestartButton.click(*pygame.mouse.get_pos()):
					game = 1
					break
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_F11:
					fullscreen = fullscreen * -1 + 1
					if fullscreen:
						screen = pygame.display.set_mode(window_size, pygame.FULLSCREEN)
					else:
						screen = pygame.display.set_mode(window_size)
		else:
			bg.draw(screen)
			screen.blit(finishBackdrop, finishBackdropPos)
			y = 0
			for i in scoreRecordText:
				screen.blit(i, (240, y))
				y += 24
			del y
			RemainHighestScoreButton.draw(screen)
			RestartButton.draw(screen)
			pygame.display.update()
			clock.tick(fps)
