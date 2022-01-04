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
            metadata_list.append(Metadata(file[0], file[1], file[2]))
        return metadata_list
