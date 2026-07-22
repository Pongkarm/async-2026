# โน้ตกันลืม Assignment 1: การใช้ Task ควบคุมเวลาทำงานและยกเลิกด้วย CancelledError
import asyncio
from time import ctime

async def delivery_task(package_id, duration):
    try:
        # พิมพ์แจ้งเริ่มวิ่งส่งของ
        print(f"{ctime()} Courier started delivering {package_id}...")
        
        # หลับจำลองเวลาเดินทาง
        await asyncio.sleep(duration)
        
        return f"Package {package_id} Delivered!"
        
    except asyncio.CancelledError:
        # ดักจับตอนโดน cancel ปลายทางสั่งให้ส่งของคืนคลัง (พิมพ์ข้อความตามสเปกอาจารย์เป๊ะๆ)
        print(f"{ctime()} Delivery Canceled! Returning package to warehouse.")
        # สำคัญมาก: ต้อง raise ขว้างข้อผิดพลาดไปต่อ ไม่งั้นสถานะ .cancelled() ของ Task ด้านนอกจะไม่เปลี่ยนเป็น True
        raise

async def main():
    # แตก Task ย่อยส่งของและตั้งชื่อป้ายกำกับไว้ตรวจสอบในลูป
    task = asyncio.create_task(delivery_task("P001", 5.0), name="Express-Courier")
    
    # ปล่อยให้รถวิ่งไปก่อน 2 วินาทีแรก
    await asyncio.sleep(2.0)
    
    # เช็กว่าส่งเสร็จหรือยังผ่านสถานะ .done()
    print(f"{ctime()} Checking task '{task.get_name()}'. Is it done? {task.done()}")
    
    # ถ้าครบกำหนด 2 วินาทีแล้วยังไม่เสร็จ (เนื่องจาก duration ตั้งไว้ 5) ให้สั่งดึงรถกลับคลังทันที
    if not task.done():
        print(f"{ctime()} Taking too long! Canceling the task...")
        task.cancel()
        
    # รอให้ลูปประมวลผลการยกเลิกภายในตัวแปรเสร็จสิ้น
    try:
        await task
    except asyncio.CancelledError:
        pass
        
    # ยืนยันสถานะสุดท้ายว่ายกเลิกสำเร็จชัวร์ๆ (cancelled() ต้องแสดงค่าเป็น True)
    print(f"{ctime()} Final verify: Is task officially canceled? {task.cancelled()}")

if __name__ == "__main__":
    asyncio.run(main())
