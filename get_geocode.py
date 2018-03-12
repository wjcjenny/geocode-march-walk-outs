import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='Add Your Key here')

import csv
import time

count = 0
dict_loc = {}
flag = 0

with open('final-data/0308.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
    	location = row['school'] + ',' + row['city'] + ',' + row['state']
    	count += 1
    	geocode_result = gmaps.geocode(location)
    	if geocode_result == []:
    		dict_loc[count] = [location, '', '']
    		str_1 = str(count) + '#' + location + '#' + '' + '#' + ''
    		# print count, location, '', ''
    		print str_1
    	else:
    		dict_loc[count] = [location, geocode_result[0]["geometry"]['location']['lat'], geocode_result[0]["geometry"]['location']['lng']]
    		str_2 = str(count) + '#' + location + '#' + str(geocode_result[0]["geometry"]['location']['lat']) + '#' + str(geocode_result[0]["geometry"]['location']['lng'])
    		# print count, location, geocode_result[0]["geometry"]['location']['lat'], geocode_result[0]["geometry"]['location']['lng']
    		print str_2
    	# break

print count
for i in xrange(1, count+1):
	print i, dict_loc[i]

# # Geocoding an address
# geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

# print geocode_result[0]["geometry"]['location']
