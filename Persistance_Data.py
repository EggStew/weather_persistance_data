import pandas as pd
import numpy as np
import enum 
import matplotlib.pyplot as plt
# uploads data file and converts it to a usable array

file = (r'C:/Users/edward.stewart/OneDrive - Sealand Projects Ltd/Desktop/Python/2021Data.csv')
raw_data = pd.read_csv(file)
data = np.array(raw_data)
raw_data.head()

# generates an empty list to be used later in persistance values

myList = []
mydata = []

#initialises varaibles to be used

datapoint1 = 0
datapoint2 = 0

# generates enumeration for the available months

class Month(enum.Enum):
   June = 1
   July = 2
   August = 3
   September = 4

# asks the user for which month to calculate persistance data for

month = input("Which month would you like persistance data for? (June, July, August, September) ")
#month in Month.                                                                                                                                 
persist_month = Month[month]

# define data range based upon chosen month (slicing)

if persist_month == Month.June:
   datapoint1 = 0
   datapoint2 = 7193

elif persist_month == Month.July:
   datapoint1 = 7194
   datapoint2 = 14488
     
elif persist_month == Month.August:
   datapoint1 = 14489
   datapoint2 = 21807

elif persist_month == Month.September:
    datapoint1 = 21808
    datapoint2 = 28989
    
# ask user what wind speed persistance data is the focus of persistance data

persist_wspd = int(input("Which wind speed would you like persistance data for? "))

#search through data range for inputed speed and month selected
for value in data[datapoint1:datapoint2, 7]:  
 mydata.append(value)
 
itr = 0
isfinished = 0
while itr < len(mydata):
    count = 0
    if mydata[itr] >= persist_wspd:
        itr2 = 0
        while isfinished == 0 and mydata[itr + itr2] >= persist_wspd:
            count += 1
            itr2 += 1
            check = itr + itr2 + 1
            if check > len(mydata):
                isfinished = 1
        else:
            myList.append(count)
            check = itr + itr2 + 1
            if check > len(mydata):
                itr = len(mydata)
            else:
                itr += itr2 + 1
    
    else:
        check = itr + 1
        if check > len(mydata):
            itr = len(mydata)
        else:
            itr += 1
if len(myList) > 0:
    print(myList)
    avg = sum(myList)/len(myList)
    avgMin = avg*6
    print("The average persistance data for Wind Speed: " + str(persist_wspd) + ", in the month of: " + str(persist_month) + ", is: " + str(avgMin))  
else:
    print("Windspeed does not exceed: " + str(persist_wspd))
# when first instance of inputed speed is found add 1 to counter
#perform check IF the next data value is also inputed speed, if it is then add to counter, else add counter value to mylist
#continue through data set
#once data set is completed average out list value
#multiply average by 6 minute data interval
# print average duration for inputed wind speed for inputed month 

num_bins = 11
n, bins, patches = plt.hist(mydata, num_bins, facecolor='blue', alpha=0.5)
plt.xlabel('Wind Speed (m/s)')
plt.ylabel('Number of Data Points')
plt.title(r'Histogram of 2021, September, Gust Wind Speed')
plt.subplots_adjust(left=0.15)
plt.show()
