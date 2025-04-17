import datetime
import os


def add_news():
    text = input("Enter news text: ")
    city = input("Enter city: ")
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    return f"--- News ---\n{text}\n{city}, {date}\n"


def add_private_ad():
    text = input("Enter ad text: ")
    exp_date_str = input("Enter expiration date (YYYY-MM-DD): ")
    try:
        exp_date = datetime.datetime.strptime(exp_date_str, "%Y-%m-%d").date()
        today = datetime.date.today()
        days_left = (exp_date - today).days
        if days_left < 0:
            return "--- Private Ad ---\n[EXPIRED]\n"
        return f"--- Private Ad ---\n{text}\nExpires in {days_left} day(s)\n"
    except ValueError:
        return "--- Private Ad ---\nInvalid expiration date format!\n"


def add_weather_forecast():
    city = input("Enter city: ")
    temp = input("Enter temperature in °C: ")
    forecast = input("Enter weather summary (e.g., sunny, cloudy): ")
    now = datetime.datetime.now().strftime("%A, %d %B %Y")
    return (f"--- Weather Forecast ---\nCity: {city}\nTemp: "
            f"{temp}°C\nForecast: {forecast}\nDate: {now}\n")


def write_to_file(content, filename="news_feed.txt"):
    with open(filename, "a", encoding="utf-8") as f:
        f.write(content + "\n")
    print(f"✔ Record added to {os.path.abspath(filename)}")


def main():
    while True:
        print("\nSelect a data that you want to create:")
        print("1 - News")
        print("2 - Private Ad")
        print("3 - Weather Forecast")
        print("0 - Exit")

        choice = input("Your choice: ")

        if choice == "1":
            record = add_news()
        elif choice == "2":
            record = add_private_ad()
        elif choice == "3":
            record = add_weather_forecast()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("❌ Invalid option. Try again.")
            continue

        write_to_file(record)


if __name__ == "__main__":
    main()
