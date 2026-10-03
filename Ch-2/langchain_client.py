import asyncio
import os
from langchain_mcp_adapters.client import MultiServerMCPClient
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]  

SERVER_PATH = ROOT / "Ch-1" / "first_MCPServer_stdio.py"
command = str(ROOT / ".venv" / "Scripts" / "python.exe") 

async def main():
    Client =  MultiServerMCPClient(
        {
        "My_local_server" : {
           "transport" : "stdio",
           "command":command,
           "args" : [str(SERVER_PATH)]
        },
        "http_server": {
            "url": "http://127.0.0.1:8100/mcp",
            "transport": "streamable_http",
        }
    }
    )

    tools = await Client.get_tools()
    for tool in tools:
        name = tool.name
        description = tool.description

        print(f"Tool name : {name}")
        print(f"Description : {description}")


if __name__ == "__main__":
    asyncio.run(main())