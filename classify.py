#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
IC-PCA2
Ice-crystal Classification with Pricipal Component Analysis
A complete rewrite in Python 3

Based on the original IC-PCA Matlab tool by Hannakaisa Lindqvist, Jussi Tiira
and Hanne Hakkarainen

Author: Jussi Tiira <jussi.tiira@helsinki.fi>

License: GPL v3
"""

from optparse import OptionParser

def main():
    parser = OptionParser()
    parser.add_option("-d", "--inputdir", dest="inputdir", default=".",
                      help="use PATH as input directory", metavar="PATH")
                      
    (options,args) = parser.parse_args()
    
    print(options.inputdir)
    
if __name__ == "__main__":
    main()