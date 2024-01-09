# **E**cg**d**ata**s**ets

![Python version support](https://img.shields.io/pypi/pyversions/ecgdatasets)
[![PyPI version](https://badge.fury.io/py/ecgdatasets.svg)](https://badge.fury.io/py/ecgdatasets)
[![Downloads](https://pepy.tech/badge/ecgdatasets/month)](https://pepy.tech/project/ecgdatasets?versions=0.0.*)

Ecgdatasets is a Python library with esay-to-use interfaces for ECG datasets.

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
import ecgdatasets as eds
from torch.utils.data import DataLoader

# torch.Dataset
dataset = eds.PTBXL('.', '1.0.3', download=True, mapper=None)

# torch.DataLoader that is ready to use with torch.nn.Module
dataloader = DataLoader(dataset, batch_size=32, shuffle=True)
```

## Available datasets

| Name      | Labels | Source                                             | Comments |
| ---:      | :---:  | :---:                                              | :---:    |
| LUDB      | -      | [Physionet](https://physionet.org/content/ludb/)   | -        |
| PTBXL     | -      | [Physionet](https://physionet.org/content/ptb-xl/) | -        |
| INCARTDB  | -      | [Physionet](https://physionet.org/content/ptb-xl/) | -        |

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
