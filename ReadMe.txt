Created By: Dan Massa
Date: 3/26/17

How to use:

Place the scheduler.exe file into a directory with a csv file of the name "KMNRShowScheduleSubmission.csv"

The file should contain information that is a result of a google form (or anything of identical structure) 
to the following attributes in order:

Timestamp 
E-Mail
DJ Name(s)
Seniority (MUST BE A FLOATING POINT NUMBER)
Show Name
Show Preference 1
Show Preference 2
...
Show Preference n

for any number of preferences.

The file tuples must also follow the following structure (defaulted by google forms)
0) Header info (attribute names)
1) Blank/discarded row
2) First Submission
3) Second Submission
4) ...
n+1) nth Submission


So long as all of the show slots (i.e. Saturday 2pm-4pm) are repeated identically throughout the google form,
this program will work, no matter how much the individual slots change over time 
(in case Saturday 2pm-4pm becomes Saturday 2pm-3pm and Saturday 3pm-4pm).