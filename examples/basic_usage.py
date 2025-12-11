#!/usr/bin/env python3
"""
Basic Usage Examples
====================

This script demonstrates basic usage of the Mini-Parser.
Run this to see the parser in action!
"""

import sys
sys.path.insert(0, '..')

from tokenizer import Tokenizer
from parser import Parser, Interpreter


def example_1_simple_evaluation():
    """Example 1: Evaluate a simple expression."""
    print("=" * 60)
    print("Example 1: Simple Evaluation")
    print("=" * 60)
    
    expression = "3 + 5"
    print(f"Expression: {expression}")
    
    # Create tokenizer and get tokens
    tokenizer = Tokenizer(expression)
    tokens = tokenizer.tokenize()
    
    # Parse into AST
    parser = Parser(tokens)
    ast = parser.parse()
    
    # Evaluate
    interpreter = Interpreter()
    result = interpreter.evaluate(ast)
    
    print(f"Result: {result}")
    print()


def example_2_complex_expression():
    """Example 2: Evaluate a complex expression with multiple operators."""
    print("=" * 60)
    print("Example 2: Complex Expression")
    print("=" * 60)
    
    expression = "10 + 2 * 6 - (4 / 2)"
    print(f"Expression: {expression}")
    
    tokenizer = Tokenizer(expression)
    tokens = tokenizer.tokenize()
    
    parser = Parser(tokens)
    ast = parser.parse()
    
    interpreter = Interpreter()
    result = interpreter.evaluate(ast)
    
    print(f"Result: {result}")
    print(f"Explanation: 10 + (2 * 6) - (4 / 2) = 10 + 12 - 2 = 20.0")
    print()


def example_3_show_tokenization():
    """Example 3: Show the tokenization process."""
    print("=" * 60)
    print("Example 3: Tokenization Process")
    print("=" * 60)
    
    expression = "(15 + 3) * 2"
    print(f"Expression: {expression}\n")
    
    tokenizer = Tokenizer(expression)
    tokens = tokenizer.tokenize()
    
    print("Tokens generated:")
    for i, token in enumerate(tokens, 1):
        print(f"  {i}. {token}")
    print()


def example_4_show_ast():
    """Example 4: Show the Abstract Syntax Tree."""
    print("=" * 60)
    print("Example 4: Abstract Syntax Tree (AST)")
    print("=" * 60)
    
    expression = "2 + 3 * 4"
    print(f"Expression: {expression}\n")
    
    tokenizer = Tokenizer(expression)
    tokens = tokenizer.tokenize()
    
    parser = Parser(tokens)
    ast = parser.parse()
    
    print("AST structure:")
    print(f"  {ast}")
    print("\nVisualization:")
    print("       +")
    print("      / \\")
    print("     2   *")
    print("        / \\")
    print("       3   4")
    print("\nThis shows that 3*4 is evaluated first (higher precedence)")
    print("Then 2 is added to the result")
    print()


def example_5_error_handling():
    """Example 5: Demonstrate error handling."""
    print("=" * 60)
    print("Example 5: Error Handling")
    print("=" * 60)
    
    invalid_expressions = [
        "3 + + 5",           # Syntax error
        "10 / 0",            # Division by zero
        "(3 + 5",            # Mismatched parentheses
        "3 @ 5",             # Invalid character
    ]
    
    for expr in invalid_expressions:
        print(f"Expression: {expr}")
        try:
            tokenizer = Tokenizer(expr)
            tokens = tokenizer.tokenize()
            parser = Parser(tokens)
            ast = parser.parse()
            interpreter = Interpreter()
            result = interpreter.evaluate(ast)
            print(f"Result: {result}")
        except Exception as e:
            print(f"Error: {e}")
        print()


def example_6_multiple_evaluations():
    """Example 6: Evaluate multiple expressions."""
    print("=" * 60)
    print("Example 6: Multiple Evaluations")
    print("=" * 60)
    
    expressions = [
        "100 / (2 + 3)",
        "2 * 3 + 4 * 5",
        "(2 + 3) * (4 + 5)",
        "-10 + 20",
        "3.14 * 2",
    ]
    
    interpreter = Interpreter()
    
    for expr in expressions:
        tokenizer = Tokenizer(expr)
        tokens = tokenizer.tokenize()
        parser = Parser(tokens)
        ast = parser.parse()
        result = interpreter.evaluate(ast)
        
        print(f"{expr:20} = {result}")
    print()


if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("MINI-PARSER: Basic Usage Examples")
    print("=" * 60 + "\n")
    
    example_1_simple_evaluation()
    example_2_complex_expression()
    example_3_show_tokenization()
    example_4_show_ast()
    example_5_error_handling()
    example_6_multiple_evaluations()
    
    print("=" * 60)
    print("All examples completed!")
    print("=" * 60)
