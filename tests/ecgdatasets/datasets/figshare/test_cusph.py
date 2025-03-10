import pytest

import os

from pathlib import Path

from ecgdatasets.datasets.figshare.cusph import CUSPH

@pytest.mark.cusph
@pytest.mark.figshare
def test_CUSPH_CASE_create_AND_no_exist():
    msg = 'Dataset not found. You can use download=True to download it.'

    with pytest.raises(RuntimeError, match=msg):
        CUSPH('', download=False, mapper=None)

@pytest.mark.cusph
@pytest.mark.figshare
@pytest.mark.skipif(os.getenv('EDSLOAD', None) is None, reason='Set EDSLOAD to run tests.')
def test_CUSPH_CASE_create():
    datadir = Path(__file__).parent.parent.parent.parent / 'files'

    dataset = CUSPH(datadir, download=True, mapper=None)

    assert len(dataset) == 10646

    for datum in dataset:
        assert datum.shape == (5000, 12)
