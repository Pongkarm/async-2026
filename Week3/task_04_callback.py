# Objective: Attach a plain synchronous function that automatically triggers the moment a task finishes.
# วัตถุประสงค์: แนบฟังก์ชันซิงโครนัสธรรมดา (Callback) ให้ทำงานอัตโนมัติทันทีที่ Task นั้นๆ รันเสร็จสิ้น
import asyncio
from time import ctime

def alert_manager(finished_task):
    # ฟังก์ชันนี้จะถูกเรียกใช้งานเมื่อ Task ประมวลผลเสร็จสิ้น โดยจะส่งตัวแปร Task เข้ามาเป็นอาร์กิวเมนต์ตัวแรก
    # เราสามารถดึงค่าผลลัพธ์ผ่านการเรียกใช้ .result() ได้โดยตรงจากในนี้
    print(f"{ctime()} Callback Triggered! Task output fetched: {finished_task.result()}")

async def download_file():
    print(f"{ctime()} Downloading packet...")
    await asyncio.sleep(1.0)
    return "Data_Payload.zip"

async def main():
    task = asyncio.create_task(download_file())
    # ลงทะเบียนฟังก์ชัน Callback เพื่อสแตนด์บายทำงานทันทีที่ Task ทำงานเสร็จ
    task.add_done_callback(alert_manager)
    
    await task # รันและรอคอยให้ Task ทำงานเสร็จเพื่อให้ผลลัพธ์แสดงและสังเกตพฤติกรรมของ Callback

asyncio.run(main())