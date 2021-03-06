#!/usr/bin/env python3

import os
import argparse

from networks.lecun_net import LecunNet
from networks.pure_cnn import PureCnn
from networks.network_in_network import NetworkInNetwork
from networks.resnet import ResNet
from networks.densenet import DenseNet
from networks.wide_resnet import WideResNet
from networks.capsnet import CapsNet

models = { 
    'lecun_net': LecunNet,
    'pure_cnn': PureCnn,
    'net_in_net': NetworkInNetwork,
    'resnet': ResNet,
    'densenet': DenseNet,
    'wide_resnet': WideResNet,
    'capsnet': CapsNet
}

parser = argparse.ArgumentParser(description="Train models on Cifar10")
parser.add_argument('--model', choices=models.keys(), required=True)

parser.add_argument('--epochs', default=None, type=int)
parser.add_argument('--batch_size', default=None, type=int)

args = parser.parse_args()
model_name = args.model

args = {k:v for k,v in vars(args).items() if v != None}
del args['model']

model = models[model_name](**args, load_weights=False)

model.train()
