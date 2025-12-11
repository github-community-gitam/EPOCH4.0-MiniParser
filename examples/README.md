# Examples

This directory contains example scripts demonstrating how to use the Mini-Parser.

## Running the Examples

From the repository root:

```bash
cd examples
python basic_usage.py
```

Or from the examples directory:

```bash
python basic_usage.py
```

## Available Examples

### basic_usage.py

Demonstrates:
- Simple expression evaluation
- Complex expressions with multiple operators
- Tokenization process
- Abstract Syntax Tree (AST) visualization
- Error handling
- Multiple evaluations

Run it to see the parser in action with detailed explanations!

## Creating Your Own Examples

Feel free to create your own example scripts! Here's a template:

```python
#!/usr/bin/env python3
"""
Your Example Script
===================

Description of what this example demonstrates.
"""

import sys
sys.path.insert(0, '..')

from tokenizer import Tokenizer
from parser import Parser, Interpreter

def your_example():
    expression = "your expression here"
    
    tokenizer = Tokenizer(expression)
    tokens = tokenizer.tokenize()
    
    parser = Parser(tokens)
    ast = parser.parse()
    
    interpreter = Interpreter()
    result = interpreter.evaluate(ast)
    
    print(f"{expression} = {result}")

if __name__ == "__main__":
    your_example()
```

## Learning Path

1. **Start with basic_usage.py**: See all features in action
2. **Experiment**: Modify the examples to try different expressions
3. **Read the code**: Look at `tokenizer.py` and `parser.py` to understand how it works
4. **Run tests**: Execute `test_parser.py` to see comprehensive test cases
5. **Try interactive mode**: Run `python mini_parser.py --interactive` to experiment

## Ideas for More Examples

Want to contribute? Here are some ideas:
- Calculator application
- Expression validator
- Step-by-step evaluation visualizer
- Performance benchmarks
- Real-world use cases

See [CONTRIBUTING.md](../CONTRIBUTING.md) for guidelines!
