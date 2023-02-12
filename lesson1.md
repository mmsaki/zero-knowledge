# Zero Knowledge Class

Courtesy of Encode Club Bootcamp.

## Lesson 1

### Overview

Human dignity demands that personal information be hidden from the public e.g medical records, forensic data

But veils of secrecy designed to preserve privacy may also be abused to cover up lies and deceipt by institutions entrusted with data, unjustly harming citizens and eroding trust in central institutions. - Starkware

ZK gives similar vibes to Machine Learning. More and more people just mention ZK as a magic solution that fixes everything with no context of this current limitation. - 0xMisaka

## Intoductory maths

### Numbers

Set of integers is denoted by Z. {...-4,-3,-2,-1,0,1,2,3,4..}

Set of Rational numbers denoted by Q. {..1, 3/2, 2, 22/7,...}

Set of Real Numbers denoted by R. {2, -4, 613, Ï€, âˆš2,..}

Field denoted by F, if they are a finite field or K  for a field of real or complex numbers we also use Z<sub>p</sub><sup>*</sup> to represent a finite field of integers mod prime p

We use finite field for cryptography because they have short exact representations and useful properties

### Modular Arithmetic

n mod k simply means the remainder when n is divided by k

35 mod 3 = 1
15 mod 4 = 3

[See modular arithmentic exercize](https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/what-is-modular-arithmetic)

the remainders shoul be positive

### Group Theory

Simply a group is a set of elements {a, b, c, ...} plus a binary operation

To be concidered a group the combination needs certain properties

1. Closure
2. Associativity
3. Identity element
4. Inverse element

**Closure:** For all a, b in set G, the result of operation aâ€¢b, is also in G

**Associativity:** for all a, b and c in set G, (aâ€¢b)â€¢c

**Identity element:** there exists an element e in G such that every element a in G, the equation eâ€¢a = aâ€¢e=a holds.

**Inverse element:** for each a in G, there exists an element b in G, denoted a<sup>-1</sup> (or -a if the operation is "+"), such that aâ€¢b = bâ€¢a = e, where e is the identity element

### Sub Groups

if a subset of the elements in a group also satisfies the group properties, then that is a subgroup of the original group

### Cyclic groups and generators

A finite group can be cyclic. That means it has a generator element. If you start at any point and apply a group operation with the generator as argument a certain number of times, you can go around the whole group and end in the same place.

### Finding an inverse

fermat's little theorem

a<sup>-1</sup> â‰¡ a <sup>p-2</sup> (modp)

Let p = 7 and a = 2. We can compute the inverse of a as:

a<sup>p-2</sup> = 2<sup>5</sup> = 32 â‰¡ 4 mod 7

Verify: 2 x 4 â‰¡ 1 mod 7

### Equivalence classes

since

6 mod 7 = 6

13 mod 7 = 6

20 mod 7 = 6

6, 13, 20 form equivalence classes

more formally

i + kN | k EZ for some i between 0 and N - 1.

Thus if we are trying to solve the equation

x mod 7 = 6

x could be 6, 13, 20 ....

This gives us the basis for a one way function

### Fields

A field is a set of say integers together with two operations called addition and multiplication.

One example of a field is the Real Numbers under addition and multiplication, another is a ser of integers mod a prime number with addition and multiplication.

The field operations are required to satisfy the following field axioms. In these axioms, a, b and c are arbitrary element s of the field F.

1. Associativity of addition and multiplication: a+(b+c) = (a+b)+c and  aâ€¢(bâ€¢c)=(aâ€¢b)â€¢c

2. Commutativity of addition and multiplication: a+b=b+a and aâ€¢b=bâ€¢a

3. Additive and multiplicative identity. Additve = 0, a + 0 = a, multiplicative = 1, a â€¢ 1 = a

4. Additive inverse: For every a in F, there exists an element in F, denoted -a, called the additive invers of a, such that a + (-a) = 0

5. Multicative inverse: For every a â‰  0 in F, the exists an element in F, denoted by a<sup>-1</sup>, called the multiplicative inverse of a, such that aâ€¢a<sup>-1</sup>=1

6. Distributivity of multiplication over addition: aâ€¢(b+c) = (aâ€¢b)+(aâ€¢c)

### Finite fields and generators

### Proving systems

- Instance variables --> which are public
- Witness variables ---> which are private

- Interactive proofs --> Multiple rounds
- Non-interactive proofs ---> no repeated communications between the prover and the verifier
- Succint  --->
- Non Succint --->
- Proof
- Proof of Knowledge --->
- Argument

- [Homework 1](./homework/homework1.py)
