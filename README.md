Currently working on the project

## How to create account on IBMQ and get token

<details>
<summary><b><ins>Create Account</ins></b></summary>
<br>

<img src="https://github.com/user-attachments/assets/6aa7fc26-529a-4611-8d9e-d5c283134390" width="600" height="600">

###### ↳ [https://academic.ibm.com/](https://academic.ibm.com/) Make account using school email(intra_id@student.42.fr)
<br>


<img src="https://github.com/user-attachments/assets/79aaf909-b638-4b02-a8da-e0eb7e3dc10b" width="600" height="600">

###### ↳ IBM Cloud
<br>


<img src="https://github.com/user-attachments/assets/09d93be2-9419-411e-895d-410466d15745" width="600" height="600">

###### ↳ IBM Cloud Feature Code
<br>


<img src="https://github.com/user-attachments/assets/4a471a4c-e8ef-4a54-8aa9-753581942fff" width="600" height="600">

###### ↳ Request Feature Code
<br>


<img src="https://github.com/user-attachments/assets/bb338abf-a0a7-42ee-b0be-48505506333f" width="600" height="600">

###### ↳ Copy Code
<br>


<img src="https://github.com/user-attachments/assets/694d2db3-6aeb-4d3c-84b6-47f89b72125a" width="600" height="600">

###### ↳ [https://quantum.cloud.ibm.com/](https://quantum.cloud.ibm.com/) Sign in with the account created on the academic.ibm.com
<br>


<img src="https://github.com/user-attachments/assets/b58fc875-6bf7-47a7-913e-f381d66252fd" width="600" height="600">

###### ↳ Create an IBM Cloud account
<br>


<img src="https://github.com/user-attachments/assets/4a8cc10d-bdc1-4773-8b39-9a4b094e8b19" width="600" height="600">

###### ↳ Register with a code
<br>


<img src="https://github.com/user-attachments/assets/923240b9-ac67-4661-93e3-be54073c71dc" width="600" height="600">

###### ↳ Enter the code copied from academic.ibm.com
<br>


<img src="https://github.com/user-attachments/assets/bf2e29dd-9537-4ce1-8c91-60f4967fbe8d" width="600" height="600">

###### ↳ [https://quantum.ibm.com/](https://quantum.ibm.com/) Sign in and fill in your information
<br>
<br>


</details>


<details>
<summary><b><ins>Get API(Channel: ibm_cloud)</ins></b></summary>
<br>

<img src="https://github.com/user-attachments/assets/3042a7f0-2d71-4b23-b73d-a6adef75cb15" width="600" height="600">

###### ↳ [https://quantum.cloud.ibm.com/](https://quantum.cloud.ibm.com/) Sign in and Create API key
<br>


<img src="https://github.com/user-attachments/assets/bc50996a-7f53-4aa2-9897-38bbf4548c2f" width="600" height="600">

###### ↳ Create
<br>


<img src="https://github.com/user-attachments/assets/7ef22ed5-b50b-40ec-b80f-a2a9bc863aac" width="600" height="600">

###### ↳ Copy the API key or download .json file
<br>


<img src="https://github.com/user-attachments/assets/aaa4a8ae-3584-48db-b02b-4b12bcf8d11b" width="600" height="600">

###### ↳ Check the API keys
<br>
<br>


</details>


<details>
<summary><b><ins>Get Instance(Channel: ibm_cloud)</ins></b></summary>
<br>

<img src="https://github.com/user-attachments/assets/84e09334-65c5-4188-878b-dabdee97aa5c" width="600" height="600">

###### ↳ [https://quantum.cloud.ibm.com/](https://quantum.cloud.ibm.com/) Create an instance
<br>


<img src="https://github.com/user-attachments/assets/7e5ede05-020a-4dcc-9cd5-d85153568cec" width="600" height="600">

###### ↳ Create
<br>


<img src="https://github.com/user-attachments/assets/30417da9-66af-45ca-b770-ccaf6d13c28f" width="600" height="600">

###### ↳ Click
<br>


<img src="https://github.com/user-attachments/assets/4ffb28f3-2ef6-4a2f-b195-6a09d39f7aed" width="600" height="600">

###### ↳ Copy the instance CRN
<br>
<br>


</details>


<details>
<summary><b><ins>Get API(Channel: ibm_quantum: valid until 1 July 2025)</ins></b></summary>
<br>

