# This file ships with dronebot.

#  (c) Copyright 2016 Nathan Krantz-Fire (a.k.a zippynk). Some rights reserved.
#  https://github.com/zippynk/dronebot

#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at http://mozilla.org/MPL/2.0/.

from urllib import request
import json
def get_location(latit,longit):
    url = "http://nominatim.openstreetmap.org/reverse?lat={0}&lon={1}&format=json&addressdetails=0&accept-language=en".format(latit,longit)
    load = json.loads(request.urlopen(url).read().decode())
    if "error" in load.keys():
        return False
    else:
        return load["display_name"]
