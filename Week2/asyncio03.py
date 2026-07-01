# Program 3: The Event Loop (asyncio.run)
# Concept: Using the Event Loop to actually execute a Coroutine Object.
import asyncio

async def greet():
    print("Hello from thr Event Loop!")

if __name__ == "__main__":
    coro_object = greet()

    asyncio.run(coro_object)
