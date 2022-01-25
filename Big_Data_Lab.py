import csv
from typing import Dict

NRMN = []
ARD2 = []
BEAV = []
BOIS = []
CENT = []
STIL = []
TISH = []
TULN = []
WOOD = []
nrmn_day = 0
nrmn_days = []
ard2_day = 0
ard2_days = []
beav_day = 0
beav_days = []
bois_day = 0
bois_days = []
cent_day = 0
cent_days = []
stil_day = 0
stil_days = []
tish_day = 0
tish_days = []
tuln_day = 0
tuln_days = []
wood_day = 0
wood_days = []
stations = [NRMN, ARD2, BEAV, BOIS, CENT, STIL, TISH, TULN, WOOD]

with open('BigData2016.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    

    for row in reader:
        if float(row['TMAX']) != -996 and float(row['TMIN']) != -996:
            if row['STID'] == 'NRMN':
                NRMN.append(float(row['TMAX']))
                nrmn_day += 1
                nrmn_days.append(nrmn_day)
               #NRMN.append(float(row['TMIN']))
            if row['STID'] == 'ARD2':
                ARD2.append(float(row['TMAX']))
                ard2_day += 1
                ard2_days.append(ard2_day)
                #ARD2.append(float(row['TMIN']))
            if row['STID'] == 'BEAV':
                BEAV.append(float(row['TMAX']))
                beav_day += 1
                beav_days.append(beav_day)
                #BEAV.append(float(row['TMIN']))
            if row['STID'] == 'BOIS':
                BOIS.append(float(row['TMAX']))
                bois_day += 1
                bois_days.append(bois_day)
                #BOIS.append(float(row['TMIN']))
            if row['STID'] == 'CENT':
                CENT.append(float(row['TMAX']))
                cent_day += 1
                cent_days.append(cent_day)
                #CENT.append(float(row['TMIN']))
            if row['STID'] == 'STIL':
                STIL.append(float(row['TMAX']))
                stil_day += 1
                stil_days.append(stil_day)
                #STIL.append(float(row['TMIN']))
            if row['STID'] == 'TISH':
                TISH.append(float(row['TMAX']))
                tish_day += 1
                tish_days.append(tish_day)
                #TISH.append(float(row['TMIN']))
            if row['STID'] == 'TULN':
                TULN.append(float(row['TMAX']))
                tuln_day += 1
                tuln_days.append(tuln_day)
                #TULN.append(float(row['TMIN']))
            if row['STID'] == 'WOOD': 
                WOOD.append(float(row['TMAX']))
                wood_day += 1
                wood_days.append(wood_day)
                #WOOD.append(float(row['TMIN']))
        


#for i in stations:
    #print(f"max:{max(i)}, min:{min(i)}")

import matplotlib.pyplot as plt
plt.plot(nrmn_days, NRMN, color='red', marker='o')
plt.plot(ard2_days, ARD2, color='blue', marker='o')
plt.plot(beav_days, BEAV, color='purple', marker='o')
plt.plot(bois_days, BOIS, color='yellow', marker='o')
plt.plot(cent_days, CENT, color='green', marker='o')
plt.plot(stil_days, STIL, color='orange', marker='o')
plt.plot(tish_days, TISH, color='gray', marker='o')
plt.plot(tuln_days, TULN, color='turquoise', marker='o')
plt.plot(wood_days, WOOD, color='violet', marker='o')
plt.title('Maximum Tempature per Day', fontsize=14)
plt.xlabel('Day', fontsize=14)
plt.ylabel('Tempature (F)', fontsize=14)
plt.grid(True)
plt.show()



