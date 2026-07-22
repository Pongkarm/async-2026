# Program 8: Interleaving Tasks (Context Switching)
# Concept: Demonstrating how single-threaded event loop switches execution context between tasks.
import asyncio
from time import ctime

async def kitchen_crew():
    print(f"{ctime()} -> [Chef] puts noodle in boiling water...")
    await asyncio.sleep(1)
    print(f"{ctime()} -> [Chef] strains the noodle!")

async def bar_crew():
    print(f"{ctime()} -> [Bar] starts grinding coffee bean...")
    await asyncio.sleep(1)
    print(f"{ctime()} -> [Bar] pours espresso shot!")

async def main():
    task_kitchen = asyncio.create_task(kitchen_crew())
    task_bar = asyncio.create_task(bar_crew())
    
    await task_kitchen
    await task_bar

if __name__ == "__main__":
    asyncio.run(main())
