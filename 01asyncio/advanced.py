# This advanced example uses asyncio to implement a producer-consumer scenario, 
# where the producer generates data at certain intervals and the consumer processes 
# it as it becomes available. 
# This scenario is typical in applications that require real-time data processing.


import asyncio
import random

async def producer(queue):
    for _ in range(10):
        await asyncio.sleep(random.uniform(0.1,1.0)) # simulate irregular production
        item = random.randint(1,100)
        await queue.put(item)
        print(f"Produced {item}")

    await queue.put(None) # Sentinel to indicate completion


async def consumer(queue):
    while True:
        item = await queue.get()
        if item is None:
            break # end when producer has no more tasks
        await asyncio.sleep(random.uniform(0.1,1.0)) # simulate processing time
        print(f"Consumed {item}")


async def main():
    queue = asyncio.Queue()
    producer_task = asyncio.create_task(producer(queue))
    consumer_task = asyncio.create_task(consumer(queue))

    await producer_task
    await consumer_task


asyncio.run(main())



