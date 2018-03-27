"""
Written by Peter Laursen, 2018.
"""
import numpy as np
import matplotlib.pyplot as plt
import argparse
from argparse import RawTextHelpFormatter

def main():
    # Store arguments in `args`
    purpose = 'purpose:\n' +\
              '  Plot data from text file.'
    example = 'example:\n' +\
              '  Make a scatter plot of column 4 vs. column 1 with a logarithmic x axis:\n' +\
              '  > python plotdat.py file.dat -s -ycol 3 -xlog'
    parser = argparse.ArgumentParser(description=purpose, formatter_class=RawTextHelpFormatter, epilog=example)
    parser.add_argument('-s',      action='store_true', help='Scatter instead of plot')
    parser.add_argument('-l',      action='store_true', help='Use header as label (if it exists)')
    parser.add_argument('-xlog',   action='store_true', help='Use logarithmic x axis')
    parser.add_argument('-ylog',   action='store_true', help='Use logarithmic y axis')
    parser.add_argument('-xcol', default=0, type=int,   help='Column number for x data (first column is 0, default is 0)')
    parser.add_argument('-ycol', default=1, type=int,   help='Column number for y data (default 1)')
    parser.add_argument('fname', help='Name of file containing data in two (or more) columns.')
    args   = parser.parse_args()

    # Change defaults if necessary
    plotter = plt.scatter if args.s    else plt.plot
    xscale  = 'log'       if args.xlog else 'linear'
    yscale  = 'log'       if args.ylog else 'linear'
    if args.l:
        with open(args.fname) as f: hdr = f.readline().split()
        if hdr[0] == '#':
            xlabel = hdr[args.xcol+1]
            ylabel = hdr[args.ycol+1]
        else:
            xlabel = 'x'
            ylabel = 'y'
    else:
        xlabel = ''
        ylabel = ''

    # Read data
    x,y = np.loadtxt(args.fname,unpack=True,usecols=(args.xcol,args.ycol))

    # Plot it
    plt.xscale(xscale)
    plt.yscale(yscale)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plotter(x,y)
    plt.ion()
    plt.show()

    # End it
    input("Hit Enter to quit")
    plt.close()

if __name__ == '__main__':
    main()
