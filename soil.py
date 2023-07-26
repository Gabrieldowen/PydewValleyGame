import pygame
from settings import *
from pytmx.util_pygame import load_pygame
from support import *


class SoilTile(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft=pos)
        self.z = LAYERS['soil']


class SoilLayer:
    def __init__(self, all_sprites):

        # sprite groups
        self.all_sprites = all_sprites
        self.soil_sprites = pygame.sprite.Group()

        # graphics
        self.soil_surf = pygame.image.load('./graphics/soil/o.png')
        self.soil_surfs = import_folder_dict('./graphics/soil/')
        print(self.soil_surfs)

        self.create_soil_grid()
        self.create_hit_rect()
        # requirements
        #    if the area is farmable
        #    if the soil has been watered
        #    if the soil has a plant already

    def create_soil_grid(self):
        ground = pygame.image.load('./graphics/world/ground.png')
        h_tiles, v_tiles = ground.get_width() // TILE_SIZE, ground.get_height() // TILE_SIZE

        self.grid = [[[] for col in range(h_tiles)] for row in range(v_tiles)]
        for x, y, _ in load_pygame('./data/map.tmx').get_layer_by_name('Farmable').tiles():
            self.grid[y][x].append('F')

    def create_hit_rect(self):
        self.hit_rects = []
        for index_row, row in enumerate(self.grid):
            for index_col, cell in enumerate(row):
                x = index_col * TILE_SIZE
                y = index_row * TILE_SIZE
                rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)
                self.hit_rects.append(rect)

    def get_hit(self, point):
        for rect in self.hit_rects:  # converts pixel position to a tile position
            if rect.collidepoint(point):
                x = rect.x // TILE_SIZE
                y = rect.y // TILE_SIZE

                if 'F' in self.grid[y][x]:
                    self.grid[y][x].append('X')
                    self.create_soil_tiles()

    def create_soil_tiles(self):
        self.soil_sprites.empty()
        for index_row, row in enumerate(self.grid):
            for index_col, cell in enumerate(row):
                if 'X' in cell:
                    SoilTile(
                        pos=(index_col * TILE_SIZE, index_row * TILE_SIZE),
                        surf=self.soil_surf,
                        groups=[self.all_sprites, self.soil_sprites])