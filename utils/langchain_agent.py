from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain.prompts import SystemMessagePromptTemplate, PromptTemplate
from langchain import hub
from .fn_tools import liquidity, solvency, profitability,income_growth
import os
from dotenv import load_dotenv
load_dotenv()

os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
os.environ['LANGSMITH_API_KEY'] = os.getenv('LANGSMITH_API_KEY')

class LangChainAgent:
    def __init__(self):
        # Initialize the Language Model
        
        

        self.llm = ChatOpenAI(model="gpt-3.5-turbo-0125")
        self.tools = [liquidity, solvency, profitability, income_growth]  # Placeholder for your tools
        self.prompt = hub.pull("hwchase17/openai-tools-agent")
        
        # Modify the system prompt part only
        new_system_prompt = SystemMessagePromptTemplate(
            prompt=PromptTemplate(
                input_variables=[], 
                template=(
                    'You are a financial analysis assistant designed for SEC analysts, '
                    'equipped with tools to evaluate liquidity, profitability, solvency, and year-over-year income changes. '
                    'Your task is to analyze relevant financial ratios and provide concise, accurate financial overviews of companies based on these metrics. '
                    'Always maintain a professional, clear, and precise tone. '
                    'If you do not know the answer, state that you do not know.'
                )
            )
        )

        # Replace the system prompt in the original prompt template
        self.prompt.messages[0] = new_system_prompt
        # Bind the LLM with the provided tools
        self.llm_with_tools = self.llm.bind_tools([])  # Currently no tools to bind
        self.agent = create_tool_calling_agent(self.llm, self.tools, self.prompt)
        
        # Create an agent executor by passing in the agent and tools
        self.agent_executor = AgentExecutor(agent=self.agent, tools=self.tools, verbose=True)

    def chat_bot(self, user_input):
        # Use the agent executor to handle user input
        response = self.agent_executor.invoke(
            {
                "input": user_input
            }
        )
        answer = response['output']
        return answer

# Example usage
if __name__ == "__main__":

    agent = LangChainAgent()
    user_query = "Can you provide the solvency analysis?"
    response = agent.chat_bot(user_query)
    print(response)
