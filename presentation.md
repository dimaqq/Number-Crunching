### Number Crunching

Dima Tisnek

Pythonic Wisdom

Egnyte Inc

dimaqq@gmail.com

[code on github](http://github.com/dimaqq/When-Python-is-not-enough)



## Plan

* simple problem
* optimisation in Python
* making Python faster
* Python libraries
* interfacing C



<img src="bifurcation.png"/>

simple problem


## simple problem

dynamical system

```python
    # next state
    x = r * x * (1 - x)

    0 < x < 1

    0 < r < 4

    # first bifurcation
    r == 3.0
```


<img src="0000.png"/>

initial conditions


<img src="0001.png"/>

after 1 step


<img src="0002.png"/>

after 2 steps


<img src="0003.png"/>

after 3 steps


<img src="0006.png"/>

after 6 steps


<img src="0010.png"/>

after 10 steps


<img src="0020.png"/>

after 20 steps


<img src="0050.png"/>

after 50 steps


<img src="0100.png"/>

after 100 steps


<img src="0200.png"/>

after 200 steps


<img src="0500.png"/>

after 500 steps


<img src="1000.png"/>

after 1000 steps



## optimise code

* use builtin types
* inline code



## faster Python

* Psyco
* pypy



## Psyco

* by Armin Rigo
* 2003 ~ 2008
* specializing compiler

<img src="oldpython.png"/>


### Psyco pros

* simple to use
* runs code faster


### Psyco cons

* only Python <= 2.6
* only 32-bit arch
* only functions



<img src="pypy.png"/>

* Python in Python
* Experimentation
* trace compiler, JIT
* active development
* the future


## PyPy

* Armin Rigo
* Maciej Fijałkowski
* Antonio Cuni
* very smart lot


## PyPy cons

* limited architectures
* memory (solved?)
* binary size (?)



## Libraries

* numpy
* scipy
* scikits.*


## numpy pros

* syntax
* fast
* GIL


## numpy cons

* homogenous data
* tracing errors



## C

* cython
* ctypes
* cffi



## cython

* compiles py code to libpython calls
* mix Python and C



## ctypes

* since Python 2.5
* dlopen in Python
* shared objects
* symbols
* data types
* allocation


## ctypes cons

* complex APIs
* debugging


## complex APIs

```cpp
LONG WINAPI SCardConnect(
    _In_   SCARDCONTEXT hContext,
    _In_   LPCTSTR szReader,
    _In_   DWORD dwShareMode,
    _In_   DWORD dwPreferredProtocols,
    _Out_  LPSCARDHANDLE phCard,
    _Out_  LPDWORD pdwActiveProtocol
);
```


## complex APIs

```cpp
guint g_signal_new (const gchar *signal_name,
                    GType itype,
                    GSignalFlags signal_flags,
                    guint class_offset,
                    GSignalAccumulator accumulator,
                    gpointer accu_data,
                    GSignalCMarshaller c_marshaller,
                    GType return_type,
                    guint n_params,
                    ...);
```



## cffi

* C parser
* smarter
* pypy
* cffi.load
* cffi.verify


## cffi cons

* new
* verify compiler



## Results

```no-highlight
                                    steps/s
              -----------------------------
              classes                  1.1M
              builtin                  1.9M
              inline                   3.5M
```


## More results

```no-highlight
                                    steps/s
              -----------------------------
              inline                     5M
              psyco                     26M
              pypy                      90M
              numpy                    120M
              cython                   ???M
              ctypes                   ???M
              cffi                     207M
```



## System
* osx
* iterm2
* aliased 10pt Monaco
* xcode cl
* virtualenv
* pip
* flake8


## Console
* ipython
* matplotlib


## Editor
* vim
* pathogen
* syntastic
* conque term
* highlight
* pyte


## Presentation
* markdown + js 
* github.com/hakimel/reveal.js
* slid.es



## SystemExit

Dima Tisnek

Pythonic Wisdom

Egnyte Inc

dimaqq@gmail.com
