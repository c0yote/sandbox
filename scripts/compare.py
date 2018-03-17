import hashlib
import os

store = {}

c = 0

duplicates = []

for root, directories, filenames in os.walk('.\\'):
  for filename in filenames:
    the_hash = hashlib.md5(open(os.path.join(root,filename), 'rb').read()).hexdigest()
    if the_hash in store:
      print('+',end='',flush=True)
      duplicates.append('Duplicate: '+store[the_hash]+' & '+ os.path.join(root,filename))
    else:
      print('.',end='', flush=True)
      store[the_hash] = os.path.join(root,filename)
      
    c += 1
    if c % 50 == 0:
      print('\t'+str(c), flush=True)
      
print('------------------------------------------------------------',flush=True)
for d in duplicates:
  print(d,flush=True)
print('------------------------------------------------------------',flush=True)
print('Processed '+str(len(store))+' files.',flush=True)
print('Found '+str(len(duplicates))+' duplicates.',flush=True)