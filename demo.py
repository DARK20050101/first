#!/usr/bin/env python3
"""
Demo script for the Equation Solver
Shows various examples of equation solving
"""

from equation_solver import EquationSolver, format_solution
import time


def print_separator():
    print("\n" + "=" * 60 + "\n")


def demo_solver():
    """Demonstrate the equation solver with various examples"""
    solver = EquationSolver()
    
    print("╔" + "=" * 58 + "╗")
    print("║" + " " * 10 + "快速方程求解器演示 (Equation Solver Demo)" + " " * 9 + "║")
    print("╚" + "=" * 58 + "╝")
    
    # Linear equations demo
    print_separator()
    print("📐 LINEAR EQUATIONS (线性方程)")
    print("-" * 60)
    
    examples = [
        ("2x + 4 = 0", "Simple linear equation"),
        ("3x - 9 = 0", "Linear equation with positive solution"),
        ("5x = 2x + 6", "Variables on both sides"),
        ("-4x + 8 = 0", "Negative coefficient"),
    ]
    
    for equation, description in examples:
        print(f"\n{description}")
        print(f"Equation: {equation}")
        try:
            result = solver.solve(equation)
            print(f"Solution: {format_solution(result)}")
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(0.3)
    
    # Quadratic equations demo
    print_separator()
    print("📈 QUADRATIC EQUATIONS (二次方程)")
    print("-" * 60)
    
    examples = [
        ("x^2 - 5x + 6 = 0", "Two distinct real roots"),
        ("x^2 + 2x + 1 = 0", "One double root (perfect square)"),
        ("x^2 - 4 = 0", "Difference of squares"),
        ("x^2 + 3x = 0", "Missing constant term"),
        ("x^2 + x + 1 = 0", "Complex roots (无实数解)"),
        ("2x^2 - 8 = 0", "Coefficient on x^2 term"),
    ]
    
    for equation, description in examples:
        print(f"\n{description}")
        print(f"Equation: {equation}")
        try:
            result = solver.solve(equation)
            print(f"Solution: {format_solution(result)}")
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(0.3)
    
    # Special cases
    print_separator()
    print("⚠️  SPECIAL CASES (特殊情况)")
    print("-" * 60)
    
    print("\nPositive discriminant (Δ > 0): Two distinct real roots")
    equation = "x^2 - 7x + 10 = 0"
    print(f"Equation: {equation}")
    result = solver.solve(equation)
    print(f"Solution: {format_solution(result)}")
    
    print("\nZero discriminant (Δ = 0): One double root")
    equation = "x^2 - 6x + 9 = 0"
    print(f"Equation: {equation}")
    result = solver.solve(equation)
    print(f"Solution: {format_solution(result)}")
    
    print("\nNegative discriminant (Δ < 0): Complex roots")
    equation = "x^2 + 2x + 5 = 0"
    print(f"Equation: {equation}")
    result = solver.solve(equation)
    print(f"Solution: {format_solution(result)}")
    
    # Summary
    print_separator()
    print("✅ SUMMARY (总结)")
    print("-" * 60)
    print("\n✓ Linear equations: Fast O(1) solution")
    print("✓ Quadratic equations: Handles all cases")
    print("✓ Real solutions: Precise calculations")
    print("✓ Complex solutions: Automatic detection")
    print("✓ Easy to use: Simple string input format")
    
    print_separator()
    print("Try it yourself:")
    print("  python solver_cli.py              # Interactive mode")
    print("  python solver_cli.py 'x^2 - 4 = 0'  # Single equation")
    print_separator()


if __name__ == "__main__":
    demo_solver()
