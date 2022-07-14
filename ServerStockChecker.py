import asyncio
import websockets


async def handler(websocket):
    while True:
        try:
            message = await websocket.recv()
        except websockets.ConnectionClosedOK:
            print("###Connection Closed###")
            break
        print(message)


async def main():
    async with websockets.serve(handler, "", 8000):
        await asyncio.Future() #Runs code forever


if __name__ == "__main__":
    asyncio.run(main())
