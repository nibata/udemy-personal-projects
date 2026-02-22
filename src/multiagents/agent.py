from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm


#AGENT_MODEL = "ollama_chat/mistral"
AGENT_MODEL = "ollama_chat/llama3.2"

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
                       "You are a trip travel planner. Help users find trips and check weather. "
                       "When the user asks about weather, you MUST call the 'get_weather' tool with the city name. "
                       "ONLY use tools that are explicitly listed. NEVER call tools that are not provided to you. "
                       "Available tools: get_weather."
                   ),
                   tools=[get_weather])
