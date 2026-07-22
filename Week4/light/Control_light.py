# Control_light.py
import asyncio
import httpx
from time import time, ctime

BASE_URL = "http://172.16.2.117:8088"
MY_STUDENT_ID = "6710301009"

LIGHTS = ["light_1", "light_2", "light_3", "light_4"]


async def turn_on_light(student_id: str, light_id: str) -> dict:
    url = f"{BASE_URL}/api/{student_id}/lights/{light_id}"
    payload = {"status": "ON"}
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=payload, timeout=10.0)
        return response.json()


async def reset_lights():
    async with httpx.AsyncClient() as client:
        await client.delete(f"{BASE_URL}/api/{MY_STUDENT_ID}/lights/reset")
    print(f"{ctime()} | Lights reset to OFF.\n")


async def sequential_mode():
    """Mode 1: เปิดไฟทีละดวงแบบเรียงลำดับ (Sequential)"""
    await reset_lights()
    print(f"{ctime()} | === [Mode 1] Sequential: Turn on lights one by one ===")
    start_time = time()

    for light_id in LIGHTS:
        print(f"{ctime()} | Turning on {light_id}...")
        result = await turn_on_light(MY_STUDENT_ID, light_id)
        print(f"{ctime()} | Response: {result}")

    print(f"{ctime()} | Total time (Sequential): {time() - start_time:.2f} seconds.")


async def async_mode():
    """Mode 2: เปิดไฟทุกดวงพร้อมกัน (Async with gather)"""
    await reset_lights()
    print(f"{ctime()} | === [Mode 2] Async: Turn on all lights concurrently ===")
    start_time = time()

    tasks = [asyncio.create_task(turn_on_light(MY_STUDENT_ID, light_id)) for light_id in LIGHTS]
    results = await asyncio.gather(*tasks)

    for result in results:
        print(f"{ctime()} | Response: {result}")

    print(f"{ctime()} | Total time (Async): {time() - start_time:.2f} seconds.")


async def both_modes():
    """Mode 3: รันทั้ง 2 โหมดเพื่อเปรียบเทียบ"""
    await sequential_mode()
    print()
    await async_mode()


async def main():
    print("=" * 50)
    print("   💡 Smart Lab Lighting System Controller")
    print("=" * 50)
    print("  [1] Sequential - เปิดไฟทีละดวง")
    print("  [2] Async      - เปิดไฟพร้อมกัน")
    print("  [3] Both       - รันทั้ง 2 โหมดเปรียบเทียบ")
    print("  [reset] reset  - ปิดทุกดวง")
    print("=" * 50)

    choice = input("Select mode (1/2/3/reset): ").strip()

    if choice == "1":
        await sequential_mode()
    elif choice == "2":
        await async_mode()
    elif choice == "3":
        await both_modes()
    elif choice == "reset":
        await reset_lights()
    else:
        print("Invalid choice. Please select 1, 2, 3 or reset.")


if __name__ == "__main__":
    asyncio.run(main())
