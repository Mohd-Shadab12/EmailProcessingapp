from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv
load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite",
                             api_key=os.getenv("GOOGLE_API_KEY"))

prompt="""
You are helper that helps with email handling.
Email:{email}
Generate these :
1. A professionaly written reply based on the email context (sutable to send directly)
2. A short summary of this email (4-5 sentences maximum).
3. Most actionable follow-up email actions(concise and clear).

Do not add optional placeholders unless absolutely necessary.
"""

prompttemplate=PromptTemplate(
    input_variables=["email"],
    template=prompt
)

def process_given_email(email_text:str):
    final_input=prompttemplate.format(email=email_text)
    output=model.invoke(final_input)
    return output.content