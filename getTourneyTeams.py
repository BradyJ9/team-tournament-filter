import sys
import os
import csv

if not len(sys.argv) > 2:
    print("ERROR...USAGE: <year> <.csv file>")
    #exit()

#csv_file= sys.argv[1]

#year = sys.argv[2]

csv_file = 'raw_2011teams.csv'
year = '2011'

if os.path.exists(year + "team_data.csv"):
    os.remove(year + "team_data.csv")

with open(year + 'team_data.csv', 'w+', newline='') as csvfile_write:
    _file = open(csv_file, 'r')
    text_str = _file.read()

    writer = csv.writer(csvfile_write, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

    lines = str.splitlines(text_str)

    for l in range(len(lines)):
        if not str.isdigit(lines[l][0]) or str.find(lines[l], "NCAA") != -1: #team that made tourney (plus include column names)
            writer.writerow(str.split(lines[l], ','))

    _file.close()
