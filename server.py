import asyncio
import websockets
import os

PORT = int(os.environ.get("PORT", 5000))
clientes = set()

async def handler(websocket):
    print("Jugador conectado")
    clientes.add(websocket)
    try:
        async for message in websocket:
            for c in clientes:
                if c != websocket:
                    await c.send(message)
    except:
        pass
    finally:
        clientes.remove(websocket)
        print("Jugador desconectado")

async def main():
    async with websockets.serve(handler, "0.0.0.0", PORT):
        print("Servidor WebSocket listo")
        await asyncio.Future()  # corre para siempre

asyncio.run(main())
