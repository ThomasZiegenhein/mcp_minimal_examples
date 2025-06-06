import asyncio
from mcp.client.streamable_http import streamablehttp_client
from mcp import ClientSession
async def main():
    # Connect to a streamable HTTP server
    async with streamablehttp_client("http://127.0.0.1:8820/mcp") as (
        read_stream,
        write_stream,
        _,
    ):
        # Create a session using the client streams
        async with ClientSession(read_stream, write_stream) as session:
            # Initialize the connection
            await session.initialize()
            # Get all tools from the server
            resource_templates= await session.list_resource_templates()
            print(f"list_resource_templates() command: \n {resource_templates}")

            print('\n--- avail resource templates:')
            for res_template in resource_templates.resourceTemplates:
                print(res_template.uriTemplate)
                #print(f" - {res_template.uri_template}")

            print("\n+++ get resources")
            user = await session.read_resource("user://123")
            print(f'extracted user:   \n   {user} \n')
            product = await session.read_resource("product://123/True")
            print(f'extracted product:   \n   {product}')
            #print("Generated Prompt:", prompt)

if __name__ == "__main__":
    asyncio.run(main())
