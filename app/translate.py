# import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from flask_babel import _
from app import app


def translate(text, source_language, dest_language):
    if 'WATSON_APIKEY' not in app.config or \
            not app.config['WATSON_APIKEY']:
        return _('Error: the translation service is not configured.')

    authenticator = IAMAuthenticator(app.config['WATSON_APIKEY'])
    language_translator = LanguageTranslatorV3(
        version='2018-05-01',
        authenticator=authenticator
    )
    language_translator.set_service_url('https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/8adea71b-4647-40e0-970c-0e5070ad08fc')
    # language_translator.set_disable_ssl_verification(True)
    detailed_response = language_translator.translate(
        text=text,
        model_id=f'{source_language}-{dest_language}'
    )
    if detailed_response.get_status_code() != 200:
        return _('Error: the translation service failed.')
    result = detailed_response.get_result()
    return result["translations"][0]["translation"]
