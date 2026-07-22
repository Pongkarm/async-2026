from time import ctime, time
import asyncio

# ฟังก์ชันจำลองการทำกาแฟแบบ Asynchronous
async def make_coffee(customer_name):
    print(f"{ctime()} กำลังชงกาแฟให้ ลูกค้า {customer_name}...")
    await asyncio.sleep(1) # จำลองเวลาชงกาแฟ 1 วินาที (แทน 1 นาที)
    print(f"{ctime()} ลูกค้า {customer_name}: ได้รับกาแฟแล้ว!")

async def main():
    queue = ['A', 'B', 'C']
    print(f"{ctime()} === เริ่มระบบจำลองตู้กาแฟแบบ asyncio ===")
    start_time = time()

    tasks = []
    for customer in queue:
        # สร้าง Coroutine และแปลงให้เป็น Task เพื่อให้ Event Loop บริหาร
        task = asyncio.create_task(make_coffee(customer))
        tasks.append(task)

    # สั่งให้ทำงานพร้อมกัน
    await asyncio.gather(*tasks)

    duration = time() - start_time
    print(f"{ctime()} ลูกค้า {len(queue)} คน ได้รับกาแฟครบแล้ว! ใช้เวลารวมทั้งหมด: {duration:0.2f} วินาที")

# สั่งให้ระบบ Async เริ่มทำงาน
if __name__ == "__main__":
    # ใช้ asyncio.run เพื่อเปิด Event Loop หลักของโปรแกรม
    asyncio.run(main())