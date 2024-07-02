import requests
import os
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view()
def hello(request):
    user_ip = request.META.get('REMOTE_ADDR')
    myapikey = os.environ.get('Weatherapikey')

    
    print(f'User IP address: {user_ip}')

    visitor_name = request.GET.get('visitor_name', '')

    
    if not visitor_name:
        return Response({'error': 'Visitor name is required.'}, status=400)

    
    url = f'http://api.weatherapi.com/v1/current.json?key={myapikey}&q={user_ip}&aqi=no'
    urlresponse = requests.get(url)

    if urlresponse.status_code == 200:
        urldata = urlresponse.json()

        
        if 'location' in urldata and 'current' in urldata:
            location_city = urldata['location']['name']
            weather = urldata['current']['temp_c']
            print(f'API response: location: {location_city}, weather: {weather}°C')
        else:
            
            return Response({'error': 'Incomplete data received from the weather API.'}, status=500)
    else:
        
        print(f"Error retrieving data: {urlresponse.status_code}")
        return Response({'error': 'Failed to retrieve data from the weather API.'}, status=urlresponse.status_code)

    mydict = {
        'client_ip': user_ip,
        'location': location_city,
        'greeting': f'Hello, {visitor_name}, the temperature is {weather} degrees Celsius in {location_city}.'
    }
    return Response(mydict)
