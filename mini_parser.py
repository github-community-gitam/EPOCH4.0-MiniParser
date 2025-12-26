#!/usr/bin/env python3
"""
Mini Parser - Main Interface
=============================

Improved version with specific error handling.
"""

import sys
from tokenizer import Tokenizer
from parser import Parser, Interpreter

# Define custom exceptions
class TokenizationError(Exception):
    pass

class ParsingError(Exception):
    pass

class EvaluationError(Exception):
    pass


def parse_and_evaluate(expression: str, verbose: bool = False) -> float:
    """
    Parse and evaluate a mathematical expression.
    Raises specific errors for each stage.
    """
    # Step 1: Tokenize
    try:
        tokenizer = Tokenizer(expression)
        tokens = tokenizer.tokenize()
    except Exception as e:
        raise TokenizationError(f"Tokenization failed: {e}")

    if verbose:
        print("\n=== TOKENIZATION ===")
        print(f"Input: {expression}")
        print("Tokens:", tokens)

    # Step 2: Parse
    try:
        parser = Parser(tokens)
        ast = parser.parse()
    except Exception as e:
        raise ParsingError(f"Parsing failed: {e}")

    if verbose:
        print("\n=== PARSING ===")
        print("AST:", ast)

    # Step 3: Evaluate
    try:
        interpreter = Interpreter()
        result = interpreter.evaluate(ast)
    except Exception as e:
        raise EvaluationError(f"Evaluation failed: {e}")

    if verbose:
        print("\n=== EVALUATION ===")
        print("Result:", result)

    return result


def interactive_mode():
    """
    Run parser in interactive mode with improved error reporting.
    """
    print("Mini Parser - Interactive Mode")
    print("=" * 50)
    verbose = False

    while True:
        try:
            expression = input(">>> ").strip()

            if expression.lower() in ('quit', 'exit'):
                print("Goodbye!")
                break
            if expression.lower() == 'verbose':
                verbose = not verbose
                print(f"Verbose mode: {'ON' if verbose else 'OFF'}")
                continue
            if not expression:
                continue

            result = parse_and_evaluate(expression, verbose=verbose)
            if not verbose:
                print(result)

        except (TokenizationError, ParsingError, EvaluationError) as e:
            print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            # Catch any unexpected errors
            print(f"Unexpected Error: {e}")


def main():
    if len(sys.argv) == 1:
        print("Usage: python mini_parser.py <expression> or --interactive/-i")
        sys.exit(0)

    # Interactive mode
    if sys.argv[1] in ('--interactive', '-i'):
        interactive_mode()
        return

    # Verbose mode
    verbose = False
    expression_index = 1
    if sys.argv[1] in ('--verbose', '-v'):
        verbose = True
        expression_index = 2
        if len(sys.argv) < 3:
            print("Error: --verbose requires an expression argument")
            sys.exit(1)

    expression = sys.argv[expression_index]

    try:
        result = parse_and_evaluate(expression, verbose=verbose)
        print(result)
    except (TokenizationError, ParsingError, EvaluationError) as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

