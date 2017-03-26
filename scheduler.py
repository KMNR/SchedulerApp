import csv
import sys
from dj import *

#Variable Declarations
lineno = 0
DJlist = []
TheSchedule = []

#Ripping CSV file to DJ objects, then creating a list of DJ objects.

with open('KMNRShowScheduleSubmission.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        if (lineno < 2):
            lineno = lineno + 1
        else:
            tempDJ = DJ()
            tempDJ.timestamp, tempDJ.username, tempDJ.fullName, tempDJ.seniority, tempDJ.showName = row[:5]  
            tempDJ.preferences = row[5:]          
            DJlist.append(tempDJ)

#Sorting Based on Seniority
DJlist.sort();
DJlist.reverse();

# Determining Show Slots
for i in range(0,len(DJlist)):
    for j in range(0,(len(DJlist[i]))):
        if(   any(x for x in TheSchedule if x.timeSlot == DJlist[i][j])   ):
            pass
        else:
            tempSchedule = Schedule(DJlist[i].showName, DJlist[i].fullName, DJlist[i][j])
            TheSchedule.append(tempSchedule)
            break

# Writting Schedule to output File

fo = open('FinalSchedule.txt', 'w')
for item in TheSchedule:
    fo.write("%s\n" % item)
fo.close()
