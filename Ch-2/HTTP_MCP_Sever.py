from fastmcp import FastMCP


mcp =  FastMCP()

@mcp.tool()
def fetch():
    """Use this tool to fetch the data"""

    return {"date" : "Hello, World!"}

@mcp.tool()
def process():
    """Use this tool to process the data"""\

    return {"processed data" : "I am yogeshwaran from tiruchirrappalli"}


if __name__ =="__main__":
    mcp.run(transport="streamable-http", host="0.0.0.0" , port=8100)
