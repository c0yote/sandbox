import asyncio
from time import sleep

# Not Asynchronous
def sync_go():
  print('Wait for it...')
  sleep(1)
  print('Go!')
  
async def async_go():
  print('Wait for it...')
  await asyncio.sleep(1)
  print('Go!')
  
if __name__ == '__main__':
  print('Running synchronously takes 3 seconds.')
  for _ in range(0,3):
    sync_go()
  
  print('Running asynchronously takes 1 second.')
  loop = asyncio.get_event_loop()
  loop.run_until_complete(asyncio.gather(
    async_go(),
    async_go(),
    async_go()))