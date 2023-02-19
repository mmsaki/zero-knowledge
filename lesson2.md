# Lesson 2

This stuff is hard. Don't feel bad if you don't get it.

- Fully Homomorphic encryption

Plonomials in ZKPs

If a prover claims to know some polynomial (no matter how large its degree is) that the verifier also knows, they can follow a simple protocol to verify the statement:

- verifier chooses a random value for x and evaluates his polynomial locally
- Verifier gives x to the prover and asks to evaluate the polynimial in question
- prover evaluates her polynomial at x and the result to the verifier
- Verifier checks if the local result is equal to the prover's result, and if so then the statement is proven with a high confidence

Why is degree important

in general, there is a rule that if a polynomial is zeor accross some set

S = x1, x2 ... sn then it can be expressed as

P(x) = Z(x) * H(s), where Z(x) = (x-x1) • (x-x2) •...•(x-xn) and H(x) is also a polynomial.

In other words, any polynomial that equals zero accross set is a (polynomial) mulitiple of the (lowest-degree) polynomial that equals zero across that same set.

## Homomorphic Hiding

Taken from Zcash explanation

if E(x) is a function with the following properties.

- Given E(x) it is hard to find x
- Different inputs lead to different outputs so if x≠yE(x) ≠ E(y)
- We can compute E(x+y) given E(x) and E(y)

The group Z<sub>p</sub> with operations addition and multiplication allows this.

Here's a toy example of why Homomorphic Hiding is useful for Zero-Knowledge proofs.

Suppoese Alice wants to prove to bob she knows numbers x,y such taht x+y = 7

1. Alice sends E(x) and E(y) to Bob.
2. Bob computes E(x+y) from these values (which he is to do since E is an HH).
3. Bob also computes E(7), and now checks whether E(x+y) = E(7). He accepts Alice's proof pnly if equality holds.

As different inputs are mapped by E to different hidings. Bob indedd accepts the proof oonly if Alice sent hidings of x,y such that x + y = 7. On the other hand, Bob does not learn x and y he just has acess to their hidings.

## ZoKrates - xkSNARKs on Ethereum
