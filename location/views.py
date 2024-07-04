import requests
import os
from django.shortcuts import render, HttpResponse
import socket
from rest_framework.response import Response
from rest_framework.decorators import api_view

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


# Create your views here.
@api_view()
def hello(request):
    client_ip = get_client_ip(request)

    myapikey = os.environ.get('weatherapikey')


    visitor_name = request.GET.get('visitor_name', '')
    if not visitor_name:
        return Response({'error': 'Visitor name is required.'}, status=400)

    url = f'http://api.weatherapi.com/v1/current.json?key={myapikey}&q={client_ip}&aqi=no'
    urlresponse = requests.get(url)

    if urlresponse.status_code == 200:
        urldata = urlresponse.json()
        location_city = urldata['location']['name']
        weather = urldata['current']['temp_c']
        print(f'here is what the api got for me : location: {location_city} and weather: {weather}')
        pass
    else:
        print(f"Error retrieving data: {urlresponse.status_code}")

    mydict = {'client_ip' :  client_ip,
     'location: ': location_city,
     'greeting':f'Hello, {visitor_name}!, the temperature is {weather} degrees Celcius in {location_city}'}

    return Response(mydict)