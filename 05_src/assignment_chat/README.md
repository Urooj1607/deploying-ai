# Assignment 2: HealthWise Research Assistant

## Overview

HealthWise Research Assistant is a conversational AI chatbot designed to support users with healthcare research, public health, epidemiology, study design, and data analysis questions.

The chatbot is implemented with Gradio and includes three services:

1. API-based public health data service
2. Semantic search service using ChromaDB
3. Function-calling style study design helper

## Chatbot Personality

The chatbot acts as a friendly healthcare research assistant. It uses a clear, professional, and supportive tone.

## Service 1: API Service

The API service uses a public COVID-19 API from disease.sh. The chatbot does not return raw JSON. Instead, it converts the API response into a short natural-language public health summary.

## Service 2: Semantic Search Service

The semantic search service uses a small healthcare research text dataset stored in:

data/health_notes.txt

The dataset includes notes on diabetes, hypertension, informed consent, REDCap, qualitative research, quantitative research, and data cleaning.

The system uses ChromaDB with file persistence through:

chroma_db/

The text is split into small chunks and stored in a persistent ChromaDB collection.

## Service 3: Function Calling Service

The third service is a function-calling style research helper. When the user asks for a research question or study design, the chatbot generates a simple study design including:

- Research question
- Suggested study design
- Population
- Data to collect
- Analysis plan
- Expected output

## User Interface

The chatbot uses Gradio ChatInterface. The interface is chat-based and allows users to interact with the assistant in a natural conversational format.

## Memory

The Gradio chat interface maintains memory during the active session through the conversation history. This allows the chatbot to keep track of the ongoing conversation.

## Guardrails

The chatbot blocks restricted topics required by the assignment, including:

- Cats
- Dogs
- Horoscopes or Zodiac signs
- Taylor Swift

It also blocks attempts to reveal or modify the system prompt.

## How to Run

From the assignment folder, run:

```bash
python app.py