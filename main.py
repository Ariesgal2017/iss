#!/usr/bin/env python


import json
import turtle
import urllib.request
import time
import webbrowser
import geocoder


def astronauts():
    url = "http://api.open-notify.org/astros.json"
    response = urllib.request.urlopen(url)
    res = json.loads(response.read())
    f = open("iss.txt", "w")
    f.write("There is currently " + str(res["number"]) + "Astronauts onboard")
    people = res["people"]
    for p in people:
        f.write(p['name'] + " - on board" + "\n")

    # print lat and long
    g = geocoder.ip("me")
    f.write("\n Your current lat/long is: " + str(g.latlng))
    f.close()
    webbrowser.open("iss.txt")
    screen = turtle.Screen()
    screen.setup(1280, 720)
    screen.setworldcoordinates(-180, -90, 180, 90)
    screen.bgpic("map.gif")
    screen.register_shape("iss.gif")
    iss = turtle.Turtle()
    iss.shape("iss.gif")
    iss.setheading(45)
    iss.penup()
    while True:
        url = "http://api.open-notify.org/iss-now.json"
        response = urllib.request.urlopen(url)
        response = json.loads(response.read())
        location = response["iss_position"]
        lat = location["latitude"]
        lon = location["longitude"]
        lat = float(lat)
        lon = float(lon)
        print("\nLatitude: " + str(lat))

        print("\nLongitude: " + str(lon))
        iss.goto(lat, lon)
        time.sleep(5)

astronauts()