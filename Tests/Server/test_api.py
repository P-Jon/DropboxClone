import pytest

from Server.Server import Server

list_of_files = """
{ "files" : [ { "filename" : "test.txt", "size" : "0", "last_edit" : "001"},
{"filename" : "test2.txt", "size" : "2", "last_edit" : "002"} ] }"""

test_server = Server()

def test_get_metadata():
    assert "loud".upper() == "LOUD"

def test_lower():
    assert "LOWER".lower() == "lower"