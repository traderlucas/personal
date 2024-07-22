# In another module or script
from data_fetch import OscarsDataFetcher
from data_cleaner import DataCleaner


exchange_rates = {
    'USD': 1,
    'GBP': 1.30,
    'EUR': 1.12
}

def main(url):
    fetcher = OscarsDataFetcher(url)
    data = fetcher.get_data()
    cleaner = DataCleaner(data, exchange_rates)
    cleaner.clean_dataframe()

    return "Succes, Oscars dataframe ready to be consumed"
if __name__ == "__main__":
    url = "http://oscars.yipitdata.com/"
    data = main(url)

