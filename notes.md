# Intro
- no late homework. you will be killed.
- two lowest labs, reading, and writing homework assignments get dropped at the end of semester.
- no formula sheets on exams.
- mandatory attendance (5% of grade).
- exams are 50% total of final grade.
- coding is the easiest part -- actually designing what you're coding is the hard part

# Scheme / DrRacket
- DrRacket seems to work exactly like IDLE
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
    > (number? "haha")
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