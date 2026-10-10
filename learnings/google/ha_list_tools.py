"""List the tools your Home Assistant MCP server offers. No AI model is called.

Uses the same environment variables as the agent:
    HA_MCP_URL, HA_TOKEN
Requires: pip install "mcp>=1.28,<2"
"""
import asyncio
import os

from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client

HA_MCP_URL = os.environ["HA_MCP_URL"]
HA_TOKEN = os.environ["HA_TOKEN"]


async def main() -> None:
    headers = {"Authorization": f"Bearer {HA_TOKEN}"}
    async with streamablehttp_client(HA_MCP_URL, headers=headers) as (read, write, _):
        async with ClientSession(read, write) as session:
            init = await session.initialize()
            print("Server:", init.serverInfo.name, init.serverInfo.version)

            tools = (await session.list_tools()).tools
            print(f"\n{len(tools)} tools:")
            for t in tools:
                desc = (t.description or "").strip().replace("\n", " ")
                print(f"  - {t.name}: {desc[:90]}")

            try:
                resources = (await session.list_resources()).resources
                print(f"\n{len(resources)} resources:")
                for r in resources:
                    print(f"  - {r.uri}")
            except Exception as e:  # not all servers support resources
                print("\n(resources not listed:", type(e).__name__, ")")


if __name__ == "__main__":
    asyncio.run(main())