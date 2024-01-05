# **E**cg**d**ata**s**ets

## Table of contents
- [Authors](#authors)
- [Installation](#installation)
- [A simple example](#a-simple-example)
- [Available datasets](#available-datasets)
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

# torch.Dataset
dataset = edb.PTBXL('.', '1.0.3', download=True, mapper=None)

# torch.DataLoader that is ready to use with torch.nn.Module
dataloader = DataLoader(dataset, batch_size=32, shuffle=True)
```

## Available datasets

| Name      | Labels | Source |
| ---:      | :---:  | :---: |
| LUDB      | -      | [Physionet](https://physionet.org/content/ludb/) |
| PTBXL     | -      | [Physionet](https://physionet.org/content/ptb-xl/) |
| INCARTDB  | -      | [Physionet](https://physionet.org/content/ptb-xl/)|

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
