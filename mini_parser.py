#!/usr/bin/env python3
"""
Mini Parser - Main Interface
=============================

This is the main entry point for the mini parser.
It provides a simple command-line interface for parsing expressions.

Usage:
    python mini_parser.py "3 + 5 * 2"
    python mini_parser.py --interactive
"""

import sys
from tokenizer import Tokenizer
from parser import Parser, Interpreter


def parse_and_evaluate(expression: str, verbose: bool = False) -> float:
    """
    Parse and evaluate a mathematical expression.
    
    Args:
        expression: The mathematical expression to evaluate
        verbose: If True, print detailed information about the parsing process
    
    Returns:
        The numeric result of the expression
    
    Raises:
        ValueError: If there's a parsing or evaluation error
    """
    # Step 1: Tokenize
    tokenizer = Tokenizer(expression)
    tokens = tokenizer.tokenize()
    
    if verbose:
        print("\n=== TOKENIZATION ===")
        print(f"Input: {expression}")
        print("Tokens:")
        for token in tokens:
            print(f"  {token}")
    
    # Step 2: Parse
    parser = Parser(tokens)
    ast = parser.parse()
    
    if verbose:
        print("\n=== PARSING ===")
        print(f"AST: {ast}")
    
    # Step 3: Evaluate
    interpreter = Interpreter()
    result = interpreter.evaluate(ast)
    
    if verbose:
        print("\n=== EVALUATION ===")
        print(f"Result: {result}")
    
    return result


def interactive_mode():
    """
    Run the parser in interactive mode.
    
    Users can type expressions and see the results immediately.
    Type 'quit' or 'exit' to leave.
    """
    print("Mini Parser - Interactive Mode")
    print("=" * 50)
    print("Type mathematical expressions to evaluate them.")
    print("Type 'quit' or 'exit' to leave.")
    print("Type 'verbose' to toggle detailed output.")
    print("=" * 50)
    print()
    
    verbose = False
    
    while True:
        try:
            # Get input from user
            expression = input(">>> ").strip()
            
            # Check for special commands
            if expression.lower() in ('quit', 'exit'):
                print("Goodbye!")
                break
            
            if expression.lower() == 'verbose':
                verbose = not verbose
                print(f"Verbose mode: {'ON' if verbose else 'OFF'}")
                continue
            
            if expression.lower() == 'help':
                print("\nAvailable operators:")
                print("  +  Addition")
                print("  -  Subtraction")
                print("  *  Multiplication")
                print("  /  Division")
                print("  () Parentheses for grouping")
                print("\nExamples:")
                print("  3 + 5")
                print("  10 - 2 * 3")
                print("  (10 + 2) * 3")
                print("  -5 + 10")
                print()
                continue
            
            if not expression:
                continue
            
            # Parse and evaluate
            result = parse_and_evaluate(expression, verbose=verbose)
            
            if not verbose:
                print(f"{result}")
            
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")
        
        if not verbose:
            print()


def main():
    """Main entry point for the mini parser."""
    if len(sys.argv) == 1:
        # No arguments, show usage
        print("Mini Parser")
        print("=" * 50)
        print("\nUsage:")
        print("  python mini_parser.py <expression>")
        print("  python mini_parser.py --interactive")
        print("  python mini_parser.py --verbose <expression>")
        print("\nExamples:")
        print('  python mini_parser.py "3 + 5"')
        print('  python mini_parser.py "10 - 2 * 3"')
        print('  python mini_parser.py "(10 + 2) * 3"')
        print('  python mini_parser.py --interactive')
        print("\nFor interactive mode, use: --interactive or -i")
        sys.exit(0)
    
    # Check for interactive mode
    if sys.argv[1] in ('--interactive', '-i'):
        interactive_mode()
        return
    
    # Check for verbose mode
    verbose = False
    expression_index = 1
    
    if sys.argv[1] in ('--verbose', '-v'):
        verbose = True
        expression_index = 2
        if len(sys.argv) < 3:
            print("Error: --verbose requires an expression argument")
            sys.exit(1)
    
    # Parse and evaluate the expression
    expression = sys.argv[expression_index]
    
    try:
        result = parse_and_evaluate(expression, verbose=verbose)
        print(result)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
