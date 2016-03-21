import requests
from argparse import ArgumentParser

api_key = '2b300a60599ab3e4aba5a2a0395b4f49'
api_url = 'http://api.openweathermap.org/data/2.5/weather?q=%s&APPID=%s'


def main(options):
    url = api_url % (options.city, api_key)
    req = requests.get(url)
    if req.status_code == 200:
        json = req.json()
        if json['cod'] == 200:
            print 'Country: %s, City: %s' % (json['sys']['country'], json['name'])
            print 'Weather today:'
            print 'Pressure: %s' % json['main']['pressure']
            print 'Temperature: %s F' % json['main']['temp']
            print 'Minimum temperature: %s F' % json['main']['temp_min']
            print 'Maximum temperature: %s F' % json['main']['temp_max']
        else:
            print json['message']
    elif req.status_code == 401:
        print req.json()['message']
    else:
        print 'Unknown problem on the server, try later!'

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-c', '--city', type=str, default='Kiev',
                        help='Choose a city you want to know the weather')

options, unknown = parser.parse_known_args()
main(options)
