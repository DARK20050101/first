#!/usr/bin/env python3
"""
Command-line interface for the Equation Solver
"""

import sys
from equation_solver import EquationSolver, format_solution


def print_banner():
    """Print application banner"""
    print("=" * 60)
    print("  快速方程求解器 (Quick Equation Solver)")
    print("=" * 60)
    print("Supports:")
    print("  • Linear equations: ax + b = 0")
    print("  • Quadratic equations: ax² + bx + c = 0")
    print()


def print_help():
    """Print help information"""
    print("Usage:")
    print("  python solver_cli.py                    - Interactive mode")
    print("  python solver_cli.py 'equation'         - Solve single equation")
    print()
    print("Examples:")
    print("  python solver_cli.py '2x + 4 = 0'")
    print("  python solver_cli.py 'x^2 - 5x + 6 = 0'")
    print("  python solver_cli.py 'x^2 + x + 1 = 0'")
    print()
    print("Equation format:")
    print("  • Use 'x' as the variable")
    print("  • Use '^' or '²' for squared terms (e.g., x^2 or x²)")
    print("  • Include '=' sign in the equation")
    print("  • Examples: '2x + 3 = 7', 'x^2 - 4 = 0', '3x = 15'")
    print()


def solve_equation_interactive():
    """Interactive mode for solving equations"""
    solver = EquationSolver()
    
    print_banner()
    print("Interactive Mode - Enter equations to solve")
    print("Commands: 'help' for help, 'exit' or 'quit' to exit")
    print()
    
    while True:
        try:
            equation = input("Enter equation: ").strip()
            
            if not equation:
                continue
            
            if equation.lower() in ['exit', 'quit', 'q']:
                print("Goodbye!")
                break
            
            if equation.lower() in ['help', 'h', '?']:
                print()
                print_help()
                continue
            
            # Solve the equation
            result = solver.solve(equation)
            print(f"Solution: {format_solution(result)}")
            print()
            
        except ValueError as e:
            print(f"Error: {e}")
            print("Type 'help' for usage instructions")
            print()
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"Unexpected error: {e}")
            print()


def solve_equation_single(equation: str):
    """Solve a single equation from command line"""
    solver = EquationSolver()
    
    try:
        result = solver.solve(equation)
        print(f"Equation: {equation}")
        print(f"Solution: {format_solution(result)}")
        return 0
    except ValueError as e:
        print(f"Error: {e}")
        return 1
    except Exception as e:
        print(f"Unexpected error: {e}")
        return 1


def main():
    """Main entry point"""
    if len(sys.argv) > 1:
        if sys.argv[1] in ['-h', '--help', 'help']:
            print_banner()
            print_help()
            return 0
        else:
            # Solve equation from command line argument
            equation = ' '.join(sys.argv[1:])
            return solve_equation_single(equation)
    else:
        # Interactive mode
        solve_equation_interactive()
        return 0


if __name__ == "__main__":
    sys.exit(main())
