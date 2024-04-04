import os 
import sys 
from pathlib import Path

ext = {
    'images': ('.jpeg', '.png', '.jpg', '.svg', '.dng'),
    'video': ('.avi', '.mp4', '.mov', '.mkv'),
    'documents': ('.doc', '.docx', '.txt', '.pdf', '.xls', '.xlsx', '.pptx', '.djvu', '.rtf'),
    'audio': ('.mp3', '.ogg', '.wav', '.amr'),
    'archives': ('.zip', '.gz', '.tar'),
}

main_folder: Path | None = None

def check_path(path_variable):
    
    global main_folder

    true_folder = Path(path_variable) 

    main_folder = true_folder

    check_files(main_folder)

def check_files(folder:Path):

    for file in folder.iterdir():

        if file.is_file:

            sort(file)

        if file.is_dir():

            check_files(file)

            if not any(file.iterdir()):
                
                file.rmdir()

def sort(file:Path):
    path = Path(file)

    file_ext = file.suffix.lower()
    file_stem = file.stem
    zero_station = 0 

    for key, values in ext.items():
        if file_ext in values:
            zero_station = key 
    
    if zero_station != 0:
        file_name = file_stem + file_ext

        end_folder = main_folder.joinpath(zero_station)

        end_folder.mkdir(exist_ok=True)

        new_file_path = end_folder.joinpath(file_name) 
        
        file.rename(new_file_path)
    
    else:
        file_name = file_stem + file_ext

        end_folder = main_folder.joinpath('another')

        end_folder.mkdir(exist_ok=True)
        
        new_file_path = end_folder.joinpath(file_name) 

        file.rename(new_file_path)