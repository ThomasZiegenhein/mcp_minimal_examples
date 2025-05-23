import asyncio
from mcp.client.streamable_http import streamablehttp_client
from mcp import ClientSession

async def main():
    # Connect to a streamable HTTP server
    async with streamablehttp_client("http://127.0.0.1:8800/mcp") as (
        read_stream,
        write_stream,
        _,
    ):
        # Create a session using the client streams
        async with ClientSession(read_stream, write_stream) as session:
            # Initialize the connection
            await session.initialize()
            # Get all tools from the server
            tools = await session.list_tools()
            print(f"list_tools() command: \n {tools}")
            # Call a tool
            tool_result = await session.call_tool("echo", {"text": "Hello World"})
            print(f"call_tool for echo: \n {tool_result}")

if __name__ == "__main__":
    asyncio.run(main())