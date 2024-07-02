import requests
import os
from django.shortcuts import render, HttpResponse
import socket
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view()
def hello(request):


    user_ip = request.META.get('REMOTE_ADDR')
    myapikey = os.environ.get('Weatherapikey')
    print(f'user ip address is {user_ip}')

    Ipaddr = '102.215.57.124'

    visitor_name = request.GET.get('visitor_name', '')
    
    url = f'http://api.weatherapi.com/v1/current.json?key={myapikey}&q={Ipaddr}&aqi=no'
    urlresponse = requests.get(url)

    if urlresponse.status_code == 200:
        urldata = urlresponse.json() 
        location_city = urldata['location']['name']               
        weather = urldata['current']['temp_c']    
        print(f'here is what the api got for me : location: {location_city} and weather: {weather}')           
        pass
    else:
        print(f"Error retrieving data: {urlresponse.status_code}")        
 
    mydict = {'client_ip' :  user_ip,
     'location: ': location_city,
     'greeting':f'Hello, {visitor_name}, the temperature is {weather} degrees Celcius in {location_city}'}
    return Response(mydict)