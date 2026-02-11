import asyncio

async def make_coffee():
    print("Starting to make coffee ......")
    await asyncio.sleep(3)
    print("Coffee is readyy!!")
    return "="

async def make_toast():
    print("Starting to make toastt")
    await asyncio.sleep(2)
    print("Toast is readyyy")
    return "🍞"

async def make_breakfast():
    #run both at the same time 
    coffee ,toast = await asyncio.gather(
        make_coffee(),
        make_toast()
    )
    print(f"Breakfast:{coffee}{toast}")

asyncio.run(make_breakfast())

#this take total of 3 seconds