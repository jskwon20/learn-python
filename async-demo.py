# 동기 방식
import time

def fetch_data():
    time.sleep(3)  # 3초 동안 CPU 점유하며 멈춤
    return "data"

def main():
    print("시작")
    result = fetch_data()  # 여기서 3초 동안 멈춤 (다른 일 못 함)
    print(result)
    print("끝")

print(main())



# 비동기 방식
import asyncio

async def fetch_data():
    await asyncio.sleep(3)  # 3초 기다리되 CPU 점유 안 함
    return "data"

async def main():
    print("시작")
    result = await fetch_data()  # 여기서 대기 중 다른 작업 가능
    print(result)
    print("끝")

asyncio.run(main())
