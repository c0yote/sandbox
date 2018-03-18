import hashlib
from functools import partial
import multiprocessing
import os

from hash import hash_file_in_chunks

def hash_and_hex_digest_file(filename):
  print('.',end='',flush=True)
  return (hash_file_in_chunks(filename, hashlib.md5()).hexdigest(), filename)

def _build_recursive_filename_list(directory):
  filename_list = list()
  for root, directories, filenames in os.walk(directory):
    for filename in filenames:
      filename_list.append(os.path.join(root, filename))
  return filename_list
  
def _get_parsed_arguments():
  import argparse
  parser = argparse.ArgumentParser(description='Check for and list duplicate files in a directory.')
  parser.add_argument('dir', help='The directory with files providing the basis of comparison.')
  return parser.parse_args()
  
if __name__ == '__main__':
  LEFT_COLUMN_WIDTH = 12

  parsed_args = _get_parsed_arguments()
  directory = parsed_args.dir
  
  filenames = _build_recursive_filename_list(directory)
  
  proc_pool = multiprocessing.Pool(processes=15)
  hash_list = proc_pool.map(hash_and_hex_digest_file, filenames)
  proc_pool.close()
  
  print()
  print('File hashing complete.  Analyzing:')
  
  hash_dict = dict()
  
  HASH = 0
  FILENAME = 1
  for entry in hash_list:
    if entry[HASH] not in hash_dict:
      hash_dict[entry[HASH]] = [entry[FILENAME]]
      print('.',end='',flush=True)
    else:
      hash_dict[entry[HASH]].append(entry[FILENAME])
      print('+',end='',flush=True)

  print()
  print('Duplicates:')
  for k,v in hash_dict.items():
    if len(v) > 1:
      print(v)
  
