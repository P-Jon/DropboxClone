import pytest

from postbox.server.ServerLogic import PBServer

list_of_files = """
{ "files" : [ { "filename" : "test.txt", "size" : "0", "last_edit" : "001"},
{"filename" : "test2.txt", "size" : "2", "last_edit" : "002"} ] }"""

test_server = PBServer()

dir_path = ".\\test_dir"

def test_get_metadata():
    assert "loud".upper() == "LOUD"

def test_lower():
    assert "LOWER".lower() == "lower"

def test_list_files():
    assert True