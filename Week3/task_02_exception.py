# Objective: Extract returned data safely and inspect crashed tasks without breaking the main loop.
# วัตถุประสงค์: ดึงข้อมูลผลลัพธ์ที่ได้กลับมาอย่างปลอดภัย และตรวจสอบข้อผิดพลาด (Exception) ของ Task ที่พังโดยไม่ทำให้ระบบหลักหยุดทำงาน
import asyncio
from time import ctime

async def division_worker(a, b):
    await asyncio.sleep(0.5)
    return a / b # หาก b เป็น 0 จะเกิด ZeroDivisionError ขึ้นตรงนี้

async def main():
    # สร้าง Task สองตัว ตัวแรกสำเร็จแน่นอน ส่วนตัวที่สองจะหารด้วยศูนย์และพังลง
    task_success = asyncio.create_task(division_worker(10, 2))
    task_fail = asyncio.create_task(division_worker(10, 0))

    # จำลองเวลาผ่านไป 1 วินาทีเพื่อให้มั่นใจว่าทั้งสอง Task ทำงานเสร็จแล้ว
    await asyncio.sleep(1)
    
    # ตรวจสอบตัวที่ทำงานสำเร็จ: หากรันเสร็จแล้ว (done) และไม่มี Exception เกิดขึ้น
    if task_success.done() and not task_success.exception():
        print(f"{ctime()} Task Success Result: {task_success.result()}") # ดึงผลลัพธ์คืนมาจาก Task ด้วย .result()
        
    # ตรวจสอบตัวที่ทำงานพัง: ตรวจสอบหาข้อผิดพลาดโดยไม่ให้รันไทม์พังตาม
    if task_fail.done():
        # ดึงชนิดของ Exception ออกมาตรวจสอบโดยการเรียกใช้ .exception() แทนการปล่อยให้แอปพัง
        print(f"{ctime()} Task Fail Exception: {type(task_fail.exception()).__name__}") 

asyncio.run(main())