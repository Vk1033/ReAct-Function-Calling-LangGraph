from langchain_tavily import TavilySearch
from langchain_openrouter import ChatOpenRouter
from dotenv import load_dotenv

load_dotenv()


def triple(num: float) -> float:
    """
    param num: a number to triple
    returns: the triple of the input number
    """
    return float(num) * 3


tools = [TavilySearch(max_results=1), triple]

llm = ChatOpenRouter(
    model="nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free"
).bind_tools(tools)
