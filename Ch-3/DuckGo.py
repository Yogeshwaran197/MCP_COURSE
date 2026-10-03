
import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient


async def main():
    client =  MultiServerMCPClient(
        {
            "ddg-search": {
                "transport":"stdio",
                "command": "uvx",
                "args": ["duckduckgo-mcp-server"]
            }
        }
    )

    tools =  await client.get_tools()
    
    
    for tool in tools:
        print(tool.name, "->", tool.args)
    

    tool_by_name = {tool.name: tool for tool in tools}

    search_tool =  tool_by_name['search']

    result = await search_tool.ainvoke(
                {            
                "query" : "what is MCP?"
                }
            )
        


    for block in result:
        if block["type"] == "text":
            print(block["text"])


if __name__ == "__main__":
    asyncio.run(main())

