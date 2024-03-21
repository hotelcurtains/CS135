# Intro
- no late homework. you will be killed.
- two lowest labs, reading, and writing homework assignments get dropped at the end of semester.
- no formula sheets on exams.
- mandatory attendance (5% of grade).
- exams are 50% total of final grade.
- coding is the easiest part -- actually designing what you're coding is the hard part

# Scheme / DrRacket
- DrRacket seems to work like IDLE
- everything is either an atom or a list
- he uses language Pretty Big, idk what difference it makes
## Atoms (primitive data types)
- integers
- real numbers (0.73, 3.17E+10)
- rationals (7/8, 11/3, -12/7)
- functions are done as such: `(+ 7/8 13/17)`
  - NOT like you want them to do it (`7/8 + 13/17`)
- symbols (x, y, x+y?, bad!)
  - names for data items and variables
  - you can actually use special symbols now
  - e.g.:
    ```scheme
    > (define x+y? 7)
    > x+y?
    7
    > x+y-
    x+y-: undefined;
    cannot reference an identifier before its definition
    > (define x+y- 8)
    > x+y-
    8
    ```
- booleans (#t, #f)
- strings ("alligator", "hello world!")
- characters (#\a, #\b)

## Built-in Operators
- +, -, *, / , abs, max, min
- usually work for >=2 operands
    ```scheme 
    > (+ 1 2 3 4 5 6 7 8 9 10)
    55
    > (* 1 2 3 4 5 6 7 8 9 10)
    3628800
    ```
- relational operators: `<` `>` `<=` `>=`
    ```scheme
    > (< 8 7)
    #f
    ```
    ```scheme
    > (= 8 (* 4 2))
    #t
    ```
- relational operators for more complex data types: `eq?` `eqv?` `equal?`
- logical operators `and` `or`  `not`
    ```scheme
    > (and (= 7 7) (< 8 7))
    #f
    > (or(= 7 7) (< 8 7))
    #t
    ```
## Built-in Predicates
- a function that returns a boolean value
- `number?` `integer?` `pair?` `boolean?` `string?`
    ```scheme
    > (number? 7)
    #t
    > (number? 7/12)
    #t
    > 
    > (number? "hi")
    #f
    ```

## Applying Functions
- `(function arg1 arg2 arg3 ... argN)`

## The List Data Type
- a sequence of objects within parentheses
- the interpreter always expects the first item to be a function
    ```scheme
    > (1 2 3 4)
    application: not a procedure;
    expected a procedure that can be applied to arguments
    given: 1
    > `(1 2 3)
    (1 2 3)
    > (quote (1 2 3))
    (1 2 3)
    > (define x (1 2 3))
    application: not a procedure;
    expected a procedure that can be applied to arguments
    given: 1
    > (define x `(1 2 3))
    > x
    (1 2 3)
    ```
- `cons` returns a given list with something prepended to it
- `car` returns the first item in the list
- `cdr` returns everything except he first item in it
- `length`
- `pair?` returns true if the list *is not* empty
- `null?` returns true if the list *is* empty

## Rules for Expression Evaluation
- numbers, strings, literals, all evaluate to themselves
- symbols are interpreted as variables, so they interpret to the value they represent
- lists:
    1. make sure the first element is a function (otherwise throws error)
    2. apply the function to everything in the list
    3. return the result
- a list of data interprets as itself
  - remember to use (quote 1 2 3) or `(1 2 3)

## Defining new functions
`(define (function-name param1 param2 ...) expr)`
we will implement
- arithmetic average `(x+y)/2`
- geometric average `sqrt(x*y)`
- harmonic average `2/((1/x)+(1/y))`
```scheme
(define (a-avg x y) (* 1/2 (+ x y)))
(define (g-avg x y) (sqrt (* x y)))
(define (h-avg x y) (/ 2 (+ (/ 1 x) (/ 1 y))))
```
```scheme
> (a-avg 20 30)
25
> (g-avg 20 30)
24.49489742783178
> (h-avg 20 30)
24
```

## Equality operators
```scheme
(= n m) ; checks whether n and m are equal in value
(eq? n m) ; identity operator - checks if n and m point to the same place in memory
          ; works for literals
(eqv? n m) ; checks if n and m are numbers --
           ; if so it returns (= n m), otherwise returns (eq? n m)
(equal? n m) ; checks if n and m form structures with the same components -- 
             ; i.e. are lists whose corresponding elements are equal.
```
```scheme
> (define x 2)
> (define y 2)
> (eq? x y)
#t
```
you can do this because 2 is stored in the same memory location no matter what variable is pointing to it

```scheme
> (define x `(2 3))
> x
(2 3)
> (define y `(2 3))
> y
(2 3)
> (eq? x y)
#f
> (equal? x y)
#t
```
the lists point to different memory locations, but their elements are equal.

## Conditionals
```scheme
(if (condition) 
  "runs if true" 
  "runs if false"
)
(cond 
  [(condition1) "1 true"] 
  [(condition2) "2 true"] 
  [else "runs for else"]
)
```
the basics:
```scheme
> (if (< 1 2) "less" "more")
"less"
> (if (< 3 2) "less" "more")
"more"
> (define x 6)
> (cond [(eq? x 1) "its 1"] [(eq? x 2) "its 2"] [else "something else"])
"something else"
> (define x 1)
> (cond [(eq? x 1) "its 1"] [(eq? x 2) "its 2"] [else "something else"])
"its 1"
> (define x 2)
> (cond [(eq? x 1) "its 1"] [(eq? x 2) "its 2"] [else "something else"])
"its 2"
```


let's try to implement a function like python's `filter()` recursively:
```scheme
(define (apply-pred list pred)
  (cond 
    [(null? list)
      `()]
    [(pred (car list))
      (cons (car list) (apply-pred (cdr list) pred))]
    [else
      (apply-pred (cdr list) pred)]))
```
- we're using `cond` because there are 3 possible branches -- the list is empty, the current item is caught by the filter, and the current item is not caught by the filter.

# Logic
- Logic is a study of arguments
- Arguments are a sequence of statements whose purpose is to establish the truth of an assertion.
- those statements are *premises*, except for the last one which is a *conclusion*
- a proposition will be true or false always
  - "It is raining" is a valid proposition
  - "What time is it?" is not a T/F statement therefore it's not a proposition
- two boolean formulas are considered equivalent if they have the same formulas
  - implies that their truth tables are the same

# Compound Propositions
- The conjunction symbol ∧ is AND.

![conjunction truth table](image.png)

- The disjunction symbol ∨ is inclusive OR.

![Alt text](image-1.png)

- XOR looks the same ⊕.
  - XOR and OR are nearly the same except T XOR T = F whereas T OR T = T.
- negation symbol NOT ¬ toggles its input.


- when filling in a logic table
  - amount of rows = 2^(amt of variables)
  - just variable rows:
  - rightmost row alternates TFTF...
  - then TTFF
  - then TTTTFFFF
  - etc. (keep doubling the amount of T/F)
  - i think of it as binary counting but who cares

- given p implies q (p -> q), the only way it can return false is if p is T and q is F.
![nonstandard logic table for p implies q](image-2.png)
  - p is the hypothesis, q is the conclusion
  - in this way, a conditional statement will always return true if the hypothesis p is false
    - if you don't mow the lawn, Mr. Smith can pay you or not and it doesn't matter. this always returns T.
    - if you mow the lawn and he pays you then the contract is fulfilled and it returns T.
    - if you *do* mow the lawn and he *doesn't* pay you, the contract is broken and the statement returns false.
    - i.e. True -> False is the only way to make it return F.

here's a table for the converse, contrapositive, and inverse of a conditional statement.
![table for the converse, contrapositive, and inverse.](image-3.png)

- biconditional statements like p ↔ q require both to be the same to return T.
  - if p and q return T. if not p and not q then return T. else return F.

![Alt text](image-4.png)

- apparently you can use p ⇔ q to denote that p = q (and therefore p ↔ q = T) but i don't think the book ever does


for valid propositions p and q, these are valid propositions
- ¬p (~p)
  - not p
- p ∨ q
  - p or q
  - disjunction
- p ∧ q
  - p and q
  - conjunction
- p → q (p => q)
  - p then q
  - implication / conditional
  - p = hypothesis, q = consequence
  - uncommon versions:
    - p only if q = p → q
    - p unless q = ¬q → p = p ∨ q
  - p → q = ¬q ∨ p
- p ↔ q (p ⇔ q)
  - p iff q
  - biconditional / equivalence
- order of operations:
1. fill in actual truth values
2. any quantified statements
3. innermost parentheses
4. not ¬
5. and ∧, or ∨
6. conditionals ⇒, biconditionals ⇔

## Logical Equivalences
- a tautology is always correct, regardless of the input
  - p ∨ ¬p = T no matter the value of p
  - p ∧ q -> p = T
- a contradiction is always false, regardless of the input
  - p ∧ ¬p = F no matter the value of p
- apparently logical equivalence is supposed to be ≡ but i'm using =. i don't have ≡ on my keyboard.
  - two things are logically equivalent if, for every possible combination of inputs, output the same values
  - you can prove this by making a logic table and putting the things you want to prove equivalent next to each other

![Table 6 logical equivalences](<logical equivalences.png>)
![various properties of conditional statements](IMG_3921.JPG)
- for some laws, multiplication = AND and addition = OR
- p implies q ≡ (not p) or q
- not(p implies q) ≡ p and (not q)
- the contrapositive of a statement is always equivalent to its original statement
  - (p → q) is logically equivalent to (not q → not p)
- ¬(p → q) ≡ p ∧ ¬q
- a *recognizer expression* is only true for one single input
  - we are doing minterm expansion i am not taking these notes again
- CNF - conjunctive normal form
  - a lot of disjunctions connected by ands
- DNF - disjunctive normal form
  - minterm expansion form
  - a lot of conjunctions connected by ors



## symbol key
- ∈ = belongs to / is an element of
- ℤ = set of integers
  - ℤ⁺ = all positive integers (excl. 0)
- ℝ = set of all real numbers
- ℚ = set of all rational integers
  - recall scheme handles fractions well
- ℕ = set of all natural numbers = **Z**⁺ ∪ `{0}`
- ∀ = for all -- universal quantifier
- ∃ = there exists -- existential quantifier
- not ¬
- and ∧
- or ∨
- xor ⊕
- logically equivalent to ≡
- implies →
- iff ↔ biconditional arrow
- requires ⇔ iff double arrow

# Quantified Statements
- recall a predicate is a statement that only returns true or false
- a predicate function contains a finite number of variables and indicates whether a relationship is held by the objects represented by those variables.
  - when you fill in the variables with objects it becomes a proposition
  - a predicate has a variable and a domain and as such has no inherent truth value vs.
  - a proposition does not contain any variables and as such has a set truth value
- the domain is the set of all variables for which it is defined, i.e. all that make sense
- ex
  - Let D = {1,2,3,4,5} and consider ∀x (x² ≥ x)
  - Is this statement true?
  - prove for every element of the domain; yes.
- Existential Quantifier ex.
  - Let P(x) = x² - 4 > x be a predicate with a domain consisting of all real numbers
  - ∃x P(x) (there exists an x for P(x) that makes P(x) true)
  - True! (10, per se)
- ∀x<0 (x² > 0)
  - for all x that are <0, are any x² > 0?
  - also ∀x(x < 0 → x² > 0)
- the input that makes a predicate false is the ***counterexample***
- proving or disproving universally/existentially quantified statements
  ![alt text](image-6.png)
- usually you have to prove a ∃ statement true, vs proving a ∀ statement false 
- the quantifiers have higher precedence than all other operators
- the variable x in P(x) is a *free variable*
  - you cannot do any calculus with this because we don't know what to do with x
- in ∀xP(x), x is now a *bound variable* bc it is bound to the quantifier
  - now we can evaluate it
- you cannot do (∀xP(x)) ∨ Q(x) because now x is both bound and free (illegal)
  - though you can do ∀x(P(x) ∨ Q(x)), because here ∀x binds both occurrences of x
- DeMorgan's law for quantified statements:
  - ¬(∀y Q(y)) = ∃y ¬Q(y)
  - ¬(∃z R(z)) = ∀z ¬R(z)
- quantifiers are sorta distributive [like here](https://math.stackexchange.com/a/3059525)
  
## Lab examples
- Given P(x) with domain 1, 2, 3, 4, 5:
  - ∃xP(x) ≡ P(1) ∨ P(2) ∨ P(3) ∨ P(4) ∨ P(5)
  - ∀xP(x) ≡ P(1) ∧ P(2) ∧ P(3) ∧ P(4) ∧ P(5)
  - ¬∃xP(x) ≡ ¬(P(1) ∨ P(2) ∨ P(3) ∨ P(4) ∨ P(5)) 
    - ≡ ¬P(1) ∧ ¬P(2) ∧ ¬P(3) ∧ ¬P(4) ∧ ¬P(5) ≡ ∀xP(x)
- given P(x) = ∀x(x² > x)
  - ¬P(x) ≡ ∃x(x² ≤ x>)
  - when negating a inequality operator, it toggles the direction *and* its "or equal to"

## Nested Quantifiers
- Consider:
- M(x,y): x sent an email to y.
  - ∀x∀yM(x,y) ≡ everyone sent an email to everyone (including themselves)
  - ∃x∃yM(x,y) ≡ someone sent an email to someone (possibly themselves)
  - ∃x∀yM(x,y) ≡ someone sent an email to everyone (including themselves)
  - ∀x∃yM(x,y) ≡ everyone sent an email to someone (possibly themselves)
- the existential quantifier is trying to make the statement true
  - only needs one to be true
- the universal quantifier is trying to make it false
- DeMorgan's law still works, it just swaps all of the nested quantifiers
![DeMorgan's law for nested quantifiers](image-7.png)
  - you can do it to one quantifier at a time if necessary, but you will probably always do the whole thing
- what if we want to say everyone sent an email to everyone else, but not themselves?
  - ∀x∀y((x≠y) ∧ M(x,y)) ≡ everyone sent an email to everyone *except themselves*
- consider L(x): x was late to the meeting
  - we want to say that only one person was late to the meeting
  - ∃x(L(x) ∧ ∀y((x≠y) → ¬L(y)))
- ∀x,yP(x,y) ≡ ∀x∀yP(x,y)

# Inference Rules
- an argument form is a sequence of formulas (preceding premises) the last of which is called the conclusion
  - premises are also called hypotheses
- argument form is valid if, when all of the premises are true, the conclusion is also true.
- p1, p2, ..., pn, ∴q is a valid argument iff p1 ∧ p2 ∧ ... ∧ pn → q is true
- syllogisms have two premises and a conclusion
- Modus Ponens:
  - p → q
  - p
  - ∴q
    - ≡ (p → q) ∧ p → q ≡ T
- Modus Tollens
  - p → q
  - ¬q
  - ∴¬p
- you can change order of premises
- you can replace or add a proposition equivalent to any premise
- when using a truth table
  - prove the conclusion true by finding all rows where all hypotheses are true AND the conclusion is true.
  - if there are any rows with a truth mismatch between any hypotheses and the conclusion than the argument is false.
- usually when they ask to prove that an argument is invalid, they want to to prove that there is some case where all of the hypotheses are true but the conclusion is false. 

![Table 1.12.1: Rules of inference known to be valid arguments.](image-8.png)
![Table 1.13.1: Rules of inference for quantified statements.](image-9.png)

# Set Theory
- A set is a well-defined collection of objects
- set builder notation: `{x ∈ ℤ+ | x <= 4}`
  - the set of all x in the se tof positive integers where x is less than or equal to 4
- set roster notation: `{1, 2, 3, 4}`
- a set whose elements can be explicitly listed is a finite set
  - i.e. the set of prime numbers
  - cardinality = |set| = amount of unique values
  - any others are infinite sets
    - cardinality of infinity
- order is irrelevant; membership is important
  - `{1, 2, 3}` = `{3, 1, 2}`
- `{0} != 0`
  - a set and object are two different things
  - a set contains objects
- a subset contains any amount of elements from another set and none that are not in that other set
  - a PROPER subset contains any amount of elements from another set but NOT all of them and none that are not in the other set.
  - if a set is a proper subset of another set, then it is also a regular subset of it too. not  vice versa.
- the power set of A, P(A), is the set of all subsets of A
  - A = `{1, 2, 3}`
  - P(A) = `{∅, {1}, {2}, {3}, {1, 2}, {1,3} {2,3}, {1,2,3}}`
  - a set's power set has 2^(|set|) elements
- the intersection of two sets is the set of all elements they have in common
- the union of two sets is the set of the contents of both sets
- set difference: A - B or A \ B = `{x ∈ U | x ∈ A and x ∉ B}`
  - A \ B = A ∩ B̄ 

# Cartesian Products
- punnet squares

![cartesian produce example](image-10.png)

- may denote a product with a set's self as a power
  - A = `{x,y}`
  - A^2 = A×A = `{(x,x), (x,y), (y,x), (y,y)}` 
    - as a set of strings: `{xx, xy, yx, yy}`
  - etc.
  - unlike in finding subsets, self-products can double up the same value.
    - `{(x,x)}` is not a subset of A but it is a subset of A^2

# Strings
- you can have sets of symbols or characters
- putting the letters together without the set notation gives you a string
  - A = `{h, i}`, string = `hi`
- the set of all characters in a set of strings is called its alphabet
- they also have a length (1-indexed)
- concatenate strings by putting the name of their sets together
  - t = abc, s = def
  - ts = abcdef
- can also concatenate one symbol the same way
  - t = 001
  - t0 = 0010
- the empty string is λ
  - tλ = t

## Binary Strings
- a binary string contains only 1s and 0s
- one bit = one character in a binary string
- all binary strings of length n = `{0,1}ⁿ`
  - `{0,1}²` = `{00, 01, 10, 11}`

# Functions
- think of them here like a map
  - mapping X onto Y: f: X → Y
    - X = *domain*, Y = *target*
  - or a subset of X × Y, where (x, y) ∈ f iff f maps x to y.
    - in this case X and Y can be the same set
- you can list all pairs of (x, y), i.e. (x, f(x)) if both X and Y are finite sets
- you can do arrow diagrams
- y is in the **range** of f iff there is an x ∈ X such that (x,y) ∈ f.
  - i.e., all elements in Y that can be produced by some f(x)
  - range is also called 
- when you have infinite domain you can't have a diagram for it
  - draw a graph instead
- a **well-defined function** has exactly one f(x) for each x
  - anything with a ± is not well defined
  - usually not considered a function if any x has >1 f(x)
- two functions f and g are equal (f = g) iff they have the same domain and f(x) = g(x) for all x in domain
- **one-to-one / injective function**: ∀(x1, x2) ∈ A: (x1 ≠ x2) → f(x1) ≠ f(x2)
  - |X| ≤ |Y| → there us an injective mapping from X to Y
- **onto / surjective function**: ∀y ∈ B ∃x ∈ A: f(x) = y
  - i.e. every element in y has an f(x) that produces it
  - or there are no elements in y that can not be produced by taking an f(x)
  - |X| ≥ |Y| → there is a surjective mapping from X to Y
- **one-to-one correspondence / bijective**: iff the function is both subjective and surjective
  - |X| = |Y| → there is a one-to-one mapping of X onto Y
  - there are no bijections from **Z** to **R** or vice versa
- if a function is strictly increasing ro strictly decreasing it is automatically one-to-one, e.g.
  - f(n) = n-1
  - f(n) = n³
  - i.e. the derivative is always either >0 or <0

## Floor & Ceiling Functions
- floor: round down
  - **R** → **Z**, where floor(x) = the largest integer Y such that y ≤ x.
  - floor(x) = ⌊x⌋
- ceiling: round up
  - **R** → **Z**, where floor(x) = the smallest integer Y such that y ≥ x.
  - ceiling(x) = ⌈x⌉

# countability of sets
- set S is finite if it has a cardinality equal to `|{1, 2, ..., n}|` for n ∈ **N**
- a set S is countable if it has the same cardinality of some subset of **Z**⁺
- a set S is countably infinite if there is a one-to-one function f: S → **Z**⁺ (which is also f: **Z**⁺ → S)
- uncountably infinite → greater cardinality than **Z**+
- countably infinite sets have lower cardinality than uncountably infinite sets
  - we know |**Z**⁺| < |P(**Z**⁺)| 
    - as a rule |P(S)| > |S|
  - for every possible list of sets including/excluding elements of **Z**⁺ there is a variation that you haven't listed yet
- **N** is not just **Z**⁺, it's actually **Z**⁺ ∪ `{0}`
- can we prove that **N** and **Z**⁺ have the same cardinality? 
  - find a one-to-one function that maps all of **N** onto **Z**⁺
  - f: **N** → **Z**⁺
  - f(n) = n+1
  - this function is strictly increasing and both sets are infinite therefore this is one-to-one
- all of the rooms in the uncountably infinite hotel are occupied; however we can accommodate one new guest by putting him in the first room and making everyone move down one
  - the rooms are uncountably infinite → there is actually another room even though we said they're all full
  - for all current guests map **Z**⁺ → **Z**⁺ by current room number n ∈ **Z**⁺ and new room no. f(n) ∈ **Z**⁺ where f(n) = n+1
  - now the first room is still here but empty for the new guest

# Midterm Review
- compressing an interval:
  - multiply it by some fraction 0 < m < 1 and add some similar fraction
  - e.g. [0,1] -> (0,1)
    - some compression function f(x) = x/3 + 1/2
  - schroder-bernstein theorem tells us that, because we can do this compression, then [0,1] has the same cardinality as (0,1)
- if X and Y is countable, then X ∪ Y is countable
- no union of countable sets will equal an uncountable set
- power set of an uncountable set will *always* have a greater cardinality than the original set

# Relations
- a relation R of A to B is any subset A × B
- A is the domain
- B is the co-domain
- instead of (x,y) ∈ R, we write x R y.
- you can draw arrow diagrams or tables to show all possible pairs

## Directed Graphs
- when the domain and co-domain are the same you can make a directed graph (digraph)
  - a directed graph G is a pair (V,E) where V is a set of vertices and E is a set of ordered pairs (u,v) ∈ V×V called the directed edges.
- like an arrow diagram but it's just one set of points
- pairs like (1,1) will show as the vertex 1 pointing to itself
- ![directed graph for a relation](image-5.png)
- **in-degree** of a vertex is the amount of arrows pointing toward it, **out-degree** is the amount pointing away
- of uRv, u is the **head** and v is the **tail**
- if a is the head and tail of an arrow, that arrow is called a **self-loop**

## Types of Relations
- a relation R on a set A is **reflexive** if (a,a) ∈ R for all a ∈ A.
  - i.e. it includes all possible self-loops
  - e.g. a reflexive relation of `{1,2}` would look like `{(1,1), (2,2)}`
  - it could also include other pairs like `{(1,1), (1,2), (2,1), (2,2)}`
  - represented as a matrix, its diagonal will be all 1s
    - place a 1 in coords where the pair exists in the relation and 0 in the rest
- an **irreflexive** relation has no pair aRa for any a ∈ R.
- a relation R on a set A is **symmetric** if (a,b) ∈ R ⇔ (b,a) ∈ R for all a,b ∈ A
  - i.e. for all pairs (a,b) in the set there will be another pair (b,a)
  - the matrix will reflect over the diagonal
  - ![symmetric directed graph + info](image-11.png)
- an **anti-symmetric** relation is one where: for a,b ∈ R, if there is aRb and bRa then a = b
  - i.e. if there is aRb, the must be **no** bRa.
  - offers no info about aRa; R could be reflexive or irreflexive
- an **asymmetric** relation is both antisymmetric and irreflexive
  - ∀a,b ∈ A: aRb ⇒ ¬(bRa)
  - there are no pairs aRa and, for all pairs xRy there is no yRx.
- a relation R on a set A is **transitive** if [for all a,b,c ∈ A] (a,b) ∈ R and (b,c) ∈ R then (a,c) ∈ R.
  - the pairs (a,b) and (b,c) require the existence of (a,c). if no (a,c) then R is not transitive.
  - ![transitive directed graph and extra info](image-12.png)
  - a relation is either transitive or not, there is no neither option.

### Equivalence Relations
- a relation R on a set A is an **equivalence** relation if it is reflexive, symmetric, and transitive
  - e.g.:
  - ![alt text](image-16.png)
- If A is the domain of an equivalence relation and a ∈ A, then [a] is defined to be the set of all x ∈ A such that a~x. The set is called an **equivalence class**.
  - i.e. `{x ∈ A | (x,a) ∈ R}`
  - i.e. all the elements than a can be paired with a to make the largest possible equivalence relation
  - when R is an equivalence relation, we will write a~b instead of aRb.
  - equivalent sets are either equal or disjoint. for y,z ∈ equivalence relation R,
    - if y~z then [y] = [z]
    - if y is not ~ z, then [y] ∩ [z] = ∅
  - let A be the set of all people in a friend group. let R be a relation over A where aRb iff a,b ∈ A and a and b know each other. this is an equivalence relation so we can write this as a~b. for z ∈ A, [z] will be the set of everyone in the group who knows z.
- partitions are isolated sections of an equivalence relation.
![partitions](image-17.png)


# Types of Walks
- we can walk through the graph like this ![alt text](image-13.png)
  - an **open walk** has different first and last vertices
  - a **closed walk** has the same first and last vertex
  - a walk from a to b to c is denoted like ⟨a, b, c⟩ which requires that (a,b) and (b,c) ∈ R
  - length is the amount of pairs that make it up, including duplicates
  - a walk with 0 length like ⟨a⟩ is valid
  - a walk ⟨a, a⟩ is valid and closed, assuming (a,a) exists
- A **trail** is a walk in which no *edge* occurs more than once.
- A **path** is a walk in which no *vertex* occurs more than once.
- trail vs path
  - ![trail vs path](image-14.png)
- A **circuit** is a closed trail.
  - all entries are unique, and first and last are the same
- A **cycle** is a circuit of length ≥1 in which no vertex occurs more than once, except the first and last vertices which are the same.
- cycle vs circuit
  - ![cycle vs circuit](image-15.png)