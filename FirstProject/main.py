from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain.tools import  tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv

load_dotenv()

@tool
def calculator(first_number: float, second_number: float) -> str:
    """Useful for performing basic arithmetic calculations with numbers"""

    return f"The sum of {first_number} and {second_number} is {first_number + second_number}"

@tool
def greeting_user(name: str) -> str:
    """Useful for greeting a user"""

    return f"Hi {name} 😍, I hope you're well today"
def main():

    model = ChatOpenAI(temperature=0)

    tools = [calculator, greeting_user]
    agent_executor = create_react_agent(model, tools)

    print("Welcome😍! I'm your AI assistant, type 'quit' to exit.")
    print("You can ask me for calculations 📠 or chat with me 👨🏽‍🦱.")

    while True:
        user_input = input("\nYou: ").strip()

        if user_input == 'quit':
            break

        print("\nYour Assistant: ", end="")
        for chunk in agent_executor.stream(
                {'messages': [HumanMessage(content=user_input)]}
        ):
            if 'agent' in chunk and 'messages' in chunk['agent']:
                 for message in chunk['agent']['messages']:
                     print(message.content, end="")
        print()

if __name__ == "__main__":
    main()