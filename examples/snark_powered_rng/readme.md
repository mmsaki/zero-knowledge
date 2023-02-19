# Tutorial: A SNARK Powered RNG

If this is your first time using zokrates make sure you have followed instructions on the [square root problem](../square_root/) before proceeding.

## Problem

Alice and bob want to be on the results of a series of coin tosses. To do so, they need to generate a series of random bits. They proceed as follows:

1. Each of them commits a 512 bit value aka a **preimage**. They publish the hash of the preimage.
2. Each time they need a new random value, they reveal on bit from their preimage, and agree that the new random value is the result of XORing these two bits, so that neither of them can contral the output.

Note that we are making the following assumptions:

1. They make sure they do no tuse all 512 bits of their preimage, as the more they reveal, the easier it gets for the other to brute-force their preimage.
2. They need a way to be convinved that the bit the other revealed is indeed part of their preimage.

In this tutorial you learn how to use ZoKrates and zero knowledge proofs to reveal a single bit from the preimage of a hash value.

## Part 1: Commit to a preimage

The first step is for Alice and Bob to each come up with a preimage value and calculate the hash to commit to it. There are many ways to calculate a hash, but here we use ZoKrates.

Create a file `get_hash.zok`:

```zokrates
import "hashes/sha256/512bit" as sha256;

def main(u32[16] hashMe) -> u32[8] {
  u32[8] hash = sha256(hashMe[0...8], hashMe[8...16]);
  return hash;
}
```

Compiler program to a form that is usable for zero knowledge proofs. This command writes the binary to `get_hash`. You can see a rext representation, at `get_hash.ztf` created by the inspect command.

```bash
zokrates compile -i get_hash.zok -o get_hash && zokrates inspect -i get_hash
```

The input to zokrates program is sixteen 32 bit values, each in decimal. Specifiy those values to get a hash. For example, to calculate the hash of `0x00000000000000010000000200000003000000040000000500000006...` use this command:

```bash
zokrates compute-witness --verbose -i get_hash -a 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
```

the result is:

```bash
Computing witness...

Witness: 
["3592665057","2164530888","1223339564","3041196771","2006723467","2963045520","3851824201","3453903005"]

Witness file written to 'witness'
```

## Part 2: Reveal a single bit

The next step is to reveal a single bit.

Use this program, `reveal_bit.zok`:

```zokrates
import "hashes/sha256/512bit" as sha256;
import "utils/casts/u32_to_bits" as u32_to_bits;

def main(private u32[16] preimage, u32 bitnum) -> (u32[8], bool) {
  // convert the preimage to bits
  bool[512] mut preimageBits = [false; 512]
  for u32 i in 0..16 {
    bool[32] val = u32_to_bits(preimage[i]);
    for u32 bit in 0..32 {
      preimageBits[i*32 + bit] = val[bit];
    }
  }
  return (sha256(preimage[0..8], preimage[8..16]), preimageBits[bitNum]);
}
```

Compile and run program:

```bash
# compile program
zokrates compile -i reveal_bit.zok -o reveal_bit

# compute witness
zokrates compute-witness --verbose -i reveal_bit -a 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 510
```

Returns Output:

```bash
Computing witness...

Witness: 
["3592665057","2164530888","1223339564","3041196771","2006723467","2963045520","3851824201","3453903005","1"]

Witness file written to 'witness'
```

## Part 3: Actually using zero knowledge proofs

The `reveal_bit.zok` program reveal a bit from the preimage, but who runs it?

1. If Alice runs the program, she can feed it her secret preimage and receive the correct result. However, when she send the output there is no reason for Bob to trust that she is proving the correct output.
2. If Bob runs the program, he does not have Alice's secret preimage. If Alice discloses he secret preimage, Bob can know the value of all the bits.

Therefore, we need to have Alice run the program and produce the output, bur produce it in such a way Bob will know it is the correct output. This is what zero knowledge proofs grive us.

Set up environment. Create two separate directories, `alice` and `bob`. You will perform the actions of Alice in the alice directory, and the actions of Bob in the `bob` directory.

### Step 1: Bob's setup

Compile `reveal_bit.zok` and create the proving and verification keys.

```bash
cd bob/
zokrates compile -i reveal_bit.zok -o reveal_bit
zokrates setup -i reveal_bit
```

Copy the file proving.key to Alice's directory.

```bash
cp proving.key ../alice && cd ../alice
```

### Step 2: Alice's setup

Alice should compile `reveal_bit.zok` independently to make sure it doesn't disclose information she want to keep secret.

```bash
zokrates compile -i reveal_bit.zok -o reveal_bit
```

Next, Alice creates the `witness` file with the values of all the parameters in the program. Using this `witness`, Bob's `proving.key`, and the compiled program she generates the actual proof.

```bash
zokrates compute-witness --verbose -i reveal_bit -a 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 510
zokrates generate-proof -i reveal_bit
```

The proof is created in the file `proof.json`. Copy this file to Bob's directory.

```bash
cp proof.json ../bob && cd ../bob
```

### Step 4: Bob accepts the prrof

Finally, Bob verifies the proof:

```bash
zokrates verify
```

Returns output:

```bash
Performing verification...
PASSED
```

### Step 5: Connecting to Ethereum

So far, Alice and Bob calculated the random bit between themselves. However, it is often useful to have the values pushed on the blockchain. To do this, Bob creates a solidity program:

```bash
zokrates export-verifier
```

The solidity program is called `verifier.sol`.

Here are the instructions to use this program when using Truffle and Ganache. We'll assume they are already installed, and the Ganache blockchain is running.

1. Create a new project with `truffle init` and copy `verifier.sol` to the subdirectory `contracts`.
   - `cd .. && mkdir deploy && cd deploy && truffle init && cp ../bob/verifier.sol contracts/`

2. Edit `truffle-config.js`. Change `module.exports.compilers.solc` version to the version required by `verifier.sol`. Uncomment `modules.exports.networks.development`.

3. Compile contract
   - `truffle compile`
  
4. Start the truffle console. The rest of this procedure is done in Javascript prompt inside that console.
   - `contract = await Verifier.new()`
   - `proof = JSON.parse(fs.readFileSync("../bob/proof.json"))`
   - `await contract.verifyTx([proof.proof.a, proof.proof.b, proof.proof.c], proof.inputs)`
   - Should return `true`

5. Pretend to cheat.

- `cheat = [...proof.inputs]`
- `cheat[cheat.length-1] = cheat[cheat.length-1].replace(/[01]$/, cheat[cheat.length-1][65] == '1' ? '0': '1')`
- `await contract.verifyTx([proof.proof.a, proof.proof.b, proof.proof.c], cheat)`

## Conclusion

At this point you should be able to create zero knowledge proofs and verify them from the commnand line. You should also be a ble to publish a veifier to a blockchain, generate proofs, and submit them using javascript.
