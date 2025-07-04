"""Minimal script to train iTransformer on the Traffic dataset."""
import argparse
from argparse import Namespace
import sys
from pathlib import Path
import torch

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT))

from experiments.exp_long_term_forecasting import Exp_Long_Term_Forecast


def main():
    parser = argparse.ArgumentParser(description="Train iTransformer on Traffic")
    parser.add_argument('--pred_len', type=int, default=96, help='prediction length')
    args_cmd = parser.parse_args()

    args = Namespace(
        is_training=True,
        model_id=f'traffic_96_{args_cmd.pred_len}',
        model='iTransformer',
        data='custom',
        root_path='./dataset/traffic/',
        data_path='traffic.csv',
        features='M',
        target='OT',
        freq='h',
        checkpoints='./checkpoints/',
        seq_len=96,
        label_len=48,
        pred_len=args_cmd.pred_len,
        enc_in=862,
        dec_in=862,
        c_out=862,
        d_model=512,
        n_heads=8,
        e_layers=4,
        d_layers=1,
        d_ff=512,
        factor=1,
        moving_avg=25,
        dropout=0.1,
        embed='timeF',
        activation='gelu',
        output_attention=False,
        do_predict=False,
        num_workers=0,
        itr=1,
        train_epochs=10,
        batch_size=16,
        patience=3,
        learning_rate=0.001,
        des='Exp',
        loss='MSE',
        lradj='type1',
        use_amp=False,
        use_gpu=torch.cuda.is_available(),
        gpu=0,
        use_multi_gpu=False,
        devices='0',
        exp_name='MTSF',
        channel_independence=False,
        inverse=False,
        class_strategy='projection',
        target_root_path='./dataset/traffic/',
        target_data_path='traffic.csv',
        efficient_training=False,
        use_norm=True,
        partial_start_index=0
    )

    exp = Exp_Long_Term_Forecast(args)
    setting = f"traffic_minimal_{args_cmd.pred_len}"
    exp.train(setting)
    exp.test(setting)


if __name__ == '__main__':
    main()
