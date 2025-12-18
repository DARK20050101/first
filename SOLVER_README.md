# 快速方程求解器 (Quick Equation Solver)

一个快速解方程的命令行应用程序，支持线性方程和二次方程求解。

A fast command-line application for solving equations, supporting linear and quadratic equations.

## 功能特点 (Features)

- ✅ 线性方程求解 (Linear equation solver): `ax + b = 0`
- ✅ 二次方程求解 (Quadratic equation solver): `ax² + bx + c = 0`
- ✅ 支持实数和复数解 (Supports real and complex solutions)
- ✅ 命令行交互模式 (Interactive CLI mode)
- ✅ 单次求解模式 (Single equation mode)
- ✅ 快速高效 (Fast and efficient)

## 安装 (Installation)

不需要额外安装依赖，只需要 Python 3.6+

No additional dependencies required, just Python 3.6+

```bash
git clone https://github.com/DARK20050101/first.git
cd first
```

## 使用方法 (Usage)

### 交互模式 (Interactive Mode)

```bash
python solver_cli.py
```

然后输入方程式:
```
Enter equation: 2x + 4 = 0
Solution: x = -2

Enter equation: x^2 - 5x + 6 = 0
Solution: x₁ = 2, x₂ = 3
```

### 单次求解模式 (Single Equation Mode)

```bash
python solver_cli.py "2x + 4 = 0"
```

输出:
```
Equation: 2x + 4 = 0
Solution: x = -2
```

### 帮助信息 (Help)

```bash
python solver_cli.py --help
```

## 示例 (Examples)

### 线性方程 (Linear Equations)

```bash
# 简单线性方程 (Simple linear equation)
python solver_cli.py "2x + 4 = 0"
# Solution: x = -2

# 带有右侧常数的方程 (Equation with constant on right side)
python solver_cli.py "3x = 9"
# Solution: x = 3

# 两侧都有变量的方程 (Equation with variable on both sides)
python solver_cli.py "5x = 2x + 6"
# Solution: x = 2
```

### 二次方程 (Quadratic Equations)

```bash
# 标准二次方程 (Standard quadratic equation)
python solver_cli.py "x^2 - 5x + 6 = 0"
# Solution: x₁ = 2, x₂ = 3

# 完全平方方程 (Perfect square)
python solver_cli.py "x^2 + 2x + 1 = 0"
# Solution: x = -1 (double root)

# 复数根 (Complex roots)
python solver_cli.py "x^2 + x + 1 = 0"
# Solution: x₁ = (-0.5+0.866025j), x₂ = (-0.5-0.866025j)

# 缺少线性项 (No linear term)
python solver_cli.py "x^2 - 4 = 0"
# Solution: x₁ = -2, x₂ = 2

# 缺少常数项 (No constant term)
python solver_cli.py "x^2 + 3x = 0"
# Solution: x₁ = -3, x₂ = 0
```

## 方程格式 (Equation Format)

- 使用 `x` 作为变量 (Use `x` as the variable)
- 使用 `^` 或 `²` 表示平方 (Use `^` or `²` for squared terms)
  - 例如: `x^2` 或 `x²`
- 方程必须包含 `=` 符号 (Equation must contain `=` sign)
- 支持空格（会被自动忽略）(Spaces are supported and will be ignored)

### 有效方程示例 (Valid Equation Examples)

```
2x + 4 = 0
3x = 9
x^2 - 5x + 6 = 0
x² + 2x + 1 = 0
5x = 2x + 6
x^2 - 4 = 0
```

## 运行测试 (Running Tests)

```bash
python test_equation_solver.py
```

或使用详细模式:
```bash
python test_equation_solver.py -v
```

或直接运行核心模块查看示例:
```bash
python equation_solver.py
```

## 项目结构 (Project Structure)

```
first/
├── equation_solver.py      # 核心方程求解器模块 (Core solver module)
├── solver_cli.py           # 命令行界面 (CLI interface)
├── test_equation_solver.py # 单元测试 (Unit tests)
├── SOLVER_README.md        # 本文档 (This documentation)
└── README.md              # GitHub 原始说明 (Original GitHub README)
```

## 技术细节 (Technical Details)

### 线性方程求解 (Linear Equation Solving)

对于方程 `ax + b = 0`:
- 解为: `x = -b/a`
- 特殊情况处理:
  - 如果 `a = 0` 且 `b = 0`: 无限多解
  - 如果 `a = 0` 且 `b ≠ 0`: 无解

### 二次方程求解 (Quadratic Equation Solving)

对于方程 `ax² + bx + c = 0`:
- 判别式: `Δ = b² - 4ac`
- 解的公式: `x = (-b ± √Δ) / (2a)`
- 根据判别式:
  - `Δ > 0`: 两个不同的实数根
  - `Δ = 0`: 一个重根（双重根）
  - `Δ < 0`: 两个复数根（共轭复数）

## 性能 (Performance)

- 线性方程: O(1) 时间复杂度
- 二次方程: O(1) 时间复杂度
- 方程解析: O(n) 时间复杂度，n 为方程字符串长度

## 贡献 (Contributing)

欢迎提交问题和拉取请求！

Issues and pull requests are welcome!

## 许可证 (License)

MIT License - 详见 LICENSE 文件

## 作者 (Author)

DARK20050101

---

**快速开始 (Quick Start)**

```bash
# 克隆仓库
git clone https://github.com/DARK20050101/first.git
cd first

# 运行测试
python test_equation_solver.py

# 启动交互模式
python solver_cli.py

# 或求解单个方程
python solver_cli.py "x^2 - 5x + 6 = 0"
```

祝你使用愉快！ Enjoy solving equations! 🎓📐
