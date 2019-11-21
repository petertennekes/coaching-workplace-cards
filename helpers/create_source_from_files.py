#!/usr/local/bin/python3
from os import listdir
from os.path import isfile, join
import sys
mypath = sys.argv[1]

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

import csv
with open(join(mypath, 'source.csv'), 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile)
    spamwriter.writerow(["@File", "Photographer"])

    for file in onlyfiles:
        if file.lower().endswith(('.png', '.jpg', '.jpeg', 'tiff')):
            name = file.split('-')[:-2]
            spamwriter.writerow([join(mypath,file),(' '.join(name) if len(name)>0 else 'unknown')])
