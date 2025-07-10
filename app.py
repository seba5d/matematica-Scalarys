# Interpretador Scalarys - Expressões Longas

# Tabela de valores simbólicos
scalarys = {
    "•x•": 1.0,
    "•∆•": 2.0,
    "•∆∆•": 4.0,
    "•O•": 3.0,
    "•OO•": 6.0,
    "∅": 0.0
}

# Converte valor numérico em símbolo Scalarys
def symbol_from_value(value):
    for k, v in scalarys.items():
        if abs(v - value) < 0.01:
            return k
    return f"[{value:.1f}]"

# Operações básicas simbólicas
def calc_scalar(op, a, b):
    if op == '⊕':
        return a + b
    elif op == '⊖':
        return max(0, a - b)
    elif op == '⊗':
        return a * b
    elif op == '⊘':
        return a / b if b != 0 else 0
    else:
        return None

# Avaliador de expressão simbólica completa
def eval_expression(expr):
    parts = expr.split()
    if len(parts) < 3 or len(parts) % 2 == 0:
        return "Erro: expressão incompleta ou mal formatada."

    try:
        acc = scalarys.get(parts[0], 0)
        steps = f"{parts[0]}"

        for i in range(1, len(parts), 2):
            op = parts[i]
            b_symbol = parts[i+1]
            b = scalarys.get(b_symbol, 0)
            acc = calc_scalar(op, acc, b)
            steps += f" {op} {b_symbol}"

        result_symbol = symbol_from_value(acc)
        return f"{steps} = {result_symbol} ({acc:.1f})"
    except Exception as e:
        return f"Erro: {e}"

# Terminal interativo
def main():
    print("📐 Interpretador Scalarys (expressões longas)")
    print("Digite: •x• ⊕ •x• ⊕ •∆• ⊗ •x•")
    print("Use operadores: ⊕ ⊖ ⊗ ⊘")
    print("Digite 'sair' para encerrar.\n")

    while True:
        expr = input("Digite: ").strip()
        if expr.lower() == "sair":
            break
        result = eval_expression(expr)
        print(result + "\n")

if __name__ == "__main__":
    main()







