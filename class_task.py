import datetime
import os
from abc import ABC, abstractmethod


class Record(ABC):
    @abstractmethod
    def compose(self) -> str:
        pass


class News(Record):
    def __init__(self, text: str, city: str):
        self.text = text
        self.city = city
        self.date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    def compose(self) -> str:
        return f"--- News ---\n{self.text}\n{self.city}, {self.date}\n"


class PrivateAd(Record):
    def __init__(self, text: str, exp_date_str: str):
        self.text = text
        self.exp_date_str = exp_date_str

    def compose(self) -> str:
        try:
            exp_date = datetime.datetime.strptime(self.exp_date_str, "%Y-%m-%d").date()
            today = datetime.date.today()
            days_left = (exp_date - today).days
            if days_left < 0:
                return "--- Private Ad ---\n[EXPIRED]\n"
            return f"--- Private Ad ---\n{self.text}\nExpires in {days_left} day(s)\n"
        except ValueError:
            return "--- Private Ad ---\nInvalid expiration date format!\n"


class WeatherForecast(Record):
    def __init__(self, city: str, temp: str, forecast: str):
        self.city = city
        self.temp = temp
        self.forecast = forecast
        self.date = datetime.datetime.now().strftime("%A, %d %B %Y")

    def compose(self) -> str:
        return (f"--- Weather Forecast ---\nCity: {self.city}\nTemp: "
                f"{self.temp}°C\nForecast: {self.forecast}\nDate: {self.date}\n")


class NewsFeedWriter:
    def __init__(self, filename: str = "news_feed.txt"):
        self.filename = filename

    def write(self, record: Record):
        with open(self.filename, "a", encoding="utf-8") as f:
            f.write(record.compose() + "\n")
        print(f"✔ Record added to {os.path.abspath(self.filename)}")


class App:
    def __init__(self):
        self.writer = NewsFeedWriter()

    def run(self):
        while True:
            print("\nSelect a data that you want to create:")
            print("1 - News")
            print("2 - Private Ad")
            print("3 - Weather Forecast")
            print("0 - Exit")

            choice = input("Your choice: ")

            if choice == "1":
                text = input("Enter news text: ")
                city = input("Enter city: ")
                record = News(text, city)
            elif choice == "2":
                text = input("Enter ad text: ")
                exp_date = input("Enter expiration date (YYYY-MM-DD): ")
                record = PrivateAd(text, exp_date)
            elif choice == "3":
                city = input("Enter city: ")
                temp = input("Enter temperature in °C: ")
                forecast = input("Enter weather summary (e.g., sunny, cloudy): ")
                record = WeatherForecast(city, temp, forecast)
            elif choice == "0":
                print("Goodbye!")
                break
            else:
                print(" Invalid option. Try again.")
                continue

            self.writer.write(record)


if __name__ == "__main__":
    app = App()
    app.run()