from langchain_tavily import TavilySearch
from langchain_openrouter import ChatOpenRouter
from dotenv import load_dotenv

load_dotenv()


def triple(num: float) -> float:
    """
    Args:
        num (float): The number to be tripled
    Returns:
        float: The tripled number
    """
    return float(num) * 3


tools = [TavilySearch(max_results=1), triple]

llm = ChatOpenRouter(
    model="nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free"
).bind_tools(tools)
