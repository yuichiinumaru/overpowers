import sys
import asyncio

async def run_simple_research(query, report_type="research_report", report_source="web"):
    """
    Run a basic research using GPTResearcher.
    """
    from gpt_researcher import GPTResearcher
    researcher = GPTResearcher(
        query=query,
        report_type=report_type,
        report_source=report_source,
    )
    await researcher.conduct_research()
    report = await researcher.write_report()
    return report

if __name__ == "__main__":
    if len(sys.argv) > 1:
        query = " ".join(sys.argv[1:])
        print(f"Starting research on: {query}")
        result = asyncio.run(run_simple_research(query))
        print(result)
    else:
        print("Usage: python gpt_researcher_helper.py <research_query>")
