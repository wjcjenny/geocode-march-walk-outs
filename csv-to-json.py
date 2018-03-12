#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""

$ python3 csv-to-json.py -i 1.csv -o 1.json -f pretty

$ python3 csv-to-json.py -i original-data.csv -o jan.json -f dump
"""

import sys, getopt
import csv
import json

#Get Command Line Arguments
def main(argv):
    input_file = ''
    output_file = ''
    format = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:f:",["ifile=","ofile=","format="])
    except getopt.GetoptError:
        print ('csv_json.py -i <path to inputfile> -o <path to outputfile> -f <dump/pretty>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('csv_json.py -i <path to inputfile> -o <path to outputfile> -f <dump/pretty>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            input_file = arg
        elif opt in ("-o", "--ofile"):
            output_file = arg
        elif opt in ("-f", "--format"):
            format = arg
    read_csv(input_file, output_file, format)


#Read CSV File
def read_csv(file, json_file, format):
    csv_rows = {}
    temp_list_dict = {}
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        # title = reader.fieldnames
        for row in reader:
            # print (row['key'])
            # if row['message'] == '' and row['type'] == '':
            #     continue
            temp_dict = {}
            temp_list = []
            temp_dict['date'] = row['date']
            temp_dict['school'] = row['school']
            if row['link'] == '':
                temp_dict['web'] = 'false'
                temp_dict['webtype'] = 'false'
            else:
                temp_dict['web'] = row['link']
                if 'facebook' in row['link']:
                    temp_dict['webtype'] = 'facebook'
                else:
                    temp_dict['webtype'] = 'action'
            if row['iglink'] == 'FALSE' or row['iglink'] == '?':
                temp_dict['ig'] = 'false'
            else:
                temp_dict['ig'] = row['iglink']
            # if row['IG Hashtag'] == '':
            #     temp_dict['ig-hashtag'] = 'false'
            # else:
            #     temp_dict['ig-hashtag'] = row['IG Hashtag']

            # if row['Longitude'] == '':
            #     temp_dict['Longitude'] = 'false'
            # else:
            #     temp_dict['Longitude'] = row['Longitude']
            # if row['Latitude'] == '':
            #     temp_dict['Latitude'] = 'false'
            # else:
            #     temp_dict['Latitude'] = row['Latitude']

            temp_dict['longitude'] = row['longitude']
            temp_dict['latitude'] = row['latitude']
            if row['city'] == '':
                temp_dict['city'] = 'false'
            else:
                temp_dict['city'] = row['city']
            # temp_dict['State'] = row['State']

            str_state= row['state']
            if row['city'] == "Washington, D.C.":
                str_state = "Washington, D.C."
            str_state = str_state.replace(' ', '')
            # print (str_state)

            if str_state not in temp_list_dict:
                temp_list_dict[str_state] = []
                temp_list_dict[str_state].append(temp_dict)
            else:
                temp_list_dict[str_state].append(temp_dict)

            # temp_list_dict[row['State']].append(temp_dict)

            # if row['state'] == '0':
            #     temp_dict['state'] = 'false'
            # else:
            #     temp_dict['state'] = row['state']
            # if row['florida'] == '0':
            #     temp_dict['florida'] = 'false'
            # else:
            #     temp_dict['florida'] = row['florida']
            # if row['texas'] == '0':
            #     temp_dict['texas'] = 'false'
            # else:
            #     temp_dict['texas'] = row['texas']
            # if row['vegas'] == '0':
            #     temp_dict['vegas'] = 'false'
            # else:
            #     temp_dict['vegas'] = row['vegas']
            # if row['pulse'] == '0':
            #     temp_dict['pulse'] = 'false'
            # else:
            #     temp_dict['pulse'] = row['pulse']

            # temp_dict['name'] = row['senator']
            # temp_dict['party'] = row['party']


            # temp_dict['day'] = row['day']
            # temp_dict['date'] = int(float(row["date"]))
            # temp_dict['message'] = row['message']
            # if row['article'] == 'false' or row['article'] == 'FALSE':
            #     temp_dict['article'] = False
            # else:
            #     temp_dict['article'] = row['article']
            # if row['video'] == 'false' or row['video'] == 'FALSE':
            #     temp_dict['video'] = False
            # else:
            #     temp_dict['video'] = row['video']
            # if row['twitter'] == 'false' or row['twitter'] == 'FALSE':
            #     temp_dict['twitter'] = False
            # else:
            #     temp_dict['twitter'] = row['twitter']
            # if row['facebook'] == 'false' or row['facebook'] == 'FALSE':
            #     temp_dict['facebook'] = False
            # else:
            #     temp_dict['facebook'] = row['facebook']
            # temp_dict['url'] = row['embedlink']
            # temp_dict['type'] = row['type']
           

            # temp_list.append(temp_dict)
            # temp_list_dict = {}
            # # print(temp_list)
            # temp_list_dict[row['key']]=temp_dict  //////////////
            # print(temp_list_dict)
            # csv_rows.add(temp_list_dict)
            # print(csv_rows)
            # break
        write_json(temp_list_dict, json_file, format)


#Convert csv data into json and write it
def write_json(data, json_file, format):
    with open(json_file, "w") as f:
        if format == "pretty":
            f.write(json.dumps(data, sort_keys=False, indent=4, separators=(',', ': '), ensure_ascii=False))  ##encoding="utf-8"  encoding = "ISO-8859-1"
        else:
            f.write(json.dumps(data))



if __name__ == "__main__":
    main(sys.argv[1:])
