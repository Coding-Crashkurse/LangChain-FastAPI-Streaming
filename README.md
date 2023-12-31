# OpenAI GPT-3.5-turbo Streaming API with FastAPI 

This project demonstrates how to create a real-time conversational AI by streaming responses from OpenAI's GPT-3.5-turbo model. It uses FastAPI to create a web server that accepts user inputs and streams generated responses back to the user.

## Running the Project

1. Clone the repository.
2. Install Python (Python 3.7+ is recommended).
3. Install necessary libraries. This project uses FastAPI, uvicorn, LangChain, among others. You can install them with pip: `pip install fastapi uvicorn langchain`.
4. Add your OpenAI API key to the `.env` file.
5. Start the FastAPI server by running `uvicorn main:app` in the terminal.
6. Access the application by opening your web browser and navigating to `localhost:8000`.

Note: Ensure the appropriate CORS settings if you're not serving the frontend and the API from the same origin.

## Project Overview

The project uses an HTML interface for user input. The user's input is sent to a FastAPI server, which forwards it to the GPT-3.5-turbo model. The generated response is streamed back to the user, simulating a real-time conversation. 
