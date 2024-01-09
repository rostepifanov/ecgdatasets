from ecgdatasets.core import EcgDataset

class FigShareDataset(EcgDataset):
    """Base class for making datasets from FigShare source.
    """
    _template_url = 'https://figshare.com/ndownloader/files/{}'

    @property
    def _id(self):
        raise NotImplementedError

    @property
    def _url(self):
        return self._template_url.format(self._id)
