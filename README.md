# Multiple Cancer mutations

Write a Python program called `mutation.py` that will show the mutation genes give the related cancer.
The program should accept a single, required, readable file argument.
When run with no arguments, it should produce a brief usage statement:

```
$ ./mutation.py
usage: mutation.py [-h] FILE
mutation.py: error: the following arguments are required: FILE
```

When run with `-h|--help` flags, it should produce a longer help:

```
$ ./mutation.py -h
usage: mutation.py [-h] FILE

Show mutation genes

positional arguments:
  FILE        Input file

optional arguments:
  -h, --help  show this help message and exit
```

The first test input file has 4 mutated genes:

```
$ cat cancer/genes1.fa
Pancreatic cancer
KRAS
CDKN2A
TP53
SMAD4/DPC4
```

When run with this file, the program should print the type of cancer the number of mutated genes and the list of genes:

```
$ ./mutation.py cancer/genes1.fa
This is Pancreatic cancer with 4 mutated genes: ['KRAS', 'CDKN2A', 'TP53', 'SMAD4/DPC4']
```

The second test file has a different cancer, and the output should be similar:

```
$ ./mutation.py cancer/genes2.fa
This is Breast cancer with 2 mutated genes: ['BRCA1', 'BRCA2']
```

A passing test suite looks like the following:

```
$ make test
pytest -xv --pylint test.py mutation.py
============================= test session starts ==============================
...
collected 7 items                                                                                                                              
--------------------------------------------------------------------------------
Linting files
..
--------------------------------------------------------------------------------

test.py::PYLINT PASSED                                                                                                                   [ 14%]
test.py::test_exists PASSED                                                                                                              [ 28%]
test.py::test_usage PASSED                                                                                                               [ 42%]
test.py::test_bad_file PASSED                                                                                                            [ 57%]
test.py::test_good_input1 PASSED                                                                                                         [ 71%]
test.py::test_good_input2 PASSED                                                                                                         [ 85%]
mutation.py::PYLINT PASSED                                                                                                               [100%]

============================================================== 7 passed in 1.51s ===============================================================
```

## Author

Ken Youens-Clark <kyclark@gmail.com>
