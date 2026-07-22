# Objective: Label task objects explicitly to simplify logging and production tracking.
# วัตถุประสงค์: ตั้งชื่อป้ายกำกับของออบเจกต์ Task เพื่อช่วยในการทำ Logging ตรวจสอบปัญหา และติดตามระบบในขณะทำงานจริง
import asyncio
from time import ctime

async def background_worker():
    await asyncio.sleep(0.1)

async def main():
    task = asyncio.create_task(background_worker())
    
    # ดึงชื่อเริ่มต้นของ Task ที่สร้างขึ้นมาใหม่ (โดยปกติ Python จะตั้งชื่อออโต้เป็นรูปแบบ Task-N)
    print(f"{ctime()} Initial Name: {task.get_name()}") 
    
    # ทำการกำหนดชื่อใหม่ตามใจชอบเพื่อให้อ่านง่ายและสื่อความหมายถึงฟังก์ชันการทำงานจริง
    task.set_name("Payment-Gateway-Validator")
    # ดึงชื่อที่แก้ไขใหม่ขึ้นมาพิมพ์ตรวจสอบ
    print(f"{ctime()} Updated Name: {task.get_name()}") 

asyncio.run(main())