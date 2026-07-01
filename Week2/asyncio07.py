# Program 7: Dual Tasks Concurrency
# Concept: Scheduling two distinct tasks concurrently and awaiting them individually without gather.
import asyncio
from time import time, ctime

async def cook_spaghetti(customer):
    print(f"{ctime()} -> Starting cooking for Customer {customer}...")
    await asyncio.sleep(1)
    print(f"{ctime()} -> Finished cooking for Customer {customer}!")

async def main():
    start_time = time()

    # Both tasks are thrown into the Event Loop execution queue immediately.
    task_a = asyncio.create_task(cook_spaghetti("A"))
    task_b = asyncio.create_task(cook_spaghetti("B"))

    # Awaiting task_a allows task_b to also advance concurrently during task_a's sleep time.
    await task_a
    await task_b

    # Total time drops to ~1 second because they ran concurrently!
    print(f"Total Operation Time: {time() - start_time:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())
