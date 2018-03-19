from functools import partial
from multiprocessing import Manager, Pool
from time import sleep

def increment(value, pool_queue):
  sleep(0.001)
  pool_queue.put(True)
  return value + 1

def result(value):
  print('Done')
  
def error(exception):
  print(exception)
  
if __name__ == '__main__':
  data = [1 for i in range(1000)]

  pool = Pool(processes=5)
  pool_manager = Manager()
  pool_queue = pool_manager.Queue()
  
  job_partial = partial(increment, pool_queue=pool_queue)
  results = pool.map_async(job_partial, data, callback=result, error_callback=error)
  pool.close()
  
  while not results.ready():
    print(pool_queue.qsize()/len(data))
    sleep(0.1)
    
  print(repr(results.get()))