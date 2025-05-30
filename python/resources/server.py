from fastmcp import FastMCP

mcp = FastMCP("Resource Server")

def _user_producer(user_id):
    return {"user_id": user_id, "name": "John Doe", "status": "active"}

def _product_producer(product_id, details):
    product = {"product_id": product_id,
                "name": "Doe Product",
                "status": "avail"}
    if details:
        product["location"] = "unknown"
        return product
    return product

@mcp.resource("user://{user_id}")
def get_user_data(user_id: str) -> dict:
    """Returns a mock user record."""
    return _user_producer(user_id=user_id)

@mcp.resource("product://{product_id}/{detail_level}")
def get_user_data(product_id: str,  detail_level: bool) -> dict:
    """Returns a mock user record."""
    return _product_producer(product_id=product_id, details=detail_level)

if __name__ == "__main__":
    mcp.run(transport="streamable-http", host="0.0.0.0", port=8020, path="/mcp")