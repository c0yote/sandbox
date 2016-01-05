import os

for fn in os.listdir('.'):
  if os.path.isfile(fn):
    if 'B.Cu' in fn:
      os.rename(fn, 'board.GBL')
    elif 'B.Mask' in fn:
      os.rename(fn, 'board.GBS')
    elif 'B.SilkS' in fn:
      os.rename(fn, 'board.GBO')
    elif 'Edge.Cuts' in fn:
      os.rename(fn, 'board.GKO')
    elif 'F.Cu' in fn:
      os.rename(fn, 'board.GTL')
    elif 'F.Mask' in fn:
      os.rename(fn, 'board.GTS')
    elif 'F.SilkS' in fn:
      os.rename(fn, 'board.GTO')
    elif '.drl' in fn:
      os.rename(fn, 'board.XLN')