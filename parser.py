"""
Parser Module
=============

This module implements a recursive descent parser for mathematical expressions.
It takes tokens from the tokenizer and builds an Abstract Syntax Tree (AST).

The parser respects operator precedence:
  - Parentheses: highest
  - Multiplication and Division: medium
  - Addition and Subtraction: lowest

Grammar (in EBNF notation):
    expression  := term ((PLUS | MINUS) term)*
    term        := factor ((MULTIPLY | DIVIDE) factor)*
    factor      := NUMBER | LPAREN expression RPAREN | (PLUS|MINUS) factor
"""

from tokenizer import Token, TokenType, Tokenizer
from typing import Optional, List


class ASTNode:
    """
    Base class for all Abstract Syntax Tree nodes.
    
    An AST represents the structure of the expression in a tree form,
    which makes it easy to evaluate or transform.
    """
    pass


class NumberNode(ASTNode):
    """
    Represents a number in the AST.
    
    Example: In "3 + 5", both 3 and 5 are NumberNodes.
    """
    def __init__(self, value: float):
        self.value = value
    
    def __repr__(self):
        return f"Number({self.value})"


class BinaryOpNode(ASTNode):
    """
    Represents a binary operation (an operation with two operands).
    
    Examples: 
      - "3 + 5" becomes BinaryOpNode(+, Number(3), Number(5))
      - "2 * 4" becomes BinaryOpNode(*, Number(2), Number(4))
    
    Attributes:
        operator: The operator token (PLUS, MINUS, etc.)
        left: The left operand (another ASTNode)
        right: The right operand (another ASTNode)
    """
    def __init__(self, operator: Token, left: ASTNode, right: ASTNode):
        self.operator = operator
        self.left = left
        self.right = right
    
    def __repr__(self):
        return f"BinaryOp({self.operator.value}, {self.left}, {self.right})"


class UnaryOpNode(ASTNode):
    """
    Represents a unary operation (an operation with one operand).
    
    Example: "-5" becomes UnaryOpNode(-, Number(5))
    
    Attributes:
        operator: The operator token (PLUS or MINUS)
        operand: The operand (another ASTNode)
    """
    def __init__(self, operator: Token, operand: ASTNode):
        self.operator = operator
        self.operand = operand
    
    def __repr__(self):
        return f"UnaryOp({self.operator.value}, {self.operand})"


class Parser:
    """
    Parses tokens into an Abstract Syntax Tree (AST).
    
    This is a recursive descent parser, which means it uses recursive
    functions that mirror the grammar rules.
    
    Example:
        >>> tokenizer = Tokenizer("3 + 5 * 2")
        >>> tokens = tokenizer.tokenize()
        >>> parser = Parser(tokens)
        >>> ast = parser.parse()
        >>> print(ast)
        BinaryOp(+, Number(3.0), BinaryOp(*, Number(5.0), Number(2.0)))
    """
    
    def __init__(self, tokens: List[Token]):
        """
        Initialize the parser with a list of tokens.
        
        Args:
            tokens: List of Token objects from the tokenizer
        """
        self.tokens = tokens
        self.position = 0
        self.current_token = self.tokens[0] if tokens else None
    
    def error(self, message: str):
        """Raise a parsing error with context."""
        raise ValueError(
            f"Parser error at position {self.current_token.position}: {message}\n"
            f"Current token: {self.current_token}"
        )
    
    def advance(self):
        """Move to the next token."""
        self.position += 1
        if self.position < len(self.tokens):
            self.current_token = self.tokens[self.position]
    
    def expect(self, token_type: TokenType):
        """
        Verify that the current token matches the expected type.
        
        Args:
            token_type: The expected TokenType
        
        Raises:
            ValueError: If the current token doesn't match
        """
        if self.current_token.type != token_type:
            self.error(f"Expected {token_type.name}, got {self.current_token.type.name}")
    
    def factor(self) -> ASTNode:
        """
        Parse a factor (the highest precedence items).
        
        Grammar: factor := NUMBER | LPAREN expression RPAREN | (PLUS|MINUS) factor
        
        This handles:
          - Numbers: 42, 3.14
          - Parenthesized expressions: (3 + 5)
          - Unary operators: -5, +3
        
        Returns:
            An ASTNode representing the factor
        """
        token = self.current_token
        
        # Unary plus or minus
        if token.type in (TokenType.PLUS, TokenType.MINUS):
            self.advance()
            return UnaryOpNode(token, self.factor())
        
        # Number
        elif token.type == TokenType.NUMBER:
            self.advance()
            return NumberNode(token.value)
        
        # Parenthesized expression
        elif token.type == TokenType.LPAREN:
            self.advance()
            node = self.expression()
            self.expect(TokenType.RPAREN)
            self.advance()
            return node
        
        else:
            self.error(f"Unexpected token in factor: {token.type.name}")
    
    def term(self) -> ASTNode:
        """
        Parse a term (multiplication and division).
        
        Grammar: term := factor ((MULTIPLY | DIVIDE) factor)*
        
        This handles expressions like:
          - 3 * 5
          - 10 / 2
          - 2 * 3 * 4
        
        Returns:
            An ASTNode representing the term
        """
        node = self.factor()
        
        while self.current_token.type in (TokenType.MULTIPLY, TokenType.DIVIDE):
            operator = self.current_token
            self.advance()
            node = BinaryOpNode(operator, node, self.factor())
        
        return node
    
    def expression(self) -> ASTNode:
        """
        Parse an expression (addition and subtraction).
        
        Grammar: expression := term ((PLUS | MINUS) term)*
        
        This is the lowest precedence level, so it's called first.
        It handles expressions like:
          - 3 + 5
          - 10 - 2
          - 2 + 3 * 4 (correctly evaluates as 2 + (3 * 4))
        
        Returns:
            An ASTNode representing the expression
        """
        node = self.term()
        
        while self.current_token.type in (TokenType.PLUS, TokenType.MINUS):
            operator = self.current_token
            self.advance()
            node = BinaryOpNode(operator, node, self.term())
        
        return node
    
    def parse(self) -> ASTNode:
        """
        Parse the tokens and return the root of the AST.
        
        This is the main entry point for parsing.
        
        Returns:
            The root ASTNode of the parsed expression
        
        Raises:
            ValueError: If there's a syntax error
        """
        ast = self.expression()
        
        # Make sure we consumed all tokens (except EOF)
        if self.current_token.type != TokenType.EOF:
            self.error(f"Unexpected token after expression: {self.current_token.type.name}")
        
        return ast


