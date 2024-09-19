# import vertexai
# import streamlit as st
# from vertexai.preview import generative_models
# from vertexai.preview.generative_models import GenerativeModel, Part, Content, ChatSession
# project = "gemini-explorer"
# vertexai.init(project = project)
# config = generative_models.GenerationConfig(
#     temperature=0.4
# )
# model = GenerativeModel(
#     "gemini-pro",
#     generation_config = config
# )
# chat = model.start_chat()


# def process_response(response):
#     # Perform any processing or formatting of the chatbot's response here
#     # For example, you might want to add emojis, format the text, or apply any other transformations
    
#     # For now, let's just return the response as is
#     return response
# def llm_function(chat: ChatSession, query):
#     # Check if the message history is empty
#     if len(st.session_state.messages) == 0:
#         initial_prompt = "Introduce yourself as ReX, an assistant powered by Google Gemini. You use emojis to be interactive"
#         # Send the initial prompt to the chat session
#         response = chat.send_message(initial_prompt)
#         # Process and display the response
#         processed_response = process_response(response)
#         st.write(processed_response)
#         # Update the session state with the initial prompt message
#         st.session_state.messages.append(processed_response)
    
#     # Send the user's query to the chat session and retrieve the response
#     response = chat.send_message(query)
    
#     # Process the response (e.g., formatting, filtering, etc.)
#     processed_response = process_response(response)
    
#     # Display the processed response in the Streamlit app
#     st.write(processed_response)
    
#     # Update the session state with the user's query and the chatbot's response
#     st.session_state.messages.append(query)
#     st.session_state.messages.append(processed_response)


# st.title("Gemini Explorer")
# if "messages" not in st.session_state:
#     st.session_state.messages = []
# for index, message in enumerate(st.session_state.messages):
#     st.write(f"Message {index + 1}: {message}")



# for index, message in enumerate(st.session_state.messages):
#     # Create a Content object for the message
#     content = Content(message)
    
#     # Display the content in the Streamlit app
#     st.write(content)
# query = st.chat_input("Gemini Flights")
# user_name = st.text_input("Please enter your name")

# # Store the user's name in the session state for future use
# st.session_state.user_name = user_name

# # Implement Logic for Initial Prompt
# if len(st.session_state.messages) == 0:
#     # Personalized initial prompt
#     initial_prompt = f"Ahoy, {user_name}! I be ReX, an assistant powered by Google Gemini. Let's sail the seas of knowledge together! 🏴‍☠️"
#     llm_function(chat, initial_prompt)

import vertexai
import streamlit as st
from vertexai.preview import generative_models
from vertexai.preview.generative_models import GenerativeModel, Content, ChatSession

# Initialize Vertex AI
project = "gemini-explorer"
vertexai.init(project=project)

# Configuring the generative model
config = generative_models.GenerationConfig(
    temperature=0.4
)
model = GenerativeModel(
    "gemini-pro",
    generation_config=config
)
chat = model.start_chat()

# Function to process chatbot responses
def process_response(response):
    # Perform any processing or formatting of the chatbot's response here
    # For now, returning the response as is
    return response

# Function to handle LLM interactions
def llm_function(chat: ChatSession, query):
    # Send the user's query to the chat session and retrieve the response
    response = chat.send_message(query)
    
    # Process the response
    processed_response = process_response(response)
    
    # Display the processed response
    st.write(processed_response)
    
    # Update the session state with the user's query and the chatbot's response
    st.session_state.messages.append(f"User: {query}")
    st.session_state.messages.append(f"ReX: {processed_response}")

# Set the title of the app
st.title("Gemini Explorer")

# Initialize session state for storing messages if not already done
if "messages" not in st.session_state:
    st.session_state.messages = []

# Collect user input for name
user_name = st.text_input("Please enter your name")
st.session_state.user_name = user_name

# Display initial prompt if this is the first interaction
if user_name and len(st.session_state.messages) == 0:
    initial_prompt = f"Ahoy, {user_name}! I be ReX, an assistant powered by Google Gemini. Let's sail the seas of knowledge together! 🏴‍☠️"
    st.write(initial_prompt)
    st.session_state.messages.append(f"ReX: {initial_prompt}")

# Display conversation history
for message in st.session_state.messages:
    st.write(message)

# User query input
query = st.chat_input("Ask me anything!")
if query:
    llm_function(chat, query)
