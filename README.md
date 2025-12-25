# AI File Q&A

This script uses AI to answer your questions about the content of `.txt` and `.pdf` files.

## How It Works

- For **.txt files**, it reads the text directly.
- For **.pdf files**, it first extracts the text into a new file called `output.txt`.

Then, it sends the text and your question to an AI model to get an answer.

## Setup

1.  **Install Libraries:**
    Open your terminal or command prompt and run:
    ```bash
    pip install openai pypdf2
    ```

2.  **Set API Key:**
    You need to tell the script your API key. Set it as an environment variable named `XIAOMI_KEY`.
    ```bash
    # For Windows PowerShell
    $Env:XIAOMI_KEY="your_api_key_here"

    # For macOS/Linux
    export XIAOMI_KEY="your_api_key_here"
    ```
    *Note: You can also just paste your key directly into the `testingsmth.py` file where it says `os.environ.get("XIAOMI_KEY")`, but this is less secure.*

## How to Use

1.  Place your `.txt` or `.pdf` file in the same folder as the script.
2.  Open `testingsmth.py` in an editor.
3.  **Find the "Usage" section** at the bottom of the file.
4.  To ask about a `.txt` file, change `random_story.txt` to your filename and edit the `question`.
    ```python
    txt_file_path =            "your_file.txt"
    question =                 "What is this file about?"
    ```
5.  To ask about a `.pdf` file, uncomment the PDF section and change `random_story_2.pdf` to your filename and edit the `question`.
    ```python
    pdf_file_path =           "your_file.pdf"
    question =                "Summarize this document."
    ```
6.  Save the file and run it from your terminal:
    ```bash
    python testingsmth.py
    ```
The answer will be printed in the terminal.
