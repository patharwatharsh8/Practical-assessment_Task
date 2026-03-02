from langchain.agents import initialize_agent, AgentType
from langchain_openai import ChatOpenAI
from config import settings
import logging

logger = logging.getLogger(__name__)

def create_agent(tool, memory):
    llm = ChatOpenAI(model=settings.MODEL_NAME)

    system_prompt = """
    You are a CV question answering agent.
    You must answer strictly from the CV context retrieved using tools.
    If answer not found, say:
    'This information is not available in the provided CV.'
    Always say: 'Based on the CV...'
    """

    agent = initialize_agent(
        tools=[tool],
        llm=llm,
        agent=AgentType.OPENAI_FUNCTIONS,
        memory=memory,
        verbose=True
    )

    return agent
