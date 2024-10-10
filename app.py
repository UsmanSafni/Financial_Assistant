
import gradio as gr
from utils.langchain_agent import LangChainAgent
from utils.visualizer import generate_plot


s=LangChainAgent()

# Define the Gradio UI with simplified inline style
with gr.Blocks() as demo:
    gr.Markdown(
    """
    <div style='background-color: #3F51B5; padding: 20px; text-align: center; border-radius: 10px;'>
        <h1 style='color: white; margin: 0;'>Financial ChatBot Assistant</h1>
        <h2 style='color: white; margin: 10px 0 0;'>A professional assistant to guide you through financial metrics and analytics.</h2>
    </div>
    """,
    elem_id="title_container"
    )


    # Layout for chat and plot side by side
    with gr.Row():
        # Left column for ChatBot
        with gr.Column(scale=1):
            gr.Markdown("### ChatBot Section")
            user_input = gr.Textbox(label="Enter your query", placeholder="Ask about liquidity, solvency, profitability metrics, etc.", elem_id="textbox")
            # Wrapping the submit button in an indigo box


            submit_btn = gr.Button("Submit", elem_id="button")
            output_text = gr.Textbox(label="Chatbot Response", elem_id="textbox")
            submit_btn.click(fn=s.chat_bot, inputs=user_input, outputs=output_text)

        # Right column for Plots
        with gr.Column(scale=1):
            gr.Markdown("### Financial Ratios Plots Section")
            
            with gr.Row():
        # Dropdown for plot type
                plot_type_dropdown = gr.Dropdown(
                choices=["Liquidity Ratios", "Solvency Ratios", "Profitability Ratios", "Revenue Growth"],
                label="Select Plot Type",
                interactive=True,
                elem_id="dropdown"
                )
        
        # Dropdown for company name
                company_name_dropdown = gr.Dropdown(
                choices=["Microsoft","Apple","Tesla"],  # This will be your list of company names
                label="Select Company Name",
                interactive=True,
                elem_id="company_dropdown"
                )


            generate_plot_btn = gr.Button("Generate Plot", elem_id="button")
            output_plot = gr.Plot(label="Financial Ratios Plot")
            generate_plot_btn.click(fn=generate_plot, inputs=[plot_type_dropdown,company_name_dropdown], outputs=output_plot)

# Custom CSS for Indigo and White Theme
demo.css = """
    .gradio-container {
        background-color: #FFFFFF;  /* White background */
        color: #3F51B5;  /* Indigo text color */
    }

"""

# Launch the app
demo.launch()

