## Compiling a circuit

1. Create `circuit.zok` file inside `coordinator/` directory with the following code:

```zokrates
def main(private field a, private field b) -> {
  return a * b;
}
```

2. Compile the program:

```bash
cd coordinator
```

```bash
zokrates compile -i circuit.zok -o circuit --curve bls12_381
```

3. Grab a file which contains the parameters for our circuit with depth 2 and save it in `coordinator/`:

```bash
wget https://download.z.cash/downloads/powersoftau/phase1radix2m2
```

4. Initialize a phase 2 ceremony in `coordinator/`:

```bash
zokrates mpc init -i circuit -o mpc.params -r ./phase1radix2m2
```

5. We shall conduct the ceremony between 3 participants: Alice, Bob and Charlie, who will run the contributions in sequential order, managed by a coordinator (us). We send `mpc.params` to `alice/`.

```bash
mkdir ../alice && mv mpc.params ../alice && cd ../alice
```

5. Alice must give some randomness to the contribution, which is done by the -e flag on the following command:

```bash
zokrates mpc contribute -i mpc.params -o alice.params -e "alice 1" --curve bls12_381
```

Examples of entropy sources:

- `/dev/urandom` from one or more devices
- The most recent block hash
- Randomly mashing keys on the keyboard

6. The output of alice `alice.params` is sent to `bob/`, using `mkdir ../bob && mv alice.params ../bob && cd ../bob`,

```bash
zokrates mpc contribute -i alice.params -o bob.params -e "bob 2" --curve bls12_381
```

7. The output of bob `bob.params` is sent to `charlie/`, using `mkdir ../charlie && mv bob.params ../charlie && cd ../charlie`, and charlie wil run the following command:

```bash
zokrates mpc contribute -i bob.params -o charlie.params -e "charlie 3" --curve bls12_381
```

8. To finalize the ceremony, we (coordinator?)`mv charlie.params ../coordinator && cd ../coordinator`,, can apply a random beacon to get the final parameters:

```bash
zokrates mpc beacon -i charlie.params -o final.params -h b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9 -n 10 --curve bls12_381
```

The random beacon is the 2^n iteration of SHA256 over the hash evaluated on some high entropy and publicly available data. Possible sources of data could be:

- The closing value of the stock market on a certain date
- The output of a selected set of national lotteries
- The value of a block at a particular height in one or more blockchains
- [League of Entropy](https://www.cloudflare.com/leagueofentropy/) (drand)

9. At any point in the ceremony we can verify contributions by running the following command:

```bash
zokrates mpc verify -i final.params -c circuit -r ./phase1radix2m2
```

10. Exporting keys. Once the ceremony is finalized, we can export the keys and use them to generate proofs and verify them:

```bash
zokrates mpc export -i final.params
```

Use keys to generate proofs and verify.

```bash
zokrates compute-witness -i circuit -a 123456789 987654321 --verbose
```

Generate proof

```bash
zokrates generate-proof -i circuit -b bellman
```

Verify proof

```bash
zokrates verify -b bellman
```

## Conclusion

The secure generation of parameters for zk-SNARKs is a crucial step in the trustworthiness of the resulting proof system. The security of the ceremony relies entirely on the fact that at least one participant needs to securely delete their "toxic waste" for the resulting parameters to be generated honestly. Opening the ceremony to a large number of participants reduces the probability that the resulting parameters are dishonest. Once the ceremony is finalized, we can generate a verifier smart contract by using the keys we obtained through the trusted setup ceremony. At this point, we can safely deploy the contract and verify proofs on-chain.