<img src="https://github.com/user-attachments/assets/abecb504-36c4-481a-bf80-70a48be87007" width="600" height="600">

###### ↳ Copy the API Token
<br>
<br>


</details>
<br>


## Ex01

### Simulator

A classical(non-quantum) program that mimics how a quantum computer would behave. It runs on a regular CPU(sometimes GPU) and emulates quantum behavior using algorithms.<br>
- Fast for small circuites(under 25 qubits)
- Free and available locally
- Good for development, testing, debugging
- No queue or hardware noise

- Doesn't reflect real quantum hardware limitations
- Performance drops quickly with more qubits
<br>

### Real Quantum Computer

Uses physical quantum bits(qubits) made from superconducting circuits, trapped ions, or other quantum technologies.<br>
- Runs on actual quantum hardware
- Ideal for testing how algorithm handles quantum noise, decoherence, device errors
- required for real-world quantum applications

- Limited access
- Queue times can be long
<br>

### IBM Quantum channels: ibm_quantum, ibm_cloud

- ibm_quantum
	- Legacy access through the original IBM Quantum Experience.
	- Requires only a token.
	- Now deprecated, will be retired July 1, 2025.

- ibm_cloud
	- Modern access through IBM Cloud.
	- Requires a token and cloud instance CRN.
	- Provides access to newer features like Qiskit Runtime, sessions, and fine-grained backend control.
<br>

### IBMQ.get_provider()

Finding and connecting to a quantum computer or simulator on IBM's network.(old)<br>
- Old Qiskit system(pre-2023).
- `IBMQ`: a global object that manages connections to IBM Quantum computers.
- `IBMQ.get_provider`: gets access to provider(simulators or quantum devices).
- Qiskit version < 0.39, part of `qiskit-ibmq-provider` package.

```
from qiskit import IBMQ

IBMQ.enable_account(API_TOKEN)

provider = IBMQ.get_provider(hub='ibm-q')
backend = provider.get_backend('ibmq_quito')

```
<br>

### QiskitRuntimeService()

New way to Connecting to a connect dto device and runtime programs, faster and better.<br>
- Newer way(post-2023) to connect to IBM quantum devices.
- `QiskitRuntimeService` manages access to both hardware and runtime programs.
- Qiskit version 0.39+, part of `qiskit-ibm-runtime` package.

```
from qiskit_ibm_runtime import QiskitRuntimeService

# ibm_quantum
service = QiskitRuntimeService(
    channel="ibm_quantum",
    token=API_TOKEN
)

# ibm_cloud
service = QiskitRuntimeService(
    channel="ibm_cloud",
    token=API_TOKEN,
    instance=INSTANCE_CRN
)

backend = service.backend("ibmq_quito")

```
<br>

### Simulators don't show up

IBM has removed public access to most simulators on both channels.<br>
- on ibm_quantum, simulators were phased out and may no longer appear.
- on ibm_cloud, simulator access is controlled by your cloud instance.
<br>

For development, use local simulators.<br>

```
from qiskit_aer import Aer

simulator = Aer.get_backend("aer_simulator")

```
<br>
<br>

## Ex02

### Classical bit and Quantum bit

- Classical bit
	- It can be either 0 or 1.
	- There is no in-between.

- Quantum bit(qubit)
	- It is not limited to 0 or 1, can be in a superposition of both.

```
|ψ⟩ = α|0⟩ + β|1⟩,
The constraint: |α|² + |β|² = 1
(normalization: it ensures total probablity is 1)

|0⟩: qubit is in the 0 state
|1⟩: qubit is in the 1 state
α, β: complex numbers called amplitudes.

```
- |0⟩ and |1⟩
	- Basis vectors(column vectors) of 2d complex vector space called a Hilbert space.
	- Any valid qubit state is a linear combination of them.
<br>

### Superposition

- Superposition: the quantum generalization of being in multiple states at once.
- In physics, it is rooted in linear combinations of eigenstates(like |0⟩ + |1⟩).
- It does not mean it is in 0 or 1, it means that it has the potential to become either, and the amplitudes(α, β) determine how likely each outcome is. 
- Superposition comes from The Hadamard Gate.
<br>

### Measurement

- When qubit is measured, it collapses into either |0⟩ or |1⟩, with probablity P(0) = |α|², P(1) = |β|².
- Superposition can be never directly observed, observer infers it by running the same experiment many times and analyzing the probablities.
<br>

