import json
import os
import ibm_watson
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
translator = ibm_watson.LanguageTranslatorV3(
    version='2021-02-01',
    authenticator=authenticator
)
translator.set_service_url(url)


def english_to_french(english_text):
    """Permite traducir de englis a french"""
    if english_text is None:
        return ""
    if english_text == "":
        return ""
    translation = translator.translate(
        text=english_text,
        model_id='en-fr'
    ).get_result()
     
    return translation['translations'][0]['translation']


def french_to_english(french_text):
    if french_text is None:
        return ""
    if french_text == "":
        return ""
    """Permite traducir de frances al english"""
    translation = translator.translate(
        text=french_text,
        model_id='fr-en'
    ).get_result()
    return translation['translations'][0]['translation']
