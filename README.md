# Ecgdatasets

## Table of contents
- [Authors](#authors)
- [Installation](#installation)
- [A simple example](#a-simple-example)
- [List of datasets](#list-of-datasets)
- [Citing](#citing)

## Authors
[**Rostislav Epifanov** — Researcher in Novosibirsk]()

## Installation
Installation from PyPI:

```
pip install ecgdatasets
```

Installation from GitHub:

```
pip install git+https://github.com/rostepifanov/ecgdatasets
```

## A simple example

```python
import ecgdatasets as edb
from torch.utils.data import DataLoader

dataset = edb.PTBXL('.', '1.0.3', download=True, mapper=None) # torch.Dataset
dataloader = DataLoader(dataset, batch_size=32, shuffle=True) # ready to use with torch.nn.Module
```

## List of datasets

The list of all datasets:

  - [LUDB](https://physionet.org/content/ludb/)
  - [PTBXL](https://physionet.org/content/ptb-xl/)
  - [INCARTDB](https://physionet.org/content/incartdb/)

## Citing

If you find this library useful for your research, please consider citing:

```
@misc{epifanov2023ecgdatasets,
  Author = {Rostislav Epifanov},
  Title = {Ecgdatasets},
  Year = {2023},
  Publisher = {GitHub},
  Journal = {GitHub repository},
  Howpublished = {\url{https://github.com/rostepifanov/ecgdatasets}}
}
```
