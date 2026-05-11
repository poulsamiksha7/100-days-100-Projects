import requests

while True:
    try:
        user_input = input("Enter country name (or type exit): ")

        if user_input.lower() == "exit":
            print("Program exited.")
            break

        r = requests.get(
            f"https://restcountries.com/v3.1/name/{user_input}"
        )

        r.raise_for_status()

        data = r.json()

        country = data[0]

        name = country["name"]["common"]
        capital = country["capital"][0]
        region = country["region"]
        population = country["population"]

        print("\n--- Country Information ---")
        print(f"Name: {name}")
        print(f"Capital: {capital}")
        print(f"Region: {region}")
        print(f"Population: {population}")
        print("----------------------------\n")

    except requests.exceptions.RequestException as e:
        print(f"Request Failed: {e}")

    except (KeyError, IndexError):
        print("Country data not found properly.")