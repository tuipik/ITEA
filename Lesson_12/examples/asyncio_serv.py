import asyncio


async def echo_handler(reader, writer):
  # data = sock.recv(100) # !!! blocking
  data = await reader.read(100)
  # sock.sendall(data)
  writer.write(data)
  await writer.drain()
  writer.close()
  
async def echo_server():
  # socket.bind(host, port)
  # socket.listen()
  server = await asyncio.start_server(
      echo_handler, '127.0.0.1', 5555)
  async with server:
    # while True:
    #   sock.accept()
    await server.serve_forever()

asyncio.run(echo_server())
