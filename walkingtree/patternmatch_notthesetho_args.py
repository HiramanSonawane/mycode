#!/usr/bin/env python3
#Author: RZFeeser RZFeeser@alta3.com


"""Script to search for a pattern match"""

import os # used to walk the system
import fnmatch # for regex pattern matching
import argparse

EXCLUDE = ["/usr", "/home", "/var"] ## Don't search in these locations


def find(pattern, path):
    """search through filesystem based on given path location"""
    result = []
    for root, dirs, files in os.walk(path, topdown=True):
        if root in EXCLUDE: # if the root matches the exclude list
            dirs[:] = [] # remove the directory list for this iteration
            files[:] = [] # remove the file list for this iteration
        for name in files: # always perform the nested loop, but it maybe empty
            if fnmatch.fnmatch(name.lower(), pattern.lower()): # if match
                result.append(os.path.join(root, name)) # add to our list
    return result # return the list

def main():
    """runtime code"""
    parser = argparse.ArgumentParser(description="Searches for files with patterns...")
    parser.add_argument('lookfor', type=str, help='Filename pattern to search')
    parser.add_argument('lookwhere', type=str, help='Search Path')

    args = parser.parse_args()
#    lookfor = input("What pattern am I looking for (Example: *.txt or *.cfg) ")
#    lookwhere = input("What is the path in which I should search? ")
    print("Results: ", find(args.lookfor, args.lookwhere)) # call function

main()

