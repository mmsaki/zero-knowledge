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

Set of Real Numbers denoted by R. {2, -4, 613, π, √2,..}

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

**Closure:** For all a, b in set G, the result of operation a•b, is also in G

**Associativity:** for all a, b and c in set G, (a•b)•c 

**Identity element:** there exists an element e in G such that every element a in G, the equation e•a = a•e=a holds. 

**Inverse element:** for each a in G, there exists an element b in G, denoted a<sup>-1</sup> (or -a if the operation is "+"), such that a•b = b•a = e, where e is the identity element

### Sub Groups

if a subset of the elements in a group also satisfies the group properties, then that is a subgroup of the original group


### Cyclic groups and generators

A finite group can be cyclic. That means it has a generator element. If you start at any point and apply a group operation with the generator as argument a certain number of times, you can go around the whole group and end in the same place.

### Finding and inverse

a<sup>-1</sup> ≡ a <sup>p-2</sup> (modp)

Let p = 7 and a = 2




- Homework 1

## Lesson 2: ZKP Theory / Zokrates

- Homework 2


