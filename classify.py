#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
IC-PCA2
Ice-crystal Classification with Pricipal Component Analysis
A complete rewrite in Python 3

Based on the original IC-PCA Matlab tool by Hannakaisa Lindqvist, Jussi Tiira
and Hanne Hakkarainen

@author: Jussi Tiira <jussi.tiira@helsinki.fi>

License: GPL v3
"""

import os, glob, configparser
from optparse import OptionParser

def main():
    parser = OptionParser()
    parser.add_option("-d", "--inputdir", dest="inputdir", default=os.getcwd(),
                      help="use PATH as input directory", metavar="PATH")
                      
    (options,args) = parser.parse_args()
    
    config = configparser.ConfigParser()
    config['DEFAULT'] = {'InputFilenames': '*.jpg'}
    with open('classify.conf', 'w') as configfile:
        config.write(configfile)
    
    config.read('classify.conf')
    
    files = glob.glob(os.path.join(options.inputdir,config['DEFAULT']['InputFilenames']))
    print(files)
    
if __name__ == "__main__":
    main()