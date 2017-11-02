import asyncio
from time import sleep

from aioconsole import ainput
  
stop = False
  
async def async_go():
  global stop
  while not stop:
    print('Going!')
    await asyncio.sleep(3)
  
async def async_in():
  global stop
  while not stop:
    cmd = await ainput('> ')
    print(cmd)
    if 'stop' in cmd:
      stop = True
      print('Flag set, waiting for tasks to stop.')
  
if __name__ == '__main__':
  print('Type "stop" to stop the async tasks.')
  loop = asyncio.get_event_loop()
  loop.run_until_complete(asyncio.gather(
    async_go(),
    async_go(),
    async_in()))