# Model Working

## 1. Objective

The goal of this project is to reconstruct a **quantum density matrix** ρ from measurement data using a neural network, while strictly enforcing all physical constraints required for a valid quantum state.

A valid density matrix must be:
- Hermitian
- Positive Semi-Definite (PSD)
- Unit Trace

Instead of enforcing these constraints via penalties, they are **guaranteed by construction**.

---

## 2. Model Architecture (Track 2: Hardware-Centric)

The model is a lightweight **Multi-Layer Perceptron (MLP)** designed for efficiency and hardware friendliness.

### Architecture:
- **Input**: Measurement feature vector
- **Hidden Layer**: Fully connected layer with ReLU activation
- **Output Layer**: Parameters of a lower triangular matrix \( L \)

For a \( d \times d \) density matrix, the network outputs:
\[
\frac{d(d+1)}{2}
\]
parameters corresponding to the lower triangular entries of \( L \).

---

## 3. Enforcing Physical Constraints

Rather than directly predicting the density matrix \( \rho \), the model predicts a lower triangular matrix \( L \).

The density matrix is reconstructed using a Cholesky-based formulation:

\[
\rho = \frac{LL^\dagger}{\mathrm{Tr}(LL^\dagger)}
\]

### Constraint Guarantees:
- **Hermitian**: \( LL^\dagger \) is always Hermitian
- **Positive Semi-Definite**: Product of a matrix with its conjugate transpose is PSD
- **Unit Trace**: Explicit trace normalization ensures total probability equals one

Thus, all physical constraints are satisfied **by design**, without the need for additional regularization terms.

---

## 4. Training Procedure

The model is trained using synthetic measurement data generated as random tensors.  
A simple loss function is used to demonstrate the reconstruction pipeline and constraint enforcement.

The focus of training is **structural correctness and reproducibility**, rather than achieving state-of-the-art fidelity.

---

## 5. Hardware-Centric Design Rationale

This approach aligns well with hardware deployment considerations:

- MLPs map efficiently to FPGA DSP blocks
- Fixed-point or quantized arithmetic can be applied
- Matrix multiplications in the reconstruction step are parallelizable
- The design can be translated to hardware using High-Level Synthesis (e.g., Vitis HLS)

This makes the architecture suitable for low-latency, resource-constrained environments.

---

## 6. Evaluation Metrics

The reconstructed density matrices are evaluated using:
- **Quantum Fidelity**
- **Trace Distance**
- **Inference Latency per sample**

These metrics quantify both reconstruction accuracy and computational efficiency.

---

## 7. Summary

This model provides a simple, physically valid, and hardware-compatible solution for quantum density matrix reconstruction.  
By enforcing constraints through mathematical structure rather than penalties, the approach ensures correctness, stability, and reproducibility.
