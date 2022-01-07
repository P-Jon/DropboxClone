from postbox.client.ClientRepository import ClientRepository
from postbox.models.Metadata import Metadata

client_repo = ClientRepository()

metadata_match_1 = []
metadata_match_1.append(Metadata("f1.txt", 2, 0))
metadata_match_1.append(Metadata("f2.txt", 3, 40))
metadata_match_1.append(Metadata("f3.txt", 4, 20))

metadata_match_2 = []
# Mixing up the order... just incase
metadata_match_2.append(Metadata("f1.txt", 2, 0))
metadata_match_2.append(Metadata("f3.txt", 4, 20))
metadata_match_2.append(Metadata("f2.txt", 3, 40))

metadata_unmatch = []
metadata_unmatch.append(Metadata("f1.txt", 1, 0))
metadata_unmatch.append(Metadata("f3.txt", 1, 0))

metadata_new_files = metadata_match_1[:]
metadata_new_files.append(Metadata("new.txt", 50, 30))

# Similar meaning of the same length, disimilar meaning not of the same length.
def test_check_metadata_true_similar():
    flag, flagged_files = client_repo.check_metadata_match(metadata_match_1, metadata_match_2)
    assert flag == True

def test_check_metadata_false_similar():
    flag, flagged_files = client_repo.check_metadata_match(metadata_match_1, metadata_unmatch)
    assert flag == False

def test_check_metadata_true_dissimilar():
    m2 = metadata_match_2[:] # Python pass by ref means this would pop the original list
    m2.pop()
    flag, flagged_files = client_repo.check_metadata_match(metadata_match_1, m2)
    assert flag == False

def test_check_metadata_false_dissimilar():
    flag, flagged_files = client_repo.check_metadata_match(metadata_match_1, metadata_unmatch)
    assert flag == False

def test_check_deleted_files_true():
    files = client_repo.check_deleted_files(metadata_match_1, metadata_unmatch)
    flag = False
    if len(files) > 0:
        flag = True
    assert flag == True and files[0] == 'f2.txt'

def test_check_deleted_files_false():
    files = client_repo.check_deleted_files(metadata_match_1, metadata_match_2)
    flag = False
    if len(files) > 0:
        flag = True
    assert flag == False

def test_check_new_files_true():
    flag, files = client_repo.check_new_file_data(metadata_match_1, metadata_new_files)
    assert flag == True and files[0] == 'new.txt'

def test_check_new_files_false():
    flag, files = client_repo.check_new_file_data(metadata_match_1, metadata_match_2)
    assert flag == False