# CNF_Converter: A logic library to convert First-Order-Logic statements to Conjunctive Normal Form

------------------


## You have just found it.

In logic, a formula is in conjunctive normal form (CNF) or clausal normal form if it is a conjunction of clauses, where a clause is a disjunction of predicates; otherwise put, it is an AND of ORs. As a normal form, it is useful in automated theorem proving.

CNF_Converter is a library, written in Python and capable of converting all logic statements into conjunction of clauses.

CNF_Converter is compatible with: __Python 2.7-3.5__.


------------------


## Guiding principles

- This library is built on the top ply, an implementation of the yacc parsing tool for the Python programming language.

- First get the ast of the original statment. Then do some operations on the ast and get the ast of the CNF statment. Finally, get the CNF statment.


------------------


## Installation

CNF_Converter uses the following dependencies:

- ply


To install CNF_Converter,  and run the install command:
```sh
sudo python setup.py install
```

You can also install CNF_Converter from PyPI:
```
pip install cnfconverter
```

Or you can just import cnfconverter.py in your code.


------------------


## Getting started: 30 seconds to CNF_Converter


```python
from cnf import cnfconverter
```

In CNF_Concerter, what you input is a logic statment string:

```python
data = '((AD(x,y) | BD(x,y) )=> PD(z))'
```

You can get the ast of the logic statment:

```python
cnfconverter.get_AST(data)

{'left': {'child': {'left': {'value': 'AD(x,y)'},
   'op': '|',
   'right': {'value': 'BD(x,y)'}},
  'op': '~'},
 'op': '|',
 'right': {'value': 'PD(z)'}}
```

You can get the CNF of the logic statment:

```python
cnfconverter.to_CNF(data)

[['~AD(x,y)', 'PD(z)'], ['~BD(x,y)', 'PD(z)']]
```

The result is list of list. The element is a clause which consists of list of predicates.


------------------