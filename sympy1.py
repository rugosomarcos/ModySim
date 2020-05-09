from sympy import *
#Defino t y a f como funcion
t = symbols("t")
f = Function('f')
dfdt = diff(f(t), t)
C1, p_0 = symbols('C1 p_0')

# Defino alpha y beta
alpha = symbols('alpha')
beta = symbols('beta')
eq1 = Eq(dfdt, alpha*f(t)+beta * f(t)**2)
print("Ecuacion a resolver :",eq1)
solucion_eq= dsolve(eq1)
print("Solucion de la ecuacion diferencial:")
print(solucion_eq)
general = solucion_eq.rhs
print(general)

general_t0 = general.subs(t, 0)
print(general_t0)
condicion_inicial = Eq(general_t0, p_0)

print ("Condicion inicial")
print(condicion_inicial)
solucion = solve(condicion_inicial, C1)
print(solucion[0])

valor_C1 = solucion[0]

particular = general.subs(C1, valor_C1)
print("Solucion Particular:")
print(particular)
print("Simplificada:")
particular_simple = simplify(particular)
print(particular_simple)

