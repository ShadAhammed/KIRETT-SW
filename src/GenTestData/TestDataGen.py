from src.models.PredModel import *
import pandas as pd
import tkinter as tk
from tkinter.filedialog import askopenfilename
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from colorama import Fore, Back, Style

class GenTestData:
    vital = ['RR', 'SBP', 'DBP', 'MAD', 'BG', 'BodyTemperature', 'PulseOximetry', 'PR']
    def __init__(self):
        pass

    def SelectFile(self):
        # Select a file and output the GenTestData in the file as a variable
        root = tk.Tk()
        filename = askopenfilename()
        root.destroy()
        Data = pd.read_excel(filename, index_col=0)
        return Data

    def ChangeTestData(self, data,vital):
        #Method to modify the GenTestData by percentage. The modification rate can be choosen independently
        k = input("Type yes if you want to modify the value of testdata's health vitals: ")
        k = str(k)
        ChangedData= data.copy()
        if k == 'yes' or k == 'y':
            i = input('What percent of GenTestData should be changed? : ')
            i = int(i) / 100
            ChangedData[vital] = ChangedData[vital] * (1 + i)
            print('The GenTestData is modiefied\n')
            print('Original Data: \n', data[vital].to_string())
            print('\n')
            print('Modified Data: \n', ChangedData[vital].to_string())
        else:
            ModifiedTestData = data
            print('The GenTestData is not modiefied\n')
        return ChangedData

    def ScaleData(self, Data):
        # Scaling the GenTestData with standard scalers
        AllTestData = Data.iloc[:, 0:]
        scaler = MinMaxScaler()
        ScaledData = scaler.fit_transform(AllTestData)
        FinalTestData = pd.DataFrame(ScaledData, columns=AllTestData.columns)
        return FinalTestData

    def SelectTestData(self, TestData, i):
        # Selection of specific test GenTestData to test through all complication models
        print(Style.RESET_ALL)
        if i == 1:
            data = TestData.loc[TestData['c'] == 0]
            cdata = data[['RR', 'SBP', 'DBP', 'SkinCond', 'MAD', 'Herz Complain']]
            rdata = data[['PR', 'BG', 'BodyTemperature', 'PulseOximetry', 'PRh', 'RR', 'RespAbnormCond', 'RespPreIllness']]
            ndata = data[
                ['GCS', 'Consciousness Disorder', 'HeadDiscomfort', 'Brain Injury', 'Trauma', 'NeuroAbnormCond',
                 'NeuroCommDisturbance', 'NeuroPreIllness']]
            mdata = data[['PR', 'BG', 'RR', 'SBP', 'DBP', 'MetaAbnormCond', 'MetaPreIllness']]
            pdata = data[
                ['SBP', 'RR', 'circ', 'GCS', 'PRh', 'MentalSickness', 'PsySyndrom', 'PsyPreIllness', 'Alkohlic',
                 'Intoxication']]
            adata = data[['AbdAbnormCond', 'AbdPreIllness', 'AbdominalSchmerzen', 'BG', 'RR', 'SBP', 'DBP']]

        if i == 2:
            data = TestData.loc[TestData['r'] == 0]
            cdata = data[['RR', 'SBP', 'DBP', 'SkinCond', 'MAD', 'Herz Complain']]
            rdata = data[
                ['PR', 'BG', 'BodyTemperature', 'PulseOximetry', 'PRh', 'RR', 'RespAbnormCond', 'RespPreIllness']]
            ndata = data[
                ['GCS', 'Consciousness Disorder', 'HeadDiscomfort', 'Brain Injury', 'Trauma', 'NeuroAbnormCond',
                 'NeuroCommDisturbance', 'NeuroPreIllness']]
            mdata = data[['PR', 'BG', 'RR', 'SBP', 'DBP', 'MetaAbnormCond', 'MetaPreIllness']]
            pdata = data[
                ['SBP', 'RR', 'circ', 'GCS', 'PRh', 'MentalSickness', 'PsySyndrom', 'PsyPreIllness', 'Alkohlic',
                 'Intoxication']]
            adata = data[['AbdAbnormCond', 'AbdPreIllness', 'AbdominalSchmerzen', 'BG', 'RR', 'SBP', 'DBP']]
        if i == 3:
            data = TestData.loc[TestData['n'] == 0]
            cdata = data[['RR', 'SBP', 'DBP', 'SkinCond', 'MAD', 'Herz Complain']]
            rdata = data[
                ['PR', 'BG', 'BodyTemperature', 'PulseOximetry', 'PRh', 'RR', 'RespAbnormCond', 'RespPreIllness']]
            ndata = data[
                ['GCS', 'Consciousness Disorder', 'HeadDiscomfort', 'Brain Injury', 'Trauma', 'NeuroAbnormCond',
                 'NeuroCommDisturbance', 'NeuroPreIllness']]
            mdata = data[['PR', 'BG', 'RR', 'SBP', 'DBP', 'MetaAbnormCond', 'MetaPreIllness']]
            pdata = data[
                ['SBP', 'RR', 'circ', 'GCS', 'PRh', 'MentalSickness', 'PsySyndrom', 'PsyPreIllness', 'Alkohlic',
                 'Intoxication']]
            adata = data[['AbdAbnormCond', 'AbdPreIllness', 'AbdominalSchmerzen', 'BG', 'RR', 'SBP', 'DBP']]
        if i == 4:
            data = TestData.loc[TestData['m'] == 0]
            cdata = data[['RR', 'SBP', 'DBP', 'SkinCond', 'MAD', 'Herz Complain']]
            rdata = data[
                ['PR', 'BG', 'BodyTemperature', 'PulseOximetry', 'PRh', 'RR', 'RespAbnormCond', 'RespPreIllness']]
            ndata = data[
                ['GCS', 'Consciousness Disorder', 'HeadDiscomfort', 'Brain Injury', 'Trauma', 'NeuroAbnormCond',
                 'NeuroCommDisturbance', 'NeuroPreIllness']]
            mdata = data[['PR', 'BG', 'RR', 'SBP', 'DBP', 'MetaAbnormCond', 'MetaPreIllness']]
            pdata = data[
                ['SBP', 'RR', 'circ', 'GCS', 'PRh', 'MentalSickness', 'PsySyndrom', 'PsyPreIllness', 'Alkohlic',
                 'Intoxication']]
            adata = data[['AbdAbnormCond', 'AbdPreIllness', 'AbdominalSchmerzen', 'BG', 'RR', 'SBP', 'DBP']]
        if i == 5:
            data = TestData.loc[TestData['p'] == 0]
            cdata = data[['RR', 'SBP', 'DBP', 'SkinCond', 'MAD', 'Herz Complain']]
            rdata = data[
                ['PR', 'BG', 'BodyTemperature', 'PulseOximetry', 'PRh', 'RR', 'RespAbnormCond', 'RespPreIllness']]
            ndata = data[
                ['GCS', 'Consciousness Disorder', 'HeadDiscomfort', 'Brain Injury', 'Trauma', 'NeuroAbnormCond',
                 'NeuroCommDisturbance', 'NeuroPreIllness']]
            mdata = data[['PR', 'BG', 'RR', 'SBP', 'DBP', 'MetaAbnormCond', 'MetaPreIllness']]
            pdata = data[
                ['SBP', 'RR', 'circ', 'GCS', 'PRh', 'MentalSickness', 'PsySyndrom', 'PsyPreIllness', 'Alkohlic',
                 'Intoxication']]
            adata = data[['AbdAbnormCond', 'AbdPreIllness', 'AbdominalSchmerzen', 'BG', 'RR', 'SBP', 'DBP']]
        if i == 6:
            data = TestData.loc[TestData['a'] == 0]
            cdata = data[['RR', 'SBP', 'DBP', 'SkinCond', 'MAD', 'Herz Complain']]
            rdata = data[
                ['PR', 'BG', 'BodyTemperature', 'PulseOximetry', 'PRh', 'RR', 'RespAbnormCond', 'RespPreIllness']]
            ndata = data[
                ['GCS', 'Consciousness Disorder', 'HeadDiscomfort', 'Brain Injury', 'Trauma', 'NeuroAbnormCond',
                 'NeuroCommDisturbance', 'NeuroPreIllness']]
            mdata = data[['PR', 'BG', 'RR', 'SBP', 'DBP', 'MetaAbnormCond', 'MetaPreIllness']]
            pdata = data[
                ['SBP', 'RR', 'circ', 'GCS', 'PRh', 'MentalSickness', 'PsySyndrom', 'PsyPreIllness', 'Alkohlic',
                 'Intoxication']]
            adata = data[['AbdAbnormCond', 'AbdPreIllness', 'AbdominalSchmerzen', 'BG', 'RR', 'SBP', 'DBP']]
        return cdata, rdata, adata, mdata, pdata, ndata

    def TensorConvert(self, cdata, rdata, ndata, mdata, adata, pdata):
        cdataPT= torch.FloatTensor(cdata.values)
        rdataPT = torch.FloatTensor(rdata.values)
        ndataPT = torch.FloatTensor(ndata.values)
        mdataPT = torch.FloatTensor(mdata.values)
        adataPT = torch.FloatTensor(adata.values)
        pdataPT = torch.FloatTensor(pdata.values)
        return cdataPT, rdataPT, ndataPT, mdataPT, adataPT, pdataPT

    def GenerateDiagnose(self,k):

        # Show information on the original diagnosis done in reality during the rescue situation by rescue personnel

        if k == 1: print(Fore.RED + 'Patients diagnostic detail from Rettungswach - -  Unklarer Thoraxschmerz\n')
        if k == 2: print(
            Fore.RED + 'Patients diagnostic detail from Rettungswach - - Differentialdiagnose: Erkrankung: ACS,\n '
                       'Hauptdiagnose: Erkrankung: Dyspnoe unklarer Ursache\n')
        if k == 3: print(
            Fore.RED + 'Patients diagnostic detail from Rettungswach - - Hauptdiagnose: Erkrankung: Suizidalität, \n'
                       'Differentialdiagnose: Platzwunde:  Schädel-Hirn   Durchblutung distal: Normal  Motorik distal:\n '
                       'Normal  Sensibilität: Normal  Wundlänge : ~4cm  Schwere der Verletzung: Leicht\n')
        if k == 4: print(
            Fore.RED + 'Patients diagnostic detail from Rettungswach - - Verdachtsdiagnose: Magen Darm Grippe mit '
                       'Ausschluss Noro Virus\n')
        if k == 5: print(
            Fore.RED + 'Patients diagnostic detail from Rettungswach - - Verdachtsdiagnose: Erkrankung: Intoxikation Alkohol ('
                       'Psychiatrische Erkrankungen)\n')
        if k == 6: print(Fore.RED + 'Patients diagnostic detail from Rettungswach - - Appendizitis, Zyste rechts\n')


