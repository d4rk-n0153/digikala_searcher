import sqlite3
import pandas as pd
from scraper import Digikala

def df_creation():
    dk=Digikala(input("please enter ur search Item: "))
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


df_creation().to_excel("digikala.xlsx")
