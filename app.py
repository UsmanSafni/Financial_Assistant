
import gradio as gr
from utils.langchain_agent import LangChainAgent
from utils.visualizer import generate_plot

class FinancialChatBotApp:
    def __init__(self):
        """Initialize the application with required components."""
        self.lang_chain_agent = LangChainAgent()

    def create_header(self):
        """Create and return the header markdown for the application."""
        return gr.Markdown(
            """
            <div style='background-color: #3F51B5; padding: 20px; text-align: center; border-radius: 10px;'>
                <h1 style='color: white; margin: 0;'>Financial ChatBot Assistant</h1>
                <h2 style='color: white; margin: 10px 0 0;'>A professional assistant to guide you through financial metrics and analytics.</h2>
            </div>
            """,
            elem_id="title_container"
        )

    def create_chatbot_section(self):
        """Create and return the chatbot section (UI elements)."""
        with gr.Column(scale=1):
            gr.Markdown("### ChatBot Section")
            gr.Markdown("""
              <h4><i>Instructions for Use</i></h4>

              <p style="font-size:10px; font-style:italic;">
              This chatbot section offers insights into key financial ratios and metrics, including:
              <br>
              - <b>Liquidity</b><br>
              - <b>Solvency</b><br>
              - <b>Profitability</b><br>
              - Year-over-year changes in <b>Net Income</b><br>
              You can ask questions related to these metrics for three US SEC-listed companies: <b>Microsoft</b>, <b>Apple</b>, and <b>Tesla</b>.
            
              </p>
              """)
            
            


            # Input textbox for user queries
            user_input = gr.Textbox(
                label="Enter your query",
                placeholder="Ask about liquidity, solvency, profitability metrics, etc.",
                elem_id="user_input"
            )
            
            # Button for submitting user query
            submit_btn = gr.Button("Submit", elem_id="submit_button")


            # Output textbox for chatbot response
            output_text = gr.Textbox(label="Chatbot Response", elem_id="chatbot_response")

            # Add sample questions section
            gr.Markdown("<h4>Sample Questions:</h4>")
            sample_questions = [
                "Please give your insights about profitability of Microsoft?",
                "Which among these, apple or tesla performs better?",
                "What is your take on Microsoft's financial growth?",
                "Which among these companies , microsoft, tesla, apple has the highest liquidity?",
                "Which among these companies, Microsoft, tesla, apple is good to invest now?"

            ]

             # Create buttons for sample questions and link them to the user_input
            for question in sample_questions:
                gr.Button(question).click(
                    fn=lambda q=question: (q, self.lang_chain_agent.chat_bot(q)),
                    inputs=[],
                    outputs=[user_input, output_text]
                )
            

            # Connect the button to the chatbot function
            submit_btn.click(
                fn=self.lang_chain_agent.chat_bot,
                inputs=user_input,
                outputs=output_text
            )

    def create_plot_section(self):
        """Create and return the plot section (UI elements)."""
        with gr.Column(scale=1):
            gr.Markdown("### Financial Ratios Plots Section")

            gr.Markdown("""
              <h4><i>Instructions for Use</i></h4>

              <p style="font-size:10px; font-style:italic;">
              This plot section offers visual representation into key financial ratios and metrics from 2019 to 2023, including:
              <br>
              - <b>Liquidity</b><br>
              - <b>Solvency</b><br>
              - <b>Profitability</b><br>
              - Year-over-year changes in <b>Net Income</b><br>
              You can choose the plot type and company to get a visual representation of the data.
              </p>
              """)

            with gr.Row():
                # Dropdown for selecting plot type
                plot_type_dropdown = gr.Dropdown(
                    choices=["","Liquidity Ratios", "Solvency Ratios", "Profitability Ratios", "Income Growth"],
                    label="Select Plot Type",
                    interactive=True,
                    elem_id="plot_type_dropdown"
                )

                # Dropdown for selecting company name
                company_name_dropdown = gr.Dropdown(
                    choices=["","Microsoft", "Apple", "Tesla"],
                    label="Select Company Name",
                    interactive=True,
                    elem_id="company_dropdown"
                )

            # Button to generate plot
            generate_plot_btn = gr.Button("Generate Plot", elem_id="generate_plot_button")

            # Output area for displaying the plot
            output_plot = gr.Plot(label="Financial Ratios Plot")

            # Connect the button to the plot generation function
            generate_plot_btn.click(
                fn=generate_plot,
                inputs=[plot_type_dropdown, company_name_dropdown],
                outputs=output_plot
            )

    def build_ui(self):
        """Build the complete Gradio UI by combining different sections."""
        with gr.Blocks() as demo:
            # Add the header
            self.create_header()

            # Layout for chat and plot side by side
            with gr.Row():
                # Left column for chatbot section
                self.create_chatbot_section()

                # Right column for plot section
                self.create_plot_section()

        return demo

    def launch(self):
        """Launch the Gradio application."""
        ui = self.build_ui()  # Build the UI
        ui.launch()  # Launch the Gradio interface


# Instantiate the FinancialChatBotApp class and run the application
if __name__ == "__main__":
    app = FinancialChatBotApp()
    app.launch()
