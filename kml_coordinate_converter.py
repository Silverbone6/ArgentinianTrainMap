from inputcoordinates import *
finalcoord = []
x=0
lon = str()
lat = str()
for i in inputcoordinates:
    if i==',':
        x+=1
    if i!=',' and i!=' ':
        if x==0:
            lon+=i
        if x==1:
            lat+=i     
    if i==' ':
        x=0
        finalcoord.append((float(lat),float(lon)))
        lon = str()
        lat = str()
f = open("outputcoordinates.py", "w")
finalcoord.reverse()
f.write(str(finalcoord))
f.close()