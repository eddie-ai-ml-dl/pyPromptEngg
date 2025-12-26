# gemini_agent_run.py
import asyncio
from agents import Agent, Runner

Runner.trace_export_enabled = False

async def main():
    # Create Gemini agent
    gemini_agent = Agent(
        name="Gemini Agent",
        instructions="""
        You are a helpful assistant powered by Gemini.
        Be concise, factual, and clear in your responses.
        """,
        model="litellm/gemini/gemini-2.5-flash"
    )

    # Run the agent asynchronously
    result = await Runner.run(gemini_agent, "Explain agentic AI in simple terms.")
    print("=== Gemini Agent Output ===")
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
