import json, requests


api_key = '2c47a7c36e59270ba2c88bf07835fc6c'
Base_url ='http://api.openweathermap.org/data/2.5/weather?'

country_code = 'us'
#TODO: create class so it'll be easir for geting information from the user 

        

def get_temp(zip_code):
    '''this will get the current temp''' 

    full_url = f'{Base_url}zip={zip_code},{country_code}&units=imperial&appid={api_key}'
    x = requests.get(full_url).json()
    return x['main']['temp']

def get_description(zip_code):
    '''this will get the description of the weather ''' 

    full_url = f'{Base_url}zip={zip_code},{country_code}&units=imperial&appid={api_key}'
    x = requests.get(full_url).json()
    return x['weather'][0].get('description')

def get_LocalName(zip_code):
    '''This will get the name of the localtion ''' 

    full_url = f'{Base_url}zip={zip_code},{country_code}&units=imperial&appid={api_key}'
    x = requests.get(full_url).json()
    return x['name']


def get_icon(zip_code):
    ''' This will get the icon '''
    
    full_url = f'{Base_url}zip={zip_code},{country_code}&units=imperial&appid={api_key}'
    x = requests.get(full_url).json()
    return x['weather'][0].get('icon')

def check_zip(zip_code):
    ''' cheks for valit Zip ''' 

    full_url = f'{Base_url}zip={zip_code},{country_code}&units=imperial&appid={api_key}'
    x = requests.get(full_url).json()
    return x['cod']


conditions = {'group1':['clear sky','few clouds'],'group2':['scattered clouds','broken clouds','shower rain'],'group3':['rain','thunderstorm'],'group4':['snow','mist']}

