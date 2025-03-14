import numpy as np

from pathlib import Path
from zipfile import ZipFile

from ecgdatasets.datasets.physionet.dataset import PhysioNetDataset

class PTBXL(PhysioNetDataset):
    """PTBXL. Read more in https://physionet.org/content/ptb-xl/
    """

    default_version = '1.0.3'

    allowed_versions = [
        '1.0.1',
        '1.0.3',
    ]

    hashs = {
        '1.0.1': 'f1558ce941870ba39402ba6a1b96f5e6',
        '1.0.3': '052c28a24e1a8ad222748bee399a79ee',
    }

    _lengths = {
        '1.0.1': 21837,
        '1.0.3': 21799,
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
        """
            :args:
                root (string): root directory of dataset.
                version (string): version of dataset for usage.
                download (bool):  If true, downloads the dataset from the internet and
                    puts it in root directory. If dataset is already downloaded, it is
                    not downloaded again.
                mapper(callable or None):   function to transform targets. If None, it
                    is used default mapper.
        """
        version = version if version in self.allowed_versions else self.default_version
        super().__init__(root, version, download, mapper)

    @property
    def frequency(self):
        return 500

    def __getitem__(self, idx):
        ecg = super().__getitem__(idx)

        return ecg

    @property
    def name(self):
        return 'ptb-xl'

    @property
    def _fullname(self):
        return 'ptb-xl-a-large-publicly-available-electrocardiography-dataset'

    def _load_data(self):
        data = dict()

        with ZipFile(self._zippath, 'r') as zf:
            for path in zf.namelist():
                if 'records500' in path:
                    path = Path(path)

                    if path.suffix == '.dat':
                        datpath = path
                        heapath = path.with_suffix('.hea')

                        header = zf.read(str(heapath))
                        lines = header.decode().split('\n')

                        _, nleads, _, length = lines[0].split(' ')[:4]

                        ecg = zf.read(str(datpath))
                        ecg = np.frombuffer(ecg, np.int16)
                        ecg.shape = (int(length), int(nleads))

                        gains, baselines = [], []

                        for s in lines[1:int(nleads)+1]:
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
