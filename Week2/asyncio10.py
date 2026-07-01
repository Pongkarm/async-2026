# Program 10: Extracting Return Values from Tasks
# Concept: Accessing returned results from completed Task objects using .result() or direct assignment.
import asyncio

async def calculate_bill(customer, base_price):
    print(f"Calculating receipt for Customer {customer}...")
    await asyncio.sleep(1)
    final_price = base_price * 1.07 # Adding 7% tax
    return final_price

async def main():
    # Schedule tasks with return statements
    task_a = asyncio.create_task(calculate_bill("A", 100))
    task_b = asyncio.create_task(calculate_bill("B", 200))

    # Awaiting a task object captures its return value directly
    result_a = await task_a
    result_b = await task_b

    # Alternative way: extracting via the .result() method after completion
    # result_b = task_b.result()

    print(f"\nFinal Bill A: {result_a:.2f}")
    print(f"Final Bill B: {result_b:.2f}")
    print(f"Combined Total Revenue: {result_a + result_b:.2f}")

if __name__ == "__main__":
    asyncio.run(main())
