#!/usr/bin/env python
# coding=utf-8

from ImageLoader import ImageLoader
from optparse import OptionParser
import os.path

parser = OptionParser()
parser.add_option("-i", "--input",
                  dest="input", metavar="FILE", default='in.png',
                  help="Change input file (default in.png)")
                  
parser.add_option("-o", "--output",
                  dest="output", metavar="FILE", defult='out/',
                  help="Change output folder (default out/)")

options, optionsValues = parser.parse_args()

if not os.path.isfile(options.input):
    print(options.input, "file is missing!")
else:
    imageLoader = ImageLoader()
    noiseImage = imageLoader.loadFromImage(options.input, 2)
    imageLoader.saveToImage(options.output, noiseImage, 100, True)

    print("success")