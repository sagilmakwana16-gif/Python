
import os
import json
import datetime
from dotenv import load_dotenv
from sarvamai import SarvamAI

load_dotenv()

# API
client = SarvamAI(
    api_subscription_key=os.getenv("SARVAM_API_KEY")
)

# Create folders
os.makedirs("output", exist_ok=True)
os.makedirs("logs", exist_ok=True)

# User input
path = input("Enter your file path: ")

# Get files
if os.path.isfile(path):
    files = [path]
elif os.path.isdir(path):
    files = [
        os.path.join(path, f)
        for f in os.listdir(path)
        if f.endswith(".txt")
    ]
else:
    files = []

# Process files
for file in files:
    print("Processing file:", file)

    status = "Failure"
    error = ""

    try:
        with open(file, "r", encoding="utf-8") as f:
            text = f.read().strip()

        if not text:
            raise ValueError("File is empty")

        word_count = len(text.split())

        prompt = f"""
        Summarise the following text in 2-3 lines.

        Return ONLY a valid JSON object.
        Do not add markdown or ```json.

        Format:
{{
    "title": "Text title",
    "summary": "Short summary",
    "keywords": ["keyword1", "keyword2"]
}}

Text:
{text}
"""

        response = client.chat.completions(
            model="sarvam-105b",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        answer = response.choices[0].message.content

        if not answer:
         raise ValueError("AI returned an empty response")

         print("AI Response:", answer)
        # Convert response to JSON
        data = json.loads(answer)

        # Check required fields
        for key in ["title", "summary", "keywords"]:
            if key not in data:
                raise ValueError("Missing field: " + key)

        data["word_count"] = word_count
        data["file_name"] = os.path.basename(file)

        # Read old summaries
        output_file = "output/summaries.json"

        if os.path.exists(output_file):
            with open(output_file, "r", encoding="utf-8") as f:
                summaries = json.load(f)
        else:
            summaries = []

        # Add new summary
        summaries.append(data)

        # Save summaries
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(summaries, f, indent=4, ensure_ascii=False)

        status = "Success"
        print("Summary saved successfully!")

    except Exception as e:
        error = str(e)
        print("Error processing file:", error)

    # Save log
    with open("logs/app.log", "a", encoding="utf-8") as f:
        f.write(
            f"{datetime.datetime.now()} | "
            f"{file} | {status} | {error}\n"
        )

print("All files processed!")

