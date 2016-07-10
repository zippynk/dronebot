# This file ships with dronebot and is meant to be run locally, not on the server.

#  (c) Copyright 2016 Nathan Krantz-Fire (a.k.a zippynk). Some rights reserved.
#  https://github.com/zippynk/dronebot

#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at http://mozilla.org/MPL/2.0/.

from urllib import request
import json
import sys

def world_map(server):
    url1 = "http://{0}:10407/update".format(server)
    load = json.loads(request.urlopen(url1).read().decode())
    if "error" in load.keys():
        raise DroneInfoError
    else:
        url2 = "http://staticmap.openstreetmap.de/staticmap.php?center=0,0&zoom=2&size=1024x1024&maptype=mapnik&markers={0},{1},red-pushpin{2}".format(load["lat"],load["lon"],("|" + str(load["destinations"][0][0]) + "," + str(load["destinations"][0][1]) + ",lightblue1") if len(load["destinations"]) > 0 else "",("|" + str(load["destinations"][1][0]) + "," + str(load["destinations"][1][1]) + ",lightblue2") if len(load["destinations"]) > 1 else "",("|" + str(load["destinations"][2][0]) + "," + str(load["destinations"][2][1]) + ",lightblue3") if len(load["destinations"]) > 2 else "")
        return url2

if __name__ == "__main__":
    print world_map(input("Server? ") if len(sys.argv == 0) else sys.argv[1])
