from ecgdatasets.core import EcgDataset

class PhysioNetDataset(EcgDataset):
    """Base class for making datasets from PhysioNet source.
    """
    _template_url = 'https://www.physionet.org/static/published-projects/{}/{}-{}.zip'

    def __init__(
        self,
        root,
        version,
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
        self.version = version
        super().__init__(root, download, mapper)

    @property
    def _fullname(self):
        """
            :return:
                dataset name according to physionet
        """
        raise NotImplementedError

    @property
    def _zippath(self):
        return self.root / ( self.name + '-' + self.version + '.zip' )

    @property
    def _hash(self):
        return self.hashs[self.version]

    @property
    def _url(self):
        return self._template_url.format(self.name, self._fullname, self.version)
