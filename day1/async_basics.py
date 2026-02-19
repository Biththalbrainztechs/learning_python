import time
import asyncio


async def fetch_data(name,delay):
    """simulates fetching data from api"""
    print(f"[{name}] Starting to fetch data.....")
    await asyncio.sleep(delay)     #simulating network delay
    print(f"[{name}] data received.....")
    return f"data from {name}"

async def main():
    print("==Sequential Execution ===")
    start =time.time()
    result1 = await fetch_data("API-1",2)
    result2 = await fetch_data("API-2",3)
    result3= await fetch_data("API-3",1)

    print(f"Results:{result1},{result2},{result3}")
    print(f"Time Taken:{time.time()-start:.2f}s\n")


    print("===Concurrent Execution ===")
    start = time.time()
    results = await asyncio.gather(
        fetch_data("API-1",2),
        fetch_data("API-2",3),
        fetch_data("API-1",1)
    )
    print(f"Results:{results}")
    print(f"Time taken:{time.time()-start:.2f}s")

if __name__=="__main__":
    asyncio.run(main())

   