### Hadamard Gate
- Hadamard gate: A single-qubit quantum gate that puts a qubit into a superposition.
- It is defiend by:
```
     1  ┏       ┓
H = ————┃ 1   1 ┃
    √(2)┃ 1  -1 ┃
	┗       ┛
```
- When H is applied by |0⟩:
```
        1  ┏       ┓ ┏   ┓    1  ┏   ┓    1
H|0⟩ = ————┃ 1   1 ┃⋅┃ 1 ┃ = ————┃ 1 ┃ = ————|0⟩ + |1⟩
       √(2)┃ 1  -1 ┃ ┃ 0 ┃   √(2)┃ 1 ┃	 √(2)
	   ┗       ┛ ┗   ┛	 ┗   ┛
```
<br>

### Bra-Ket Formalism(Dirac natoation)

- Ket: |ψ⟩
	- A column vector.
	- Example: 
	```
	      ┏   ┓        ┏   ┓
	|0⟩ = ┃ 1 ┃  |1⟩ = ┃ 0 ┃
	      ┃ 0 ┃,       ┃ 1 ┃
	      ┗   ┛        ┗   ┛
	```
	- A general state:
	```
			     ┏   ┓     ┏   ┓   ┏   ┓
	|ψ⟩ = α|0⟩ + β|1⟩ = α┃ 1 ┃ + β ┃ 0 ┃ = ┃ α ┃
			     ┃ 0 ┃     ┃ 1 ┃   ┃ β ┃
			     ┗   ┛     ┗   ┛   ┗   ┛
	(|α|² + |β|² = 1)
	```
<br>

- Bra: ⟨ψ| = (|ψ⟩)†
	- The dual(transpose + complex conjugate) of a ket.
	- A row vector.
	- Useful for computing inner products.
	- If:
	```
	      ┏   ┓		     ┏        ┓
	|ψ⟩ = ┃ α ┃ → ⟨ψ| = (|ψ⟩)† = ┃ α*  β* ┃
	      ┃ β ┃		     ┗        ┛
	      ┗   ┛
	(* means complex conjugate)
	```
<br>

- Bra-Ket(inner product): ⟨ϕ|ψ⟩
	- A complex number.
	- Physically interpreted as the overlap between two states.
	- If:
	```
	      ┏   ┓        ┏   ┓
	|ϕ⟩ = ┃ a ┃  |ψ⟩ = ┃ x ┃
	      ┃ b ┃,       ┃ y ┃
	      ┗   ┛        ┗   ┛
	```
	- Then:
	```
		┏        ┓ ┏   ┓		     
	⟨ϕ|ψ⟩ = ┃ a*  b* ┃⋅┃ x ┃ = a*x + b*y
		┗        ┛ ┃ y ┃		     
			   ┗   ┛
	```
	- Example:
	```
		┏    ┓† ┏   ┓   ┏      ┓ ┏   ┓
	⟨0|0⟩ = ┃ 1* ┃ ⋅┃ 1 ┃ = ┃ 1  0 ┃⋅┃ 1 ┃ = 1
		┃ 0* ┃  ┃ 0 ┃   ┗      ┛ ┃ 0 ┃
		┗    ┛  ┗   ┛		 ┗   ┛
	∴ the probability that |0⟩ is in state |0⟩ is 1.

		┏    ┓† ┏   ┓   ┏      ┓ ┏   ┓
	⟨0|1⟩ = ┃ 1* ┃ ⋅┃ 0 ┃ = ┃ 1  0 ┃⋅┃ 0 ┃ = 0
		┃ 0* ┃  ┃ 1 ┃   ┗      ┛ ┃ 1 ┃
		┗    ┛  ┗   ┛		 ┗   ┛
	∴ the probability that |0⟩ is in state |1⟩ is 0,
	  no overalp between |0⟩ and |1⟩.
	```
	- Inner product of superposition states:
	```
	Let:
	       1		1  ┏   ┓
	|ψ⟩ = ————(|0⟩ + |1⟩)= ————┃ 1 ┃
	      √(2)	       √(2)┃ 1 ┃
				   ┗   ┛
	Then:
		  1  ┏      ┓	 1  ┏   ┓
	⟨ψ|ψ⟩ = (————┃ 1  1 ┃)⋅(————┃ 1 ┃) = 1
		 √(2)┗      ┛	√(2)┃ 1 ┃
				    ┗   ┛
	```
