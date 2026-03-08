from google.adk.agents import Agent, SequentialAgent
from google.adk.models.lite_llm import LiteLlm

from duckduckgo_search import DDGS


AGENT_MODEL = "ollama_chat/qwen2.5"

def search_web(query: str):
    """
    Searches the live web for current information, news, or facts.
    Use this when the user asks about recent events.
    """
    with DDGS() as ddgs:
        # Get the top 3 results for a clean response
        results = [r for r in ddgs.text(query, max_results=3)]
        return results

web_search_tool = search_web


destination_agent = Agent(
    name="destination_agent",
    model=LiteLlm(AGENT_MODEL),
    tools=[web_search_tool],
    description="Agent to find the best destination for a trip",
    instruction="""
    You are a traveler researcher. You will be given a destination and respond with:
    - A list of recommended destinations
    - Top attractions in the destination
    - culture and food
    - transportation options
    - safety tips and best practices
    Provide a comprehensive destination insights for trip planning.
    """,
    output_key="best_destinations"
)

itinerary_agent = Agent(
    name="itinerary_agent",
    model=LiteLlm(AGENT_MODEL),
    description="Agent to create an structured itinerary for a trip",
    instruction="""
    You are a travel planner that will uses the research from "best_destinations" output to create a structured itinerary for a trip.
    You will be given a list of activities and respond with:
    - A day by day activities plan
    - accommodation suggestion
    - transportation options
    - estimated time in activities
    - estimated cost of of activities 
    - estimated total cost of trip
    Estructure the itinerary in a way that is easy to understand and follow.
    
    Provide a comprehensive itinerary for the trip.
    """,
    output_key="travel_itinerary"
)


travel_optimizer_agent = Agent(
    name="travel_optimizer_agent",
    model=LiteLlm(AGENT_MODEL),
    description="Agent to optimize the travel itinerary based on user preferences with practical advises ",
    instruction="""
    You are a seasoned travel planner that will uses the research from "travel_itinerary" output to optimize the itinerary based on user preferences and practical recommendations
    You will be given a list of activities and respond with:
    - optimized budget
    - A day by day activities plan
    - accommodation suggestion
    - backups plans
    - transportation options
    
    Format the final output as:
    
    ITINERARY: {travel_itinerary}
    
    OPTIMIZED BUDGET: [your money saving and practical advice]
    
    TRAVEL ESSENTIALS: [accommodation, transportation, food, culture] 
    
    BACKUP PLANS: [backup plan for the trip]  
    
    """
)


root_agent = SequentialAgent(
    name="travel_agent",
    description="A comprehensive travel planner that will optimize the itinerary based on user preferences and practical recommendations",
    sub_agents=[
        destination_agent,
        itinerary_agent,
        travel_optimizer_agent,
    ]
)
