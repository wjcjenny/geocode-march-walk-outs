## Requirements

 - Python 2.7 or later.
 - A Google Maps API key.
 - $ pip install -U googlemaps (https://github.com/googlemaps/google-maps-services-python)

### API keys
Each Google Maps Web Service request requires an API key or client ID.

To get an API key:

 1. Visit https://developers.google.com/console and log in with
    a Google Account.
 1. Select one of your existing projects, or create a new project.
 1. Enable the API(s) you want to use. The Python Client for Google Maps Services
    accesses the following APIs:
    * Geocoding API
 1. Create a new **Server key**.
 1. If you'd like to restrict requests to a specific IP address, do so now.

## Usage
 - $ python get_geocode.py
   * Change the input file in get_geocode.py
   * Get the latitude and longitude from geocode_result[0]["geometry"]['location'] 

 - $ python merge.py 
   * Merge sereval .csv files to one .csv file

 - $ python csv-to-json.py -i final-data/total.csv -o final-data/total.json -f pretty
   * Convert csv to json format
