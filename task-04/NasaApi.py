import argparse
import urllib.request
import json
import webbrowser

parser=argparse.ArgumentParser(description='Fetch Image From NASA Database', epilog = "Example query: /imageapi.py -r curiosity -d 2020-05-05")
parser.add_argument('-r','--rover', type=str , metavar='', required=True, help = 'usage: -r ROVER NAME')
parser.add_argument('-d','--date', type=str , metavar='' ,required=True ,help = 'usage: -d DATE (YYYY-MM-DD format)')
parser.add_argument('-id','--id', type=str , metavar='' ,required=True ,help = 'usage: -id ID ')
args = parser.parse_args()

rovername=args.rover
date=args.date
id = args.id
api_key = 'i0jPvq1bB6fgGzdSFx2JuiYmYGLEZrnnVx5Hh4dB'

apiurl = 'https://api.nasa.gov/mars-photos/api/v1/rovers/'+ rovername + '/photos?earth_date=' + date + '&api_key=' + api_key
apiurlobj = urllib.request.urlopen(apiurl)
response = apiurlobj.read()
d_response = json.loads(response.decode('utf-8'))

lst = d_response['photos']
for i in lst :
    x = i['id']
    if x == int(id):
        y = i['camera']['full_name']
        z = i ['rover']['name']
        print("Image:",x, "taken by" ,"Rover Name:",y)
        print("Enter to open image")
        input()
        print("Please wait...")
        webbrowser.open(i['img_src'])
        break
else:
    print("id not found")
