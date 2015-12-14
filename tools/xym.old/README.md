# xym.py

xym is a simple utility for extracting yang modules from files. Its module dependencies are documented in [requirements.txt](requirements.txt).

Help with it's options may be displayed thus:

```
$ ./xym.py --help
usage: xym.py [-h] [--srcdir SRCDIR] [--dstdir DSTDIR] [--strict]
               [--strict-examples] [--debug DEBUG]
               source

Extracts one or more yang models from an IETF RFC/draft text file

positional arguments:
  source             The URL or file name of the RFC/draft text from which to
                     get the model

optional arguments:
  -h, --help         show this help message and exit
  --srcdir SRCDIR    Optional: directory where to find the source text;
                     default is './'
  --dstdir DSTDIR    Optional: directory where to put the extracted yang
                     module(s); default is './'
  --strict           Optional flag that determines syntax enforcement; If set
                     to 'True', the <CODE BEGINS> / <CODE ENDS> tags are
                     required; default is 'False'
  --strict-examples  Only output valid examples when in strict mode
  --debug DEBUG      Optional: debug level - determines the amount of debug
                     info printed to console; default is 0 (no debug info
                     printed)
```

The following behavior is implemented with respect to the "strict" and "strict-exmaples" options (none of the other options influence this behavior):

* No options -- all yang modules found in the source file will be extracted and yang files created.
* ```--strict``` -- only yang modules bracketed by \<CODE BEGINS\> and \<CODE-ENDS\> will be extracted
* ```--strict --strict-examples``` -- only yang module **outside** of \<CODE BEGINS\> and \<CODE-ENDS\> **and** with a name starting with "example-" will be extracted.

Please note:

* Some errors will be generated to aid in debugging the content of modules. For example:

```
ERROR: 'test-file.txt', Line 21 - Yang module 'ex-error' with no <CODE BEGINS> and not starting with 'example-'
ERROR: 'test-file.txt', Line 47 - Yang module 'example-error' with <CODE BEGINS> and starting with 'example-'
```

* If any yang modules that will be extracted already exist, the tool will exit without creating any yang modules

* If there are syntactic errors such as a yang module statement nested in a yang module, the tool will exit without creating any yang modules

## Testing

xym has a simple set of tests exercising a subset of functionality. These may be invoked while in the xym subdirectory thus:

```
$ python -m unittest xym
```

Expected output is:

```
$ python -m unittest xym
ERROR: 'test-file.txt', Line 21 - Yang module 'ex-error' with no <CODE BEGINS> and not starting with 'example-'
ERROR: 'test-file.txt', Line 47 - Yang module 'example-error' with <CODE BEGINS> and starting with 'example-'
.ERROR: 'test-file.txt', Line 21 - Yang module 'ex-error' with no <CODE BEGINS> and not starting with 'example-'
ERROR: 'test-file.txt', Line 47 - Yang module 'example-error' with <CODE BEGINS> and starting with 'example-'
.ERROR: 'test-file.txt', Line 21 - Yang module 'ex-error' with no <CODE BEGINS> and not starting with 'example-'
ERROR: 'test-file.txt', Line 47 - Yang module 'example-error' with <CODE BEGINS> and starting with 'example-'
.
----------------------------------------------------------------------
Ran 3 tests in 0.004s

OK
$
```
