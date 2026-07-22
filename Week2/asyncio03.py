# Program 3: Event Loop (asyncio.run)
# Concept: Using the event loop to execute a coroutine object to completion.
import asyncio
from time import time, ctime

async def serve_customer(name):
    print(f"{ctime()} -> Cooking for {name}...")
    await asyncio.sleep(1)
    print(f"{ctime()} -> Served {name}!")
    return f"Spaghetti for {name}"

if __name__ == "__main__":
    start_time = time()
    print(f"{ctime()} -> Creating coroutine object...")
    coro = serve_customer("A")
    
    print(f"{ctime()} -> Running the coroutine object using asyncio.run()...")
    result = asyncio.run(coro)
    print(f"{ctime()} -> Coroutine finished. Returned value: {result}")
    print(f"Total Operation Time: {time() - start_time:.2f} seconds")
