from fastmcp import FastMCP

mcp = FastMCP("Echo Server")

@mcp.tool()
def echo(text: str) -> str:
    """Echoes the input text."""
    return text

if __name__ == "__main__":
    mcp.run(transport="streamable-http", host="0.0.0.0", port=8800, path="/mcp") # 127.0.0.1 will fail when dockerized! 127.0.0.1 is private to the container and will not work via portforwarding!
