import datetime
dt = datetime.datetime.now()
print ("Current Date : ",end=" ")
print (dt.strftime("%d-%m-%Y"))
print ("Current Time : ",end=" ")
print (dt.strftime("%H:%M:%S"))
