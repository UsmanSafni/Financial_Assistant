# Financial ChatBot Assistant

## Overview
The Financial ChatBot Assistant is a professional tool designed to guide users through financial metrics and analytics. It leverages Langchain's tool calling agent and data visualization to provide insights and visualizations based on user queries.

## Features
1. **Interactive ChatBot**: Users can interact with the bot to ask questions about various financial metrics such as liquidity ratios, solvency ratios, profitability metrics, etc.
2. **Financial Ratios Plots**: Generate visual representations of financial ratios for selected companies. Available plots include Liquidity Ratios, Solvency Ratios, Profitability Ratios, and Income Growth.

## Installation
To use this application, ensure you have Python installed. Then, install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

## Usage
1. Clone the repository or download the source code.
2. Run the script:

```bash
python app.py
```

This will start a Gradio interface where you can interact with the Financial ChatBot Assistant.

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

