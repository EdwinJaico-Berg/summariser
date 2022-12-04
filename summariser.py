import openai
import requests
import nltk
from bs4 import BeautifulSoup

from api import API_KEY

openai.api_key = API_KEY

def summarise_text(text: str) -> list:
    """Summarises the content of a given text"""
    # Ensure input is valid
    if not text:
        return None

    # Generate summary of the text
    try:
        summary_response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"{text}\n\nTl;dr",
            temperature=0.7,
            max_tokens=100,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=1
        )
    except:
        return "Sorry there has been an issue. Please reduce the size of the input text"

    summary = summary_response["choices"][0]["text"]

    summary = clean_output(summary)

    return summary

def summarise_webpage(url: str) -> list:
    """A function that uses openai's GPT-3 to summarize the contents of a given url."""
    # Ensure that input is valid 
    if not url:
        return None
    # Read the text
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")

    # Remove script and style elements
    for element in soup(['script', 'style']):
        element.extract()

    # Get text
    text = soup.get_text()

    # Break into lines and remove leading and trailing space
    lines = (line.strip() for line in text.splitlines())

    # Break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines 
              for phrase in line.split("  "))

    # Drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)

    return summarise_text(text)

def clean_output(text: str) -> str:
    """Cleans the text of typical errors."""
    # Remove starting colon
    if not text[0].isalpha():
        text = text[1:]
    
    # Remove white spaces
    text = text.strip()

    # Remove incomplete sentences
    # These will only occur at the end of the summary
    ending_punctuation = ["!", "?", "."]

    sentences = nltk.sent_tokenize(text)

    remove = True
    for punctuation in ending_punctuation:
        if punctuation in sentences[-1]:
            remove = False

    if remove:
        sentences.pop(-1)

    text = " ".join(sentence for sentence in sentences)

    return text
    
    
