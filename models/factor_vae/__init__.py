"""This module is the implementation of the FactorVAE proposed in
(https://arxiv.org/abs/1802.05983).
This model adds a new parameter to the VAE loss function balancing the weight of the 
reconstruction term and the Total Correlation.


Available samplers
-------------------

.. autosummary::
    ~disco.samplers.NormalSampler
    ~disco.samplers.GaussianMixtureSampler
    ~disco.samplers.TwoStageVAESampler
    ~disco.samplers.MAFSampler
    ~disco.samplers.IAFSampler
    :nosignatures:
"""

from .factor_vae_config import FactorVAEConfig
from .factor_vae_model import FactorVAE

__all__ = ["FactorVAE", "FactorVAEConfig"]
