def calculate_expression(expression):
    try:
        result = eval(expression)
    except Exception as e:
        result = f"Expressão invalida:{str(e)}"
    return result