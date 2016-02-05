# himawaripy
*Put near-realtime picture of Earth as your desktop background*

himawaripy is a Python 2 script that fetches near-realtime (10 minutes delayed)
picture of Earth as its taken by
[Himawari 8 (ひまわり8号)](https://en.wikipedia.org/wiki/Himawari_8) and sets it
as your desktop background.

Set a cronjob that runs in every 10 minutes to automatically get the
near-realtime picture of Earth.

This is a fork of the original specifically for OS X

## Installation
    cd ~
    git clone https://github.com/snakie/himawaripy.git

    # install pillow
    brew install homebrew/python/pillow
    
    # configure
    cd ~/himawaripy
    vi himawaripy.py
    
    # test whether it's working
    ./himawaripy.py
    
    # set up a cronjob
    crontab -e
    # Add the line:
    */10 * * * * $HOME/himawaripy/himawaripy.py > /dev/null && $HOME/himawaripy/update_wallpaper.sh 
    
## Example
![Earth, as 2016/02/04/13:30:00 GMT](http://i.imgur.com/4XA6WaM.jpg)
    
## Attributions
Bora M. Alper - for the original Python 3 implementation: https://github.com/boramalper/himawaripy

Thanks to *[MichaelPote](https://github.com/MichaelPote)* for the [initial
implementation](https://gist.github.com/MichaelPote/92fa6e65eacf26219022) using
Powershell Script.

Thanks to *[Charlie Loyd](https://github.com/celoyd)* for image processing logic
([hi8-fetch.py](https://gist.github.com/celoyd/39c53f824daef7d363db)).

Obviously, thanks to the Japan Meteorological Agency for opening these pictures
to public.
