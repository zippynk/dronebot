#!/usr/bin/env python3

# This file ships with dronebot and is meant to be run locally, not on the server.

#  (c) Copyright 2016 Nathan Krantz-Fire (a.k.a zippynk). Some rights reserved.
#  https://github.com/zippynk/dronebot

#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at http://mozilla.org/MPL/2.0/.

from __future__ import print_function
from urllib import request
import json
import sys

def world_map(server,port=10407):
    url1 = "http://{0}:10407/update".format(server)
    load = json.loads(request.urlopen(url1).read().decode())
    if "error" in load.keys():
        raise DroneInfoError
    else:
        url2 = "http://staticmap.openstreetmap.de/staticmap.php?center=0,0&zoom=2&size=1024x1024&maptype=mapnik&markers={0},{1},purple-pushpin{2}".format(load["lat"],load["lon"],(("|" + str(load["destinations"][0][0]) + "," + str(load["destinations"][0][1]) + ",lightblue1") if len(load["destinations"]) > 0 else "") + (("|" + str(load["destinations"][1][0]) + "," + str(load["destinations"][1][1]) + ",lightblue2") if len(load["destinations"]) > 1 else "") + (("|" + str(load["destinations"][2][0]) + "," + str(load["destinations"][2][1]) + ",lightblue3") if len(load["destinations"]) > 2 else "") + (("|" + str(load["destinations"][3][0]) + "," + str(load["destinations"][3][1]) + ",lightblue4") if len(load["destinations"]) > 3 else "") + (("|" + str(load["destinations"][4][0]) + "," + str(load["destinations"][4][1]) + ",lightblue5") if len(load["destinations"]) > 4 else "") + "|" + str(load["startloc"][0]) + "," + str(load["startloc"][1]) + ",ol-marker")
        return url2



if __name__ == "__main__":
    print(world_map(input("Server? ") if len(sys.argv) <= 1 else sys.argv[1]))
