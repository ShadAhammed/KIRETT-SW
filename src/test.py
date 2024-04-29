from src.models.PredModel import *
import pandas as pd
import tkinter as tk
from tkinter.filedialog import askopenfilename

from src.GenTestData.TestDataGen import *

test= GenTestData()
testdata= test.SelectFile()
data = testdata.loc[testdata['abd'] == 0]
print(data.to_string(index=False))