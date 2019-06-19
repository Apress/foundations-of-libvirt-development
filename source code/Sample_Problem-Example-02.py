#!/usr/bin/python -u

from __future__ import print_function
import argparse
import csv
import runJobOnDomain

# setup
"""Run the set of jobs defined in the CSV input file.
"""
__version__ = '1.0'
debug = False

parser = argparse.ArgumentParser( \
           description='Proess runJobs command line arguments.', \
           version=__version__)
parser.add_argument('--ifile', help='the csv input file.')
args = parser.parse_args()
# get the arguments
ifile = args.ifile
if debug == True:
    print('The command line arguments were:')
    print('ifile =', ifile)
with open(ifile, 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in reader:
        domain = row[0]
        userid = row[1]
        cmd = row[2]
        runJobOnDomain.runJob(domain, userid, cmd)
exit(0)
