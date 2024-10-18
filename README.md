# Financial ChatBot Assistant

## Overview
The Financial ChatBot Assistant is a professional tool designed to guide users through financial metrics and analytics. It leverages Langchain's tool calling agent and data visualization to provide insights and visualizations based on user queries.

## Features
1. **Interactive ChatBot**: Users can interact with the bot to ask questions about various financial metrics such as liquidity ratios, solvency ratios, profitability metrics, etc.
2. **Financial Ratios Plots**: Generate visual representations of financial ratios for selected companies. Available plots include Liquidity Ratios, Solvency Ratios, Profitability Ratios, and Income Growth.
![image](https://github.com/user-attachments/assets/42cac309-0bc8-4412-895d-c1bc339a63e7)
*Figure 1: Langchain's tool calling agent*

## Installation
To use this application, first create a new conda environmnet with python==3.12. Then, install the required dependencies using pip:

```bash
conda create -p venv python=3.12
conda activate venv/
pip install -r requirements.txt
```

Sign up at OpenAI and obtain your own key to start making calls to the gpt model. Once you have the key, create a .env file in your repository and store the OpenAI key. similarly obtain your Langsmith Key and store in the .env file.

## Usage
Run the script:

```bash
python app.py
```

This will start a Gradio interface where you can interact with the Financial ChatBot Assistant.
## Application flow
The agent in our pipeline will have a set of tools at its disposal that it can use to answer a user query. The Large Language Model (LLM) serves as the “brain” of the agent, guiding its decisions. When a user submits a question, the agent uses the LLM to select the most appropriate tool or a combination of tools to provide an answer. If the agent determines it needs multiple tools, it will also specify the order in which the tools are used. The agentic flow is depicted below:
![image](https://github.com/user-attachments/assets/ebda33fa-21e5-4ff3-9607-058b6fb067f3)


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

### generate_plot Function
Generates and returns a plot based on the selected plot type and company name.

## Contributing
Contributions are welcome! Please fork the repository and submit pull requests.

