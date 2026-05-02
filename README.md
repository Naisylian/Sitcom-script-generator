# Sitcom script generator
A Chatbot creation project using Azure tools
#AI Powered Sitcom Script Generator

 An AI-powered content generation tool built on Microsoft Azure that creates sitcom style scripts using large language models, structured data, and dynamic prompt engineering.

## Overview

This project is a creative AI system designed to assist writers in generating sitcom style scenes quickly and efficiently. It leverages Azure OpenAI and a structured sitcom corpus to produce context aware, character driven scripts.

The application replicates the tone and humor of classic sitcoms and allows users to customize scenes, characters, and dialogue styles, making it a powerful tool for both learning and production.


##Key Features
- AI generated sitcom scripts using LLMs
- Dynamic prompt engineering for better dialogue quality
- Character driven scene generation
- Scene and mood customization
- PDF export for generated scripts
- Interactive UI powered by Streamlit

##Tech Stack
- **Python**
- **Microsoft Azure**
  - Azure OpenAI Service
  - Azure Blob Storage
- **Large Language Models (LLMs)**
- **Streamlit**

## How It Works

1. Sitcom transcripts are stored and retrieved from **Azure Blob Storage**
2. The corpus is processed and used as contextual input
3. User prompts (or prebuilt templates) are enhanced using **prompt engineering**
4. **Azure OpenAI** generates structured sitcom dialogue
5. Output is displayed and can be exported as a formatted script

## Project Structure

```
sitcom-script-generator/
├── app.py                  # Streamlit web interface
├── main.py                 # Azure OpenAI + Blob Storage logic
├── requirements.txt        # Python dependencies
├── unique.yml              # Environment/config file
├── .venv/                  # Virtual environment (not pushed)
└── corpus/                 # Downloaded transcript files (auto-generated)
```

##Setup
### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
```

### 2. Create and activate virtual environment
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Mac/Linux
source .venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file
```
AZURE_STORAGE_CONNECTION_STRING=your_azure_storage_connection_string
AZURE_OPENAI_KEY=your_azure_openai_key
AZURE_OPENAI_ENDPOINT=your_azure_openai_endpoint
AZURE_OPENAI_API_VERSION=your_api_version
AZURE_OPENAI_DEPLOYMENT=your_deployment_name
```

### 5. Run the app
```bash
streamlit run app.py
```

## Why This Project Matters

- **Practical application of AI** :demonstrates real world use of LLMs in content generation
- **Cloud integration** : end-to-end use of Azure services in a production-like system
- **Prompt engineering** : structured techniques for high quality, consistent outputs
- **Full stack development**  : covers data ingestion, model integration, and UI deployment

##Business Value

- Accelerates scriptwriting and ideation
- Reduces production time for content creators
- Enables scalable content generation
- Opens opportunities for SaaS-based creative tools

## Future Improvements
- Add voice generation for script playback
- Deploy as a full web application
- Introduce collaborative writing features

##Context

Built as a project to explore practical applications of **Generative AI**, **Retrieval-Augmented Generation (RAG)**, and **Azure cloud services**.
