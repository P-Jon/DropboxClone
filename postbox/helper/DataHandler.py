from postbox.models.Metadata import Metadata
class DataHandler(object):

    @staticmethod
    def strip_metadata_from_json(metadata_json):
        '''
        Expecting a JSON list of metadata
        '''
        metadata_list = []
        metadata_json = metadata_json.get("files")
        for file in metadata_json:
            metadata_list.append(Metadata(file.get("filename"), file.get("size"), file.get("last_edit")))
        return metadata_list
