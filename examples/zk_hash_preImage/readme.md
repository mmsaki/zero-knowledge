# Example: Proving knowledge of a hash preimage

We'll implement an operations that's very common in blockchain use cases: proving knowledge of a preimage for a given hash digest. In particular, we'll show how Zokrates and the Ethereum blockchain can be used to allow a prover, Peggy, to demonstrate beyond any doubt to a verifier, Victor, that she knows a hash preimage for a digest chosen by Victor, without revealing what that preimage is.

## Prerequisites

Try and follow instructions on the [square root problem](../square_root/) for general knowledge on how zokrates works.

## Step 1: Computing a hash using ZoKrates

First, we create a new file named `hashexample.zok` with the following content:

```zokrates
import "hashes/sha256/512bitPacked" as sha256packed;

def main(private field a, private field b, private field c, private field d) -> field[2] {
  field[2] hash = sha256packed([a,b,c,d]);
  return hash;
}
```

`sha256packed` is a SHA256 implementation that is optimized for the use in the ZoKrates DSL. We want to pass 512 bits of input to SHA256. However, a field value can only hold 254 bits due to the size of the underlying prime field we are using. As a consequence, we use four field elements, each one encoding 128 bits, to represent our input. The four elements are then concatenated in ZoKrates and passed to SHA256. Given that the resulting hash is 256 bit long, we split it in two and return each value as a 128 bit number.

In case you are interested in an example that is fully compliant with existing SHA256 implementations in Python or Solidity, you can have a look at this [blog](https://blog.decentriq.com/proving-hash-pre-image-zksnarks-zokrates/) post.

First, we compile the program into an arithmetic circuit:

```bash
zokrates compile -i hashexample.zok
```

Next, we can create a witness file using the following command:

```bash
zokrates compute-witness -a 0 0 0 5
```

The `-a` flag is used to pass in our arguments.

We can check the witness file for the return values:

```bash
grep '~out' witness
```

We get the output:

```bash
~out_1 65303172752238645975888084098459749904
~out_0 263561599766550617289250058199814760685
```

## Step 2: Prove knowledge of pre-image

For now, we have seen that we can compute a hash using ZoKrates.

Let's recall our goal: Peggy wants to prove that she know a preimage for a digest chosen by Victor, without revealing what the preimage is. Let's assume that Victor chooses the digest to be the one we found in our example above.

To make this work, the two parties have to follow their roles in the protocol:

1. First, Victor has to specify what hash he is interested in. Therefore, we have to adjust the zkSNARK circuit, compiled by ZoKrates, such that in addition to computing the digest, it also validates it against the digest of interest, provided by Victor. This leads to the following update for `hashexample.zok`.

```zokrates
import "hashes/sha256/512bitPacked" as sha256packed;

def main(private a, private field b, private field c, private field d) {
  field[2] hash = sha256packed([a,b,c,d]);
  assert(hash[1] == 65303172752238645975888084098459749904);
  assert(hash[0] == 263561599766550617289250058199814760685);
  return;
}
```

Note that we now compare the result fo `sha256packed` with hard-coded correct solution defined by Victor. These lines we added are assertions where the verifier will not accept a proof where these constraints were not satisfied. Clearly, this program only returns 1 if all of the computed bits are equal.

2. So, after writing the program. Victor is now ready to compile the code.

```bash
zokrates compile -i hashexample.zok
```

3. Based on that Victor can run the setup phase and export a verifier smart contract.

```bash
zokrates setup && zokrates export-verifier
```

4. The `setup` creates a `verification.key` and a `proving.key` file.
   - Victor gives the proving key to Peggy. `mkdir peggy && cp victor/proving.key peggy`
   - Victor deploys the `verifier.sol` contract created by `export-verifier`.

5. Peggy provided the correct pre-image as an argument to the program.
   - `zokrates compute-witness -a 0 0 0 5`

6. Finally Peggy can run the command to construct the proof.
   - `zokrates generate-proof`

As the inputs were declared as private in the program, they do not appear in the proof, thanks to the zero-knowledge property of the protocol.

Zokrates creates a file for Peggy, `proof.json`, consisting of the three elliptic curve points that make up the zkSNARKs proof. The `verifyTx` function in the smart contract deployed by Victor accepts these three values, along with an array of public inputs. The array of public inputs consists of:

- Any public inputs to the main function, declared without the private keyword
- the return values of the ZoKrates function.

In this example we're considering, all inputs are private and there is a single return value of 1, hence Peggy has to define her public input array as follows: `[1]`.

Peggy can then submit he proof by calling `verifyTx`.

Victor monitor the verification smart contract for the return value of Peggy's transaction. As soon as he observes a transaction from Peggy's public address with a `true` return value, he can be sure that she has a valid pre-image for the hash he set in the smart contract.

## Conclusion

Remember that in this example only two parties were involved. This special case makes it easy to deal with the trust assumptions of zkSNARKs: only Victor was interested in verifying the claim by Peggy, hence he can trust his execution of the setup phase.

In general, multiple parties may be interested in verifying the correctness of Peggy's statement. For example, in the zero-knowledge based cryptocurrency ZCash, each node needs to be able to validate the correctness of transactions. In order to generalize the setup phase to these multi-party use-cases a tricky process, commonly referred to as "trusted setup" or "ceremony" needs to be conducted.

ZoKrates would welcome ideas to add support for such ceremonies!
