from time import sleep, ctime, time
import threading

# ฟังก์ชันจำลองการทำกาแฟให้ลูกค้า 1 คน
def make_coffee(customer_name):
    print(f"{ctime()} กำลังชงกาแฟให้ ลูกค้า {customer_name}...")
    sleep(1) # จำลองเวลาชงกาแฟ 1 วินาที (แทน 1 นาที)
    print(f"{ctime()} ลูกค้า {customer_name}: ได้รับกาแฟแล้ว!")

def main():
    # คิวลูกค้า
    queue = ['A', 'B', 'C']
    print(f"{ctime()} === เริ่มระบบจำลองตู้กาแฟแบบ Multi-threading ===")
    start_time = time()

    # รายชื่อที่จะเอาไว้เก็บ Thread ของแต่ละคน
    threads = []

    # สร้าง "(Thread)" แยกให้ลูกค้าแต่ละคนทำงานพร้อมกัน
    for customer in queue:
        # สร้าง Thread ใหม่ โดยระบุให้ไปวิ่งที่ฟังก์ชัน make_coffee และส่งชื่อลูกค้าไปเป็น argument
        t = threading.Thread(target=make_coffee, args=(customer,))
        threads.append(t)
        t.start() # สั่งให้ Thread เริ่มทำงานทันที (ไม่ต้องรอให้รอบลูปถัดไปเสร็จ)

    # รอให้ "ช่างทุกคน" ชงกาแฟเสร็จครบหมดก่อน ถึงจะไปสเต็ปถัดไป
    for t in threads:
        t.join()

    duration = time() - start_time # คำนวณเวลาที่ใช้จริง
    print(f"{ctime()} ลูกค้า {len(queue)} คน ได้รับกาแฟครบแล้ว! ใช้เวลารวมทั้งหมด: {duration:0.2f} วินาที")

# สั่งให้โปรแกรมทำงาน
if __name__ == "__main__":
    main()