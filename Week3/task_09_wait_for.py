# Objective: Enforce strict deadlines on operations and raise errors if exceeded.
# วัตถุประสงค์: กำหนดขอบเขตเวลาเส้นตาย (Deadline Timeout) ให้กับการทำงาน และสั่งยกเลิกงานทิ้งทันทีหากหมดเวลาที่ตั้งไว้
import asyncio
from time import ctime

async def long_query_simulation():
    print(f"{ctime()} Database: Fetching data...")
    await asyncio.sleep(5.0) # จำลองฐานข้อมูลดึงข้อมูลขนาดใหญ่ใช้เวลานานถึง 5 วินาที
    return "Heavy_Report_Data"

async def main():
    try:
        print(f"{ctime()} Main: Enforcing a strict 2-second timeout deadline...")
        # สั่งรันคอรูทีนพร้อมกับบังคับเงื่อนไขเวลา Timeout ไว้ที่ 2.0 วินาที
        # หากเวลารันจริงเกิน 2.0 วินาที ระบบจะยกเลิก Task นั้นทิ้งอัตโนมัติและโยน TimeoutError ขึ้นมา
        result = await asyncio.wait_for(long_query_simulation(), timeout=2.0)
        print(f"{ctime()} Result acquired: {result}")
    except asyncio.TimeoutError:
        # ดักจับเมื่อเวลารันการทำงานภายนอกเกินขีดจำกัดที่ตั้งไว้
        print(f"{ctime()} Main Error Alert: Operation timed out! Task terminated.")

asyncio.run(main())