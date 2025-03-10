import numpy as np

from pathlib import Path
from zipfile import ZipFile

from ecgdatasets.datasets.physionet.dataset import PhysioNetDataset

class AFDB(PhysioNetDataset):
    """AFDB. Read more in https://physionet.org/content/afdb/
    """
    default_version = '1.0.0'

    allowed_versions = [
        '1.0.0',
    ]

    hashs = {
        '1.0.0': '340a255db1a643b404f589d650495eb0',
    }

    def __init__(
        self,
        root,
        version,
        download=False,
        mapper=None,
        ):
        version = version if version in self.allowed_versions else self.default_version
        super().__init__(root, version, download, mapper)

    @property
    def frequency(self):
        return 250

    def __getitem__(self, idx):
        ecg = super().__getitem__(idx)

        return ecg

    @property
    def name(self):
        return 'afdb'

    @property
    def _fullname(self):
        return 'mit-bih-atrial-fibrillation-database'

    def _load_data(self):
        data = dict()

        with ZipFile(self._zippath, 'r') as zf:
            for path in zf.namelist():
                path = Path(path)

                if path.suffix == '.dat':
                    datpath = path
                    heapath = path.with_suffix('.hea')

        return data