class Interpreter:
    """
    Evaluates an AST and returns the result.
    
    This is also called the "semantic analysis" phase.
    It walks the tree and computes the actual values.
    
    Example:
        >>> tokenizer = Tokenizer("3 + 5")
        >>> tokens = tokenizer.tokenize()
        >>> parser = Parser(tokens)
        >>> ast = parser.parse()
        >>> interpreter = Interpreter()
        >>> result = interpreter.evaluate(ast)
        >>> print(result)
        8.0
    """
    
    def evaluate(self, node: ASTNode) -> float:
        """
        Recursively evaluate an AST node.
        
        Args:
            node: The ASTNode to evaluate
        
        Returns:
            The numeric result
        
        Raises:
            ValueError: If there's a runtime error (like division by zero)
        """
        if isinstance(node, NumberNode):
            return node.value
        
        elif isinstance(node, UnaryOpNode):
            operand = self.evaluate(node.operand)
            if node.operator.type == TokenType.PLUS:
                return +operand
            elif node.operator.type == TokenType.MINUS:
                return -operand
            else:
                raise ValueError(f"Unknown unary operator: {node.operator.type}")
        
        elif isinstance(node, BinaryOpNode):
            left = self.evaluate(node.left)
            right = self.evaluate(node.right)
            
            if node.operator.type == TokenType.PLUS:
                return left + right
            elif node.operator.type == TokenType.MINUS:
                return left - right
            elif node.operator.type == TokenType.MULTIPLY:
                return left * right
            elif node.operator.type == TokenType.DIVIDE:
                if right == 0:
                    raise ValueError("Division by zero")
                return left / right
            else:
                raise ValueError(f"Unknown binary operator: {node.operator.type}")
        
        raise ValueError(f"Unknown node type: {type(node)}")


# Example usage
if __name__ == "__main__":
    examples = [
        "3 + 5",
        "10 - 2 * 3",
        "(10 - 2) * 3",
        "2 + 3 * 4",
        "-5 + 10",
        "100 / (2 + 3) * 2"
    ]
    
    interpreter = Interpreter()
    
    print("Mini Parser Examples")
    print("=" * 50)
    
    for expr in examples:
        try:
            # Tokenize
            tokenizer = Tokenizer(expr)
            tokens = tokenizer.tokenize()
            
            # Parse
            parser = Parser(tokens)
            ast = parser.parse()
            
            # Evaluate
            result = interpreter.evaluate(ast)
            
            print(f"\nExpression: {expr}")
            print(f"AST: {ast}")
            print(f"Result: {result}")
            
        except Exception as e:
            print(f"\nExpression: {expr}")
            print(f"Error: {e}")
