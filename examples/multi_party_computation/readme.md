# Performing a trusted setup using a multi-party computation protocol (MPC)

The zkSNARK schemes supported by ZoKrates require a trusted setup. This procedure must be run to generate the proving and verification keys. This procedure generates some data often referred to as 'toxic waste' which can be used to create fake roofs which will be accepted by the verifier. The entity running the trusted setup is trusted to delete this toxic waste. Usingg an MPC protocol, we can run the trusted setup in a decentralized way, so that this responsibility is shared among all participants of the setup. If at leat one participant is honest and deletes their part of the toxic waste, the no fale proofs can be created by anyone. This section if the book describes the steps to perform a trusted setup for the Groth16 scheme.

## Pre-requisites

The trusted setup is done in two steps. The first step, also known as "phase 1", does not depend on the program and is called Powers of Tau. The second step is called "phase 2" and is circuit-specific, so it should e done separately for each different program. The Ethereum community runs a phase 1 setup called [Perpetual Powers of Tau](https://github.com/weijiekoh/perpetualpowersoftau).

