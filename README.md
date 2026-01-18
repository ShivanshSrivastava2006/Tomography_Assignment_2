# Quantum Density Matrix Reconstruction  
**Tomography Assignment 2 – QCG × PaAC Open Project (Winter 2025–2026)**

## Overview
This project implements a neural-network-based approach to reconstruct a quantum density matrix from measurement data while strictly enforcing all physical constraints:
- Hermitian
- Positive Semi-Definite (PSD)
- Unit Trace

The constraints are guaranteed **by construction** using a Cholesky-based parameterization.

---

## Track Chosen
**Track 2: Hardware-Centric Model**

A lightweight Multi-Layer Perceptron (MLP) is used due to its simplicity, efficiency, and suitability for hardware acceleration (e.g., FPGA deployment).

---

## Methodology
Instead of directly predicting the density matrix \( \rho \), the model predicts a lower triangular matrix \( L \).  
The density matrix is reconstructed as:

\[
\rho = \frac{LL^\dagger}{\mathrm{Tr}(LL^\dagger)}
\]

This ensures all physical constraints are satisfied automatically.

---

## Repository Structure

/src
model.py # Neural network model definition
train.py # Training and model generation script
/outputs
model.pt # Saved trained model
/docs
model_working.md
replication.md
AI_USAGE.md
README.md


---

## How to Run
See `docs/replication.md` for detailed, step-by-step instructions to reproduce the results, including environment setup and training execution.

---

## Evaluation Metrics
The reconstructed density matrices are evaluated using:
- Quantum Fidelity
- Trace Distance
- Inference Latency per reconstruction

---

## AI Usage Disclosure
This project used AI tools (e.g., ChatGPT) for code scaffolding and documentation assistance.  
Details are provided in `AI_USAGE.md`.

---

## Notes
- Synthetic data is used for demonstration purposes.
- The focus of this project is correctness, constraint enforcement, and reproducibility rather than performance optimization.

---

## Author
Shivansh Srivastava  
Indian Institute of Technology Roorkee

