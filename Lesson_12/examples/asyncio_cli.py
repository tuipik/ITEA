import asyncio

async def echo_cli():
  # socket.connect(host, port)
  reader, writer = await asyncio.open_connection(
      '127.0.0.1', 5555)
  # sock.send(..)
  writer.write(b'Hello asyncio')
  # sock.recv()
  data = await reader.read(100)
  print(data.decode())

# loop = asyncio.new_event_loop()
# loop.run_until_complete(coro)
asyncio.run(echo_cli())
