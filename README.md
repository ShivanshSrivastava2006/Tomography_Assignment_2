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
