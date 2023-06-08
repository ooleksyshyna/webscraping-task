import requests
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re


DOMAIN = "https://sleepcalculator.com"
FAKE_DOMAIN = "https://not.valid.domain"
DATA_GOV = "https://catalog.data.gov/dataset"


def ping_server(*, domain: str) -> bool:
    try:
        requests.get(domain)
        return True
    except requests.ConnectionError:
        print("SERVER ERROR")
        return False


def retrieve_robot_wiki_file() -> str:
    try:
        response = requests.get("https://en.wikipedia.org/robots.txt")
        return response.text
    except Exception as e:
        return e


def retrieve_number_of_datasets_from_data_gov():
    req = Request("https://data.gov")
    html_page = urlopen(req).read()

    soup = BeautifulSoup(html_page, 'html.parser')
    text = soup.findAll('span', {'class': 'text-color-red'})[0].string
    return text


def main():
    print("--------First--------")
    res1_1 = ping_server(domain=DOMAIN)
    print(f"Successful result:::{res1_1}")
    res1_2 = ping_server(domain=FAKE_DOMAIN)
    print(f"Unsuccessful result:::{res1_2}")
    print("--------Second--------")
    res2 = retrieve_robot_wiki_file()
    print(f"Result:::{res2}")
    print("--------Third--------")
    res3 = retrieve_number_of_datasets_from_data_gov()
    print(f"Result:::{res3}")



if __name__ == "__main__":
    main()
