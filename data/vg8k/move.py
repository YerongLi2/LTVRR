import os
  
source = './VG_100K/images/'
destination = './VG_100K/'
  
allfiles = os.listdir(source)
  
for f in allfiles:
    print(f)
    # os.rename(source + f, destination + f)