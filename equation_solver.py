#!/usr/bin/env python3
"""
Equation Solver - A fast equation solving application
Supports linear, quadratic, and general algebraic equations
"""

import re
from typing import Union, List, Dict, Tuple


class EquationSolver:
    """A class to solve various types of equations"""
    
    def __init__(self):
        self.variable = 'x'
    
    def solve_linear(self, a: float, b: float) -> float:
        """
        Solve linear equation: ax + b = 0
        
        Args:
            a: coefficient of x
            b: constant term
            
        Returns:
            Solution to the equation
            
        Raises:
            ValueError: If a is zero (not a linear equation)
        """
        if a == 0:
            if b == 0:
                raise ValueError("Infinite solutions: 0 = 0")
            else:
                raise ValueError("No solution: equation is inconsistent")
        
        return -b / a
    
    def solve_quadratic(self, a: float, b: float, c: float) -> Tuple[Union[float, complex], Union[float, complex]]:
        """
        Solve quadratic equation: ax^2 + bx + c = 0
        
        Args:
            a: coefficient of x^2
            b: coefficient of x
            c: constant term
            
        Returns:
            Tuple of two solutions (may be complex numbers)
            
        Raises:
            ValueError: If a is zero (not a quadratic equation)
        """
        if a == 0:
            # It's actually a linear equation
            x = self.solve_linear(b, c)
            return (x, x)
        
        discriminant = b**2 - 4*a*c
        
        if discriminant >= 0:
            # Real solutions
            sqrt_discriminant = discriminant ** 0.5
            x1 = (-b + sqrt_discriminant) / (2*a)
            x2 = (-b - sqrt_discriminant) / (2*a)
        else:
            # Complex solutions
            sqrt_discriminant = (abs(discriminant) ** 0.5) * 1j
            x1 = (-b + sqrt_discriminant) / (2*a)
            x2 = (-b - sqrt_discriminant) / (2*a)
        
        return (x1, x2)
    
    def parse_equation(self, equation_str: str) -> Dict[str, any]:
        """
        Parse equation string to extract coefficients
        
        Args:
            equation_str: Equation as string (e.g., "2x + 3 = 0", "x^2 - 5x + 6 = 0")
            
        Returns:
            Dictionary with equation type and coefficients
        """
        # Remove spaces and convert to lowercase
        equation = equation_str.replace(" ", "").lower()
        
        # Split by equals sign
        if "=" not in equation:
            raise ValueError("Equation must contain '=' sign")
        
        left, right = equation.split("=")
        
        # Move everything to left side (subtract right from left)
        # This means we're solving: left - right = 0
        
        # Parse for quadratic equation
        if "x^2" in equation or "x²" in equation:
            # Extract coefficients for ax^2 + bx + c = 0
            a = self._extract_coefficient(left, r'([+-]?\d*\.?\d*)x[\^²]2') - \
                self._extract_coefficient(right, r'([+-]?\d*\.?\d*)x[\^²]2')
            b = self._extract_coefficient(left, r'([+-]?\d*\.?\d*)x(?![²\^])') - \
                self._extract_coefficient(right, r'([+-]?\d*\.?\d*)x(?![²\^])')
            c = self._extract_constant(left) - self._extract_constant(right)
            
            return {'type': 'quadratic', 'a': a, 'b': b, 'c': c}
        
        # Parse for linear equation
        elif "x" in equation:
            a = self._extract_coefficient(left, r'([+-]?\d*\.?\d*)x') - \
                self._extract_coefficient(right, r'([+-]?\d*\.?\d*)x')
            b = self._extract_constant(left) - self._extract_constant(right)
            
            return {'type': 'linear', 'a': a, 'b': b}
        
        else:
            raise ValueError("No variable found in equation")
    
    def _extract_coefficient(self, expr: str, pattern: str) -> float:
        """Extract coefficient from expression using regex pattern"""
        matches = re.findall(pattern, expr)
        if not matches:
            return 0.0
        
        total = 0.0
        for match in matches:
            if match in ['', '+']:
                total += 1.0
            elif match == '-':
                total -= 1.0
            else:
                total += float(match)
        
        return total
    
    def _extract_constant(self, expr: str) -> float:
        """Extract constant terms from expression"""
        # Remove all terms with x
        expr_no_x = re.sub(r'[+-]?\d*\.?\d*x[\^²]?\d?', '', expr)
        
        if not expr_no_x or expr_no_x in ['+', '-']:
            return 0.0
        
        # Find all numbers
        matches = re.findall(r'[+-]?\d+\.?\d*', expr_no_x)
        
        if not matches:
            return 0.0
        
        return sum(float(m) for m in matches)
    
    def solve(self, equation_str: str) -> Union[float, List[float], List[complex]]:
        """
        Solve any supported equation
        
        Args:
            equation_str: Equation as string
            
        Returns:
            Solution(s) to the equation
        """
        parsed = self.parse_equation(equation_str)
        
        if parsed['type'] == 'linear':
            return self.solve_linear(parsed['a'], parsed['b'])
        elif parsed['type'] == 'quadratic':
            return self.solve_quadratic(parsed['a'], parsed['b'], parsed['c'])
        else:
            raise ValueError(f"Unsupported equation type: {parsed['type']}")


def format_solution(solution: Union[float, Tuple, List]) -> str:
    """Format solution for display"""
    if isinstance(solution, (int, float)):
        return f"x = {solution:.6g}"
    elif isinstance(solution, tuple) or isinstance(solution, list):
        if len(solution) == 2:
            x1, x2 = solution
            if isinstance(x1, complex) or isinstance(x2, complex):
                return f"x₁ = {x1}, x₂ = {x2}"
            elif abs(x1 - x2) < 1e-10:
                return f"x = {x1:.6g} (double root)"
            else:
                return f"x₁ = {x1:.6g}, x₂ = {x2:.6g}"
    return str(solution)


if __name__ == "__main__":
    # Quick test examples
    solver = EquationSolver()
    
    print("Equation Solver - Quick Tests")
    print("=" * 50)
    
    # Test linear equations
    print("\n1. Linear equation: 2x + 4 = 0")
    result = solver.solve("2x + 4 = 0")
    print(f"   Solution: {format_solution(result)}")
    
    print("\n2. Linear equation: 3x - 9 = 0")
    result = solver.solve("3x - 9 = 0")
    print(f"   Solution: {format_solution(result)}")
    
    # Test quadratic equations
    print("\n3. Quadratic equation: x^2 - 5x + 6 = 0")
    result = solver.solve("x^2 - 5x + 6 = 0")
    print(f"   Solution: {format_solution(result)}")
    
    print("\n4. Quadratic equation: x^2 + 2x + 1 = 0")
    result = solver.solve("x^2 + 2x + 1 = 0")
    print(f"   Solution: {format_solution(result)}")
    
    print("\n5. Quadratic equation (complex roots): x^2 + x + 1 = 0")
    result = solver.solve("x^2 + x + 1 = 0")
    print(f"   Solution: {format_solution(result)}")
