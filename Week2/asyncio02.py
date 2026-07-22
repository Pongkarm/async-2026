# Program 2: Coroutine Object
# Concept: Calling an async def function returns a coroutine object, it doesn't run the function yet.
import asyncio
import inspect
from time import ctime

async def serve_customer(name):
    print(f"{ctime()} -> Cooking for {name}...")
    await asyncio.sleep(1)
    print(f"{ctime()} -> Served {name}!")

if __name__ == "__main__":
    print(f"{ctime()} -> Calling serve_customer('A')...")
    coro = serve_customer("A")
    print(f"{ctime()} -> Coroutine object created: {coro}")
    print(f"{ctime()} -> Note that 'Cooking for A...' was not printed yet because it has not run.")
    
    print(f"{ctime()} -> type(coro): {type(coro)}")
    print(f"{ctime()} -> inspect.iscoroutine(coro): {inspect.iscoroutine(coro)}")
