from csv import reader
from os import walk
import pygame

# eu não aguento mais, nunca me arrependi tanto de usar o tiled

def import_csv_layout(path):
    
    terrain_map = []
    with open(path) as level_map:
        layout = reader (level_map, delimiter = ",")
        for row in layout:
            terrain_map.append(list(row))

        return terrain_map

# CSV são arquivos de texto que usam vírgulas pra separar valores

def import_folder(path):

    surface_list = []
    
    for _, _, img_files in walk (path):
        for image in img_files:
            full_path = path + "/" + image
            image_surf = pygame.image.load (full_path).convert_alpha()
            surface_list.append (image_surf)
             
    return surface_list
