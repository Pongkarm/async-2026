# foodcourt_05_mix_concepts.py
import asyncio
from time import time, ctime
from food_utils import send_order_to_kitchen

async def main():
    MY_STUDENT_ID = "6710301007"
    print(f"{ctime()} | --- [Task 5] Advanced Practice: Mixing concepts together ---")
    start_time = time()

    noodle_task = asyncio.create_task(send_order_to_kitchen(MY_STUDENT_ID, "noodle", "Egg Noodles"))

    chicken_task = asyncio.create_task(asyncio.wait_for(
        send_order_to_kitchen(MY_STUDENT_ID, "hainanese_chicken", "Chicken Rice Special"),
        timeout=1.0
    ))

    try:
        results = await asyncio.gather(noodle_task, chicken_task)
        print(f"{ctime()} | Success: All food served on time! Received {len(results)} dishes.")
    except asyncio.TimeoutError:
        print(f"{ctime()} | Error: An unexpected timeout occurred during gather process...")

    print(f"{ctime()} | Total elapsed time: {time() - start_time:.2f} seconds.")

if __name__ == "__main__":
    asyncio.run(main())
