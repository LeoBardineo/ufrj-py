import math

# Cálculos Algébricos
max(3, 2.8, 3.9)
min(7, 2, 4, 1, 0)

def mediaSimples(n1, n2, n3):
  return (n1 + n2 + n3) / 3

def diffMaiorMedia(n1, n2, n3):
  return max(n1, n2, n3) - mediaSimples(n1, n2, n3)

def sumMenorMedia(n1, n2, n3):
  return min(n1, n2, n3) + mediaSimples(n1, n2, n3)

def delta(a, b, c):
  return b ** 2 - 4 * a * c

def primeiraRaiz(a, b, c):
  return (-b + delta(a, b, c) ** (1/2)) / (2 * a)

def segundaRaiz(a, b, c):
  return (-b - delta(a, b, c) ** (1/2)) / (2 * a)

def numeroTermosPA(a1, an, r):
  return (an - a1) / r + 1

def somaTermosPA(a1, an, r):
  return numeroTermosPA(a1, an, r) * (a1 + an) / 2

# Cálculos Geométricos

def pitagoras(b, c):
  return math.sqrt(b ** 2 + c ** 2)

def distanciaDoisPontos(x1, x2, y1, y2):
  return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def perimetroTrianguloRetangulo(b, c):
  return pitagoras(b, c) + b + c

def somaQuadradoSenCos(x):
  return math.sin(math.radians(x)) ** 2 + math.cos(math.radians(x)) ** 2

def comprimentoCirculo(r):
  return 2 * math.pi * r

def areaSetorCircular(r, angulo = 360):
  return (angulo * math.pi * r ** 2) / 360

# Cálculos Aplicados

def comprarBombons(dinheiro, precoBombom):
    return dinheiro // precoBombom

def calcularIMC(peso, altura):
    return peso / altura ** 2

def numCarros(pessoas):
    return math.ceil(pessoas / 5)

def numVoltas(raio, distancia):
    return distancia / comprimentoCirculo(raio)

def fazerBolo(A, B, C):
    return min(A//2, B//3, C//5)
