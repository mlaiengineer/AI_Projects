from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain.tools import  tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv

load_dotenv()
def main():

    model = ChatOpenAI(temperature=0)

    tools = []
    agent_executor = create_react_agent(model, tools)

    print("Welcome😍! I'm your AI assistant, type 'quit' or 'خروج' to exit.")
    print("You can ask me for calculations 📠 or chat with me 👨🏽‍🦱.")

    while True:
        user_input = input("\nYou: ").strip()

        if user_input == 'quit':
            print("Thanks 😍 for chat with me 🤖🍵, this chat is ended🫡")
            break
        if user_input == 'خروج':
            print("شكراً لتحدث معي 🤖😍، انتهينا من هذه المحادثة🤖✈️")

        print("\nYour Assistant:", end="")
        for chunk in agent_executor.stream(
                {"messages": [HumanMessage(content=user_input)]}
        ):
            if 'agent' in chunk and 'messages' in chunk['agent']:
                 for message in chunk['agent']['messages']:
                     print(message.content, end="")
        print()

if __name__ == "__main__":
    main()
