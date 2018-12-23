import csv
import re


FIRST_COLUMN_NAME = 'column1'
SECOND_COLUMN_NAME = 'column2'
N_COLUMN = 'column3' # to filter non-login values
LOGIN_REGEX = re.compile("^[a-zA-Z0-9_.-]+$", re.MULTILINE)

with open('unsorted.csv') as csvfile:
    spamreader = csv.DictReader(csvfile, delimiter=",")
    sortedlist = sorted(spamreader, key=lambda row:(row[FIRST_COLUMN_NAME],row[SECOND_COLUMN_NAME]), reverse=False)
    filteredlist = [x for x in sortedlist if re.match(LOGIN_REGEX, x[N_COLUMN])]


with open('sorted.csv', 'w') as f:
    fieldnames = [FIRST_COLUMN_NAME, SECOND_COLUMN_NAME, N_COLUMN]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for row in sortedlist:
        writer.writerow(row)
