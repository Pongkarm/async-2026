# Objective: Stop an ongoing execution prematurely by triggering a cancellation exception.
# วัตถุประสงค์: หยุดการทำงานของ Task ที่กำลังรันอยู่ก่อนกำหนด โดยการส่ง Exception การยกเลิก (CancelledError) เข้าไปกระตุ้น
import asyncio
from time import ctime

async def background_loop():
    try:
        print(f"{ctime()} Worker: Starting long infinite process...")
        while True:
            await asyncio.sleep(1)
            print(f"{ctime()} Worker: Still ticking...")
    except asyncio.CancelledError:
        # เมื่อ Task ถูกสั่งยกเลิก (.cancel) จะมีการโยน CancelledError เข้ามาที่จุด await ถัดไปใน Coroutine
        # ทำให้เราดักจับข้อผิดพลาดนี้เพื่อเคลียร์ทรัพยากรที่ใช้ค้างอยู่ได้ก่อนที่จะจบการทำงาน
        print(f"{ctime()} Worker: Interrupted! Executing clean-up logic before exit...")

async def main():
    task = asyncio.create_task(background_loop())
    await asyncio.sleep(2.5) # ปล่อยให้ Task รันไปประมาณ 2.5 วินาที
    
    print(f"{ctime()} Main: Changing plans, canceling the worker task now!")
    task.cancel() # ส่งคำสั่งขอยกเลิก Task นี้ทันที
    await asyncio.sleep(0.1) # พักรอระยะสั้นๆ เพื่อให้ Task ได้ประมวลผลในฝั่งบล็อก except CancelledError จนจบ

asyncio.run(main())