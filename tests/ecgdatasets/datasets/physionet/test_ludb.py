import pytest

import os

from pathlib import Path

from ecgdatasets.datasets.physionet.ludb import LUBD

def test_LUBD_CASE_create_AND_no_exist():
    msg = 'Dataset not found. You can use download=True to download it.'

    with pytest.raises(RuntimeError, match=msg):
        LUBD('', '1.0.1', download=False, mapper=None)

@pytest.mark.skipif(os.getenv('EDBLOAD', None) is None, reason='Set EDBLOAD to run tests.')
def test_LUBD_CASE_download_version_1_0_1():
    datadir = Path(__file__).parent.parent.parent.parent / 'files'

    LUBD(datadir, '1.0.1', download=True, mapper=None)
