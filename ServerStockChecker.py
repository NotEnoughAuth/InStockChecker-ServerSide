import asyncio
import websockets
import threading
import time
import datetime
import CheckStock
import FileManager
from websockets import typing


async def newUrl(URL):
    data = FileManager.readProducts()
    inStockATM = CheckStock.checkinstock(URL)
    data.append([URL, inStockATM, inStockATM])
    FileManager.logProduct(data)

async def on_message():
    print()

async def handler(websocket):
    x = 0
    print(websocket.id)
    if await websocket.recv() == "ping":
        await websocket.send("pong")
    await websocket.send("Please enter urls that you want to check stock availability on (enter STOP to continue)")
    while True:
        while True:
            try:
                message = await websocket.recv()
                if message.upper() == 'STOP':
                    await websocket.send('Stoping URL Entering')
                    break
                print('Got the message: ' + message)
                await newUrl(message)
            except websockets.ConnectionClosedOK:
                print("### Connection Closed ###")
                break
        time.sleep(1)
        x += 1
        await websocket.send(str(x) + " seconds")


def checkStock():
    while True:
        prod = FileManager.readProducts()
        for i in range(0, prod.__len__()):
            prod[i][1] = prod[i][2]
            url = prod[i][0]
            prod[i][2] = (CheckStock.checkinstock(url))
            if prod[i][2] != prod[i][1]:
                FileManager.logProduct(prod)
            print(prod[i][2])
        time.sleep(30)


async def main():
    async with websockets.serve(handler, "", 44932):
        await asyncio.Future()  # Runs code forever


if __name__ == "__main__":
    constantStock = threading.Thread(target=checkStock)
    constantStock.start()
    asyncio.run(main())
    # temp = [['https://www.adafruit.com/product/5058', True, True], ['https://www.adafruit.com/product/909', True, True]]
    # FileManager.logProduct(temp)
    # secTemp = FileManager.readProducts()
    # url = secTemp[0][0]
    # print(CheckStock.checkinstock(url))
