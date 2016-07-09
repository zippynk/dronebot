#!/usr/bin/python3

from __future__ import print_function
from pyrcb.pyrcb import IRCBot
from datetime import *
import random
import pickle
import threading
import sys
import os
from math import *
# from old_haversine import distance as old_haversine
from geo.geo import distance_deg as haversine
from geo.geo import *
from getloc import get_location
from getpass import getpass
from bottle import *
import json

#  (c) Copyright 2016 Nathan Krantz-Fire (a.k.a zippynk). Some rights reserved.
#  https://github.com/zippynk/dronebot

#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at http://mozilla.org/MPL/2.0/.


main_channels = ["#`","##`bots"] # Change this if you are running it
authorized_operators = ["nkf1"] # Change this if you are running it

if len(sys.argv) > 2:
    coords = [float(sys.argv[1]),float(sys.argv[2])]
else:
    coords = False

# Drone stop info format: (Latitude Cordinate, Longitude Cordinate, Dump on Arrival?)

#def haversine(lat1,lat2,lon1,lon2):
#    r = 3959
#    dlat = (lat2-lat1)*pi/180
#    dlon = (lon2-lon2)*pi/180
#    a = (sin(dlat/2)*sin(dlat/2))+(cos(lat1*pi/180)*cos(lat2*pi/180)*sin(dlon/2)*sin(dlon/2))
#    c = atan2(sqrt(a),sqrt(1-a))
#    d = r * c
#    return d

@route("/update")
def update():
    response.content_type = 'application/json'  
    try:
        return json.dumps({"lat":bot.drone_current_location[0],"lon":bot.drone_current_location[1],"destinations":bot.destinations,"fraction":bot.a})
#        return '{{"lat":{0}, "lon":{1}, "next3dests":{{{{"lat":{2}, "lon":{3}, id:0}}, {{"lat":{4}, "lon":{5}, id:1}}, {{"lat":{6}, "lon":{7}, id:2}}}}, "fraction":{8}}}'.format(bot.drone_current_location[0],bot.drone_current_location[1],bot.destinations[0][0] if len(bot.destinations) > 0 else "null",bot.destinations[0][1] if len(bot.destinations) > 0 else "null",bot.destinations[1][0] if len(bot.destinations) > 1 else "null",bot.destinations[1][1] if len(bot.destinations) > 1 else "null",bot.destinations[2][0] if len(bot.destinations) > 2 else "null",bot.destinations[2][1] if len(bot.destinations) > 2 else "null",bot.a)
    except IndexError:
        return '{"error":"Index error. Most likely cause: The drone is not ready."}'
    except:
        #print(e)
        return '{"error":"An unexpected error occurred."}'

