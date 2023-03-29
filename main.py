import sqlite3
import pandas as pd
from scraper import Digikala
search_term=input("please enter ur search Item: ")


dk=Digikala(search_term)
def df_creation():
    names=dk.names()
    prices=dk.prices()
    statuses=dk.statuses()
    urls=dk.urls()
    total_scores=dk.total_scores()
    count_of_scores=dk.count_of_scores()

    digikala_list=dict({"نام محصول":names,
                        "قیمت" : prices,
                        "قابل معامله":statuses,
                        "امتیاز کل":total_scores,
                        "تعداد رای دهندگان":count_of_scores,
                        "آدرس محصول" : urls,
    })
    return pd.DataFrame(digikala_list)

df=df_creation().sort_values(["تعداد رای دهندگان","امتیاز کل"],ascending=False)

with sqlite3.connect(f'{search_term}.db') as conn:
    df.to_sql(f'{search_term}_table', conn, if_exists='replace', index=False)