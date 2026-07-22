# Objective: Implement complex processing workflows based on task fulfillment conditions.
# วัตถุประสงค์: ออกแบบลอจิกการทำงานแบบกลุ่มที่ซับซ้อนขึ้นตามเงื่อนไขความสำเร็จของงานด้วย asyncio.wait()
import asyncio
from time import ctime

async def network_probe(server_name, delay):
    await asyncio.sleep(delay)
    return f"Ping successful: {server_name}"

async def main():
    # แตกกลุ่ม Task ย่อยเพื่อส่งสัญญาณพร้อมกันใน Event Loop
    tasks = {
        asyncio.create_task(network_probe("Primary-Server", 2.0)),
        asyncio.create_task(network_probe("Backup-Server-1", 0.5)),
        asyncio.create_task(network_probe("Backup-Server-2", 1.0))
    }
    
    # ใช้ asyncio.wait รอคอยแบบแข่งกัน โดยจะหยุดรอก็ต่อเมื่อมี Task ตัวแรกทำสำเร็จ (FIRST_COMPLETED)
    # ฟังก์ชันจะแยกผลลัพธ์คืนมาให้ 2 เซต คือ done (ตัวที่เสร็จแล้ว) และ pending (ตัวที่ยังวิ่งค้างคาอยู่)
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    
    print(f"{ctime()} Count of Tasks Done: {len(done)}")       # คาดว่าจะเป็น 1 (Backup-Server-1 ทำงานเสร็จก่อน)
    print(f"{ctime()} Count of Tasks Pending: {len(pending)}") # คาดว่าจะเป็น 2 (อีกสองเซิร์ฟเวอร์ที่เหลือรันช้ากว่า)
    
    # พิมพ์แสดงผลลัพธ์ของตัวแปรที่ดึงสำเร็จเป็นอันดับแรก
    for finished_task in done:
        print(f"{ctime()} Fastest Task Result: {finished_task.result()}")
        
    # วนลูปเพื่อยกเลิก Task ที่เหลือทั้งหมดที่ยังอยู่ระหว่างประมวลผล เพื่อประหยัดพลังงานทรัพยากรและป้องกันการรั่วไหล
    for ongoing_task in pending:
        ongoing_task.cancel()

asyncio.run(main())