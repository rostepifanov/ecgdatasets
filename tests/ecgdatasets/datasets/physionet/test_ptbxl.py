import pytest

import os

from pathlib import Path

from ecgdatasets.datasets.physionet.ptbxl import PTBXL

@pytest.mark.ptbxl
@pytest.mark.physionet
def test_PTBXL_CASE_create_AND_no_exist():
    msg = 'Dataset not found. You can use download=True to download it.'

    with pytest.raises(RuntimeError, match=msg):
        PTBXL('', '1.0.3', download=False, mapper=None)

@pytest.mark.ptbxl
@pytest.mark.physionet
@pytest.mark.skipif(os.getenv('EDSLOAD', None) is None, reason='Set EDSLOAD to run tests.')
def test_PTBXL_CASE_download_version_1_0_3():
    datadir = Path(__file__).parent.parent.parent.parent / 'files'

    dataset = PTBXL(datadir, '1.0.3', download=True, mapper=None)

    assert len(dataset) == 21799

@pytest.mark.ptbxl
@pytest.mark.physionet
@pytest.mark.skipif(os.getenv('EDSLOAD', None) is None, reason='Set EDSLOAD to run tests.')
def test_PTBXL_CASE_check_shape():
    datadir = Path(__file__).parent.parent.parent.parent / 'files'

    dataset = PTBXL(datadir, '1.0.3', download=True, mapper=None)

    assert dataset[0].shape == (5000, 12)
