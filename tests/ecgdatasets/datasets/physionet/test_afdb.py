import pytest

import os

from pathlib import Path

from ecgdatasets.datasets.physionet.afdb import AFDB

def test_AFDB_CASE_create_AND_no_exist():
    msg = 'Dataset not found. You can use download=True to download it.'

    with pytest.raises(RuntimeError, match=msg):
        AFDB('', '0.0.1', download=False, mapper=None)

@pytest.mark.skipif(os.getenv('EDBLOAD', None) is None, reason='Set EDBPATH to run tests.')
def test_AFDB_CASE_download_version_0_0_1():
    datadir = Path(__file__).parent.parent.parent.parent / 'files'

    AFDB(datadir, '0.0.1', download=True, mapper=None)
