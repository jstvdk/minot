__version__ = '0.1.0'

try:
    from .model import Cluster
except ImportError:
    print('WARNING: Could not import Cluster from model. You')
    print('         may try (re)installing dependencies by  ')
    print('         hand. For example running:              ')
    print('             conda install matplotlib            ')
