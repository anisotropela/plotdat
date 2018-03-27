# plotdat
Quick-plot data from text file.

### Description
A simple Python script for plotting data from the command line.

### Installation
For easier usage, put the code in your favorite directory (e.g. `~/myFavDir/`),
and then add the following line in your startup configuration file
(e.g. `.bashrc` or `zshrc`):

`alias plotdat="python ~/myFavDir/plotdat.py"`

If you're using csh or tcsh, your config file is called `.cshrc`, and you should omit the `=`:

`alias plotdat "python ~/myFavDir/plotdat.py"`

If you don't know which shell you're using, check with

`> echo $SHELL`

### Usage
If you have added the line above, use the examples below as written. Otherwise, instead of just `plotdat`, you should write `python plotdat.py`:

Plot column 2 vs. column 1 in a text file `file.dat`:

`> plotdat file.dat`

Make a scatter plot of column 4 vs. column 1 with a logarithmic x axis:

`> plotdat file.dat -s -ycol 3 -xlog`

Get help

`> plotdat -h`
