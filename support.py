from os import walk


def import_folder(path):
    surface_list = []

    # print(path)
    # walk will help return a list with all the contents of the folder
    for img_files in walk(path):
        print(img_files)

    return surface_list