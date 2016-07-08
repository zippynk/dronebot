# Legacy file -- used to be used for haversine until nickolas360 created a replacement library

# Mainly by Salvador Dali: http://stackoverflow.com/users/1090562/salvador-dali 
# This is minorly edited from the Stack Overflow answer found at http://stackoverflow.com/a/21623206
# As such, it is licensed under the Creative Commons Attritubion Share-Alike 3.0 License, the same as under which it was used.
# License link: https://creativecommons.org/licenses/by-sa/3.0/

# This file ships as a part of dronebot, which is licensed under a different license.

from math import cos, asin, sqrt
def distance(lat1, lat2, lon1, lon2):
    p = 0.017453292519943295
    a = 0.5 - cos((lat2 - lat1) * p)/2 + cos(lat1 * p) * cos(lat2 * p) * (1 - cos((lon2 - lon1) * p)) / 2
    return 7918 * asin(sqrt(a))
