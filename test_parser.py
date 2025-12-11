"""
Test Suite for Mini Parser
===========================

This module contains comprehensive tests for the mini parser.
It's a great way to learn how the parser works by seeing examples.
"""

import unittest
from tokenizer import Tokenizer, TokenType
from parser import Parser, Interpreter, NumberNode, BinaryOpNode


class TestTokenizer(unittest.TestCase):
    """Tests for the Tokenizer class."""
    
    def test_simple_addition(self):
        """Test tokenizing a simple addition expression."""
        tokenizer = Tokenizer("3 + 5")
        tokens = tokenizer.tokenize()
        
        self.assertEqual(len(tokens), 4)  # 3 tokens + EOF
        self.assertEqual(tokens[0].type, TokenType.NUMBER)
        self.assertEqual(tokens[0].value, 3.0)
        self.assertEqual(tokens[1].type, TokenType.PLUS)
        self.assertEqual(tokens[2].type, TokenType.NUMBER)
        self.assertEqual(tokens[2].value, 5.0)
        self.assertEqual(tokens[3].type, TokenType.EOF)
    
    def test_all_operators(self):
        """Test that all operators are recognized."""
        tokenizer = Tokenizer("1 + 2 - 3 * 4 / 5")
        tokens = tokenizer.tokenize()
        
        operator_types = [t.type for t in tokens if t.type != TokenType.NUMBER and t.type != TokenType.EOF]
        expected = [TokenType.PLUS, TokenType.MINUS, TokenType.MULTIPLY, TokenType.DIVIDE]
        
        self.assertEqual(operator_types, expected)
    
    def test_parentheses(self):
        """Test tokenizing parentheses."""
        tokenizer = Tokenizer("(3 + 5) * 2")
        tokens = tokenizer.tokenize()
        
        self.assertEqual(tokens[0].type, TokenType.LPAREN)
        self.assertEqual(tokens[4].type, TokenType.RPAREN)
    
    def test_decimal_numbers(self):
        """Test tokenizing decimal numbers."""
        tokenizer = Tokenizer("3.14 + 2.5")
        tokens = tokenizer.tokenize()
        
        self.assertEqual(tokens[0].value, 3.14)
        self.assertEqual(tokens[2].value, 2.5)
    
    def test_leading_decimal_point(self):
        """Test tokenizing numbers with leading decimal point."""
        tokenizer = Tokenizer(".5 + .25")
        tokens = tokenizer.tokenize()
        
        self.assertEqual(tokens[0].value, 0.5)
        self.assertEqual(tokens[2].value, 0.25)
    
    def test_whitespace_handling(self):
        """Test that whitespace is properly ignored."""
        tokenizer1 = Tokenizer("3+5")
        tokenizer2 = Tokenizer("3 + 5")
        tokenizer3 = Tokenizer("  3   +   5  ")
        
        tokens1 = tokenizer1.tokenize()
        tokens2 = tokenizer2.tokenize()
        tokens3 = tokenizer3.tokenize()
        
        # All should produce the same tokens
        self.assertEqual(len(tokens1), len(tokens2))
        self.assertEqual(len(tokens2), len(tokens3))
    
    def test_invalid_character(self):
        """Test that invalid characters raise an error."""
        tokenizer = Tokenizer("3 + @")
        
        with self.assertRaises(ValueError) as context:
            tokenizer.tokenize()
        
        self.assertIn("Unexpected character", str(context.exception))
    
    def test_multiple_decimal_points(self):
        """Test that numbers with multiple decimal points raise an error."""
        tokenizer = Tokenizer("3.14.15")
        
        with self.assertRaises(ValueError) as context:
            tokenizer.tokenize()
        
        self.assertIn("multiple decimal points", str(context.exception))
    
    def test_standalone_decimal_point(self):
        """Test that a standalone decimal point raises an error."""
        tokenizer = Tokenizer("3 + .")
        
        with self.assertRaises(ValueError) as context:
            tokenizer.tokenize()
        
        # A standalone decimal point is caught as an unexpected character
        self.assertIn("Unexpected character", str(context.exception))


