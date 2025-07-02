import requests

city_name = input("Enter City Name : ")
API_KEY = 'e802eed25566c7534a0d146d9c4e1818'
url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric'

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print('Weather : ' , data['weather'][0]['description'])
    print('Current Temperature : ' , data['main']['temp'])
    print('Current Temperature Feels Like : ' ,data['main']['feels_like'])
    print('Humidity : ', data['main']['humidity'])
    
else:
    print("Error:" , response.status_code)
    













