from time import sleep, ctime, time

# Greeting synchronous
def greet_diners(customer):
    print(f"{ctime()} Greeting for Customer-{customer} ...")
    sleep(1)
    print(f"{ctime()} Greeting for Customer-{customer} ...Done!")

# Take Order
def take_orders(customer):
    print(f"{ctime()} Taking Order for Customer-{customer} ...")
    sleep(1)
    print(f"{ctime()} Taking Order for Customer-{customer} ...Done!")

# Do Cooking
def do_cooking(customer):
    print(f"{ctime()} Cooking for Customer-{customer} ...")
    sleep(1)
    print(f"{ctime()} Cooking for Customer-{customer} ...Done!")

# Do Cooking
def mini_bar(customer):
    print(f"{ctime()} Mini Bar for Customer-{customer} ...")
    sleep(1)
    print(f"{ctime()} Mini Bar for Customer-{customer} ...Done!")

if __name__ == "__main__":
    # Begin of main thread
    customers = ['A', 'B', 'C']

    start_time = time()
    # Cooking for each customer
    for customer in customers:
        greet_diners(customer)
        take_orders(customer)
        do_cooking(customer)
        mini_bar(customer)

    duration = time() - start_time
    print(f"{ctime()} Finished Cooking in {duration:0.2f} seconds.")
