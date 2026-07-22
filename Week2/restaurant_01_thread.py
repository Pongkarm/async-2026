import threading
from time import sleep, ctime, time

# 1. ขั้นตอนต้อนรับหน้าร้าน ทำแบบ Synchronous เรียงทีละคน
def greet_diners(customer):
    print(f"{ctime()} Greeting for Customer-{customer} ...")
    sleep(1)
    print(f"{ctime()} Greeting for Customer-{customer} ...Done!")

# 2. กระบวนการส่วนตัวของลูกค้าแต่ละคน ที่จะถูกนำไปรันแยกในเธรดของตัวเอง
def customer_private_workflow(customer):
    # Take Order
    print(f"{ctime()}  [Thread-{customer}] Taking Order ...")
    sleep(1)
    print(f"{ctime()}  [Thread-{customer}] Taking Order ...Done!")

    # Do Cooking
    print(f"{ctime()}  [Thread-{customer}] Cooking Spaghetti ...")
    sleep(1)
    print(f"{ctime()}  [Thread-{customer}] Cooking Spaghetti ...Done!")

    # Manage Bar
    print(f"{ctime()}  [Thread-{customer}] Manage Bar for Drink ...")
    sleep(1)
    print(f"{ctime()}  [Thread-{customer}] Manage Bar for Drink ...Done!")
    print(f"{ctime()}  [Thread-{customer}] All served!\n")

if __name__ == "__main__":
    customers = ['A', 'B', 'C']
    start_time = time()

    # ----------------------------------------------------
    # PHASE 1: Greet diners sequentially
    # ----------------------------------------------------
    for customer in customers:
        greet_diners(customer)

    print(f"\n{ctime()} --- All customers greeted. Scheduling independent Threads! ---\n")

    # ----------------------------------------------------
    # PHASE 2: Spawn threads for concurrent phases
    # ----------------------------------------------------
    customer_threads = []
    for customer in customers:
        # สร้างเธรดแยกให้ลูกค้าแต่ละคน
        t = threading.Thread(target=customer_private_workflow, args=(customer,))
        customer_threads.append(t)
        t.start()

    # รอให้ลูกค้าทุกคนทำขั้นตอนทั้งหมดเสร็จสิ้น
    for t in customer_threads:
        t.join()

    duration = time() - start_time
    print(f"{ctime()} Finished Cooking in {duration:0.2f} seconds.")
