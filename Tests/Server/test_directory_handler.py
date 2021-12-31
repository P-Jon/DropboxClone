import pytest

import os
from postbox.models.Metadata import Metadata
from postbox.helper.DirectoryHandler import DirectoryHandler

dir_prefix = os.getcwd()
directory = dir_prefix + "\\Server\\test_dir"
dir_handler = DirectoryHandler()

dir_string = "{ \"files\": [ {\"filename\": \"file1.txt\", \"size\": 77, \"last_edit\": 1640464854.159165}, {\"filename\": \"file2.txt\", \"size\": 0, \"last_edit\": 1640464825.9357572}] }"
dir_files = ['file1.txt', 'file2.txt']

def test_get_metadata():
    assert dir_handler.get_file_metadata(directory) == dir_string

def test_get_filenames():
    assert dir_handler.list_filenames(directory) == dir_files

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
    assert file[0] == "file2.txt"

def test_get_all_files():
    files = dir_handler.get_files(directory)
    assert files[0][0] == "file1.txt"