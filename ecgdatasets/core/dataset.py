from pathlib import Path
from torch.utils.data import Dataset

class EcgDataset(Dataset):
    """
    Base class for making datasets which are compatible with ecgdatasets.
    It is necessary to override the ``__getitem__`` and ``__len__`` method.
    """

    _repr_indent = 4

    def __init__(
        self,
        root,
        ):
        """
        :args:
            root (string): root directory of dataset.
        """
        self.root = Path(root).expanduser()

    def __getitem__(self, idx):
        """
        :args:
            idx (int): index
        """
        raise NotImplementedError

    def __len__(self):
        raise NotImplementedError

    def __repr__(self):
        head = 'Dataset ' + self.__class__.__name__
        body = [f'Number of datapoints: {self.__len__()}']

        if self.root is not None:
            body.append(f'Root location: {self.root}')

        body += self.extra_repr().splitlines()

        lines = [head] + [' ' * self._repr_indent + line for line in body]
        return '\n'.join(lines)

    def extra_repr(self) -> str:
        return ''
