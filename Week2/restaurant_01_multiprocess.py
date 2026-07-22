import multiprocessing
from time import sleep, ctime, time

# 1. ขั้นตอนต้อนรับหน้าร้าน ทำแบบ Synchronous เรียงทีละคน
def greet_diners(customer):
    print(f"{ctime()} Greeting for Customer-{customer} ...")
    sleep(1)
    print(f"{ctime()} Greeting for Customer-{customer} ...Done!")

# 2. กระบวนการย่อยของลูกค้าแต่ละคน ที่รอบนี้จะถูกนำไปรันแยกในโปรเซสของตัวเอง
def customer_private_workflow(customer):
    # ในแต่ละ Process จะทำงาน 3 Tasks นี้
    pid = multiprocessing.current_process().pid
    print(f"{ctime()}  [Process-{customer} (PID: {pid})] Taking Order ...")
    sleep(1)
    print(f"{ctime()}  [Process-{customer} (PID: {pid})] Taking Order ...Done!")

    print(f"{ctime()}  [Process-{customer} (PID: {pid})] Cooking Spaghetti ...")
    sleep(1)
    print(f"{ctime()}  [Process-{customer} (PID: {pid})] Cooking Spaghetti ...Done!")

    print(f"{ctime()}  [Process-{customer} (PID: {pid})] Manage Bar for Drink ...")
    sleep(1)
    print(f"{ctime()}  [Process-{customer} (PID: {pid})] Manage Bar for Drink ...Done!")
    print(f"{ctime()}  [Process-{customer} (PID: {pid})] All served!\n")

if __name__ == "__main__":
    customers = ['A', 'B', 'C']
    start_time = time()

    # ----------------------------------------------------
    # PHASE 1: Greet ลูกค้าทีละคนแบบ Synchronous ใน Main Process
    # ----------------------------------------------------
    for customer in customers:
        greet_diners(customer)

    print(f"\n{ctime()} --- All customers greeted. FORKING into independent Processes (Branch)! ---\n")

    # ----------------------------------------------------
    # PHASE 2: แตกโปรเซส (เปิดสาขาใหม่แยกขาดจากกันตามคอร์ซีพียู)
    # ----------------------------------------------------
    processes = []
    for customer in customers:
        # เปลี่ยนจาก threading.Thread เป็น multiprocessing.Process
        p = multiprocessing.Process(target=customer_private_workflow, args=(customer,))
        processes.append(p)
        p.start() # OS จะทำการโคลนทุกอย่างแล้วเตะไปรันบน CPU คอร์อื่น ๆ ขนานกันทันที

    # รอให้ทุกโปรเซส (ทุกสาขา) ทำงานของตัวเองเสร็จสิ้นทั้งหมด
    for p in processes:
        p.join()

    duration = time() - start_time
    print(f"{ctime()} Finished Entire Restaurant Operation in {duration:0.2f} seconds.")
