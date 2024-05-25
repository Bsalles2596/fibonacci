# Função para calcular o n-ésimo termo da sequência de Fibonacci, 

def fibonacci(n):
    """
    Calcula o n-ésimo termo da sequência de Fibonacci.
    
    A sequência de Fibonacci é uma série numérica em que cada número é a soma dos
    dois anteriores, começando por 0 e 1. Os primeiros termos da sequência são:
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
    
    Args:
    n (int): O índice do termo a ser calculado na sequência de Fibonacci.
    
    Returns:
    int: O n-ésimo termo da sequência de Fibonacci.
    
    Examples:
    >>> fibonacci(0)
    0
    >>> fibonacci(1)
    1
    >>> fibonacci(10)
    55
    >>> fibonacci(20)
    6765
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a


# Testes da função fibonacci()
print("Sequência de Fibonacci:")
for i in range(11):    
    print(f"Termo {i}: {fibonacci(i)}") ## Isso irá imprimir os primeiros 10 termos da sequência de Fibonacci:   
 
### testes adicionais para verificar o comportamento da função com casos extremos,
### como n = 0, n = 1 e n < 0

assert fibonacci(0) == 0
assert fibonacci(1) == 1
assert fibonacci(10) == 55
assert fibonacci(-1) == 0  # Caso de entrada inválida

### Cláusula doctest no final do código para que os testes possam ser executados automaticamente
### quando o módulo for carregado.
if __name__ == "__main__":
    import doctest
    doctest.testmod()
