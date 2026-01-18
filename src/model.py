import torch
import torch.nn as nn

class DensityMatrixMLP(nn.Module):
    def __init__(self, input_dim, dim):
        super().__init__()
        self.dim = dim
        self.fc = nn.Sequential(
            nn.Linear(input_dim, 128),
            nn.ReLU(),
            nn.Linear(128, dim * (dim + 1) // 2)
        )

    def forward(self, x):
        batch = x.shape[0]
        L = torch.zeros(batch, self.dim, self.dim, device=x.device)
        idx = torch.tril_indices(self.dim, self.dim)
        L[:, idx[0], idx[1]] = self.fc(x)
        rho = L @ L.conj().transpose(-1, -2)
        trace = rho.diagonal(dim1=1, dim2=2).sum(-1)
        rho = rho / trace.unsqueeze(-1).unsqueeze(-1)

        return rho
