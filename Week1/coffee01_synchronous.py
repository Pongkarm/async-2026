from time import sleep, ctime, time

# ฟังก์ชันจำลองการทำกาแฟให้ลูกค้า 1 คน
def make_coffee(customer_name):
    print(f"{ctime()} กำลังชงกาแฟให้ ลูกค้า {customer_name}...")
    sleep(1) # จำลองเวลาชงกาแฟ 1 วินาที (แทน 1 นาที)
    print(f"{ctime()} ลูกค้า {customer_name}: ได้รับกาแฟแล้ว!")

def main():
    # คิวลูกค้า
    queue = ['A', 'B', 'C']
    print(f"{ctime()} === เริ่มระบบจำลองตู้กาแฟ Synchronous ===")
    start_time = time()

    # ลูปทำงานตามลำดับ Synchronous
    for customer in queue:
        # กระบวนการชงกาแฟแต่ละลูกค้า
        make_coffee(customer)

    duration = time() - start_time # คำนวณเวลาที่ใช้
    print(f"{ctime()} ลูกค้า {len(queue)} คน ใช้เวลา: {duration:0.2f} วินาที")

# สั่งให้โปรแกรมทำงาน
if __name__ == "__main__":
    main()
    