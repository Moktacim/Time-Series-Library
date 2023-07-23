import random
import h5py, os
import numpy as np 
import logging 
import torch  
from typing import Tuple


def logging_data(data: np.array) -> None:
	
	raise NotImplementedError

def log_loaded_dataset(dataset, format, name):
    logging.info(f"[*] Loaded dataset '{name}' from '{format}':")
    logging.info(f"  {dataset.data}")
    logging.info(f"  undirected: {dataset[0].is_undirected()}")
    logging.info(f"  num graphs: {len(dataset)}")

    total_num_nodes = 0
    if hasattr(dataset.data, 'num_nodes'):
        total_num_nodes = dataset.data.num_nodes
    elif hasattr(dataset.data, 'x'):
        total_num_nodes = dataset.data.x.size(0)
    logging.info(f"  avg num_nodes/graph: "
                 f"{total_num_nodes // len(dataset)}")
    logging.info(f"  num node features: {dataset.num_node_features}")
    logging.info(f"  num edge features: {dataset.num_edge_features}")
    if hasattr(dataset, 'num_tasks'):
        logging.info(f"  num tasks: {dataset.num_tasks}")

    if hasattr(dataset.data, 'y') and dataset.data.y is not None:
        if isinstance(dataset.data.y, list):
            # A special case for ogbg-code2 dataset.
            logging.info(f"  num classes: n/a")
        elif dataset.data.y.numel() == dataset.data.y.size(0) and \
                torch.is_floating_point(dataset.data.y):
            logging.info(f"  num classes: (appears to be a regression task)")
        else:
            logging.info(f"  num classes: {dataset.num_classes}")
    elif hasattr(dataset.data, 'train_edge_label') or hasattr(dataset.data, 'edge_label'):
        # Edge/link prediction task.
        if hasattr(dataset.data, 'train_edge_label'):
            labels = dataset.data.train_edge_label  # Transductive link task
        else:
            labels = dataset.data.edge_label  # Inductive link task
        if labels.numel() == labels.size(0) and \
                torch.is_floating_point(labels):
            logging.info(f"  num edge classes: (probably a regression task)")
        else:
            logging.info(f"  num edge classes: {len(torch.unique(labels))}")
            

def load_data1(root_path: str, data_path: str) -> np.array:
    
    """
    load adopted from \
    Args:
        root_path (_type_): _description_
        data_path (_type_): _description_
        subset_size (int): Size of the subset to sample. 
    Returns:
        Tuple[np.array, np.array]: A tuple containing the input and output data arrays.
    Refs:
        https://stackoverflow.com/questions/28170623/how-to-read-hdf5-files-in-python

    """
    datx, daty = [],[]
    with h5py.File(os.path.join(root_path, data_path), 'r') as f:
        datx = f['mx_flt']['input']['signals']['0'][:].squeeze()
        daty = f['mx_flt']['output']['signals']['0'][:].squeeze()
        
    print("datx.shape[1]:", datx.shape[1])
    subset_size = int(datx.shape[1] * 1.0)  # subset size 
    print("subset Size:", subset_size)
    
    X = np.asarray(datx[:,: subset_size]).transpose()  # Select the subset of the input data
    Y = np.asarray(daty[:,:subset_size]).transpose()  # Select the subset of the output data
    
    return X, Y

#     datx, daty = [], []
#     # with h5py.File(os.path.join(root_path,
#     # 								data_path), 'r') as f:
#     # TODO 
#     with h5py.File(("/pfs/work7/workspace/scratch/rn3983-sahu/Time-Series-Library/dataset/Kiglis_hdf5/CD/training_data_11km.hdf5"), 'r') as f:
#         # for k in list(f.keys()):
#         #     datx.append(np.array(f[k]['mx_flt']['input']['signals']['0']).squeeze())
#         #     daty.append(np.array(f[k]['mx_flt']['output']['signals']['0']).squeeze())
#         datx = f['mx_flt']['input']['signals']['0'][:].squeeze()
#         daty = f['mx_flt']['output']['signals']['0'][:].squeeze()

#     X, Y = np.asarray(datx).transpose(), np.asarray(daty).transpose()
#     return X, Y

  


