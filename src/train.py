import torch
from model import DensityMatrixMLP

model = DensityMatrixMLP(input_dim=10, dim=2)
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)

for _ in range(10):
    x = torch.randn(32, 10)
    rho_pred = model(x)
    loss = torch.mean(torch.abs(rho_pred))
    loss.backward()
    optimizer.step()
    optimizer.zero_grad()

torch.save(model.state_dict(), "../outputs/model.pt")
