import numpy as np

from pathlib import Path
from zipfile import ZipFile

from ecgdatasets.datasets.physionet.dataset import PhysioNetDataset

class PTBXL(PhysioNetDataset):
    """PTBXL. Read more in https://physionet.org/content/ptb-xl/
    """

    default_version = '1.0.3'

    allowed_versions = [
        '1.0.3',
    ]

    hashs = {
        '1.0.3': '052c28a24e1a8ad222748bee399a79ee',
    }

    _raw_channel_order = [
        'i', 'ii', 'iii', 'avr', 'avl', 'avf', 'v1', 'v2', 'v3', 'v4', 'v5', 'v6'
    ]

    def __init__(
        self,
        root,
        version=default_version,
        download=False,
        mapper=None,
        ):
        version = version if version in self.allowed_versions else self.default_version
        super().__init__(root, version, download, mapper)

    @property
    def frequency(self):
        return 500

    def __getitem__(self, idx):
        """
        :args:
            idx (int): index
        """
        key = [*self.data.keys()][idx]

        return self.data[key]

    def __len__(self):
        return len(self.data)

    def extra_repr(self):
        return ''

    @property
    def _name(self):
        return 'ptb-xl'

    @property
    def _fullname(self):
        return 'ptb-xl-a-large-publicly-available-electrocardiography-dataset'

    @property
    def _hash(self):
        return self.hashs[self.version]

    def _load_data(self):
        data = dict()

        with ZipFile(self._zippath, 'r') as zf:
            for path in zf.namelist():
                if 'records500' in path:
                    path = Path(path)

                    if path.suffix == '.dat':
                        datpath = path
                        heapath = path.with_suffix('.hea')

                        ecg = zf.read(str(datpath))
                        ecg = np.frombuffer(ecg, np.int16)
                        ecg.shape = (5000, 12)

                        header = zf.read(str(heapath))

                        gains, baselines = [], []

                        for s in header.decode().split('\n')[1:13]:
                            s = s.split(' ')[2]
                            s = s.split('/')[0]
                            s = s.split(')')[0]

                            gain, baseline = s.split('(')

                            gains.append(float(gain))
                            baselines.append(int(baseline))

                        gains = np.array(gains)
                        baselines = np.array(baselines)

                        data[int(path.stem[:-3])] = (ecg - baselines) / gains

        return data
