
import asyncio
import os
from langchain_mcp_adapters.client import MultiServerMCPClient
from dotenv import load_dotenv

load_dotenv()


TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

async def main():

    client = MultiServerMCPClient(
        {
            "mcpServers": {
                "transport": "http",
                "url": f"https://mcp.tavily.com/mcp/?tavilyApiKey={TAVILY_API_KEY}"
        }
  }
)

    tools = await client.get_tools()
    
    for tool in tools:
        print(tool.name, "->", tool.args)
    
    tool_map = {tool.name : tool for tool in tools}

    select_by_tool =  tool_map["tavily_search"]

    result =  await select_by_tool.ainvoke({
        "query" : "what is mcp?"
    })

    for block in result:
        if block["type"] == "text":
            print(block["text"]) 


if __name__ == "__main__":
    asyncio.run(main())