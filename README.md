# Mini-Parser

A simple, educational mathematical expression parser written in Python. This project is designed to help others learn about:
- **Lexical Analysis** (Tokenization)
- **Syntax Analysis** (Parsing)
- **Abstract Syntax Trees** (AST)
- **Interpreter Design**

Perfect for students, beginners, and anyone interested in understanding how parsers work!

##  What This Parser Does

The Mini-Parser evaluates mathematical expressions with:
- **Basic operators**: `+`, `-`, `*`, `/`
- **Parentheses** for grouping: `(`, `)`
- **Operator precedence**: Follows standard mathematical rules (PEMDAS)
- **Unary operators**: `-5`, `+3`
- **Decimal numbers**: `3.14`, `2.5`

### Example Expressions

```python
3 + 5                    # Result: 8
10 - 2 * 3              # Result: 4 (respects precedence)
(10 - 2) * 3            # Result: 24 (parentheses first)
100 / (2 + 3) * 2       # Result: 40
-5 + 10                 # Result: 5 (unary minus)
```

##  Quick Start

### Prerequisites

- Python 3.6 or higher
- No external dependencies required!

### Installation

```bash
# Clone the repository
git clone https://github.com/ReaperKun/Mini-Parser.git
cd Mini-Parser

# No installation needed - it's pure Python!
```

### Usage

#### 1. Command Line Interface

Evaluate a single expression:

```bash
python mini_parser.py "3 + 5 * 2"
# Output: 13.0
```

With verbose output (shows tokenization and AST):

```bash
python mini_parser.py --verbose "(10 + 2) * 3"
```

#### 2. Interactive Mode

```bash
python mini_parser.py --interactive
```

This opens an interactive REPL where you can:
- Type expressions and see results immediately
- Type `verbose` to toggle detailed output
- Type `help` to see available operators
- Type `quit` or `exit` to leave

#### 3. Using as a Library

```python
from tokenizer import Tokenizer
from parser import Parser, Interpreter

# Parse and evaluate an expression
expression = "3 + 5 * 2"
tokenizer = Tokenizer(expression)
tokens = tokenizer.tokenize()

parser = Parser(tokens)
ast = parser.parse()

interpreter = Interpreter()
result = interpreter.evaluate(ast)

print(result)  # Output: 13.0
```

## 📚 How It Works

The parser follows a three-stage pipeline:

### 1. Tokenization (Lexical Analysis)

The `Tokenizer` breaks the input string into tokens:

```
Input:  "3 + 5 * 2"
Output: [NUMBER(3), PLUS, NUMBER(5), MULTIPLY, NUMBER(2), EOF]
```

**File**: `tokenizer.py`

### 2. Parsing (Syntax Analysis)

The `Parser` converts tokens into an Abstract Syntax Tree (AST):

```
Input:  [NUMBER(3), PLUS, NUMBER(5), MULTIPLY, NUMBER(2)]
Output: BinaryOp(+, Number(3), BinaryOp(*, Number(5), Number(2)))
```

The parser uses a **recursive descent** algorithm that respects operator precedence:
- **Expression**: Addition and Subtraction (lowest precedence)
- **Term**: Multiplication and Division (medium precedence)
- **Factor**: Numbers and Parentheses (highest precedence)

**File**: `parser.py`

### 3. Evaluation (Interpretation)

The `Interpreter` walks the AST and computes the result:

```
AST:    BinaryOp(+, Number(3), BinaryOp(*, Number(5), Number(2)))
Steps:  
  1. Evaluate: BinaryOp(*, Number(5), Number(2)) → 10
  2. Evaluate: BinaryOp(+, Number(3), 10) → 13
Result: 13.0
```

**File**: `parser.py`

##  Running Tests

The project includes comprehensive tests covering:
- Tokenization edge cases
- Parser correctness
- Operator precedence
- Error handling
- Edge cases (division by zero, mismatched parentheses, etc.)

```bash
python test_parser.py
```

All 27 tests should pass!

## 📖 Learning Resources

### Key Concepts Demonstrated

1. **Tokenization**: Breaking input into meaningful chunks
2. **Grammar Design**: Defining language syntax rules
3. **Recursive Descent Parsing**: Using function calls to match grammar rules
4. **AST Construction**: Building tree structures to represent code
5. **Tree Walking**: Traversing and evaluating tree structures
6. **Error Handling**: Providing helpful error messages

### Understanding the Grammar

The parser implements this grammar (in EBNF notation):

```
expression  := term ((PLUS | MINUS) term)*
term        := factor ((MULTIPLY | DIVIDE) factor)*
factor      := NUMBER | LPAREN expression RPAREN | (PLUS|MINUS) factor
```

This grammar ensures correct operator precedence and associativity.

### Code Structure

```
Mini-Parser/
├── tokenizer.py      # Lexical analysis (converts text to tokens)
├── parser.py         # Syntax analysis (builds AST) and interpreter
├── mini_parser.py    # CLI interface
├── test_parser.py    # Comprehensive test suite
├── README.md         # This file
├── CONTRIBUTING.md   # Contribution guidelines
└── examples/         # Example scripts
```

##  Contributing

We welcome contributions! This project is designed to be educational and collaborative.

### Ways to Contribute

- **Add features**: Variables, functions, more operators
- **Improve documentation**: Tutorials, explanations, diagrams
- **Add examples**: More use cases and demonstrations
- **Fix bugs**: Report and fix any issues
- **Write tests**: Expand test coverage

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

### Ideas for Extensions

- Add support for variables: `x = 5; x + 3`
- Implement functions: `max(3, 5)`, `sqrt(16)`
- Add more operators: `^` (power), `%` (modulo)
- Create a visual AST viewer
- Add step-by-step execution mode
- Support different number bases (binary, hex)

##  Contact

For questions, suggestions, or collaboration:
- Open an issue on GitHub
- Submit a pull request
- Start a discussion
- [Compiler Construction](https://en.wikipedia.org/wiki/Compiler) on Wikipedia

---

**Happy Parsing! 🎉**

Start with the examples, run the tests, and don't hesitate to experiment with the code!
