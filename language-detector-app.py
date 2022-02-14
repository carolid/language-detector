from datetime import datetime
import pytz
import requests

def main():
    while True:
        languages_dict = {
            'af': 'Afrikaans',
            'ar': 'Arabic',
            'bn': 'Bengali',
            'bg': 'Bulgarian',
            'ca': 'Catalan; Valencian',
            'cs': 'Czech',
            'cy': 'Welsh',
            'da': 'Danish',
            'de': 'German',
            'el': 'Greek, Modern',
            'en': 'English',
            'es': 'Spanish',
            'et': 'Estonian',
            'fa': 'Persian',
            'fi': 'Finnish',
            'fr': 'French',
            'gu': 'Gujarati',
            'he': 'Hemodern',
            'hi': 'Hindi',
            'hr': 'Croatian',
            'hu': 'Hungarian',
            'id': 'Indonesian',
            'it': 'Italian',
            'ja': 'Japanese',
            'kn': 'Kannada',
            'ko': 'Korean',
            'lt': 'Lithuanian',
            'lv': 'Latvian',
            'mk': 'Macedonian',
            'ml': 'Malayalam',
            'mr': 'MarMarāṭhī',
            'ne': 'Nepali',
            'nl': 'Dutch',
            'no': 'Norwegian',
            'pa': 'Panjabi, Punjabi',
            'pl': 'Polish',
            'pt': 'Portuguese',
            'ro': 'Romanian, Moldavan',
            'ru': 'Russian',
            'sk': 'Slovak',
            'sl': 'Slovene',
            'so': 'Somali',
            'sq': 'Albanian',
            'sv': 'Swedish',
            'sw': 'Swahili',
            'ta': 'Tamil',
            'te': 'Telugu',
            'th': 'Thai',
            'tl': 'Tagalog',
            'tr': 'Turkish',
            'uk': 'Ukrainian',
            'ur': 'Urdu',
            'vi': 'Vietnamese'
        }


        countries_dict = {
            "English": "Washington, DC",
            "Spanish": "Madrid, Spain",
            "French": "Paris, France",
            "Chinese": "Bejing, China",
            "Japanese": "Tokyo, Japan",
            "Portuguese": "Lison, Portugal",
            "Russian": "Moscow, Russia"
        }


        languageString = input("Please input a valid word or sentence of any language... ")
        url = "http://localhost:3000/"
        rawString = {"Raw": str(languageString)}
        transfer = requests.post(url, data=rawString)
        usable = transfer.text

        language = usable

        # Output should be:
        #   * Whichever language has been identified
        #   * Option to translate
        #   * Country of origin and timezone

        # My microservice
        # Endpoint - Ideally accessed via an HTTP POST request - POST body incl.:
        #   - String
        #   Returns: language identified
        languageID = languages_dict[language]

        # Gurus microservice - lat/lon
        ETC = pytz.timezone('America/New_York')
        now = datetime.now(ETC)

        print("The language was identified as " + languageID)

        if languageID == "Spanish":
            translate = input("Would you like to translate from Spanish to English? [Y/N] ")

            if translate == "Y":
                # Luis' microservice - Spanish translator
                print("Your word is 'good'")
            elif translate == "N":
                print("Ok! More info on the language you inputted: \n")

        if languageID in countries_dict:
            print("The language you supplied originated in " + countries_dict[languageID])
            print("The time there is: " + str(now))
        else:
            print("The language you supplied does not yet have a configured origin")



if __name__ == "__main__":
    main()
