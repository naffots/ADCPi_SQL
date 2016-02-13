import sqlite3

conn = sqlite3.connect('measurements.db')
c = conn.cursor()
list1 = []
# Create table
c.execute('''CREATE TABLE measurements
                     (date text, temperature text, moisture text)''')

with open('temp.csv') as f:
    for line in f:
        lineSplit = line.split(';')
        list1.append([lineSplit[0], lineSplit[1], ''])

index = 0
with open('moisture.csv') as f:
    for line in f:
        lineSplit = line.split(';')
        value = list1[index]
        value[2] = lineSplit[1]
        list1[index] = value
        index = index + 1

for value in list1:
    c.execute("INSERT INTO measurements VALUES ('" + value[0] + "','" + value[1] + "','" + value[2] + "')")

conn.commit()
conn.close()
