# Program 10: Retreiving Task Return Value
# Concept: Accessing the return value of completed tasks.
import asyncio

async def calculate_bill(customer, base_price):
    print(f"Calculating receipt for Customer {customer}...")
    await asyncio.sleep(1)
    final_price = base_price * 1.07
    return final_price

async def main():
    task_a = asyncio.create_task(calculate_bill("A", 100))
    task_b = asyncio.create_task(calculate_bill("B", 200))
    
    result_a = await task_a
    result_b = await task_b
    
    # result_b = task_b.result()
    
    print(f"\nFinal Bill A: {result_a:.2f}")
    print(f"Final Bill B: {result_b:.2f}")
    print(f"Combined Total Revenue: {result_a + result_b:.2f}")

if __name__ == "__main__":
    asyncio.run(main())
