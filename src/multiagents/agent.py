from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm


AGENT_MODEL = "ollama/gemma3"

root_agent = Agent(name="travel_planner_agent",
                   model=LiteLlm(AGENT_MODEL),
                   description="Travel Planner Agent",
                   instruction="You are a trip travel planner. Help to find sales for trips.")
