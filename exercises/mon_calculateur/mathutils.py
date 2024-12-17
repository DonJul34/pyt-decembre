# Fonction pour calculer la racine carrée (méthode de Newton-Raphson)
def sqrt(x, epsilon=1e-10):
    if x < 0:
        raise ValueError("La racine carrée d'un nombre négatif n'est pas définie.")
    guess = x / 2.0  # Estimation initiale
    while abs(guess * guess - x) > epsilon:
        guess = (guess + x / guess) / 2.0
    return guess

# Fonction pour calculer une puissance (exponentiation rapide)
def power(base, exp):
    if exp == 0:
        return 1
    elif exp < 0:
        return 1 / power(base, -exp)
    result = 1
    while exp > 0:
        if exp % 2 == 1:  # Si l'exposant est impair
            result *= base
        base *= base
        exp //= 2  # Division entière par 2
    return result

# Fonction pour calculer la valeur absolue
def abs_val(x):
    return x if x >= 0 else -x

# Fonction pour calculer le logarithme naturel (méthode d'approximation série de Taylor)
def ln(x, terms=50):
    if x <= 0:
        raise ValueError("Le logarithme naturel est défini uniquement pour les nombres positifs.")
    if x == 1:
        return 0
    # Normaliser x pour qu'il soit proche de 1
    n = 0
    while x > 2:
        x /= 2
        n += 1
    while x < 0.5:
        x *= 2
        n -= 1
    z = (x - 1) / (x + 1)
    series_sum = 0
    for i in range(terms):
        series_sum += power(z, 2 * i + 1) / (2 * i + 1)
    return 2 * series_sum + n * 0.6931471805599453  # Ajouter n*ln(2)

# Fonction pour calculer le factoriel
def factorial(n):
    if n < 0:
        raise ValueError("Le factoriel n'est pas défini pour les nombres négatifs.")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Fonction pour calculer le sinus (approximation avec série de Taylor)
def sin(x, terms=10):
    x %= 2 * 3.141592653589793  # Réduire x dans [-2pi, 2pi]
    result = 0
    for n in range(terms):
        sign = (-1) ** n
        result += sign * power(x, 2 * n + 1) / factorial(2 * n + 1)
    return result

# Fonction pour calculer le cosinus (approximation avec série de Taylor)
def cos(x, terms=10):
    x %= 2 * 3.141592653589793  # Réduire x dans [-2pi, 2pi]
    result = 0
    for n in range(terms):
        sign = (-1) ** n
        result += sign * power(x, 2 * n) / factorial(2 * n)
    return result