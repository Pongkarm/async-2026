from time import sleep, ctime, time
import threading

def update_cup_number(customer_name):
    print(f"{ctime()} | LCD: Processing for customer {customer_name}...")
    sleep(1.0)
    print(f"{ctime()} | LCD: Done for customer {customer_name}.")

def make_coffee(customer_name):
    print(f"{ctime()} | Making coffee for {customer_name}...")
    sleep(1.0)
    print(f"{ctime()} | Coffee ready for {customer_name}!")

def customer_task(customer_name):
    make_coffee(customer_name)
    update_cup_number(customer_name)

def main():
    queue = ['A', 'B', 'C']
    print(f"{ctime()} | === Multi-threading Coffee Machine ===")
    start_time = time()
    
    threads = []
    for customer in queue:
        t = threading.Thread(target=customer_task, args=(customer,))
        threads.append(t)
        t.start()
        
    for t in threads:
        t.join()
        
    duration = time() - start_time
    print(f"{ctime()} | Total time: {duration:.2f} seconds")

if __name__ == "__main__":
    main()