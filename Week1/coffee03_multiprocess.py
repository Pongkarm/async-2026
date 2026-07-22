from time import sleep, ctime, time
import multiprocessing

# ฟังก์ชันจำลองการทำกาแฟให้ลูกค้า 1 คน 
def make_coffee(customer_name):
    print(f"{ctime()} [Process ID: {multiprocessing.current_process().pid}] กำลังชงกาแฟให้ ลูกค้า {customer_name}...")
    sleep(1) # จำลองเวลาชงกาแฟ 1 วินาที
    print(f"{ctime()} [Process ID: {multiprocessing.current_process().pid}] ลูกค้า {customer_name}: ได้รับกาแฟแล้ว!")

def main():
    # คิวลูกค้า
    queue = ['A', 'B', 'C']
    print(f"{ctime()} === เริ่มระบบจำลองตู้กาแฟแบบ Multi-processing ===")
    start_time = time()

    processes = [] # กระดานเก็บรายชื่อหน่วยประมวลผล (Processes)

    # 1. แตกกระบวนการทำงานแยกจากกันเป็นอิสระ (คนละตู้ คนละ CPU Core)
    for customer in queue:
        p = multiprocessing.Process(target=make_coffee, args=(customer,))
        processes.append(p)
        p.start() # สั่งเริ่มประมวลผลทันที

    # 2. รอจนกระทั่งทุก Process ทำงานเสร็จครบหมด
    for p in processes:
        p.join()

    # 3. แสดงผลลัพธ์ภาพรวม
    duration = time() - start_time
    print(f"{ctime()} สำเร็จ! ทุกตู้ทำงานแยกกันเสร็จสิ้น ใช้เวลารวมทั้งหมด: {duration:0.2f} วินาที")

# สิ่งสำคัญที่สุดสำหรับ Multi-processing ใน Python: ต้องครอบด้วยบล็อกนี้เสมอ
if __name__ == "__main__":
    main()
    