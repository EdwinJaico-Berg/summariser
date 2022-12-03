import openai
import requests

from api import API_KEY

openai.api_key = API_KEY

def summarise_webpage(url: str) -> list:
    """A function that uses openai's GPT-3 to summarize the contents of a given url."""
    # Read the text
    text = requests.get(url).text

    # Generate summary of the text
    summary_response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Summarize the following text:\n{text}",
        max_tokens=4096,
        temperature=0.5,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # Extract the summary text from the API response
    summary_text = summary_response["choices"][0]["text"]

    # Split the summary text into a list of bullet points
    bullet_points = summary_text.split("\n")

    # Return the list of bullet points
    return bullet_points

def summarise_text(text: str) -> list:
    """Summarises the content of a given text"""
    
    # Generate summary of the text
    summary_response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Summarize the following text:\n{text}",
        max_tokens=4096,
        temperature=0.5,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

     # Extract the summary text from the API response
    summary_text = summary_response["choices"][0]["text"]

    # Split the summary text into a list of bullet points
    bullet_points = summary_text.split("\n")

    # Return the list of bullet points
    return bullet_points