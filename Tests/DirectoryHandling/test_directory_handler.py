import json

import os
from postbox.models.Metadata import Metadata
from postbox.helper.DirectoryHandler import DirectoryHandler

dir_prefix = os.getcwd()
directory = dir_prefix + "\\DirectoryHandling\\test_dir"
m_directory = directory + "\\subdir"
dir_handler = DirectoryHandler()

dir_string = "{ \"files\": [ {\"filename\": \"f1.txt\", \"size\": 27, \"last_edit\": 1641445804.7520137}, {\"filename\": \"f2.txt\", \"size\": 6, \"last_edit\": 1641445807.146239}] }"
dir_files = ['f1.txt', 'f2.txt']

files_json = "{\"files\": [[\"file1.txt\", \"This is intended to be a file used for testing the serverside directory code.\", 1641277099.040298, 1640919720.8362603], [\"file2.txt\", \"\", 1640919720.8372598, 1640919720.8372598]]}"
file2_json = ['file2.txt', '', 1640919720.8372598, 1640919720.8372598]

def test_get_metadata():
    assert dir_handler.get_file_metadata(m_directory) == dir_string

def test_get_filenames():
    assert dir_handler.list_filenames(m_directory) == dir_files

# Ensuring the similarity is true, aka files are the same.
f1 = Metadata("x.txt",0,0)
f2 = Metadata("x.txt",0,0)
f3 = Metadata("y.txt",0,1) # Filename isn't evaluated here...

def test_similarity_true():
    assert dir_handler.detect_change(f1,f2) == True

# Ensuring the similarity is false, aka the files are different.
def test_similarity_false():
    assert dir_handler.detect_change(f1,f3) == False

def test_get_file():
    file = dir_handler.get_file(directory, "file2.txt")
    assert file[0] == file2_json[0]

def test_get_all_files():
    files = dir_handler.get_files(directory)
    f_json = json.loads(files)
    files = f_json.get("files")
    assert files[0][0] == "file1.txt"
    