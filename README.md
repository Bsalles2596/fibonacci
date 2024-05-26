# Função Fibonacci
## Função em Python para calcular o n-ésimo termo da sequência de Fibonacci.
--
## Aqui está uma explicação do código:

### A sequência de Fibonacci é uma série numérica em que cada número é a soma dos
### dois anteriores, começando por 0 e 1. Os primeiros termos da sequência são:
###          0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
 
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


## Instruções de configuração e execução:

### Certifique-se de ter o Python 3.7 ou superior instalado.
### Crie um ambiente virtual venv.

## Comando para criar o ambiente Virtual no Windows, terminal usado powershell.

~~~
   $   python -m venv venv  
~~~

### Comando para Ativar ambiente virtual venv no terminal powershell;
 
~~~
   $   #cd .\venv\Scripts\Activate.Ps1     
~~~

## Executando:

### Executá-lo com o seguinte comando:
	
~~~
   $  python fibonacci.py
~~~	

## Isso irá imprimir os primeiros 10 termos da sequência de Fibonacci:

~~~
    print("Sequência de Fibonacci:")
    for i in range(11):    
        print(f"Termo {i}: {fibonacci(i)}")   
~~~

#### Para visualizar o projeto completo acesse repositório do Github:

[Repositório Github](https://github.com/)





