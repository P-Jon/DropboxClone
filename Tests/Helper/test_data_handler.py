import json
from postbox.helper.DataHandler import DataHandler

example_json = "{\
    \"files\": [\
        {\
            \"filename\": \"d.txt\",\
            \"size\": 18,\
            \"last_edit\": 1640654640.293093\
        },\
        {\
            \"filename\": \"new_test.txt\",\
            \"size\": 7,\
            \"last_edit\": 1641174818.2565708\
        },\
        {\
            \"filename\": \"oh.txt\",\
            \"size\": 7,\
            \"last_edit\": 1641181089.8676162\
        },\
        {\
            \"filename\": \"Test.txt\",\
            \"size\": 0,\
            \"last_edit\": 1640392004.4416108\
        }\
    ]\
}"

def test_metadata_strip():
    data = json.loads(example_json)
    metadata = DataHandler.strip_metadata_from_json(data)
    assert metadata[0].filename == "d.txt"