import hashlib
from functools import partial
import multiprocessing
import os

from hash import hash_file_in_chunks

def hash_and_hex_digest_file(filename):
  print('.',end='',flush=True)
  return hash_file_in_chunks(filename, hashlib.md5()).hexdigest()

def _build_recursive_filename_list(directory):
  filename_list = list()
  for root, directories, filenames in os.walk(directory):
    for filename in filenames:
      filename_list.append(os.path.join(root, filename))
  return filename_list
  
def _get_parsed_arguments():
  import argparse
  parser = argparse.ArgumentParser(description='Check if files in a test directory are represented in the population of an archive directory.')
  parser.add_argument('archdir', help='The archive directory with files providing the basis of comparison.')
  parser.add_argument('testdir', help='The directory with the files to check are represented in the archive directory.')
  parser.add_argument('--report', help='Write a text file report of the analysis.', action="store_true")
  return parser.parse_args()

def _get_file_unrepresented_in_archive(archive_hash_list, filename):
  hash_string = hash_file_in_chunks(filename, hashlib.md5()).hexdigest()
  print('.',end='',flush=True)
  if hash_string not in archive_hash_list:
    return filename
  
if __name__ == '__main__':
  LEFT_COLUMN_WIDTH = 12

  parsed_args = _get_parsed_arguments()
  archive_directory = parsed_args.archdir
  test_directory = parsed_args.testdir
  do_report_to_file = parsed_args.report
  
  archive_filenames = _build_recursive_filename_list(archive_directory)
  test_filenames = _build_recursive_filename_list(test_directory)
  
  archive_proc_pool = multiprocessing.Pool(processes=10)
  archive_hash_list = archive_proc_pool.map(hash_and_hex_digest_file, archive_filenames)
  archive_proc_pool.close()
  print()
  print('Collected Hash Data for ['+str(len(archive_hash_list))+'] files in archive directory.',flush=True)
  
  test_proc_pool = multiprocessing.Pool(processes=10)
  partial_function_job = partial(_get_file_unrepresented_in_archive, archive_hash_list)
  unrepresented_file_list = test_proc_pool.map(partial_function_job, test_filenames)
  test_proc_pool.close()
  
  print()
  print('Found following unrepresented files:')
  for filename in unrepresented_file_list:
    if filename: print(filename)
