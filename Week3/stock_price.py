import asyncio
from time import ctime

# โน้ตกันลืม Assignment 2: การใช้ wait() รันแข่งความเร็ว (Racing) และเคลียร์ตัวค้างกัน Memory Leak

async def fetch_stock_price(server_name, delay):
    # หลับสมมติความต่างเรื่องความหน่วงเน็ตแต่ละเซิร์ฟเวอร์
    await asyncio.sleep(delay)
    # ส่งราคาจำลองกลับเมื่อจบงาน
    return f"[{server_name}] Price: 150 USD"

async def main():
    # แตก Task รันควบคู่ขนานกัน 3 ตัว สแตนด์บายรอทำงานใน loop
    tasks = {
        asyncio.create_task(fetch_stock_price("Alpha", 3.0), name="Server-Alpha"),
        asyncio.create_task(fetch_stock_price("Beta", 0.8), name="Server-Beta"),
        asyncio.create_task(fetch_stock_price("Gamma", 1.5), name="Server-Gamma")
    }
    
    # รันแข่งดึงข้อมูล โดยหลุดเวลารอทันทีเมื่อเซิร์ฟเวอร์แรกตอบกลับมา (FIRST_COMPLETED)
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    
    # ดึงค่าเฉพาะออบเจกต์ที่ทำเสร็จคนแรกมาใช้งาน
    for finished_task in done:
        print(f"{ctime()} Winner Result: {finished_task.result()}")
        
    # ลูปสั่งเคลียร์งานย่อยที่ยังค้างคาใน pending (ตัวช้ากว่า) ทิ้งทั้งหมด ป้องกันปัญหาแรมรั่วหลังบ้าน
    if pending:
        print(f"{ctime()} Cleaning up {len(pending)} pending tasks...")
        for ongoing_task in pending:
            ongoing_task.cancel()

if __name__ == "__main__":
    asyncio.run(main())
