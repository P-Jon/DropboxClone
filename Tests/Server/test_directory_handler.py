import pytest

import os
from postbox.helper.DirectoryHandler import DirectoryHandler

dir_prefix = os.getcwd()
directory = dir_prefix + "\\test_dir"
dir_handler = DirectoryHandler()

dir_string = "{ \"files\": [ {\"filename\": \"file1.txt\", \"size\": 77, \"last_edit\": 1640464854.159165}, {\"filename\": \"file2.txt\", \"size\": 0, \"last_edit\": 1640464825.9357572}] }"
dir_files = ['file1.txt', 'file2.txt']

def test_get_metadata():
    assert dir_handler.get_file_metadata(directory) == dir_string

def test_get_filenames():
    assert dir_handler.list_filenames(directory) == dir_files