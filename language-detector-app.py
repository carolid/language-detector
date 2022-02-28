from datetime import datetime
import pytz
import requests
import json
import time


class LanguageDetector:

    def __init__(self):
        self._query_string_text = None
        self._query_string_item = None
        self._continue = True
        self._language = "Gibberish"
        self._detector_url = "http://localhost:3000/"
        self._translator_url = "http://localhost:4500/translate"
        self._scraper_url = "http://localhost:1400/"
        self._latlon_url = "http://localhost:4350/locate"
        self._geo_api_key = "AIzaSyCKa3w9Ee5Kyfdy8qeUX_j__6hsyqkpkXo"
        self._countries_dict = {
            "English": "Washington, DC",
            "Spanish": "Madrid, Spain",
            "French": "Paris, France",
            "Chinese": "Bejing, China",
            "Japanese": "Tokyo, Japan",
            "Portuguese": "Lisbon, Portugal",
            "Russian": "Moscow, Russia"
        }

    def set_query_string_text(self, query):
        self._query_string_text = query

    def get_query_string_text(self):
        return self._query_string_text

    def set_query_string_item(self, query):
        self._query_string_item = query

    def get_query_string_item(self):
        return self._query_string_item

    def set_continue(self):
        self._continue = False

    def set_language(self, lang):
        self._language = lang

    def get_language(self):
        return self._language

    def run_app(self):
        """
        This method runs the CLI application
        :return: nothing
        """
        while self._continue:
            raw_string = input("Please input a valid word or sentence of any language... ")

            self.set_query_string_text({"text": str(raw_string)})
            self.set_query_string_item({"item": str(raw_string)})
            language = self.language_detector()

            print("\n" + "The language was identified as " + language)

            if language == "English":
                translate = input("Would you like to translate from English to Spanish? [Y/N] ")
                if translate == "Y":
                    word = self.language_translator()

                    if " " in word:
                        print("Your phrase in Spanish is " + word + "\n")
                    else:
                        print("Your word in Spanish is " + word + "\n")

                time.sleep(1)
                print("Where your language originated and the lat/lon of the capital: \n")

                for _ in range(0, 3):
                    print(".    ")
                    time.sleep(0.5)

            if language in self._countries_dict:
                print("The language you supplied originated in " + self._countries_dict[language])
                latlon = self.timezone_calc()
                print("The lat/lon there is: " + str(latlon) + "\n")
            else:
                print("The language you supplied does not yet have a configured origin" + "\n")

            scrape_q = input("Would you like to know more about the language you supplied? [Y/N] ")
            if scrape_q == "Y":
                wiki_blurb = self.wiki_scraper()
                print("Here's some more information about " + language + "\n" + wiki_blurb + "\n")

            to_continue = input("Would you like to enter another word or phrase? [Y/N] ")

            if to_continue == "N":
                self.set_continue()
                print("Thank you for using AnyLanguage Detector! \nGoodbye.")

    def language_detector(self):
        """
        My microservice
        :return: String containing language (e.g. French, Spanish, etc.)
        """
        query_string = self.get_query_string_text()
        detect = requests.post(self._detector_url, data=query_string)
        self.set_language(detect.text)

        return detect.text

    def language_translator(self):
        """
        Luis' microservice
        :return: String translated to Spanish
        """
        query_string = self.get_query_string_text()
        translate = requests.post(self._translator_url, json=query_string)
        inSpanish = json.loads(translate.text)
        word = inSpanish['translated']

        return word

    def wiki_scraper(self):
        """
        Nicholas' microservices
        :return: Returns a wikipedia blurb about the detected language
        """
        language_req = self.get_language()
        wiki_scrape = requests.post(self._scraper_url, data={'item': str(language_req)})
        scraped = wiki_scrape.text

        if scraped == {"item": "None"}:
            print("I'm sorry, your language could not be searched" + "\n")
            return
        else:
            return scraped

    def timezone_calc(self):
        """
        Placeholder for Guru's microservice
        :return: String of timezone information
        """
        latlon_location = self._countries_dict[self._language]
        latlon = requests.post(self._latlon_url, json={'location': str(latlon_location)})
        response = latlon.text

        return response


if __name__ == "__main__":
    app = LanguageDetector()
    app.run_app()
