# Program 9: Dynamic Task List
# Concept: Managing multiple tasks in a list and awaiting them.
import asyncio
from time import time, ctime

async def serve_customer(name):
    print(f"{ctime()} -> Handling customer {name}")
    await asyncio.sleep(1)
    print(f"{ctime()} -> Done customer {name}")

async def main():
    start_time = time()
    customers = ["A", "B", "C", "D"]
    task_list = []
    
    for name in customers:
        t = asyncio.create_task(serve_customer(name))
        task_list.append(t)
        
    for t in task_list:
        await t
        
    print(f"Served all {len(customers)} customers in {time() - start_time:.2f} seconds.")

if __name__ == "__main__":
    asyncio.run(main())
