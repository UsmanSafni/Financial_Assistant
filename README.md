# Financial ChatBot Assistant

## Overview
The Financial ChatBot Assistant is a professional tool designed to guide users through financial metrics and analytics. It leverages Langchain's tool calling agent and data visualization to provide insights and visualizations based on user queries.

## Features
1. **Interactive ChatBot**: Users can interact with the bot to ask questions about various financial metrics such as liquidity ratios, solvency ratios, profitability metrics, etc.
2. **Financial Ratios Plots**: Generate visual representations of financial ratios for selected companies. Available plots include Liquidity Ratios, Solvency Ratios, Profitability Ratios, and Income Growth.
   
![image](https://github.com/user-attachments/assets/42cac309-0bc8-4412-895d-c1bc339a63e7)

*Langchain's tool calling agent*

## Installation Guide
1. Create a Conda Environment: Start by creating a new Conda environment with Python 3.12:

```bash
conda create -p venv python=3.12
conda activate venv/
```
2. Install Dependencies: Install the required dependencies using pip:

```bash
pip install -r requirements.txt
```
3. Obtain API Keys:

OpenAI Key: Sign up at OpenAI and obtain your API key for GPT model access.
LangSmith Key: Similarly, obtain your LangSmith API key.

4. Set Up Environment Variables: Create a .env file in your project root directory and add the following:

```bash
OPENAI_API_KEY=your_openai_api_key
LANGSMITH_API_KEY=your_langsmith_api_key
```

## Usage
Run the script:

```bash
python app.py
```

This will start a Gradio interface where you can interact with the Financial ChatBot Assistant.
## Application flow
The agent in our pipeline is equipped with a variety of tools to respond to user queries. The Large Language Model (LLM) acts as the "brain" of the agent, directing its decision-making process. When a user submits a question, the LLM helps the agent choose the most suitable tool or combination of tools to generate an answer. If multiple tools are needed, the agent will determine the appropriate sequence for using them.

![alt text](image.png)

*Agentic flow*

## Components
### FinancialChatBotApp Class
The main class responsible for building and launching the Gradio application.

#### Methods
- `__init__`: Initializes the application with a LangChainAgent instance.
- `create_header`: Creates and returns the header markdown for the application.
- `create_chatbot_section`: Creates and returns the chatbot section with input, button, and output components.
- `create_plot_section`: Creates and returns the plot section with dropdowns and button components.
- `build_ui`: Builds the complete Gradio UI by combining different sections.
- `launch`: Launches the Gradio application.

### LangChainAgent Class
Handles the logic for generating responses to user queries related to financial metrics.

### FinancialCalculator Class
Extracts financial metrics and calculates ratios.

### DataLoader Class
Loads the dataset and reads it as a dataframe.

### generate_plot Function
Generates and returns a plot based on the selected plot type and company name.

## Demo
You can check out the live demo here:

[Financial Assistant Demo](https://huggingface.co/spaces/Safni/Financial_assistant)

## Contributions
Contributions are welcome! Please fork the repository and submit pull requests.

