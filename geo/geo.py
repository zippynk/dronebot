#!/usr/bin/env python3
# Copyright (C) 2016 nickolas360 <contact@nickolas360.com>
# With minor edits by Nathan Krantz-Fire (a.k.a zippynk) <https://github.com/zippynk>

# This file ships as a part of dronebot, which is licensed under a different license. https://github.com/zippynk/dronebot

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from math import sin, cos, tan, asin, acos, atan2, sqrt
import math

# Radius of Earth in miles
RADIUS = 3963.19 # The drone's speed is 135 miles per hour, so... sorry, it's gotta be miles. Oh, also, sorry for making your code "the wrong shape". I'd apologize again for my apology making your code even longer, but this can't go on forever.

# Haversine formula
def distance_rad(lat1, lat2, lon1, lon2, radius=RADIUS):
    d_lat = lat2 - lat1
    d_lon = lon2 - lon1
    a = sin(d_lat/2)**2 + cos(lat1) * cos(lat2) * sin(d_lon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    return radius * c


def distance_deg(lat1, lat2, lon1, lon2, radius=RADIUS):
    args = [math.radians(a) for a in [lat1, lat2, lon1, lon2]] + [radius]
    return distance_rad(*args)


# https://en.wikipedia.org/wiki/Great-circle_navigation
def coordinates_rad(lat1, lat2, lon1, lon2, fraction):
    lon12 = lon2 - lon1
    a1 = atan2(sin(lon12), cos(lat1)*tan(lat2) - sin(lat1)*cos(lon12))
    s12 = acos(sin(lat1)*sin(lat2) + cos(lat1)*cos(lat2)*cos(lon12))
    a0 = asin(sin(a1) * cos(lat1))
    s01 = atan2(tan(lat1), cos(a1))
    lon01 = atan2(sin(a0) * sin(s01), cos(s01))
    lon0 = lon1 - lon01

    s = s01 + s12 * fraction
    lat = asin(cos(a0) * sin(s))
    lon = atan2(sin(a0) * sin(s), cos(s)) + lon0

    # Normalize longitude -- should be in [-pi, pi].
    if abs(lon) > math.pi:
        lon -= math.copysign(math.pi*2, lon)
    return (lat, lon)


def coordinates_deg(lat1, lat2, lon1, lon2, fraction):
    args = [math.radians(a) for a in [lat1, lat2, lon1, lon2]] + [fraction]
    return tuple(map(math.degrees, coordinates_rad(*args)))
