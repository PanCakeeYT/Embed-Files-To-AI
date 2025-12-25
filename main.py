# main.py

from openai import OpenAI # using openai python sdk
import datetime as dt # importing datetime so the ai can know the date and time
import os # for accessing environment variables


client = OpenAI( #setting up the client
    api_key =              os.environ.get("XIAOMI_KEY"), # make sure to set your Xiaomi API key in your device environment variables. or hardcode it here (not recommended obviously) (you can change to chatgpt model)
    base_url =             "https://api.xiaomimimo.com/v1" # Xiaomi MiMo API base URL (you can change to chatgpt model)
)

# embedded file (pdf, txt, html or etc..) question answering
"""
Making the main function that takes in a file path and a question, reads the file content, and sends it to the MiMo API along with the question to get an answer.
"""
def ask_file_question(file_path, question): # setting up the define function to recieve file path and question
    with open(file_path, 'rb') as f: # opening the file in binary mode
        file_content = f.read() # reading the file content

    completion = client.chat.completions.create( # creating a chat completion using the mimo model
        model="mimo-v2-flash", # specifying the model (you can change to chatgpt model)
        messages=[ # setting up the messages.
            {
                "role": "system", # system role to set the context
                "content": f"You are MiMo, an AI assistant developed by Xiaomi. Today's date is: {dt.date.today()}. and time is {dt.datetime.now().strftime('%H:%M')}. Your knowledge cutoff date is December 2024."
            },
            {
                "role": "user", # user role to provide the file content and question
                "content": f"The following is the content of the file:\n{file_content.decode('utf-8', errors='ignore')}\n\nQuestion: {question}" # asking the question about the file content
            }
        ],
        # temperature=0.3, # uncomment if you want to control how strict or creative the responses are (0 to 10 ||| 0 is strict, 1 is creative)
        extra_body={
            "thinking": {"type": "enabled"} # enabling the thinking feature (you can disable it by changing "enabled" to "disabled")
        }
    )

    return completion.choices[0].message.content # returning the answer from the completion

"""
Making a function to extract text from a PDF file and save it as a TXT file.
"""
def pdf_to_text(file_path): # defining the function to convert pdf to text
    from PyPDF2 import PdfReader # importing the PdfReader from PyPDF2 library
    reader = PdfReader(file_path) # creating a PdfReader object
    text = "" # initializing an empty string to store the text
    for page in reader.pages: # iterating through each page in the pdf
        text += page.extract_text() + "\n" # extracting text from each page and adding it to the text string
    return text # returning the extracted text

"""
Making a function to create a TXT file from extracted text.
"""
def create_txt_file(txtofpdf, output_path): # defining the function to create a txt file
    with open(output_path, 'w', encoding='utf-8') as f: # opening the output file in write mode with utf-8 encoding
        f.write(txtofpdf) # writing the extracted text to the output file










"""
Usage.

Currently programmed for pdf and txt files only, if you want to add more then you code them.
"""


# --- Usage ---


"""
If you have a PDF file and want to extract text and then ask a question about it, uncomment the following lines:
"""

#pdf_file_path =           "random_story_2.pdf"
#text_content =            pdf_to_text(pdf_file_path)
#output_file_path =        "output.txt"
#create_txt_file(text_content, output_file_path)

#file_path2 =              output_file_path
#question =                "Summarize the main points of the document."

#answer =                  ask_file_question(file_path2, question)
#print(answer)




"""
If you have a TXT file and want to ask a question about it..
"""

txt_file_path =            "random_story.txt"
question =                 "What is the main topic discussed in the text?"

answer =                   ask_file_question(txt_file_path, question)
print(answer)
