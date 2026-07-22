# Objective: Introspect runtime contexts and monitor open workload queues on the active loop.
# วัตถุประสงค์: ตรวจสอบบริบทการทำงานรันไทม์ (Introspection) และติดตามตรวจสอบคิวงานที่กำลังรันอยู่ใน Event Loop ปัจจุบัน
import asyncio
from time import ctime

async def dynamic_job(number):
    await asyncio.sleep(1.0)

async def main():
    # เรียกดูออบเจกต์ Task ของตัวเอง (จุดปัจจุบันที่ฟังก์ชันนี้กำลังรันอยู่บน Event Loop)
    me = asyncio.current_task()
    me.set_name("Main-Coordinator") # ตั้งชื่อให้กับฟังก์ชันควบคุมหลัก
    print(f"{ctime()} Active Execution Context Name: {me.get_name()}")
    
    # สั่งสร้าง Task ย่อยขึ้นมา 3 ตัว โดยตั้งชื่อป้ายกำกับไว้เพื่อสังเกตพฤติกรรมในคิวงานย่อย
    tasks = [asyncio.create_task(dynamic_job(i), name=f"Job-{i}") for i in range(3)]
    
    # ดึงรายชื่อออบเจกต์ Task ทั้งหมดที่กำลังรันอยู่ (Active) อยู่ใน Event Loop ขณะนั้น
    all_active = asyncio.all_tasks()
    print(f"{ctime()} Total Active Tasks inside Loop: {len(all_active)}") # จะเท่ากับ 4 (ตัว Main-Coordinator เอง + Job ย่อยอีก 3 ตัว)
    for t in all_active:
        # พิมพ์ชื่อป้ายกำกับของ Task ทั้งหมดที่ค้างอยู่ในลูปออกมาเพื่อดูระบบการจัดคิว
        print(f"{ctime()}  -> Active Queue Item: {t.get_name()}")

    # นอนรอ 1.1 วินาที เพื่อปล่อยให้ Job ย่อยทั้ง 3 ตัวประมวลผลเสร็จสิ้นและหลุดออกจาก Event Loop
    await asyncio.sleep(1.1) 

asyncio.run(main())