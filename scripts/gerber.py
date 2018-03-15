import os

def _get_parsed_arguments():
  import argparse
  parser = argparse.ArgumentParser(description='Add gerber file extensions to KiCAD plot files.')
  parser.add_argument('dir', 
                      nargs='?',
                      default='.', 
                      help='The directory containing the files to rename.')
  return parser.parse_args()

def _add_extension_if_found(filename, target_string, extension):
  if target_string in filename and extension not in filename:
    os.replace(filename, filename+extension)
    
if __name__ == '__main__':
  parsed_args = _get_parsed_arguments()
  directory = parsed_args.dir
  
  for filename in os.listdir('.'):
    if os.path.isfile(filename):
      _add_extension_if_found(filename, 'B.Cu', '.GBL')
      _add_extension_if_found(filename, 'B.Mask', '.GBS')
      _add_extension_if_found(filename, 'B.SilkS', '.GBO')
      _add_extension_if_found(filename, 'Edge.Cuts', '.GKO')
      _add_extension_if_found(filename, 'F.Cu', '.GTL')
      _add_extension_if_found(filename, 'F.Mask', '.GTS')
      _add_extension_if_found(filename, 'F.SilkS', '.GTO')
      _add_extension_if_found(filename, '.drl', '.XLN')
      