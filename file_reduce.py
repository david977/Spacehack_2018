import numpy as np
from numpy import genfromtxt
from numpy import savetxt

mydata=genfromtxt('C:/Users/Prashant Mahato/Downloads/powerOutCol-irradiation-1y-4EntriesPerHour.csv')
##Irradiation for 5 years for power output, one reading per hour (
leng=len(mydata)
my1=mydata[::4]
print (len(my1))
np.savetxt('irradiation1y_new.csv',my1,fmt='%d')

##24 rows to be removed from bottom for 5y output 
