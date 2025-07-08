# iTransformer Minimal Usage

This repository contains a minimal setup to run iTransformer on the Traffic dataset.

## Quick start

1. Install the lightweight dependencies:

```bash
pip install -r minimal/requirements.txt
```

2. Download and prepare the Traffic dataset:

```bash
python minimal/download_traffic.py
```

3. Run inference (optionally provide a trained checkpoint):

```bash
python minimal/inference.py --pred_len 96 --checkpoint ./checkpoints/traffic_minimal_96/checkpoint.pth
```

The script will automatically place the dataset under `./dataset/traffic/` so that the minimal inference example works out of the box.
