import pytest

import os

from pathlib import Path

from ecgdatasets.datasets.physionet.incartdb import INCARTDB

@pytest.mark.incartdb
@pytest.mark.physionet
def test_INCARTDB_CASE_create_AND_no_exist():
    msg = 'Dataset not found. You can use download=True to download it.'

    with pytest.raises(RuntimeError, match=msg):
        INCARTDB('', '1.0.0', download=False, mapper=None)

@pytest.mark.incartdb
@pytest.mark.physionet
@pytest.mark.skipif(os.getenv('EDSLOAD', None) is None, reason='Set EDSLOAD to run tests.')
def test_INCARTDB_CASE_download_version_1_0_0():
    datadir = Path(__file__).parent.parent.parent.parent / 'files'

    dataset = INCARTDB(datadir, '1.0.0', download=True, mapper=None)

    assert len(dataset) == 75

@pytest.mark.incartdb
@pytest.mark.physionet
@pytest.mark.skipif(os.getenv('EDSLOAD', None) is None, reason='Set EDSLOAD to run tests.')
def test_INCARTDB_CASE_check_shape():
    datadir = Path(__file__).parent.parent.parent.parent / 'files'

    dataset = INCARTDB(datadir, '1.0.0', download=True, mapper=None)

    assert dataset[0].shape == (462600, 12)
