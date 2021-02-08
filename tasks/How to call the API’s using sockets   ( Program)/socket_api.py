import asyncio
import websockets

connected = set()


async def server(websocket, path):

    connected.add(websocket)
    try:
        async for message in websocket:
            for conn in connected:
                if conn != websocket:
                    await conn.send(f'Hi : {message}')
    finally:

        connected.remove(websocket)


start_server = websockets.serve(server, "localhost", 9999)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()