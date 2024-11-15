from csv import reader

def import_csv_layout(path):
    
    with open(path) as level_map:
        print(level_map)

import_csv_layout("./map/map_FloorBlocks.csv") # que? CSV são arquivos de texto que usam vírgulas pra separar valores