# Contributing to Mini-Parser

Thank you for your interest in contributing to Mini-Parser! This project is designed to be educational and collaborative. We welcome contributions from developers of all skill levels.

## 🎯 Project Goals

Mini-Parser aims to:
1. **Educate**: Help others learn about parsing, tokenization, and AST construction
2. **Simplicity**: Keep the code simple and readable
3. **Documentation**: Maintain clear, comprehensive documentation
4. **Collaboration**: Provide a friendly environment for learning and contribution

## 🚀 Getting Started

### Setting Up Your Development Environment

1. **Fork the repository**
   ```bash
   # Click "Fork" on GitHub, then clone your fork
   git clone https://github.com/YOUR_USERNAME/Mini-Parser.git
   cd Mini-Parser
   ```

2. **Create a branch**
   ```bash
   git checkout -b <feature-name>
   ```

3. **Make sure tests pass**
   ```bash
   python test_parser.py
   ```

### Understanding the Codebase

Before contributing, familiarize yourself with:

- **`tokenizer.py`**: Lexical analysis (breaking text into tokens)
- **`parser.py`**: Syntax analysis (building AST) and evaluation
- **`mini_parser.py`**: Command-line interface
- **`test_parser.py`**: Test suite

Read the code comments - they explain the design decisions!

## 📋 How to Contribute

### 1. Report Bugs

Found a bug? Please open an issue with:
- A clear, descriptive title
- Steps to reproduce the bug
- Expected behavior vs. actual behavior
- Your Python version
- Any error messages

Example:
```
Title: Division by zero not caught in nested expressions

Steps to reproduce:
1. Run: python mini_parser.py "(10 / (5 - 5)) + 3"
2. Expected: Error message about division by zero
3. Actual: Python crashes with traceback
```

### 2. Suggest Features

Have an idea? Open an issue with:
- A clear description of the feature
- Why it would be useful
- Examples of how it would work
- Whether you'd like to implement it

### 3. Improve Documentation

Documentation is crucial for learning! You can:
- Fix typos or unclear explanations
- Add more examples
- Create tutorials
- Add diagrams or visualizations
- Improve code comments

### 4. Add Tests

More tests = better code! Consider:
- Edge cases not currently covered
- Error conditions
- Performance tests
- Examples from real-world use cases

### 5. Write Code

#### Code Style Guidelines

1. **Follow Python conventions (PEP 8)**
   - Use 4 spaces for indentation
   - Use snake_case for functions and variables
   - Use PascalCase for classes
   - Maximum line length: 100 characters

2. **Write clear, self-documenting code**
   ```python
   # Good
   def calculate_total_price(items, tax_rate):
       subtotal = sum(item.price for item in items)
       return subtotal * (1 + tax_rate)
   
   # Avoid
   def calc(i, t):
       s = sum(x.p for x in i)
       return s * (1 + t)
   ```

3. **Add docstrings to all public functions and classes**
   ```python
   def tokenize(text: str) -> List[Token]:
       """
       Convert input text into a list of tokens.
       
       Args:
           text: The input string to tokenize
       
       Returns:
           List of Token objects
       
       Raises:
           ValueError: If an invalid character is encountered
       """
   ```

4. **Keep it simple and educational**
   - Prioritize readability over cleverness
   - Add comments explaining "why", not just "what"
   - Use descriptive variable names

#### Testing Guidelines

- **All code changes must include tests**
- Tests should be clear and well-documented
- Use descriptive test names: `test_division_by_zero_raises_error`
- Test both success and failure cases

Example test:
```python
def test_operator_precedence(self):
    """Test that multiplication has higher precedence than addition."""
    result = self.evaluate("2 + 3 * 4")
    self.assertEqual(result, 14.0)  # Not 20
```

#### Making Changes

1. **Keep changes focused**
   - One feature or fix per pull request
   - Don't mix refactoring with new features

2. **Write meaningful commit messages**
   ```
   Good:
   - "Add support for modulo operator (%)"
   - "Fix tokenizer crash on empty input"
   - "Improve error messages for mismatched parentheses"
   
   Avoid:
   - "Update code"
   - "Fix bug"
   - "Changes"
   ```

3. **Update documentation**
   - Update README.md if you add features
   - Update docstrings if you change behavior
   - Add examples for new features

4. **Run tests before submitting**
   ```bash
   python test_parser.py
   ```

## 🔄 Pull Request Process

1. **Update your fork**
   ```bash
   git fetch upstream
   git merge upstream/main
   ```

2. **Push your changes**
   ```bash
   git push origin feature/your-feature-name
   ```

3. **Create a Pull Request**
   - Go to GitHub and click "New Pull Request"
   - Fill in the PR template
   - Link any related issues

4. **PR Description Template**
   ```markdown
   ## Description
   Brief description of what this PR does
   
   ## Changes
   - List of changes made
   - Use bullet points
   
   ## Testing
   - How did you test these changes?
   - Did you add new tests?
   
   ## Related Issues
   Closes #123
   ```

5. **Respond to feedback**
   - Be open to suggestions
   - Make requested changes
   - Ask questions if unclear

## 💡 Ideas for Contributions

### Beginner-Friendly

- Add more test cases
- Fix typos in documentation
- Add code comments
- Create examples

### Intermediate

- Add support for the modulo operator (`%`)
- Implement the power operator (`^` or `**`)
- Add support for negative numbers without spaces: `-5+3`
- Create a visual AST printer

### Advanced

- Add variable support: `x = 5; x + 3`
- Implement functions: `max(3, 5)`, `sqrt(16)`
- Create a debugging mode with step-by-step execution
- Add support for different number formats (binary, hex)
- Build a web interface

## 🤔 Questions?

- **General questions**: Open a GitHub discussion
- **Bug reports**: Open an issue
- **Feature requests**: Open an issue
- **Need help getting started?**: Comment on a "good first issue"

## 📜 Code of Conduct

Be respectful, constructive, and welcoming:
- Be patient with newcomers
- Provide constructive feedback
- Focus on the code, not the person
- Help others learn

## 🎓 Learning While Contributing

Contributing is a great way to learn! Don't worry if:
- You're new to parsers or compilers
- This is your first open source contribution
- You make mistakes (we all do!)

We're here to help you learn and grow.

## 🙏 Recognition

All contributors will be:
- Listed in the repository
- Credited in release notes
- Celebrated in our community

---

**Thank you for contributing to Mini-Parser!**

Your contributions help others learn about parsing and compilers. Every contribution, no matter how small, makes a difference! 🌟
