import os

import google.generativeai as genai

API_KEY = os.getenv("GOOGLE_API_KEY")
if not API_KEY:
    raise RuntimeError(
        "GOOGLE_API_KEY is not set. Export it in your shell before running this script."
    )

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")

PROMPT = """
Generate an ideal Dockerfile for {language} with best practices.
Output only the Dockerfile content and no explanation, no markdown fences, and no extra commentary.
Make it easy to copy by ensuring the output is only the Dockerfile itself.
Include:
- A suitable base image
- Dependency installation steps
- Working directory setup
- Copying the source code
- Running the application
- A minimal, production-ready configuration when relevant
"""


def generate_dockerfile(language):
    language = (language or "").strip()
    if not language:
        raise ValueError("Programming language cannot be empty.")

    response = model.generate_content(PROMPT.format(language=language))
    return response.text.strip()


if __name__ == "__main__":
    language = input("Enter the programming language: ").strip()
    dockerfile = generate_dockerfile(language)
    print("\nGenerated Dockerfile:\n")
    print(dockerfile)
