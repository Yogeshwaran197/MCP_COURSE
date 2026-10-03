import os
import asyncio
from pathlib import Path
from langchain_mcp_adapters.client import MultiServerMCPClient



SERVER_PATH = Path(__file__).parent / "first_MCPServer_stdio.py"

venv_path = Path(__file__).resolve().parents[1] / ".venv"
command = os.path.join(venv_path, "Scripts" , "python.exe")


async def main():
    Client = MultiServerMCPClient(
        {
            "Custom_tools" : {
                "transport" : "stdio",
                "command" : command,
                "args" : [str(SERVER_PATH)]
            }
        }
    )

    tools = await Client.get_tools()

    for tool in tools:
        print("Tool Name:", tool.name)
        print("Description:", tool.description)
        print()

    
if __name__ == "__main__":
    asyncio.run(main())


