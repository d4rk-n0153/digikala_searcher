import sqlite3
import pandas as pd
from scraper import Digikala

def df_creation():
    dk=digikala(input("please enter ur search Item: "))
    names=dk.names()
    prices=dk.prices()
    statuses=dk.statuses()
    urls=dk.urls()
    total_scores=dk.total_scores()
    count_of_scores=dk.count_of_scores()
    
