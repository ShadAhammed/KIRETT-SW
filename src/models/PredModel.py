from tensorflow.keras.models import load_model
import torch
import torch.nn as nn
import torch.optim as optim
from src.models.PTModels.Model import *
from src.models.NNModels import *
import os


class CompPrediction:
    def LoadModel(self):
        path = os.getcwd()
        Npath = path + r'\models\NNModels'
        CardioModel = load_model(Npath + r'\HerzANN-model.h5')
        RespModel = load_model(Npath + r'\RespANN-model.h5')
        NeuroModel = load_model(Npath + r'\NeuroANN-model.h5')
        MetabollicModel = load_model(Npath + r'\MetaANN-model.h5')
        AbdominalModel = load_model(Npath + r'\AbdANN-model.h5')
        PsyModel = load_model(Npath + r'\PsyANN-model.h5')
        return CardioModel, RespModel, NeuroModel, MetabollicModel, AbdominalModel, PsyModel

    def BinaryPred(self, cdata, rdata, adata, mdata, pdata, ndata):
        x = CompPrediction()
        CardioModel, RespModel, NeuroModel, MetabollicModel, AbdominalModel, PsyModel = x.LoadModel()
        cpred = (CardioModel.predict(cdata, verbose=0))
        cpred = round(cpred[0, 0] * 100, 2)
        rpred = (RespModel.predict(rdata, verbose=0))
        rpred = round(rpred[0, 0] * 100, 2)
        npred = (NeuroModel.predict(ndata, verbose=0))
        npred = round(npred[0, 0] * 100, 2)
        mpred = (MetabollicModel.predict(mdata, verbose=0))
        mpred = round(mpred[0, 0] * 100, 2)
        apred = (AbdominalModel.predict(adata, verbose=0))
        apred = round(apred[0, 0] * 100, 2)
        ppred = (PsyModel.predict(pdata, verbose=0))
        ppred = round(ppred[0, 0] * 100, 2)

        return cpred, rpred, npred, mpred, ppred, apred

    def LoadModelPT(self, c, r, n, m, a, p):
        cmodel = Net(c)
        path = os.getcwd()
        Npath = path + r'\models\PTModels'
        cmodel.load_state_dict(torch.load(Npath + r'\HerzANN-model.pt'))
        cmodel.eval()

        rmodel = Net(r)
        rmodel.load_state_dict(torch.load(Npath + r'\RespANN-model.pt'))
        rmodel.eval()

        nmodel = Net(n)
        nmodel.load_state_dict(torch.load(Npath + r'\NeuroANN-model.pt'))
        nmodel.eval()

        mmodel = Net(m)
        mmodel.load_state_dict(torch.load(Npath + r'\metaANN-model.pt'))
        mmodel.eval()

        amodel = Net(a)
        amodel.load_state_dict(torch.load(Npath + r'\AbdANN-model.pt'))
        amodel.eval()

        pmodel = Net(p)
        pmodel.load_state_dict(torch.load(Npath + r'\PsyANN-model.pt'))
        pmodel.eval()

        return cmodel, rmodel, nmodel, mmodel, amodel, pmodel

    def BinaryPredPT(self, cdata, rdata, ndata, mdata, adata, pdata):
        x = CompPrediction()
        CardioModelPT, RespModelPT, NeuroModelPT, MetaModelPT, AbdModelPT, PsyModelPT = x.LoadModelPT(cdata.shape[1],
                                                                                                      rdata.shape[1],
                                                                                                      ndata.shape[1],
                                                                                                      mdata.shape[1],
                                                                                                      adata.shape[1],
                                                                                                      pdata.shape[1])

        cpred = CardioModelPT(cdata)
        cpred = cpred.detach().numpy()
        cpred = round(cpred[0, 0] * 100, 2)

        rpred = RespModelPT(rdata)
        rpred = rpred.detach().numpy()
        rpred = round(rpred[0, 0] * 100, 2)

        npred = NeuroModelPT(ndata)
        npred = npred.detach().numpy()
        npred = round(npred[0, 0] * 100, 2)

        mpred = MetaModelPT(mdata)
        mpred = mpred.detach().numpy()
        mpred = round(mpred[0, 0] * 100, 2)

        apred = AbdModelPT(adata)
        apred = apred.detach().numpy()
        apred = round(apred[0, 0] * 100, 2)

        ppred = PsyModelPT(pdata)
        ppred = ppred.detach().numpy()
        ppred = round(ppred[0, 0] * 100, 2)

        return cpred, rpred, npred, mpred, apred, ppred
