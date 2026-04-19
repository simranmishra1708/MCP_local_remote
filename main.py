import random
from fastmcp import FastMCP
 
#create a FastMCP instance
mcp = FastMCP(name="demo-mcp") 

@mcp.tool
def roll_dice_tool(n_dice: int = 1) -> list[int]:
    """Roll a specified number of dice and return the results."""
    return [random.randint(1, 6) for _ in range(n_dice)]

@mcp.tool
def add_numbers_tool(a: int, b: int) -> int:
    """Add two numbers and return the result."""
    return a + b

if __name__ == "__main__":
    mcp.run()   