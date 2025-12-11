"""
Tokenizer Module
================

This module handles breaking input strings into tokens.
A token is the smallest unit of meaning in the input.

For example: "3 + 5" becomes tokens: NUMBER(3), PLUS, NUMBER(5)
"""

from enum import Enum, auto
from dataclasses import dataclass
from typing import List, Optional, Union


class TokenType(Enum):
    """
    Defines all possible token types our parser can recognize.
    
    Using Enum makes the code more readable and prevents typos.
    """
    NUMBER = auto()      # Integer or float numbers
    PLUS = auto()        # + operator
    MINUS = auto()       # - operator
    MULTIPLY = auto()    # * operator
    DIVIDE = auto()      # / operator
    LPAREN = auto()      # ( left parenthesis
    RPAREN = auto()      # ) right parenthesis
    EOF = auto()         # End of file/input


@dataclass
class Token:
    """
    Represents a single token with its type and value.
    
    Attributes:
        type: The TokenType of this token
        value: The actual value (e.g., the number 42 or the operator '+')
        position: Position in the input string (for error messages)
    """
    type: TokenType
    value: Union[float, str, None]
    position: int
    
    def __repr__(self):
        return f"Token({self.type.name}, {self.value}, pos={self.position})"


class Tokenizer:
    """
    Converts input text into a list of tokens.
    
    This is also called "lexical analysis" or "scanning".
    The tokenizer reads character by character and groups them into tokens.
    
    Example:
        >>> tokenizer = Tokenizer("3 + 5")
        >>> tokens = tokenizer.tokenize()
        >>> print(tokens)
        [Token(NUMBER, 3, pos=0), Token(PLUS, +, pos=2), Token(NUMBER, 5, pos=4)]
    """
    
    def __init__(self, text: str):
        """
        Initialize the tokenizer with input text.
        
        Args:
            text: The string to tokenize
        """
        self.text = text
        self.position = 0
        self.current_char = self.text[0] if text else None
    
    def error(self, message: str):
        """Raise a tokenization error with helpful context."""
        raise ValueError(f"Tokenizer error at position {self.position}: {message}")
    
    def advance(self):
        """Move to the next character in the input."""
        self.position += 1
        if self.position < len(self.text):
            self.current_char = self.text[self.position]
        else:
            self.current_char = None
    
    def skip_whitespace(self):
        """Skip over whitespace characters (spaces, tabs, newlines)."""
        while self.current_char is not None and self.current_char.isspace():
            self.advance()
    
    def read_number(self) -> float:
        """
        Read a number from the input.
        
        Supports both integers and decimals.
        Examples: 42, 3.14, 0.5
        
        Returns:
            The number as a float
        """
        num_str = ""
        start_pos = self.position
        has_decimal = False
        
        # Read digits and at most one decimal point
        while self.current_char is not None and (
            self.current_char.isdigit() or self.current_char == '.'
        ):
            if self.current_char == '.':
                if has_decimal:
                    # Already have a decimal point
                    self.error(f"Invalid number: multiple decimal points")
                has_decimal = True
            num_str += self.current_char
            self.advance()
        
        # Validate that we have at least one digit
        if not num_str or num_str == '.':
            self.error(f"Invalid number: {num_str if num_str else 'empty'}")
        
        try:
            # Try to convert to float
            return float(num_str)
        except ValueError:
            self.error(f"Invalid number: {num_str}")
    
    def tokenize(self) -> List[Token]:
        """
        Convert the input text into a list of tokens.
        
        This is the main method that performs tokenization.
        
        Returns:
            List of Token objects representing the input
        
        Raises:
            ValueError: If an unexpected character is encountered
        """
        tokens = []
        
        while self.current_char is not None:
            # Skip whitespace
            if self.current_char.isspace():
                self.skip_whitespace()
                continue
            
            # Numbers (including those starting with decimal point like .5)
            if self.current_char.isdigit() or (
                self.current_char == '.' and 
                self.position + 1 < len(self.text) and 
                self.text[self.position + 1].isdigit()
            ):
                token_pos = self.position
                number = self.read_number()
                tokens.append(Token(TokenType.NUMBER, number, token_pos))
                continue
            
            # Single-character tokens
            token_pos = self.position
            
            if self.current_char == '+':
                tokens.append(Token(TokenType.PLUS, '+', token_pos))
                self.advance()
            elif self.current_char == '-':
                tokens.append(Token(TokenType.MINUS, '-', token_pos))
                self.advance()
            elif self.current_char == '*':
                tokens.append(Token(TokenType.MULTIPLY, '*', token_pos))
                self.advance()
            elif self.current_char == '/':
                tokens.append(Token(TokenType.DIVIDE, '/', token_pos))
                self.advance()
            elif self.current_char == '(':
                tokens.append(Token(TokenType.LPAREN, '(', token_pos))
                self.advance()
            elif self.current_char == ')':
                tokens.append(Token(TokenType.RPAREN, ')', token_pos))
                self.advance()
            else:
                self.error(f"Unexpected character: '{self.current_char}'")
        
        # Add EOF token to mark the end
        tokens.append(Token(TokenType.EOF, None, self.position))
        return tokens


# Example usage
if __name__ == "__main__":
    # Example 1: Simple addition
    tokenizer = Tokenizer("3 + 5")
    tokens = tokenizer.tokenize()
    print("Example 1: '3 + 5'")
    for token in tokens:
        print(f"  {token}")
    
    print()
    
    # Example 2: Complex expression with parentheses
    tokenizer = Tokenizer("(10 + 2) * 3")
    tokens = tokenizer.tokenize()
    print("Example 2: '(10 + 2) * 3'")
    for token in tokens:
        print(f"  {token}")
