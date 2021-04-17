
import pandas as pd
import numpy as np
import torch
import torch.nn.functional as F
from dgllife.utils import smiles_to_bigraph, CanonicalAtomFeaturizer, CanonicalBondFeaturizer


def read_smiles(file_dir: str):
    df = pd.read_csv(file_dir)
    return df['SMILES'].values


def Predict_sample(smiles: str,
                   model: torch.nn):
    node_featurizer = CanonicalAtomFeaturizer(atom_data_field='h')
    edge_featurizer = CanonicalBondFeaturizer(bond_data_field='h')
    graph = smiles_to_bigraph(smiles=smiles,
                              node_featurizer=node_featurizer,
                              edge_featurizer=edge_featurizer)
    if graph is None:
        return 'invalid'
    else:
        n_feat = graph.ndata['h']
        return F.sigmoid(model(graph, n_feat)).detach().numpy()[0][0]


def Predict(file_dir: str,
            save_dir: str,
            func_list: list):
    try:
        smiles_list = read_smiles(file_dir)
    except:
        return 'Load Failed!'
    pre_all = []
    for func in func_list:
        model = torch.load('.\\model\\' + func + '_gat_model.pkl')
        model.eval()
        pre_ = []
        for smiles in smiles_list:
            pre = Predict_sample(smiles, model)
            pre_.append(pre)
        pre_all.append(pre_)
    df_out = pd.DataFrame(np.array(pre_all).T, index=smiles_list, columns=func_list)
    df_out.to_csv(save_dir, float_format='%.3f')

    return df_out