<br>

- Outer product: |ψ⟩⟨ψ|
	- A matrix.
	- Physically the matrix is a projector onto the state |ψ⟩.
	- If you multiply any state |φ⟩ by |ψ⟩⟨ψ|, you project it onto |ψ⟩(in short, ∣ψ⟩⟨ψ∣∣ϕ⟩=(⟨ψ∣ϕ⟩)∣ψ⟩): it filters |φ⟩ through |ψ⟩ and returns vector along |ψ⟩.
	- Example:
	```
	Let:
	       1		 1  ┏   ┓
	∣ψ⟩ = ————(|0⟩ + |1⟩) = ————┃ 1 ┃
	      √(2)		√(2)┃ 1 ┃
				    ┗   ┛
	Then the bra is:
	       1  ┏    ┓†   1  ┏      ┓
	⟨ψ∣ = ————┃ 1* ┃ = ————┃ 1  1 ┃
	      √(2)┃ 1* ┃   √(2)┗      ┛
		  ┗    ┛
	So the outer product is:
		   1  ┏   ┓    1  ┏      ┓
	|ψ⟩⟨ψ| = (————┃ 1 ┃)⊗(————┃ 1  1 ┃)
		  √(2)┃ 1 ┃   √(2)┗      ┛
		      ┗   ┛
		  1┏   ┓ ┏      ┓   1┏      ┓
		= —┃ 1 ┃⊗┃ 1  1 ┃ = —┃ 1  1 ┃
		  2┃ 1 ┃ ┗      ┛   2┃ 1  1 ┃
		   ┗   ┛	     ┗      ┛
	```
	- In quantum computing, |0⟩⟨0|, |1⟩⟨1|, or |ψ⟩⟨ψ| appear in measurement operators, quantum state preparation, density matrices(for mixed states).
	```
	Projector for |0⟩:
		 ┏   ┓ ┏      ┓	  ┏      ┓
	∣0⟩⟨0∣ = ┃ 1 ┃⊗┃ 1  0 ┃ = ┃ 1  0 ┃
		 ┃ 0 ┃ ┗      ┛	  ┃ 0  0 ┃
		 ┗   ┛		  ┗      ┛
	Projector for |1⟩:
		 ┏   ┓ ┏      ┓	  ┏      ┓
	∣1⟩⟨1∣ = ┃ 0 ┃⊗┃ 0  1 ┃ = ┃ 0  0 ┃
		 ┃ 1 ┃ ┗      ┛	  ┃ 0  1 ┃
		 ┗   ┛		  ┗      ┛
	```
	- If a quantum state is |ψ⟩, the density matrix is:
	```
	ρ = ∣ψ⟩⟨ψ∣
	```
	- Because ρ contains all measurable information about a quantum state.

### Projection: Measuring a quantum state

- Projection:
	- When we measure a quantum state, we don't just read its value, we project it onto a basis state like |0⟩ or |1⟩.
	- The probability that the qubit is |0⟩ = |⟨0|ψ⟩|², which is a projection of the quantum state |ψ⟩ onto |0⟩.

- Why projection?
	- Quantum measurement collapses the state into one of the basis vectors(|0⟩ or |1⟩).
	- Projection squared tells us how likely it is that the state lands on the basis vector.
	- In linear algebra, projection is how much of one vector lies along another.

- Example with code

```
qc = QuantumCircuit(1, 1)
qc.h(0)
qc.measure(0, 0)
```

The Hadamard gate gives:
```
       1
|ψ⟩ = ————(|0⟩ + |1⟩)
      √(2)
```
The probability of getting 0 on measurement P(0) is:
```
			 1			 1	     1
P(0) = |⟨0|ψ⟩|² = | ⟨0|(————(|0⟩ + |1⟩)) |² = | ————⟨0|0⟩ + ————⟨0|1⟩ |²
			√(2)			√(2)	    √(2)
	  1	   1		1	1
     = | ————*1 + ————*0 |² = |————|² = — = 0.5
         √(2)	  √(2)	       √(2)	2
```
∴ the probability that |0⟩ in state |ψ⟩ is 0.5
Which means when you measure the qubit, you get 0 with 50% probability, 1 50% probability.
<br>
