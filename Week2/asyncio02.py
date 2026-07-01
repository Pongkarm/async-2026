# Program 2: The Coroutine Object
# Concept: Seeing that calling an async def function creates an "Object" but does not execute it yet.
import asyncio

async def greet():
    print("Hello")

coro_object = greet()

print(type(coro_object))

coro_object.close()
