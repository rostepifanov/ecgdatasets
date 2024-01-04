import pytest

import os

from pathlib import Path

from ecgdatasets.datasets.physionet.ludb import LUBD

@pytest.mark.ludb
@pytest.mark.physionet
def test_LUBD_CASE_create_AND_no_exist():
    msg = 'Dataset not found. You can use download=True to download it.'

    with pytest.raises(RuntimeError, match=msg):
        LUBD('', '1.0.1', download=False, mapper=None)

@pytest.mark.ludb
@pytest.mark.physionet
@pytest.mark.skipif(os.getenv('EDSLOAD', None) is None, reason='Set EDSLOAD to run tests.')
def test_LUBD_CASE_download_version_1_0_1():
    datadir = Path(__file__).parent.parent.parent.parent / 'files'

    dataset = LUBD(datadir, '1.0.1', download=True, mapper=None)

    assert len(dataset) == 200

@pytest.mark.ludb
@pytest.mark.physionet
@pytest.mark.skipif(os.getenv('EDSLOAD', None) is None, reason='Set EDSLOAD to run tests.')
def test_LUBD_CASE_check_shape():
    datadir = Path(__file__).parent.parent.parent.parent / 'files'

    dataset = LUBD(datadir, '1.0.1', download=True, mapper=None)

    assert dataset[0].shape == (5000, 12)
