import asyncio
import websockets
import os

PORT = int(os.environ.get("PORT", 10000))
clientes = set()

async def handler(websocket, path):  
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
        print(f"Servidor WebSocket listo en puerto {PORT}")
        await asyncio.Future()  # corre para siempre

asyncio.run(main())