class TestParser(unittest.TestCase):
    """Tests for the Parser class."""
    
    def setUp(self):
        """Set up an interpreter for evaluation tests."""
        self.interpreter = Interpreter()
    
    def parse(self, expression):
        """Helper method to tokenize and parse an expression."""
        tokenizer = Tokenizer(expression)
        tokens = tokenizer.tokenize()
        parser = Parser(tokens)
        return parser.parse()
    
    def evaluate(self, expression):
        """Helper method to parse and evaluate an expression."""
        ast = self.parse(expression)
        return self.interpreter.evaluate(ast)
    
    def test_simple_addition(self):
        """Test parsing and evaluating simple addition."""
        result = self.evaluate("3 + 5")
        self.assertEqual(result, 8.0)
    
    def test_simple_subtraction(self):
        """Test parsing and evaluating simple subtraction."""
        result = self.evaluate("10 - 3")
        self.assertEqual(result, 7.0)
    
    def test_simple_multiplication(self):
        """Test parsing and evaluating simple multiplication."""
        result = self.evaluate("4 * 5")
        self.assertEqual(result, 20.0)
    
    def test_simple_division(self):
        """Test parsing and evaluating simple division."""
        result = self.evaluate("20 / 4")
        self.assertEqual(result, 5.0)
    
    def test_operator_precedence(self):
        """Test that multiplication has higher precedence than addition."""
        result = self.evaluate("2 + 3 * 4")
        self.assertEqual(result, 14.0)  # Not 20
        
        result = self.evaluate("10 - 2 * 3")
        self.assertEqual(result, 4.0)  # Not 24
    
    def test_parentheses_override_precedence(self):
        """Test that parentheses can override operator precedence."""
        result = self.evaluate("(2 + 3) * 4")
        self.assertEqual(result, 20.0)
        
        result = self.evaluate("(10 - 2) * 3")
        self.assertEqual(result, 24.0)
    
    def test_nested_parentheses(self):
        """Test nested parentheses."""
        result = self.evaluate("((2 + 3) * 4) + 1")
        self.assertEqual(result, 21.0)
        
        result = self.evaluate("2 * (3 + (4 * 5))")
        self.assertEqual(result, 46.0)
    
    def test_unary_minus(self):
        """Test unary minus operator."""
        result = self.evaluate("-5")
        self.assertEqual(result, -5.0)
        
        result = self.evaluate("-5 + 10")
        self.assertEqual(result, 5.0)
        
        result = self.evaluate("10 + -5")
        self.assertEqual(result, 5.0)
    
    def test_unary_plus(self):
        """Test unary plus operator."""
        result = self.evaluate("+5")
        self.assertEqual(result, 5.0)
    
    def test_complex_expression(self):
        """Test a complex expression with multiple operators."""
        result = self.evaluate("100 / (2 + 3) * 2")
        self.assertEqual(result, 40.0)
        
        result = self.evaluate("2 + 3 * 4 - 5 / 5")
        self.assertEqual(result, 13.0)
    
    def test_division_by_zero(self):
        """Test that division by zero raises an error."""
        with self.assertRaises(ValueError) as context:
            self.evaluate("10 / 0")
        
        self.assertIn("Division by zero", str(context.exception))
    
    def test_decimal_operations(self):
        """Test operations with decimal numbers."""
        result = self.evaluate("3.5 + 2.5")
        self.assertEqual(result, 6.0)
        
        result = self.evaluate("10.5 / 2")
        self.assertEqual(result, 5.25)
    
    def test_mismatched_parentheses(self):
        """Test that mismatched parentheses raise an error."""
        with self.assertRaises(ValueError):
            self.parse("(3 + 5")
        
        with self.assertRaises(ValueError):
            self.parse("3 + 5)")
    
    def test_empty_expression(self):
        """Test that an empty expression is handled."""
        # An empty string should have just EOF token
        tokenizer = Tokenizer("")
        tokens = tokenizer.tokenize()
        self.assertEqual(len(tokens), 1)
        self.assertEqual(tokens[0].type, TokenType.EOF)
    
    def test_multiple_operations_same_precedence(self):
        """Test left-to-right evaluation for same precedence operators."""
        # Addition and subtraction (left to right)
        result = self.evaluate("10 - 3 + 2")
        self.assertEqual(result, 9.0)  # (10 - 3) + 2
        
        # Multiplication and division (left to right)
        result = self.evaluate("20 / 4 * 2")
        self.assertEqual(result, 10.0)  # (20 / 4) * 2


class TestInterpreter(unittest.TestCase):
    """Tests for the Interpreter class."""
    
    def setUp(self):
        """Set up an interpreter instance."""
        self.interpreter = Interpreter()
    
    def evaluate(self, expression):
        """Helper method to parse and evaluate an expression."""
        tokenizer = Tokenizer(expression)
        tokens = tokenizer.tokenize()
        parser = Parser(tokens)
        ast = parser.parse()
        return self.interpreter.evaluate(ast)
    
    def test_large_numbers(self):
        """Test evaluation with large numbers."""
        result = self.evaluate("1000000 + 2000000")
        self.assertEqual(result, 3000000.0)
    
    def test_floating_point_precision(self):
        """Test that floating point operations work correctly."""
        result = self.evaluate("0.1 + 0.2")
        self.assertAlmostEqual(result, 0.3, places=10)
    
    def test_negative_results(self):
        """Test expressions that result in negative numbers."""
        result = self.evaluate("5 - 10")
        self.assertEqual(result, -5.0)


def run_tests():
    """Run all tests and print results."""
    # Create a test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add all test classes
    suite.addTests(loader.loadTestsFromTestCase(TestTokenizer))
    suite.addTests(loader.loadTestsFromTestCase(TestParser))
    suite.addTests(loader.loadTestsFromTestCase(TestInterpreter))
    
    # Run the tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Return success/failure
    return result.wasSuccessful()


if __name__ == "__main__":
    success = run_tests()
    exit(0 if success else 1)
