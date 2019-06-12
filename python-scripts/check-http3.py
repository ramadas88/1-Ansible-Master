#!/usr/bin/env python

"""
USAGE:

logparsing_apache.py apache_log_file

This script takes apache log file as an argument and then generates a report, with hostname,
bytes transferred and status

"""

import sys

def apache_output(line):
    split_line = line.split()
    print split_line
    print ("---------------------------")
    print split_line[0]
    print ("---------------------------")
    print split_line[1]
    print ("---------------------------")
    print split_line[2]
    print ("---------------------------")
    print split_line[3]
    print ("---------------------------")
    print split_line[4]
    print ("---------------------------")
    print split_line[5]
    print ("---------------------------")
    #exit(10)
    return {'remote_host': split_line[0],
            'apache_status': split_line[8],
            'data_transfer': split_line[9],
    }


def final_report(logfile):
    for line in logfile:
        line_dict = apache_output(line)
        print(line_dict)


if __name__ == "__main__":
    if not len(sys.argv) > 1:
       data = sys.stdin.readlines()
       try:
           data[0][3]
       except:
           print (__doc__)
           sys.exit(1)
    #infile_name = sys.argv[1]
    #try:
    #    infile = open(infile_name, 'r')
    #except IOError:
    #    print ("You must specify a valid file to parse")
    #    print (__doc__)
    #    sys.exit(1)
    log_report = final_report(data)
    #log_report = final_report(infile)
    print (log_report)
    #infile.close()



