# Objective: Learn how to query the lifecycle status of a task object.
# วัตถุประสงค์: เรียนรู้วิธีการตรวจสอบสถานะวงจรชีวิต (Lifecycle Status) ของออบเจกต์ Task
import asyncio
from time import ctime

async def short_job():
    await asyncio.sleep(1)
    return "Success"

async def main():
    # สร้าง Task จาก Coroutine เพื่อส่งเข้าไปทำงานใน Event Loop ทันทีแบบ Asynchronous
    task = asyncio.create_task(short_job())
    
    # ตรวจสอบสถานะทันทีหลังจากสร้าง Task (ยังทำงานไม่เสร็จ)
    print(f"{ctime()} Is task done? {task.done()}")          # คาดว่าเป็น False เพราะงานยังรันอยู่
    print(f"{ctime()} Is task canceled? {task.cancelled()}")  # คาดว่าเป็น False เพราะยังไม่ได้ถูกสั่งยกเลิก
    
    await task # รอ (await) ให้ Task ทำงานเสร็จสิ้นอย่างสมบูรณ์
    
    # ตรวจสอบสถานะอีกครั้งหลังจากที่งานทำงานเสร็จสิ้นแล้ว
    print(f"{ctime()} Is task done now? {task.done()}")      # คาดว่าเป็น True เพราะงานรันเสร็จเรียบร้อยแล้ว
    print(f"{ctime()} Is task canceled now? {task.cancelled()}") # คาดว่าเป็น False เพราะรันเสร็จโดยไม่ได้ถูกยกเลิก

asyncio.run(main())