class DroneBot(IRCBot):
    def on_message(self, message, nickname, channel, is_query):
        if is_query:
            return
        if len(message.lower().split()) == 0:
            return
        if "@pbdroneland" in message.lower().split()[0]:
            if nickname in authorized_operators:
                for i in main_channels:
                    self.send(i,"Landing.")
                pickle.dump((self.drone_current_location,self.destinations,self.stationed),open(os.path.expanduser("~") + "/.pbdroneland","wb"))
                self.wait(1)
                self.quit(message="But of all I've done, for want or wit, to my memory now, I can't recall, so fill to me a parting glass, good night, and joy be with you all.")
                exit(0)
            else:
                self.send(channel, "{0}: You are not allowed to perform that operation.".format(nickname))
        if "@pbdronelocation" in message.lower().split()[0]:
            latit = self.drone_current_location[0]
            longit = self.drone_current_location[1]
            self.send(channel,"{0}: The drone is currently located at {1},{2} ({3}).".format(nickname,latit,longit,get_location(latit,longit))) if get_location(latit,longit) != False else "{0}: The drone is currently located at {1},{2}.".format(nickname,latit,longit)
        if "@pbdronequeue" in message.lower().split()[0]: 
            if len(self.destinations) > 0:
                self.send(channel,"Drone Queue  (pinging {0})".format(nickname))
                self.send(channel, "|Destination #   |Latitude Coordinate    |Longitude Coordinate   |Estimated Time of Arrival   |Action on Arrival   |")
                lat_long_net_distance = haversine(self.drone_starting_location[0],self.destinations[0][0],self.drone_starting_location[1],self.destinations[0][1])
                print(lat_long_net_distance)
                conversion_factor = 135./3600 # Miles to hours, hours to seconds
                self.send(channel, "|" + "1" + " "*(16-len("1")) + "|" + str(self.destinations[0][0]) + " "*(23-len(str(self.destinations[0][0]))) + "|" + str(self.destinations[0][1]) + " "*(23-len(str(self.destinations[0][1]))) + "|" + str(self.drone_starting_location[2]+timedelta(0,lat_long_net_distance/conversion_factor)) + " "*(28-len(str(self.drone_starting_location[2]+timedelta(0,lat_long_net_distance/conversion_factor)))) + "|" + ("Dump                " if self.destinations[0][2] else "Continue            ") + "|")
                theoreticalCurrentTime = self.drone_starting_location[2]+timedelta(0,lat_long_net_distance/conversion_factor)
            else:
                self.send(channel,"{0}: No queued destinations.".format(nickname))
            j = 1
            if len(self.destinations) > 1:
                for i in self.destinations[1:]:
                    lat_long_net_distance = haversine(self.destinations[j-1][0],self.destinations[j][0],self.destinations[j-1][1],self.destinations[j][1])
                    self.send(channel, "|" + str(j+1) + " "*(16-len(str(j+1))) + "|" + str(i[0]) + " "*(23-len(str(i[0]))) + "|" + str(i[1]) + " "*(23-len(str(i[1]))) + "|" + str(theoreticalCurrentTime+timedelta(0,lat_long_net_distance/conversion_factor)) + " "*(28-len(str(self.drone_starting_location[2]+timedelta(0,lat_long_net_distance/conversion_factor)))) + "|" + ("Dump                " if i[2] else "Continue            ") + "|")
                    j += 1
                    theoreticalCurrentTime += timedelta(0,lat_long_net_distance/conversion_factor)
        if "@pbdqueuecontrol" in message.lower().split()[0] and len(message.lower().split()) > 1:
            if message.lower().split()[1] == "add":
                # Attempt to parse arguments.
                try:
                    arg1 = float(message.lower().split()[2])
                    arg2 = float(message.lower().split()[3])
                    arg3 = True if message.lower().split()[4] == "yes" else (False if message.lower().split()[4] == "no" else ERRORERRORERRORERRORERROR)
                except ValueError:
                    self.send(channel,"{0}: Invalid arguments.".format(nickname))
                    return
                except NameError:
                    self.send(channel,"{0}: Invalid arguments.".format(nickname))
                    return
                except IndexError:
                    self.send(channel,"{0}: Invalid arguments.".format(nickname))
                    return
                if arg1 > 90 or arg1 < -90 or arg2 > 180 or arg2 < -180:
                   self.send(channel,"{0}: Invalid coordinates.".format(nickname))
                   return
                self.destinations.append((arg1,arg2,arg3,))
                self.send(channel,"{0}: Added.".format(nickname))
            if message.lower().split()[1] == "remove":
                # Attempt to parse arguments.
                try:
                    arg1 = int(message.lower().split()[2])
                except ValueError:
                    self.send(channel,"{0}: Invalid arguments.".format(nickname))
                    return
                except IndexError:
                    self.send(channel,"{0}: Invalid arguments.".format(nickname))
                    return
                if arg1 > 0 and arg1 <= len(self.destinations):
                    self.destinations[arg1-1] = None
                else:
                    self.send(channel,"{0}: No destination with that index.".format(nickname))
                    return
                self.send(channel,"{0}: Removed.".format(nickname))
                
                    
    def setup(self):
        if os.path.isfile(os.path.expanduser("~") + "/.pbdroneland") and coords == False:
            pickleload = pickle.load(open(os.path.expanduser("~") + "/.pbdroneland","rb"))
            self.drone_current_location = pickleload[0]
            self.drone_starting_location = pickleload[0] + (datetime.now(),)
            self.destinations = pickleload[1]
            self.stationed = pickleload[2]
        else:
            # global coords
            self.drone_current_location = (40.3502,-74.6522) if coords == False else (coords[0],coords[1]) # Princeton CS Building
            self.drone_starting_location = (40.3502,-74.6522,datetime.now()) if coords == False else (coords[0],coords[1],datetime.now()) # Princeton CS Building
            self.destinations = [] # Format: (lat,long,Dump?)
            self.stationed = True
        self.a = 0
    def auto_time_loop(self, channel):
        while self.alive:
            self.wait(1)
            if len(self.destinations) > 0:
                if self.destinations[0] == None:
                    self.drone_starting_location = self.drone_current_location + (datetime.now(),)
                    self.destinations.pop(0)
                    continue
                j = 0
                while j < len(self.destinations):
                    if self.destinations[j] == None:
                        self.destinations.pop(j)
                        print("popped")
                    else:
                        j += 1

                self.stationed = False
                if self.drone_current_location != self.destinations[0][0:1]:
                    seconds_elapsed = (datetime.now()-self.drone_starting_location[2]).total_seconds()
                    lat_long_net_distance = haversine(self.drone_starting_location[0],self.destinations[0][0],self.drone_starting_location[1],self.destinations[0][1])
                    conversion_factor = 135./3600. # Miles to hours, hours to seconds
                    a = seconds_elapsed/(lat_long_net_distance/conversion_factor)
                    b = 1-a
                    self.a = a
                    print((a,b))
                    self.drone_current_location = coordinates_deg(self.drone_starting_location[0],self.destinations[0][0],self.drone_starting_location[1],self.destinations[0][1],a)
                    # self.drone_current_location = (self.drone_starting_location[0]*b+self.destinations[0][0]*a,self.drone_starting_location[1]*b+self.destinations[0][1]*a) # Weighted average formula, legacy, replaced with nickolas360's geo library
                    if a >=1:
                        self.drone_current_location = self.destinations[0][0:2]
                        self.drone_starting_location = self.drone_current_location + (datetime.now(),)
                        if self.destinations[0][2] == False:
                            for i in main_channels:
                                self.send(i,"At ({0},{1}) ({2}) and continuing on.".format(self.drone_current_location[0],self.drone_current_location[1],get_location(self.drone_current_location[0],self.drone_current_location[1])) if get_location(self.drone_current_location[0],self.drone_current_location[1]) != False else "At ({0},{1}) and continuing on.".format(self.drone_current_location[0],self.drone_current_location[1]))
                        else:
                            for i in main_channels:
                                self.send(i,"At ({0},{1}) ({2}) and dispatching peanut butter.".format(self.drone_current_location[0],self.drone_current_location[1],get_location(self.drone_current_location[0],self.drone_current_location[1])) if get_location(self.drone_current_location[0],self.drone_current_location[1]) != False else "At ({0},{1}) and dispaching peanut butter.".format(self.drone_current_location[0],self.drone_current_location[1]))
                        self.destinations.pop(0)
            else:
                if not self.stationed:
                    for i in main_channels:
                        self.send(i,"Stationed at ({0},{1}) ({2}).".format(self.drone_current_location[0],self.drone_current_location[1],get_location(self.drone_current_location[0],self.drone_current_location[1])) if get_location(self.drone_current_location[0],self.drone_current_location[1]) != False else "Stationed at ({0},{1}).".format(self.drone_current_location[0],self.drone_current_location[1]))
                    self.stationed = True

def main():
    global bot
    bot = DroneBot(debug_print=True)
    bot.setup()
    bot.connect("irc.freenode.net", 6667)
    if "--password" in sys.argv:
        bot.password(getpass("Password? "))
    bot.register("pbdronebot")
    for i in main_channels:
        bot.join(i)

    # Blocking; will return when disconnected.
    threading.Thread(target=bot.auto_time_loop,args=[main_channels[0]],daemon=False).start()
    threading.Thread(target=bot.listen).start()
    run(host="0.0.0.0",port="10407",debug=False)

if __name__ == "__main__":
    main()
