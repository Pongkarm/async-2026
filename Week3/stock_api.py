# mock_stock_api.py
# สคริปต์จำลองเว็บเซิร์ฟเวอร์ราคาหุ้นด้วย FastAPI สำหรับรองรับ Assignment 3
from fastapi import FastAPI
import asyncio

app = FastAPI(title="Asyncio Week 3 Mock Stock API")

@app.get("/price/{server_name}")
async def get_stock_price(server_name: str):
    """ API จำลองราคาหุ้น โดยแต่ละสาขาจะมีความหน่วง (Latency) ไม่เท่ากัน """
    name_lower = server_name.lower()
    
    # แยกความหน่วงเวลาจำลองตามชื่อสาขาที่ส่งเข้ามาดึงข้อมูล
    if name_lower == "alpha":
        await asyncio.sleep(3.0)  # ช้าที่สุด (หน่วงเวลา 3.0 วินาที)
        price = 152.50
    elif name_lower == "beta":
        await asyncio.sleep(0.8)  # เร็วที่สุด! (หน่วงเวลา 0.8 วินาที)
        price = 149.80
    elif name_lower == "gamma":
        await asyncio.sleep(1.5)  # ปานกลาง (หน่วงเวลา 1.5 วินาที)
        price = 150.20
    else:
        await asyncio.sleep(0.1)
        price = 100.00
        
    return {
        "server": server_name,
        "price_usd": price,
        "status": "success"
    }

# ไลบรารีที่จำเป็น: pip install fastapi uvicorn httpx
# คำสั่งใช้รันเซิร์ฟเวอร์: uvicorn stock_api:app --reload --port 8088