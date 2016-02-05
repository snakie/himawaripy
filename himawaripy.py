#!/usr/bin/env python

from io import BytesIO
from json import loads
from time import strptime, strftime
from os import system
from os.path import expanduser
from urllib2 import urlopen

from PIL import Image


# Configuration
# =============

# Increases the quality and the size. Possible values: 4, 8, 16, 20
level = 4

# ==============================================================================

def main():
    width = 550
    height = 550

    print("Updating...")
    latest_json =  urlopen("http://himawari8-dl.nict.go.jp/himawari8/img/D531106/latest.json")
    latest = strptime(loads(latest_json.read().decode("utf-8"))["date"], "%Y-%m-%d %H:%M:%S")

    print("Latest version: {} GMT\n".format(strftime("%Y/%m/%d/%H:%M:%S", latest)))

    url_format = "http://himawari8.nict.go.jp/img/D531106/{}d/{}/{}_{}_{}.png"

    png = Image.new('RGB', (width*level, height*level))

    print("Downloading tiles: 0/{} completed".format(level*level))
    for x in range(level):
        for y in range(level):
            tile_w = urlopen(url_format.format(level, width, strftime("%Y/%m/%d/%H%M%S", latest), x, y))
            tiledata = tile_w.read()

            tile = Image.open(BytesIO(tiledata))
            png.paste(tile, (width*x, height*y, width*(x+1), height*(y+1)))

            print("Downloading tiles: {}/{} completed".format(x*level + y + 1, level*level))
    print("\nDownloaded\n")

    file_loc = "~/himawaripy/himawari-latest.png"
    output_file = expanduser(file_loc)
    png.save(output_file, "PNG")
    print("saved file to %s" % file_loc)


    print("Done!\n")

if __name__ == "__main__":
    main()
