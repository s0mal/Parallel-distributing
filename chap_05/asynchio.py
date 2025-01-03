import asyncio

async def first_coroutine(future, num):
    count = sum(range(1, num + 1))
    await asyncio.sleep(1)
    future.set_result(f"Sum of first {num} integers: {count}")

async def second_coroutine(future, num):
    result = 1
    for i in range(2, num + 1):
        result *= i
    await asyncio.sleep(2)
    future.set_result(f"Factorial of {num}: {result}")

def got_result(future):
    print(future.result())

async def main():
    # Create Futures
    future1 = asyncio.Future()
    future2 = asyncio.Future()

    # Add done callbacks
    future1.add_done_callback(got_result)
    future2.add_done_callback(got_result)

    # Create tasks
    tasks = [
        asyncio.create_task(first_coroutine(future1, 5)),
        asyncio.create_task(second_coroutine(future2, 5))
    ]

    # Wait for all tasks to complete
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    # Run the main function within the event loop
    asyncio.run(main())
