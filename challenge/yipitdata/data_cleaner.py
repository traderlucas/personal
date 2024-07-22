import pandas as pd
import numpy as np
import re
import logging
from typing import Optional, Dict

class DataCleaner:
    def __init__(self, df: pd.DataFrame, exchange_rates: Optional[Dict[str, float]] = None):
        self.df = df
        self.exchange_rates = exchange_rates
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.INFO)

    @staticmethod
    def __parse_numeric_string(numeric_str: str) -> int:
        numeric_str = numeric_str.lower()
        if 'million' in numeric_str:
            return float(re.sub(r'[^\d.]', '', numeric_str)) * 1_000_000
        return float(re.sub(r'[^\d.]', '', numeric_str))

    def __clean_budget_column(self, budget_str: Optional[str]) -> float:
        if pd.isna(budget_str) or budget_str == 'N/A':
            return 0

        if any(cond in budget_str for cond in ['-', '–']):
            return 0
        
        if "or" in budget_str:
            budget_str = budget_str.split("or")[0]

        removed_brackets_and_parentheses = re.sub(r'\[.*?\]|\(.*?\)', '', budget_str).strip()
        cleaned_str = re.sub(r'[^\d.,£€$millionbillion]', '', removed_brackets_and_parentheses, flags=re.IGNORECASE)

        currency = 'USD'
        if '£' in budget_str:
            currency = 'GBP'
        elif '€' in budget_str:
            currency = 'EUR'

        try:
            numeric_value = DataCleaner.__parse_numeric_string(cleaned_str)
        except:
            return 0

        return numeric_value * self.exchange_rates.get(currency, 1)

    @staticmethod
    def __clean_year_column(year_str: Optional[str]) -> str:
        return year_str[:4] if year_str else ''

    def clean_dataframe(self) -> pd.DataFrame:
        self.df['Budget'] = np.ceil(self.df['Budget'].apply(self.__clean_budget_column))
        self.df['Year'] = self.df['Year'].apply(self.__clean_year_column)
        output_file = 'oscarData.csv'
        try:
            self.df.to_csv(output_file, index=False)
            self.logger.info(f"Data cleaned and saved to {output_file}")
        except Exception as e:
            self.logger.error(f"Failed to save the DataFrame to {output_file}: {e}")
        return self.df
