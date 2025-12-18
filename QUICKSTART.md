# Quick Start Guide

## 快速开始指南

### Installation (安装)

No dependencies needed! Just Python 3.6+
无需安装依赖！只需要 Python 3.6+

```bash
git clone https://github.com/DARK20050101/first.git
cd first
```

### Run the Demo (运行演示)

```bash
python demo.py
```

### Run Tests (运行测试)

```bash
python test_equation_solver.py
```

### Use the Solver (使用求解器)

#### Method 1: Interactive Mode (交互模式)

```bash
python solver_cli.py
```

Then enter equations one by one:

```
Enter equation: 2x + 4 = 0
Solution: x = -2

Enter equation: x^2 - 5x + 6 = 0
Solution: x₁ = 3, x₂ = 2
```

#### Method 2: Single Equation (单次求解)

```bash
python solver_cli.py "x^2 - 4 = 0"
```

Output:
```
Equation: x^2 - 4 = 0
Solution: x₁ = 2, x₂ = -2
```

### Supported Equations (支持的方程类型)

✅ **Linear Equations (线性方程)**
- `2x + 4 = 0`
- `3x = 9`
- `5x = 2x + 6`

✅ **Quadratic Equations (二次方程)**
- `x^2 - 5x + 6 = 0` (two real roots / 两个实根)
- `x^2 + 2x + 1 = 0` (double root / 重根)
- `x^2 + x + 1 = 0` (complex roots / 复数根)

### Features (特性)

🚀 **Fast** - O(1) time complexity for both linear and quadratic equations
⚡ **快速** - 线性和二次方程都是 O(1) 时间复杂度

🎯 **Accurate** - Handles all edge cases including complex numbers
🎯 **准确** - 处理所有边界情况，包括复数

💻 **Easy to Use** - Simple command-line interface
💻 **易于使用** - 简单的命令行界面

✨ **Well Tested** - 20 unit tests with 100% pass rate
✨ **测试完善** - 20个单元测试，100%通过率

### Examples (示例)

```bash
# Linear equations
python solver_cli.py "2x + 4 = 0"        # x = -2
python solver_cli.py "3x - 9 = 0"        # x = 3
python solver_cli.py "5x = 2x + 6"       # x = 2

# Quadratic equations
python solver_cli.py "x^2 - 5x + 6 = 0"  # x₁ = 3, x₂ = 2
python solver_cli.py "x^2 + 2x + 1 = 0"  # x = -1 (double root)
python solver_cli.py "x^2 + x + 1 = 0"   # complex roots
python solver_cli.py "x^2 - 4 = 0"       # x₁ = 2, x₂ = -2
```

### Get Help (获取帮助)

```bash
python solver_cli.py --help
```

---

Have fun solving equations! 祝你使用愉快！ 🎓📐
