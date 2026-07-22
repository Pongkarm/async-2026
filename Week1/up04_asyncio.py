
import asyncio
from time import ctime, time

async def update_cup_number(customer_name):
    print(f"{ctime()} | LCD: Processing for customer {customer_name}...")
    await asyncio.sleep(1.0)
    print(f"{ctime()} | LCD: Done for customer {customer_name}.")

async def make_coffee(customer_name):
    print(f"{ctime()} | Making coffee for {customer_name}...")
    await asyncio.sleep(1.0)
    print(f"{ctime()} | Coffee ready for {customer_name}!")

async def customer_task(customer_name):
    await make_coffee(customer_name)
    await update_cup_number(customer_name)

async def main():
    queue = ['A', 'B', 'C']
    print(f"{ctime()} | === Asyncio Coffee Machine ===")
    start_time = time()

    tasks = []
    for customer in queue:
        task = asyncio.create_task(customer_task(customer))
        tasks.append(task)

    await asyncio.gather(*tasks)

    duration = time() - start_time
    print(f"{ctime()} | Total time: {duration:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())