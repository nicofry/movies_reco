from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import pandas as pd
from back import ML_lezgo,title_list
import sys
import os

app = FastAPI()

@app.get('/suggest')
def suggest(name:str):
    la_liste = title_list(name)
    return la_liste