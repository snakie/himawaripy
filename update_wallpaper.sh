#!/bin/bash

# we do this copy voodoo and double set since disk 
# space is cheap and OS X ignores the desktop change 
# if the path is the same
cp $HOME/himawaripy/himawari-latest.png $HOME/himawaripy/himawari-latest1.png
osascript -e "tell application \"Finder\" to set desktop picture to POSIX file \"$HOME/himawaripy/himawari-latest.png\""
osascript -e "tell application \"Finder\" to set desktop picture to POSIX file \"$HOME/himawaripy/himawari-latest1.png\""
