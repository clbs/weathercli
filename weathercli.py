import click
import urllib, json
import pprint
import requests

@click.command()
@click.option('--zipp', prompt='Your US ZIP code:', help='Your US ZIP code')
@click.option('--temp', default=0, help='Returns Current Temperature 0 or 1')
@click.option('--rh', default=0, help='Returns Current Humidity 0 or 1')
@click.option('--con', default=0, help='Returns Current Weather Condition 0 or 1')
def weather(zipp, temp, rh, con):
    loc = ("http://api.wunderground.com/api/9394e65e04847b41/conditions/q/" + zipp + ".json")
    url1data = requests.get(loc)
    locdata = url1data.json()
    degf = (locdata['current_observation']['temp_f'])
    prh = (locdata['current_observation']['relative_humidity'])
    city = (locdata['current_observation']['display_location']['full'])
    conz = (locdata['current_observation']['weather'])
    fs = str(city + " Current Weather")
    if temp == 1:
        fs = fs + str(", Temperature: " + str(degf))
    if rh == 1:
        fs = fs + str(", Humidity: " + prh)
    if con == 1:
           fs = fs + str(", Current Conditions: " + str(conz))
    click.echo(fs)
    
        
weather()
