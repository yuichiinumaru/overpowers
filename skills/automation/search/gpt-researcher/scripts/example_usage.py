# Auto-generated example usage from SKILL.md

# from gpt_researcher import GPTResearcher
# import asyncio
#
# async def main():
#     researcher = GPTResearcher(
#         query="What are the latest AI developments?",
#         report_type="research_report",  # or detailed_report, deep, outline_report
#         report_source="web",            # or local, hybrid
#     )
#     await researcher.conduct_research()
#     report = await researcher.write_report()
#     print(report)
#
# asyncio.run(main())

# # 1. Create: gpt_researcher/retrievers/my_retriever/my_retriever.py
# class MyRetriever:
#     def __init__(self, query: str, headers: dict = None):
#         self.query = query
#
#     async def search(self, max_results: int = 10) -> list[dict]:
#         # Return: [{"title": str, "href": str, "body": str}]
#         pass
#
# # 2. Register in gpt_researcher/actions/retriever.py
# case "my_retriever":
#     from gpt_researcher.retrievers.my_retriever import MyRetriever
#     return MyRetriever
#
# # 3. Export in gpt_researcher/retrievers/__init__.py

# # In default.py: "SMART_LLM": "gpt-4o"
# # Access as: self.cfg.smart_llm  # lowercase!

# class WebSocketHandler:
#     async def send_json(self, data):
#         print(f"[{data['type']}] {data.get('output', '')}")
#
# researcher = GPTResearcher(query="...", websocket=WebSocketHandler())

# researcher = GPTResearcher(
#     query="Open source AI projects",
#     mcp_configs=[{
#         "name": "github",
#         "command": "npx",
#         "args": ["-y", "@modelcontextprotocol/server-github"],
#         "env": {"GITHUB_TOKEN": os.getenv("GITHUB_TOKEN")}
#     }],
#     mcp_strategy="deep",  # or "fast", "disabled"
# )

# researcher = GPTResearcher(
#     query="Comprehensive analysis of quantum computing",
#     report_type="deep",  # Triggers recursive tree-like exploration
# )

# async def execute(self, ...):
#     if not self.is_enabled():
#         return []  # Don't crash
#
#     try:
#         result = await self.provider.execute(...)
#         return result
#     except Exception as e:
#         await stream_output("logs", "error", f"⚠️ {e}", self.websocket)
#         return []  # Graceful degradation
