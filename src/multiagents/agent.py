from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm


AGENT_MODEL = "ollama_chat/llama3.1"

def get_weather(city: str) -> dict:
    """Retrieve weather data for a given city

    Args:
        city (str): The name of the city to check.
    Returns:
        dict: return a status (SUCCESS or FAILURE) and a message (weather data for city)

    """
    rtn = {"status": "SUCCESS", "message": f"Weather data for {city} is sunny and the temperature is 72 degrees."}

    return rtn

root_agent = Agent(name="travel_planner_agent",
                   model=LiteLlm(AGENT_MODEL),
                   description="Travel Planner Agent",
                   instruction=(
                       "You are a helpful travel planner. "
                       "1. If the user asks about weather, call the 'get_weather' tool. "
                       "2. If the user asks about anything else (trips, general questions, or chat), "
                       "   respond directly with text and DO NOT call any tools. "
                       "3. If you don't have a tool for a request, just answer to the best of your ability."
                   ),
                   tools=[get_weather])
