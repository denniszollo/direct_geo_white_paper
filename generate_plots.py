#!/bin/python2.7

# This script will generate all the plots we need for the direct georeferencing white paper
# It is intended to be run from the top-level directory of the direct_geo_white_paper directory



# check that files it needs exist
import os
if not os.path.exists('plots'):
  os.mkdir('plots')
# clear and create output directory

# Import matplotlib / numpy / pandas as needed
