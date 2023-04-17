"""
cloud translate engine
"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

# Authenticate to IBM Cloud
authenticator = IAMAuthenticator(apikey)
  # Replace <API_KEY> with your IBM Watson Language Translator API key
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

# Set the service URL
language_translator.set_service_url(url)

# Function to translate English to French
def english_to_french(english_text):
    """
    en to fr
    """
    source_language = 'en'
    target_language = 'fr'

    translation = language_translator.translate(
        text=english_text,
        source=source_language,
        target=target_language
    ).get_result()

    french_text = translation['translations'][0]['translation']
    return french_text

# Function to translate French to English

def french_to_english(french_text):
    """
    fr to en
    """
    source_language = 'fr'
    target_language = 'en'

    translation = language_translator.translate(
        text=french_text,
        source=source_language,
        target=target_language
    ).get_result()

    english_text = translation['translations'][0]['translation']
    return english_text
