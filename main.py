import sqlite3
import pandas as pd
from scraper import Digikala


def search_and_store_data(search_term):
    """
    Search Digikala website for products matching the given search term and store the data in an SQLite database.
    
    Parameters:
    -----------
    search_term : str
        The search term to use when searching Digikala website for products.
        
    Returns:
    --------
    None
    """
    # Create instance of Digikala class with search term
    dk = Digikala(search_term)

    # Get product information using methods of Digikala class
    names = dk.names()
    prices = dk.prices()
    statuses = dk.statuses()
    urls = dk.urls()
    total_scores = dk.total_scores()
    count_of_scores = dk.count_of_scores()

    # Create a dictionary from the scraped information
    digikala_dict = {
        "نام محصول": names,
        "قیمت" : prices,
        "قابل معامله": statuses,
        "امتیاز کل": total_scores,
        "تعداد رای دهندگان": count_of_scores,
        "آدرس محصول" : urls,
    }

    # Create a Pandas DataFrame from the dictionary and sort it based on votes and ratings
    df = pd.DataFrame(digikala_dict).sort_values(["تعداد رای دهندگان", "امتیاز کل"], ascending=False)

    # Store the DataFrame in an SQLite database
    with sqlite3.connect(f"{search_term}.db") as conn:
        df.to_sql(f"{search_term}_table", conn, if_exists="replace", index=False)


# Prompt user for a search term
search_term = input("Please enter your search item: ")

# Call search_and_store_data function to search for products and store the data in an SQLite database
search_and_store_data(search_term)
