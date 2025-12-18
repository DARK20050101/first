#!/usr/bin/env python3
"""
Unit tests for the Equation Solver
"""

import unittest
from equation_solver import EquationSolver, format_solution


class TestLinearEquations(unittest.TestCase):
    """Test linear equation solving"""
    
    def setUp(self):
        self.solver = EquationSolver()
    
    def test_simple_linear(self):
        """Test simple linear equation: 2x + 4 = 0"""
        result = self.solver.solve_linear(2, 4)
        self.assertAlmostEqual(result, -2.0)
    
    def test_linear_positive_solution(self):
        """Test linear equation with positive solution: 3x - 9 = 0"""
        result = self.solver.solve_linear(3, -9)
        self.assertAlmostEqual(result, 3.0)
    
    def test_linear_zero_solution(self):
        """Test linear equation with zero solution: 5x = 0"""
        result = self.solver.solve_linear(5, 0)
        self.assertAlmostEqual(result, 0.0)
    
    def test_linear_fractional(self):
        """Test linear equation with fractional coefficient"""
        result = self.solver.solve_linear(2.5, 7.5)
        self.assertAlmostEqual(result, -3.0)
    
    def test_linear_no_solution(self):
        """Test invalid linear equation: 0x + 5 = 0"""
        with self.assertRaises(ValueError):
            self.solver.solve_linear(0, 5)


class TestQuadraticEquations(unittest.TestCase):
    """Test quadratic equation solving"""
    
    def setUp(self):
        self.solver = EquationSolver()
    
    def test_quadratic_two_real_roots(self):
        """Test quadratic with two distinct real roots: x^2 - 5x + 6 = 0"""
        x1, x2 = self.solver.solve_quadratic(1, -5, 6)
        # Roots should be 2 and 3
        roots = sorted([x1, x2])
        self.assertAlmostEqual(roots[0], 2.0)
        self.assertAlmostEqual(roots[1], 3.0)
    
    def test_quadratic_double_root(self):
        """Test quadratic with double root: x^2 + 2x + 1 = 0"""
        x1, x2 = self.solver.solve_quadratic(1, 2, 1)
        # Root should be -1 (double)
        self.assertAlmostEqual(x1, -1.0)
        self.assertAlmostEqual(x2, -1.0)
    
    def test_quadratic_complex_roots(self):
        """Test quadratic with complex roots: x^2 + x + 1 = 0"""
        x1, x2 = self.solver.solve_quadratic(1, 1, 1)
        # Check that roots are complex conjugates
        self.assertIsInstance(x1, complex)
        self.assertIsInstance(x2, complex)
        self.assertAlmostEqual(x1.real, -0.5)
        self.assertAlmostEqual(x2.real, -0.5)
    
    def test_quadratic_no_linear_term(self):
        """Test quadratic without linear term: x^2 - 4 = 0"""
        x1, x2 = self.solver.solve_quadratic(1, 0, -4)
        roots = sorted([x1, x2])
        self.assertAlmostEqual(roots[0], -2.0)
        self.assertAlmostEqual(roots[1], 2.0)
    
    def test_quadratic_no_constant_term(self):
        """Test quadratic without constant term: x^2 + 3x = 0"""
        x1, x2 = self.solver.solve_quadratic(1, 3, 0)
        roots = sorted([x1, x2])
        self.assertAlmostEqual(roots[0], -3.0)
        self.assertAlmostEqual(roots[1], 0.0)


class TestEquationParsing(unittest.TestCase):
    """Test equation string parsing"""
    
    def setUp(self):
        self.solver = EquationSolver()
    
    def test_parse_linear_simple(self):
        """Test parsing simple linear equation"""
        result = self.solver.solve("2x + 4 = 0")
        self.assertAlmostEqual(result, -2.0)
    
    def test_parse_linear_with_equals_right(self):
        """Test parsing linear equation: 3x = 9"""
        result = self.solver.solve("3x = 9")
        self.assertAlmostEqual(result, 3.0)
    
    def test_parse_linear_both_sides(self):
        """Test parsing linear equation with x on both sides"""
        result = self.solver.solve("5x = 2x + 6")
        self.assertAlmostEqual(result, 2.0)
    
    def test_parse_quadratic_standard(self):
        """Test parsing standard quadratic"""
        x1, x2 = self.solver.solve("x^2 - 5x + 6 = 0")
        roots = sorted([x1, x2])
        self.assertAlmostEqual(roots[0], 2.0)
        self.assertAlmostEqual(roots[1], 3.0)
    
    def test_parse_quadratic_with_spaces(self):
        """Test parsing quadratic with spaces"""
        x1, x2 = self.solver.solve("x^2 + 2x + 1 = 0")
        self.assertAlmostEqual(x1, -1.0)
        self.assertAlmostEqual(x2, -1.0)
    
    def test_parse_invalid_no_equals(self):
        """Test parsing equation without equals sign"""
        with self.assertRaises(ValueError):
            self.solver.solve("2x + 4")
    
    def test_parse_invalid_no_variable(self):
        """Test parsing equation without variable"""
        with self.assertRaises(ValueError):
            self.solver.solve("5 = 3")


class TestFormatSolution(unittest.TestCase):
    """Test solution formatting"""
    
    def test_format_single_solution(self):
        """Test formatting single solution"""
        result = format_solution(2.5)
        self.assertIn("2.5", result)
        self.assertIn("x", result)
    
    def test_format_two_solutions(self):
        """Test formatting two solutions"""
        result = format_solution((2.0, 3.0))
        self.assertIn("2", result)
        self.assertIn("3", result)
    
    def test_format_double_root(self):
        """Test formatting double root"""
        result = format_solution((-1.0, -1.0))
        self.assertIn("double root", result)


if __name__ == '__main__':
    unittest.main()
