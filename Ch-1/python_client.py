from pathlib import Path
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client



import os
import asyncio


SERVER_PATH = Path(__file__).parent / "first_MCPServer_stdio.py"
print(SERVER_PATH)

server_parameters = StdioServerParameters(
    command="python",
    args = [str(SERVER_PATH)],
)
    
    

async def main():
    async with stdio_client(server_parameters) as (read,write):
        async with ClientSession(read,write) as session:

            await session.initialize()

            tools = await session.list_tools()
            print("Awailable Tools :", tools) 

            result = await session.call_tool("process", arguments={"path": "/path/to/data"})
            print("Result :" ,result)



if __name__ == "__main__":
    asyncio.run(main())
