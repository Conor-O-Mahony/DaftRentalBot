import os
import time

from dotenv import load_dotenv

load_dotenv(".env")


def generate_end_time():
    try:
        max_hours = os.environ.get("maxHours")
        if not (isinstance(max_hours, int) and max_hours > 0 and max_hours <= 9):
            print(
                "Conditions for Maximum hours not satisfied, therefore, running the bot for 2 hours"
            )
            max_hours = 2
    except NameError:
        # Running it for 2 hours by default
        print("Running the bot for 2 hours as there were no hours specified.")
        max_hours = 2

    end_time = time.time() + 60 * 60 * max_hours
    print("Running it for: ", max_hours, " hours.")
    return end_time


class GenerateLink:
    def __init__(self) -> None:
        # Base link on which filters will be added
        self.link = "https://www.daft.ie/property-for-rent/ireland"
        self.available_price = list(range(200, 2501, 100))
        self.available_price = self.available_price.extend(
            list(range(3000, 20000, 500))
        )
        self.available_beds = list(range(1, 16))
        self.available_bath = 

    def generate_filter_link(self):
        max_price = os.environ.get("max_price")
        min_bed = os.environ.get("min_bed")
        max_bed = os.environ.get("max_bed")
        min_bath = os.environ.get("min_bath")

        link = f"https://www.daft.ie/property-for-rent/ireland?rentalPrice_to={max_price}&numBeds_from={min_bed}&numBeds_to={max_bed}&numBaths_from={min_bath}&sort=publishDateDesc&location={city_name}&location={city_name}-city"
        return self.link

    def city_filter_link(self):
        try:
            city_name = os.environ.get("city_name")
            if not (isinstance(city_name, str) and max_hours > 0 and max_hours <= 9):
                print(
                    "Conditions for Maximum hours not satisfied, therefore, running the bot for 2 hours"
                )
                max_hours = 2
        except NameError:
            # Running it for 2 hours by default
            print("Running the bot for 2 hours as there were no hours specified.")
            max_hours = 2