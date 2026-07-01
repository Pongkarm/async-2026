# Program 6: Creating a Concurrent Task
# Concept: Wrapping a coroutine inside asyncio.create_task() to schedule it to run in the background.
import asyncio
from time import time, ctime

async def cook_spaghetti(customer):
    print(f"{ctime()} -> Starting cooking for Customer {customer}...")
    await asyncio.sleep(1)
    print(f"{ctime()} -> Finished cooking for Customer {customer}!")

async def main():
    start_time = time()

    # create_task() instantly registers the coroutine to the Event Loop background queue.
    task_a = asyncio.create_task(cook_spaghetti("A"))

    print(f"{ctime()} -> Main program can do other things while Task A runs in background.")

    # We await the task object to ensure it finishes before main() exits.
    await task_a

    print(f"Total Operation Time: {time() - start_time:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())
