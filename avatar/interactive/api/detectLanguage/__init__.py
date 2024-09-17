import logging
import requests
import json
import os

import azure.functions as func

endpoint = os.getenv("TEXT_ANALYTICS_ENDPOINT")
subscription_key = os.getenv("TEXT_ANALYTICS_KEY")

def main(req: func.HttpRequest) -> func.HttpResponse:
    apiUrl = f'{endpoint}/text/analytics/v3.2-preview.1/languages'
    text = req.params.get('text')

    requestBody = {
        'documents': [
        {
            'id': '1',
            'text': text
        }
        ]
    }

    requestOptions = {
        'headers': {
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': subscription_key
        },
        'data': json.dumps(requestBody)
    }

    response = requests.post(apiUrl, **requestOptions)
    data = response.json()
    language_code = data['documents'][0]['detectedLanguage']['iso6391Name']

    language_to_voice = {
        "de": "de-DE",
        "en": "en-US",
        "es": "es-ES",
        "fr": "fr-FR",
        "it": "it-IT",
        "ja": "ja-JP",
        "ko": "ko-KR",
        "pt": "pt-BR",
        "zh_chs": "zh-CN",
        "zh_cht": "zh-CN",
        "ar": "ar-AE",
        "hi": "hi-IN",
        "af": "af-ZA",
        "am": "am-ET",
        "bg": "bg-BG",
        "bn": "bn-IN",
        "ca": "ca-ES",
        "cs": "cs-CZ",
        "da": "da-DK",
        "el": "el-GR",
        "et": "et-EE",
        "fa": "fa-IR",
        "fi": "fi-FI",
        "fil": "fil-PH",
        "ga": "ga-IE",
        "gu": "gu-IN",
        "he": "he-IL",
        "hr": "hr-HR",
        "hu": "hu-HU",
        "id": "id-ID",
        "is": "is-IS",
        "kn": "kn-IN",
        "lt": "lt-LT",
        "lv": "lv-LV",
        "ml": "ml-IN",
        "mr": "mr-IN",
        "ms": "ms-MY",
        "nb": "nb-NO",
        "nl": "nl-NL",
        "pl": "pl-PL",
        "ro": "ro-RO",
        "ru": "ru-RU",
        "sk": "sk-SK",
        "sl": "sl-SI",
        "sv": "sv-SE",
        "ta": "ta-IN",
        "te": "te-IN",
        "th": "th-TH",
        "tr": "tr-TR",
        "uk": "uk-UA",
        "ur": "ur-PK",
        "vi": "vi-VN"
    }

    if response.status_code == 200:
        return func.HttpResponse(language_to_voice[language_code], status_code=200)
    else:
        return func.HttpResponse(response.status_code)