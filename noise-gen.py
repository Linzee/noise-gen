#!/usr/bin/env python
# coding=utf-8

from ImageLoader import ImageLoader
from optparse import OptionParser

#parser = OptionParser()
#
#options, optionsValues = parser.parse_args()
#
#if len(optionsValues) > 0:
#    inputFile = optionsValues[0]
#else:
#    print "Missing input file"

imageLoader = ImageLoader()
noiseImage = imageLoader.loadFromImage('in.png', 2)
imageLoader.saveToImage('out', noiseImage, 100, True)

print("Success")