"""
Translator module to convert English to French and vice verca
"""
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)


def translator_instance(translate, text):
    """
    watson translator instance
    """
    if translate == "en-fr":
        translation = language_translator.translate(
            text=text,
            model_id='en-fr').get_result()
        return json.dumps(translation, indent=2, ensure_ascii=False)
    translation = language_translator.translate(
        text=text,
        model_id='fr-en').get_result()
    return json.dumps(translation, indent=2, ensure_ascii=False)


def english_to_french(english_text):
    """
    to convert english to french
    """
    french_text = json.loads(translator_instance("en-fr", english_text))
    print(french_text)
    return french_text['translations'][0]['translation']


def french_to_english(french_text):
    """
    to convert french to english
    """
    english_text = json.loads(translator_instance("fr-en", french_text))
    return english_text['translations'][0]['translation']
