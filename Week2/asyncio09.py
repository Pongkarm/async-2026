# Program 9: Dynamically Tracking Tasks in a List
# Concept: Managing multiple generated tasks dynamically by appending them into a standard Python list.
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

    # 1. Schedule all tasks dynamically and add to our tracking list
    for name in customers:
        t = asyncio.create_task(serve_customer(name))
        task_list.append(t)

    # 2. Loop through the list to await each task one by one manually
    for t in task_list:
        await t

    print(f"Served all {len(customers)} customers in {time() - start_time:.2f} seconds.")

if __name__ == "__main__":
    asyncio.run(main())
