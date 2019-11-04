# CPython
This is a generic collection of information about CPython interpreter.

## Document Legend
* 🔵 - Definition
* 👌 - Good Practice (Do this), 🔴 - Bad practice (Don't do this)
* 👻 - Myth
* 👍 - Advantage, 👎 - Disadvantage
* Other Emoji - These are to **emphasize** what's said in the sentences.

## Introduction
* In this document I tried to refer to latest Python version at the time of writing or 3.7.
* 👻 CPython is an interpreter - It compiles to bytecode and interprets bytecode.
  * If you want a Just In Time (JIT) compiler too try `PyPy`


### Notations
* 🔵 **name** - How to identify objects? they have names. `a = 100` <- `a` is a name.
* 🔵 **code objects** - Objects containing executable bytecode. These are **immutable**.

### Execution Flow
1) Code is parsed. LL(1).
2) Abstract Syntax Tree is created.
3) Convert Abstract Syntax Tree to bytecode.
4) Interpret  bytecode in the interpreter loop.

```
                    [ hello.py ]
                      |
         Parsing      |--> [ Abstract Syntax Tree ]
                                    |
                    [ bytecode ] <--|    Compiler
                      |
         Interpreter  |--> [ Result ]
```

## CPython Memory
### Memory Management
* Reference: https://github.com/python/cpython/blob/master/Objects/obmalloc.c
```
    Object-specific allocators
    _____   ______   ______       ________
   [ int ] [ dict ] [ list ] ... [ string ]       Python core         |
+3 | <----- Object-specific memory -----> | <-- Non-object memory --> |
    _______________________________       |                           |
   [   Python's object allocator   ]      |                           |
+2 | ####### Object memory ####### | <------ Internal buffers ------> |
    ______________________________________________________________    |
   [          Python's raw memory allocator (PyMem_ API)          ]   |
+1 | <----- Python memory (under PyMem manager's control) ------> |   |
    __________________________________________________________________
   [    Underlying general-purpose allocator (ex: C library malloc)   ]
 0 | <------ Virtual memory allocated for the python process -------> |

   =========================================================================
    _______________________________________________________________________
   [                OS-specific Virtual Memory Manager (VMM)               ]
-1 | <--- Kernel dynamic storage allocation & management (page-based) ---> |
    __________________________________   __________________________________
   [                                  ] [                                  ]
-2 | <-- Physical memory: ROM/RAM --> | | <-- Secondary storage (swap) --> |

```
### Garbage Collection
* CPython has a reference counting garbage collector.
* When executing byte code:
  * 🔵 `Py_DECREF, Py_XDECREF` is called to decrease references.
  * When there are no more references, respective object's type's `__del__()` is called
  * 🔵 `Py_CLEAR` - decrease reference & set to `NULL`.
  * 🔵 `Py_INCREF, Py_XINCREF` - increase reference count.
* Unreachable islands are also collected - This uses a generational GC.

## Byte Code
* Python VM uses a `PyObject* stack`. Each byte-code interacts with this stack.

### Functions
* Functions are created as code objects then stored to a **name** in run time.
* 🔵 `LOAD_CONST` - load a constant python object
* 🔵 `MAKE_FUNCTION` - create a new function from `code object, qualified_named` and push to stack.
  * `Code object, qualified_named` is `Py_DECREF`d.
* 🔵 `STORE_NAME` - store current item in stack to a name

```
1           0 LOAD_CONST               0 (<code object first_func at 0x03D6C180, file "a.py", line 1>)  
            2 LOAD_CONST               1 ('first_func')                                                 
            4 MAKE_FUNCTION            0                                                                
            6 STORE_NAME               0 (first_func)                                                   
```


# References
* Source code, Documentation & `dis` module.
* http://www.pgbovine.net/cpython-internals.htm.
* https://troeger.eu/files/teaching/pythonvm08.pdf
