from hash import hash_file_in_chunks
import os

# Collect hashes from the reference directory.
archive_file_hash_list = list()
subject_file_hash_list = list()

for root, directories, filenames in os.walk('.\\'):
	for filename in filenames:
		hash_string = hash_file_in_chunks(filename).hexdigest()
		archive_file_hash_list.append(hash_string)
		
print(archive_file_hash_list)

# c = 0

# duplicates = []

# for root, directories, filenames in os.walk('.\\'):
  # for filename in filenames:
    # hash_string = hash_file_in_chunks(filename).hexdigest()
    # if hash_string in store:
      # print('+',end='',flush=True)
      # duplicates.append('Duplicate: '+store[hash_string]+' & '+ os.path.join(root,filename))
    # else:
      # print('.',end='', flush=True)
      # store[hash_string] = os.path.join(root,filename)
      
    # c += 1
    # if c % 50 == 0:
      # print('\t'+str(c), flush=True)
      
# print('------------------------------------------------------------',flush=True)
# for d in duplicates:
  # print(d,flush=True)
# print('------------------------------------------------------------',flush=True)
# print('Processed '+str(len(store))+' files.',flush=True)
# print('Found '+str(len(duplicates))+' duplicates.',flush=True)