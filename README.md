# PythonPractice
### Learn Python 3 the Hard Way - Zed Shaw
#### _1. Print Statement_
- Ex 1 - Print Statement
- Ex 2 - Comments
- Ex 3 - Numbers & Math
- Ex 4 - Variables & Names
- Ex 5 - More Variables & Printing
- Ex 6 - Strings & Text
- Ex 7 - More Printing
- Ex 8 - Printing Printing
- Ex 9 - Printing Printing Printing
- Ex 10 - Printing with Escape Characters
#### _2. User Inputs_
- Ex 11 - User Inputs
- Ex 12 - More User Inputs
- Ex 13 - User Inputs via Argument Variable 'argv'
- Ex 14 - Prompting and Passing User Inputs
#### _3. File Operation_
- Ex 15 - Reading Files
- Ex 16 - Truncating & Writing into Files
- Ex 17 - Copy file content to another - Text and Binary content
#### _4. Functions_
- Ex 18 - Functions
- Ex 19 - Functions & Variables
- Ex 20 - Functions & Files
- Ex 21 - Functions with Return values
- Ex 23 - Functions - Strings, Bytes & Character Encodings
- Ex 24 - Functions - More Practice
- Ex 25 - Create Functions as Importable modules
#### _5. Test_
- Ex 26 - Debug the existing code
#### _6. Building Logic_
- Ex 27 - Truth Tables

---
### Glossary
#### _1. Escape Characters_
| Escape | What it does |
| ------ | ------ |
| \\\\ | Backslash (\\) |
| \\' | Single-Quote (') |
| \\" | Double-Quote (") |
| \\a | ASCII Bell (BEL) |
| \\b | ASCII Backspace (BS) |
| \\f | ASCII Formfeed (FF) |
| \\n | ASCII Linefeed (LF) |
| \\r | ASCII Carriage Return (CR) |
| \\t | ASCII Horizontal Tab (TAB) |
| \\v | ASCII Vertical Tab (VT) |
| \\uxxxx | Character with 16-bit hex value xxxx |
| \\Uxxxxxxxx | Character with 32-bit hex value xxxxxxxx |
| \\000 | Character with Octal value 000 |
| \\xhh | Character with Hex value hh |
| \\N{name} | Character named name in the Unicode Database (Unicode Only) |

#### _2. File Operation Modes_
|Character|Meaning|
|---------|-------|
|r|open for reading (default)|
|w|open for writing, truncating the file first|
|x|create a new file and open it for writing|
|a|open for writing, appending to the end of the file if it exists|
|b|binary mode|
|t|text mode (default)|
|+|open a disk file for updating (reading and writing)|

* **`rt`** - Default Mode
* **`rb+`** & **`wb+`** - Process ASCII Text & Binary file content

#### _3. Truth Table_
|NOT|True?|
|---------|-------|
|not False|True|
|not True|False|

|OR|True?|
|---------|-------|
|True OR False|True|
|True OR True|True|
|False OR True|True|
|False OR False|False|

|AND|True?|
|---------|-------|
|True AND False|False|
|True AND True|True|
|False AND True|False|
|False AND False|False|

|NOT OR = NOR|True?|
|---------|-------|
|NOT(True OR False)|False|
|NOT(True OR True)|False|
|NOT(False OR True)|False|
|NOT(False OR False)|True|

|NOT AND = NAND|True?|
|---------|-------|
|NOT(True AND False)|True|
|NOT(True AND True)|False|
|NOT(False AND True)|True|
|NOT(False AND False)|True|

|==|True?|
|---------|-------|
|1 == 0|False|
|1 == 1|True|
|0 == 1|False|
|0 == 0|True|

|!=|True?|
|---------|-------|
|1 != 0|True|
|1 != 1|False|
|0 != 1|True|
|0 != 0|False|

