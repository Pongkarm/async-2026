# Program 6: Concurrent Task
# Concept: Wrapping a coroutine in asyncio.create_task() registers it on the event loop to run concurrently.
import asyncio
from time import time, ctime

async def cook_spaghetti(customer):
    print(f"{ctime()} -> Starting cooking for Customer {customer}...")
    await asyncio.sleep(1)
    print(f"{ctime()} -> Finished cooking for Customer {customer}!")

async def main():
    start_time = time()
    task_a = asyncio.create_task(cook_spaghetti("A"))
    print(f"{ctime()} -> Main program can do other things while Task A runs in background.")
    await task_a
    print(f"Total Operation Time: {time() - start_time:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())
