from datetime import datetime
import pytz
import requests

def main():
    while True:
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
        language = transfer.text

        # My microservice
        # Endpoint - Ideally accessed via an HTTP POST request - POST body incl.:
        #   - String
        #   Returns: language identified
        # languageID = languages_dict[language]

        # Gurus microservice - lat/lon
        ETC = pytz.timezone('America/New_York')
        now = datetime.now(ETC)

        print("The language was identified as " + language)

        if language == "Spanish":
            translate = input("Would you like to translate from Spanish to English? [Y/N] ")

            if translate == "Y":
                # Luis' microservice - Spanish translator
                print("Your word is 'good'")
            elif translate == "N":
                print("Ok! More info on the language you inputted: \n")

        if language in countries_dict:
            print("The language you supplied originated in " + countries_dict[language])
            print("The time there is: " + str(now))
        else:
            print("The language you supplied does not yet have a configured origin")



if __name__ == "__main__":
    main()
