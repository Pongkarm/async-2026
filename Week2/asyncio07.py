# Program 7: Concurrent Tasks (Dual Tasks)
# Concept: Scheduling multiple concurrent tasks and awaiting them.
import asyncio
from time import time, ctime

async def cook_spaghetti(customer):
    print(f"{ctime()} -> Starting cooking for Customer {customer}...")
    await asyncio.sleep(1)
    print(f"{ctime()} -> Finished cooking for Customer {customer}!")

async def main():
    start_time = time()
    task_a = asyncio.create_task(cook_spaghetti("A"))
    task_b = asyncio.create_task(cook_spaghetti("B"))
    
    await task_a
    await task_b
    print(f"Total Operation Time: {time() - start_time:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())
