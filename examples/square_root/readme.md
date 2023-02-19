# Hello Zokrates

First create `hello_zokrates.zok` and impletment your program. In this example, we will prove knowledge of the square root a of a number b:

```zokrates
def main(private field a, field b) {
  assert(a * a == b);
  return;  
}
```

- Keyword `field` is basic type, which is an element of a given prime field
- Keywork `private` siganls we do not want to reveal this input, but still prove that we know its value

Install zokrates:

```bash
# install zokrates
curl -LSfs get.zokrat.es | sh

# restart terminal or run
export PATH=$PATH:~/.zokrates/bin
```

Then run the different phases of the protocol:

```bash
# compile program
zokrates compile -i square_root.zok

# perform setup
zokrates setup

# execute the program
zokrates compute-witness -a 337 113569

# generate a proof of computation
zokrates generate-proof

# export a solidity verifier
zokrates export-verifier

# or verify natively
zokrates verify
```

You can prov that you know the square root a=337 of b=113569 without revealing the value.
