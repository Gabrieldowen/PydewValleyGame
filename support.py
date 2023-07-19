# this file extracts images for animations
from os import walk
import pygame


def import_folder(path):
    surface_list = []

    # print(path)
    # walk will help return a list with all the contents of the folder
    for _, __, img_files in walk(path):
        for image in img_files:

            full_path = path + "/"+image
            print(full_path)
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)
    return surface_list
