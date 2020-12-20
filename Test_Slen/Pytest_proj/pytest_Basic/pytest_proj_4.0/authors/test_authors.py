"""Some tests that use temp data files."""
import json


def test_brian_in_portland(author_file_json):
    """A test that uses a data file."""
    with open(author_file_json)  as f:
        authors = json.load(f)
    print('\n', authors['Brian']['City'])
    assert authors['Brian']['City'] == 'Portland'


def test_all_have_cities(author_file_json):
    """Same file is used for both tests."""
    with open(author_file_json) as f:
        authors = json.load(f)
    print("\n")
    for a in authors:
        print(a)
        assert len(authors[a]['City']) > 0
