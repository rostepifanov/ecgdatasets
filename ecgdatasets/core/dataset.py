from tqdm import tqdm
from requests import get
from pathlib import Path
from torch.utils.data import Dataset

import ecgdatasets.core.misc as M

class EcgDataset(Dataset):
    """Base class for making datasets which are compatible with ecgdatasets.
       It is necessary to override the ``__getitem__`` and ``__len__`` method.
    """

    _repr_indent = 4

    _default_channel_order = [
        'i', 'ii', 'iii', 'avr', 'avl', 'avf', 'v1', 'v2', 'v3', 'v4', 'v5', 'v6'
    ]

    def __init__(
        self,
        root,
        download=False,
        mapper=None,
        ):
        """
            :args:
                root (string): root directory of dataset.
                download (bool):  If true, downloads the dataset from the internet and
                    puts it in root directory. If dataset is already downloaded, it is
                    not downloaded again.
                mapper(callable or None):   function to transform targets. If None, it
                    is used default mapper.
        """
        self.root = Path(root).expanduser()
        self.mapper = mapper

        if download:
            self.download()

        if not self._check_integrity():
            raise RuntimeError('Dataset not found. You can use download=True to download it.')

        self.data = self._load_data()

    @property
    def frequency(self):
        """
            :return:
                the original frequency of the dataset
        """
        raise NotImplementedError

    def __getitem__(self, idx):
        """
            :args:
                idx (int): index of an accessed dataset item

            :return:
                ...
        """
        key = [*self.data.keys()][idx]

        return self.data[key]

    def __len__(self):
        """
            :return:
                the length of the dataset
        """
        return len(self.data)

    @property
    def name(self):
        """
            :return:
                shortname of the dataset
        """
        raise NotImplementedError

    def __repr__(self):
        """
            :return:
                the string representation of the dataset
        """
        head = 'Dataset ' + self.name.upper()
        body = [f'Number of datapoints: {self.__len__()}']

        if self.root is not None:
            body.append(f'Root location: {self.root}')

        body += self.extra_repr().splitlines()

        lines = [head] + [' ' * self._repr_indent + line for line in body]
        return '\n'.join(lines)

    def extra_repr(self):
        return ''

    @property
    def _zippath(self):
        return self.root / ( self.name + '.zip' )

    @property
    def _hash(self):
        raise NotImplementedError

    @property
    def _url(self):
        raise NotImplementedError

    def _check_integrity(self):
        return M._check_integrity(self._zippath, self._hash, M._calculate_md5)

    def download(self):
        if self._check_integrity():
            return

        req = get(self._url, stream=True)

        if req.status_code == 200:
            if not self._zippath.parent.is_dir():
                self._zippath.parent.mkdir(parents=True, exist_ok=True)

            length = (int(req.headers['Content-Length']) + 127) // 128

            with open(self._zippath, 'wb') as f:
                for chunk in tqdm(req, total=length):
                    f.write(chunk)
        else:
            raise RuntimeError('Remote resourse {} is not avialable.'.format(self._url))

    def _load_data(self):
        """
            :return:
                data that loaded from physionet archive
        """
        raise NotImplementedError
