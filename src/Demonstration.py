import os
import pandas as pd
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
from tensorflow.keras.models import load_model
import warnings
warnings.filterwarnings('ignore')
from src.GenTestData.TestDataGen import *
import tensorflow as tf
#tf.compat.v_org.logging.set_verbosity(tf.compat.v_org.logging.ERROR)

#Select the test file and GenTestData inside it. Afterward, the GenTestData is scaled
Test = GenTestData()
InitialTestData = Test.SelectFile()
ScaledTestData = Test.ScaleData(InitialTestData)


print('\n---Selection of testcase based on complications---\n')
print('1: Cardiovascular Complication\n'
      '2: Respiratory Complication\n'
      '3: Neurology Complication\n'
      '4: Metabollic Complication\n'
      '5: Psychiatric Complication\n'
      '6: Abdominal Complication\n\n')

k = int(input('Please provide the number to derive the testcase for the complication: '))
print('\n')

# All test GenTestData is modified based on users provided modification ratio
ModifiedTestData= Test.ChangeTestData(ScaledTestData,Test.vital)

# Creating test GenTestData for each complication from the selected testcase based on their required features
cdata_org, rdata_org, adata_org, mdata_org, pdata_org, ndata_org = Test.SelectTestData(ScaledTestData, k)
cdata_mod, rdata_mod, adata_mod, mdata_mod, pdata_mod, ndata_mod = Test.SelectTestData(ModifiedTestData, k)

# Converting test GenTestData to roch tensor
cdata_orgPT, rdata_orgPT, ndata_orgPT, mdata_orgPT, adata_orgPT, pdata_orgPT = Test.TensorConvert(cdata_org, rdata_org, ndata_org, mdata_org, adata_org, pdata_org)
cdata_modPT, rdata_modPT, ndata_modPT, mdata_modPT, adata_modPT, pdata_modPT = Test.TensorConvert(cdata_mod, rdata_mod, ndata_mod, mdata_mod, adata_mod, pdata_mod)

# Predicting the possibility of each complication using the segregated test GenTestData
PredInst= CompPrediction()

cpred_mod, rpred_mod, npred_mod, mpred_mod, ppred_mod, apred_mod = PredInst.BinaryPred(cdata_mod, rdata_mod, adata_mod, mdata_mod, pdata_mod, ndata_mod)
cpred_org, rpred_org, npred_org, mpred_org, ppred_org, apred_org = PredInst.BinaryPred(cdata_org, rdata_org, adata_org, mdata_org, pdata_org, ndata_org)

cpred_orgPT, rpred_orgPT, npred_orgPT, mpred_orgPT, apred_orgPT, ppred_orgPT = PredInst.BinaryPredPT(cdata_orgPT, rdata_orgPT, ndata_orgPT, mdata_orgPT, adata_orgPT, pdata_orgPT)
cpred_modPT, rpred_modPT, npred_modPT, mpred_modPT, apred_modPT, ppred_modPT = PredInst.BinaryPredPT(cdata_modPT, rdata_modPT, ndata_modPT, mdata_modPT, adata_modPT, pdata_modPT)

# Developing a GenTestData frame with information of the probability percentange of both modified and original test GenTestData
# This is done for all the 6 complication and sorted based on the probability percentange of the modified test GenTestData
print(f'---Probability of the 6 complications are listed below for the selected test case---\n')
data = {'': ['Probability of Cardiovascular Complication -', 'Probability of Respiratory Complication -',
             'Probability of Neurology Complication -', 'Probability of Metabollic Complication -',
             'Probability of Psychiatric Complication -', 'Probability of Abdominal Complication -'],
        'Original %': [cpred_org, rpred_org, npred_org, mpred_org, ppred_org, apred_org],
        'Modified %': [cpred_mod, rpred_mod, npred_mod, mpred_mod, ppred_mod, apred_mod],
        'TorchOriginal%': [cpred_orgPT, rpred_orgPT, npred_orgPT, mpred_orgPT, ppred_orgPT, apred_orgPT],
        'TorchModified%': [cpred_modPT, rpred_modPT, npred_modPT, mpred_modPT, ppred_modPT, apred_modPT]
        }
ProbTable = pd.DataFrame(data, index=None)
SortedTable = ProbTable.sort_values(by='Original %', ascending=False)
SortedTable.to_excel('tt.xlsx')
Test.GenerateDiagnose(k)
print(Style.RESET_ALL)
print(SortedTable.to_string(index=False))