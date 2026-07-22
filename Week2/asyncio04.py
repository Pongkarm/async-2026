# Program 4: The await keyword
# Concept: Pausing execution of a coroutine to let other tasks run, using await.
import asyncio
from time import time, ctime

async def serve_customer(name):
    print(f"{ctime()} -> Cooking for {name}...")
    await asyncio.sleep(1)
    print(f"{ctime()} -> Served {name}!")

async def main():
    start_time = time()
    print(f"{ctime()} -> Main: Starting to serve Customer A")
    await serve_customer("A")
    print(f"Total Operation Time: {time() - start_time:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())
