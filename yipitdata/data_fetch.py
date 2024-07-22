import logging
import requests
import pandas as pd
from typing import List, Dict, Optional

class OscarsDataFetcher:
    def __init__(self, url: str = 'http://oscars.yipitdata.com/'):
        self.url: str = url
        self.all_film_data: List[Dict[str, str]] = []
        self.data: Optional[List[Dict]] = None
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.INFO)

    def __fetch_movies_data(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            self.data = response.json().get("results", [])
        except requests.RequestException as e:
            self.logger.error(f"Failed to fetch movies data: {e}")
            self.data = []

    def __fetch_budget(self, detail_url: str) -> str:
        try:
            response = requests.get(detail_url)
            response.raise_for_status()
            data = response.json()
            return data.get('Budget', 'null')
        except requests.RequestException as e:
            self.logger.error(f"Failed to fetch budget for {detail_url}: {e}")
            return 'null'

    def __create_dataframe_from_movie_data(self) -> List[Dict[str, str]]:
        total_data = len(self.data)

        for i, data in enumerate(self.data, start=1):
            films = data.get('films', [])
            year = data.get('year', '')

            for film in films:
                detail_url = film.get('Detail URL', '')
                budget = self.__fetch_budget(detail_url)

                film_info = {
                    "Film": film.get('Film', ''),
                    "Year": year,
                    "Wikipedia URL": film.get('Wiki URL', ''),
                    "Oscar Winner": film.get('Winner', ''),
                    "Budget": budget
                }
                self.all_film_data.append(film_info)
            
            self.logger.info(f'Processing {i} of {total_data} data entries')

        return self.all_film_data

    def get_data(self) -> pd.DataFrame:
        if self.data is None:
            self.__fetch_movies_data()
            self.__create_dataframe_from_movie_data()
        return pd.DataFrame(self.all_film_data)
