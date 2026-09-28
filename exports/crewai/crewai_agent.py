from crewai import Agent
def create_agent():
    return Agent(role='GitInventoryFlow', goal='Autonomous Omnichannel Safety Stock, Stockout Risk & SKU Velocity Predictor Agent', backstory='Autonomous agent', verbose=True)
