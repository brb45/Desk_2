"""Demonstrate tgt_dir_factory."""

import json
import pytest
import os

tgt_dir = "C:\\Users\jsun\Documents\Desk_1\Test_Slen\Pytest_proj\pytest_02\pytest_proj_4.0\\authors"

@pytest.fixture(scope='module')
def author_file_json():
    """Write some authors to a data file."""
    python_author_data = {
        'Ned': {'City': 'Boston'},
        'Brian': {'City': 'Portland'},
        'Luciano': {'City': 'Sau Paulo'}
    }
    target_dir = os.path.join(tgt_dir, "data")
    if not os.path.isdir(target_dir):
        os.makedirs(target_dir)
    file_name = os.path.join(target_dir,'author_file.json')
    with open(file_name, "w") as fout:
        json.dump(python_author_data, fout)

    return file_name
