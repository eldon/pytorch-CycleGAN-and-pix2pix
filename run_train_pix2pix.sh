#!/bin/bash
python train.py --dataroot $1 --name $2 --model pix2pix --which_model_netG unet_256 --which_direction AtoB --lambda_B 100 --align_data --use_dropout --no_lsgan --display_id 0
