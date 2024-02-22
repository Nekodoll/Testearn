from seleniumbase import SB
import sys

# List of relative URLs
relative_urls = [
    "/faucet/currency/btc",
    "/faucet/currency/ltc",
    "/faucet/currency/doge",
    "/faucet/currency/trx",
    "/faucet/currency/sol",
    "/faucet/currency/bnb",
    "/faucet/currency/bch",
    "/faucet/currency/eth",
    "/faucet/currency/fey",
    "/faucet/currency/usdt",
    "/faucet/currency/zec",
    "/faucet/currency/dash",
    "/faucet/currency/dgb",
]

def check_url(sb, url):
    sb.open(url)
    try:
        sb.submit('#submit')
    except Exception as e:
        #print(f"Can't find submit button:")
        return False

    success_message = f"Success! Claim "
    if sb.is_text_visible("Success!", "h2.swal2-title"):
        print(success_message)
        return True

    else:
        print(f"Error claiming ")
        return False

def main(base_url, email, ref):
    with SB(uc=True, test=True, headless=True) as sb:
        sb.open(base_url+ref)
        sb.type("#InputEmail", email)
        sb.click('button:contains("Login")')
        valid_urls = [url for url in relative_urls if check_url(sb, base_url + url)]
        #print(valid_urls)
        if not valid_urls:
            print("No valid URLs found. Exiting the application.")
            sys.exit()

        while True:
            for url in valid_urls:
                check_url(sb, base_url + url)


if __name__ == "__main__":
    base_url = "https://earnsolana.xyz"
    email = input("Enter your faucetpay.io email: ")
    main(base_url, email, "/?r=329")
