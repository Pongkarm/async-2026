# Objective: Group multiple operations to run concurrently and return an ordered list of outputs.
# วัตถุประสงค์: รวมกลุ่มการทำงานหลายงานให้ทำงานควบคู่กัน (Concurrently) และส่งค่ากลับมาเป็นรายการผลลัพธ์ที่เรียงลำดับตามตัวแปรอินพุตตั้งต้น
import asyncio
from time import time, ctime

async def fetch_db_record(table_name, latency):
    await asyncio.sleep(latency)
    return f"RowData_{table_name}"

async def main():
    start = time()
    
    # รัน Coroutines ย่อยทั้งหมดแบบคู่ขนานพร้อมกัน และรอจนกว่าทุกตัวจะรันเสร็จเรียบร้อย
    # ผลลัพธ์ที่ได้จะจัดเก็บเรียงลำดับตามอินพุตที่ป้อนเข้าไปเสมอ (Users -> Products -> Invoices)
    results = await asyncio.gather(
        fetch_db_record("Users", 1.0),
        fetch_db_record("Products", 0.5),
        fetch_db_record("Invoices", 1.0)
    )
    
    print(f"{ctime()} Aggregated Output Results List: {results}")
    # แสดงระยะเวลาประมวลผลรวม (ควรจะใช้เวลาประมาณ 1.0 วินาทีตามตัวช้าที่สุด ไม่ใช่ 1.0 + 0.5 + 1.0 = 2.5 วินาที)
    print(f"{ctime()} Execution Completed in: {time() - start:.2f} seconds") 

asyncio.run(main())