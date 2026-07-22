# Program 1: The First Coroutine Function
# Concept: Understanding async def and how it differs from a normal function.
import inspect
from time import ctime

def cook_spaghetti(customer):
    return f"Spaghetti for {customer}"

async def serve_customer(customer):
    return f"Served customer {customer}"

if __name__ == "__main__":
    print(f"{ctime()} -> type(cook_spaghetti): {type(cook_spaghetti)}")
    print(f"{ctime()} -> type(serve_customer): {type(serve_customer)}")
    
    print(f"{ctime()} -> inspect.iscoroutinefunction(cook_spaghetti): {inspect.iscoroutinefunction(cook_spaghetti)}")
    print(f"{ctime()} -> inspect.iscoroutinefunction(serve_customer): {inspect.iscoroutinefunction(serve_customer)}")
