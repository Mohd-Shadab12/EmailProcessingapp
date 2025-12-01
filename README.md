# Email Assistant with GenAI
---
## Project Overview

**Email Assistant** is an AI-powered application that helps users efficiently manage professional emails.  
It processes raw email content and generates:

1. A **professionally written reply** suitable for sending directly.  
2. A **concise summary** of the email.  
3. **Actionable follow-up steps** to guide next actions.

This tool is ideal for job applications, customer support, or professional communication where quick, high-quality email handling is needed.

---

## Features

- Supports **multiline email input**  
- Generates **ready-to-send professional replies**  
- Provides a **short, clear summary** of the email  
- Suggests **actionable follow-up steps**  
- Low-latency processing using **Gemini 2.5 Flash-Lite model**  
- Easy-to-use **web interface via Streamlit**  

---

## Tech Stack

- **Backend:** FastAPI  
- **Frontend:** Streamlit 
- **AI Processing:** LangChain + Google Generative AI (Gemini)  
- **Environment Management:** python-dotenv  

---

## Deployment

- **Backend:** Hosted on Render, accessible via REST API  
- **Frontend:** Hosted on Streamlit Cloud, interacts with backend API  
- Supports **real-time email processing** through the cloud interface  

---

## Usage

1. Open the Streamlit frontend in your browser.


2. Paste the raw email content into the text area.


3. Click Generate.


4. The app will display:

Professional reply

Short summary

Follow-up actions

---

## Notes

Ensure your Google GenAI API key is valid.

Supports multiline emails, emojis, and special characters.

Designed for professional email scenarios only.

Follow security best practices when deploying publicly.


