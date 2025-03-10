import pandas as pd

from pathlib import Path
from zipfile import ZipFile

from ecgdatasets.datasets.figshare.dataset import FigShareDataset

class CUSPH(FigShareDataset):
    """CUSPH. Read more in https://figshare.com/collections/_/4560497
    """

    _raw_channel_order = [
        'i', 'ii', 'iii', 'avr', 'avl', 'avf', 'v1', 'v2', 'v3', 'v4', 'v5', 'v6'
    ]

    @property
    def frequency(self):
        return 500

    def __getitem__(self, idx):
        ecg = super().__getitem__(idx)

        return ecg

    @property
    def name(self):
        return 'cusph'

    @property
    def _id(self):
        return '15651326'

    @property
    def _hash(self):
        return '2bf32d649e30c5648ba4a5938a1398f8'

    def _load_data(self):
        data = dict()

        with ZipFile(self._zippath, 'r') as zf:
            for path in zf.namelist():
                path = Path(path)

                if path.suffix == '.csv':
                    with zf.open(str(path)) as f:
                        ecg = pd.read_csv(f).to_numpy()

                        data[path.stem] = ecg

        return data
