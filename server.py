import asyncio
import websockets
import os

PORT = int(os.environ.get("PORT", 10000))
clientes = []   # asignar roles según orden

async def handler(websocket, path):   
    print("Jugador conectado")

    # Asigna el rol automáticamente según orden de conexión
    if len(clientes) == 0:
        await websocket.send("jugador=0")   # primer → X
    else:
        await websocket.send("jugador=1")   # segundo → O

    clientes.append(websocket)
    try:
        async for message in websocket:
            # reenviar jugada a todos los demás
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



