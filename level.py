import pygame
from player import Player
from settings import *
from overlay import Overlay


class Level:
	def __init__(self):

		# get the display surface
		self.display_surface = pygame.display.get_surface()

		# sprite groups
		self.all_sprites = CameraGroup()

		self.setup()
		self.overlay = Overlay(self.player)

	def setup(self):
		self.player = Player((640, 360), self.all_sprites)

	def run(self, dt):
		self.display_surface.fill('black')
		self.all_sprites.draw(self.display_surface)
		self.all_sprites.update(dt)

		self.overlay.display()


class CameraGroup(pygame.sprite.Group):
	def __init__(self):
		super().__init__()

