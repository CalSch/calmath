from latex2sympy2 import latex2sympy

def evalLatex(tex: str, subs: dict=None) -> float:
    expr=latex2sympy(tex)
    return expr.evalf(subs=subs)