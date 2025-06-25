from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
import sqlite3

# Load env vars
load_dotenv()

# Initialize FastMCP server
mcp = FastMCP("um-mcp")

# Test tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

if __name__ == "__main__":
    # Initialize and run the server
    print("UM MCP server has started.")
    mcp.run(transport='stdio')