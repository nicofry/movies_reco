from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import pandas as pd
from back import ML_lezgo,title_list
import sys
import os

app = FastAPI()
#uvicorn main:app --reload

@app.get('/suggest')
def suggest(name:str):
    df_titles = title_list(name).to_dict()
    return df_titles

@app.get('/reco')
def reco(choice:str):
    df_result = ML_lezgo(choice).to_dict()
    return df_result