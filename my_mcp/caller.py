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
            tools = await session.list_tools()
            print("-"*100)
            print("List all tools in our server: \n")
            print(tools)
            print("\n")
            print("+"*100)
            print("Call the echo tool with a message: \n")
            # Call a tool
            tool_result = await session.call_tool("echo", {"message": "Hello, I'm a mcp tool"})
            print(tool_result)
            print("\n")

if __name__ == "__main__":
    asyncio.run(main())