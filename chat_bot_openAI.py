import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_api_key():
    """
    Get API key using dotenv
    """
    return os.getenv('OPENAI_API_KEY')

def main():
    
    # Load API key using dotenv
    api_key = get_api_key()
    
    # Initialize OpenAI client with API key
    client = OpenAI(api_key=api_key)
    
    # Conversation history
    conversation = [{"role": "user", "content": "You are a helpful assistant."}]

    print("ChatBot ready! Type 'exit' or 'quit' to end.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting the chat. Goodbye!")
            break
        
        conversation.append({"role": "user", "content": user_input})
        
        try:
            response = client.chat.completions.create(
                model="gpt-4.1-2025-04-14",
                messages=conversation
                #max_tokens=150,
                #temperature=0.7
            )
            
            bot_response = response.choices[0].message.content
            print(f"Bot: {bot_response}")
            
            conversation.append({"role": "assistant", "content": bot_response})
            
            # Keep conversation history manageable (last 10 exchanges)
            if len(conversation) > 20:
                conversation = conversation[-20:]
                
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()