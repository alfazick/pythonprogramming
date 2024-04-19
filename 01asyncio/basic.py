import asyncio 

async def hello_world():
    print("Hello")
    await asyncio.sleep(1)
    print("World")

# running the async function // must to block with executor
    
asyncio.run(hello_world())
