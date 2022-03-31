import os
import tqdm
source = './VG_100K/VG_100K_2//'
destination = './VG_100K/'
  
allfiles = os.listdir(source)
  
for f in tqdm.tqdm(allfiles):
    # print(f)
    os.rename(source + f, destination + f)