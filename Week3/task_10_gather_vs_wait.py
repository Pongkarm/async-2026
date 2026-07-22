# Objective: Compare the structural and mechanical differences of both strategies in a racing scenario.
# วัตถุประสงค์: เปรียบเทียบข้อแตกต่างเชิงโครงสร้างและพฤติกรรมระหว่างการใช้ asyncio.gather() และ asyncio.wait() ในรูปแบบการรันแข่งกัน
import asyncio
from time import ctime

async def runner(name, speed):
    await asyncio.sleep(speed)
    return f"{name} crossed line!"

async def main():
    # 1. การใช้งานแบบ gather() -> เน้นการรวมข้อมูลเป็นผืนเดียว (Unified Aggregation)
    # โปรแกรมจะต้องรอให้ทุกๆ Coroutine ทำงานเสร็จครบก่อนเสมอ ถึงจะคืนค่ากลับมารวมกันเป็น List เรียงตามลำดับที่ส่งเข้าไป
    print(f"{ctime()} --- Starting gather() approach (Unified Aggregation) ---")
    all_finishes = await asyncio.gather(runner("A", 0.5), runner("B", 2.0))
    print(f"{ctime()} Gather output: {all_finishes}\n") # แสดงผลลัพธ์พร้อมกันหลังตัวช้าสุดทำงานเสร็จ (ใช้เวลา 2.0 วินาที)
    
    # 2. การใช้งานแบบ wait() -> เน้นการควบคุมสถานะและการจัดการแบบเรียลไทม์ (State Control / Racing)
    # สามารถควบคุมเงื่อนไขการหลุดรอได้ เช่น หลุดทันทีเมื่อมีตัวแรกส่งข้อมูลสำเร็จ (FIRST_COMPLETED) โดยไม่ต้องรอตัวช้า
    print(f"{ctime()} --- Starting wait() approach (State control / Racing) ---")
    active_tasks = {asyncio.create_task(runner("A", 0.5)), asyncio.create_task(runner("B", 2.0))}
    
    done, pending = await asyncio.wait(active_tasks, return_when=asyncio.FIRST_COMPLETED)
    # ดึงค่าเฉพาะคนที่เสร็จก่อนมาแสดงผลทันที (หลังจากผ่านไปเพียง 0.5 วินาที)
    print(f"{ctime()} Wait output: The winner of the race is -> {list(done)[0].result()}")
    
    # วนลูปเพื่อยกเลิก Task ที่เหลือ (B ที่ต้องใช้เวลารัน 2.0 วินาที) เพื่อไม่ให้สิ้นเปลืองทรัพยากร
    for t in pending:
        t.cancel()

asyncio.run(main())