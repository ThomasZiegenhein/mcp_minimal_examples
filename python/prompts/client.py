import asyncio
from mcp.client.streamable_http import streamablehttp_client
from mcp import ClientSession
async def main():
    # Connect to a streamable HTTP server
    async with streamablehttp_client("http://127.0.0.1:8810/mcp") as (
        read_stream,
        write_stream,
        _,
    ):
        # Create a session using the client streams
        async with ClientSession(read_stream, write_stream) as session:
            # Initialize the connection
            await session.initialize()
            # Get all tools from the server
            prompts= await session.list_prompts()
            print(f"list_prompts() command: \n {prompts}")
            session.get_prompt

            prompt = await session.get_prompt("planet_prompt", {"planet_name": "Sun"})
            print("Generated Prompt:", prompt)

if __name__ == "__main__":
    asyncio.run(main())
