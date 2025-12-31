import requests
import sys

if len(sys.argv) < 2:
    sys.exit("Missing command-line argument")
else:
    try:
        bitcoins = float(sys.argv[1])
        r = requests.get(
            "https://rest.coincap.io/v3/assets/bitcoin?apiKey=564b26c7183482ec205a53a1c7403a09e997ab07dd4060e61bddc12e239fb680"
        )
        r.raise_for_status()

        response = r.json()
        data = response["data"]
        price = bitcoins * float(data["priceUsd"])
        print(f"${price:,.4f}")
    except requests.RequestException:
        sys.exit("Exception while sending request")
    except Exception as e:
        sys.exit("Command-line argument is not a number")
