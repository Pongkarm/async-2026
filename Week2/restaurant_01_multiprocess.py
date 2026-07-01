# Assignment Week2: Restaurant Multi-Process Workflow
# Concept: Sequential greeting followed by concurrent processes for customer ordering/cooking/drinks.
import multiprocessing
from time import sleep, ctime, time

# 1. ขั้นตอนต้อนรับหน้าร้าน ทำแบบ Synchronous เรียงทีละคน
def greet_diners(customer):
    print(f"{ctime()} Greeting for Customer-{customer} ...")
    sleep(1)
    print(f"{ctime()} Greeting for Customer-{customer} ...Done!")

# 2. กระบวนการส่วนตัวของลูกค้าแต่ละคน ที่จะถูกนำไปรันแยกในโปรเซสของตัวเอง
def customer_private_workflow(customer):
    pid = multiprocessing.current_process().pid
    # Take Order
    print(f"{ctime()}  [Process-{customer} (PID: {pid})] Taking Order ...")
    sleep(1)
    print(f"{ctime()}  [Process-{customer} (PID: {pid})] Taking Order ...Done!")

    # Do Cooking
    print(f"{ctime()}  [Process-{customer} (PID: {pid})] Cooking Spaghetti ...")
    sleep(1)
    print(f"{ctime()}  [Process-{customer} (PID: {pid})] Cooking Spaghetti ...Done!")

    # Manage Bar
    print(f"{ctime()}  [Process-{customer} (PID: {pid})] Manage Bar for Drink ...")
    sleep(1)
    print(f"{ctime()}  [Process-{customer} (PID: {pid})] Manage Bar for Drink ...Done!")
    print(f"{ctime()}  [Process-{customer} (PID: {pid})] All served!\n")

def main():
    start_time = time()
    customers = ['A', 'B', 'C']

    # ----------------------------------------------------
    # PHASE 1: Greet diners sequentially
    # ----------------------------------------------------
    for customer in customers:
        greet_diners(customer)

    print(f"\n{ctime()} --- All customers greeted. Scheduling independent Processes! ---\n")

    # ----------------------------------------------------
    # PHASE 2: Spawn processes for concurrent phases
    # ----------------------------------------------------
    processes = []
    for customer in customers:
        p = multiprocessing.Process(target=customer_private_workflow, args=(customer,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    duration = time() - start_time
    print(f"{ctime()} Finished Cooking in {duration:0.2f} seconds.")

if __name__ == "__main__":
    main()
