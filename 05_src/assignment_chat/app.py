import gradio as gr

from services.guardrails import check_guardrails
from services.api_service import get_public_health_fact
from services.rag_service import semantic_search_answer
from services.custom_service import create_study_design


SYSTEM_PERSONALITY = """
You are HealthWise Assistant, a friendly healthcare research chatbot.
You help users with public health, epidemiology, clinical research, study design, and data analysis.
You explain things clearly and professionally.
"""


def route_message(user_input: str, history):
    """
    Routes user input to the correct service.
    """

    guardrail_message = check_guardrails(user_input)
    if guardrail_message:
        return guardrail_message

    user_text = user_input.lower()

    if "api" in user_text or "covid" in user_text or "public health data" in user_text:
        return get_public_health_fact()

    elif "study design" in user_text or "research question" in user_text or "design a study" in user_text:
        return create_study_design(user_input)

    else:
        return semantic_search_answer(user_input)


def chat_function(message, history):
    """
    Main chat function for Gradio.
    History gives the chatbot short-term memory during the session.
    """
    response = route_message(message, history)
    return response


demo = gr.ChatInterface(
    fn=chat_function,
    type="messages",
    title="HealthWise Research Assistant",
    description=(
        "Ask me about healthcare research, public health, study design, "
        "data cleaning, REDCap, informed consent, diabetes, hypertension, or epidemiology."
    ),
    chatbot=gr.Chatbot(height=450, type="messages"),
    textbox=gr.Textbox(
        placeholder="Ask a healthcare research question...",
        container=False,
        scale=7
    )
)


if __name__ == "__main__":
    demo.launch()