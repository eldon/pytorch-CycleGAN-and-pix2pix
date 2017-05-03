#!/bin/bash
python test.py --dataroot $1 --name $2 --model pix2pix --which_model_netG unet_256 --which_direction AtoB --align_data
