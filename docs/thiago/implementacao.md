# Implementação de apoio — parte de Thiago

Esta parte da Missão 2 cobre o vocabulário básico e o princípio de Kerckhoffs. O [resumo](conceitos-e-kerckhoffs.md) contém a fundamentação; o [roteiro](roteiro-apresentacao.md) e os [slides sugeridos](slides.md) apoiam a fala.

## Demonstração executável

Na raiz do repositório, com Python 3.10 ou superior:

```bash
python3 -m missao_cripto2.exemplo_conceitual
python3 -m unittest discover -s tests -v
```

O programa usa apenas a primeira letra da mensagem interceptada: `T = 19`, com alfabeto `A = 0` a `Z = 25` e chave de exemplo `k = 3`. Calcula `c = (19 + 3) mod 26 = 22` (`W`) e depois `m = (22 - 3) mod 26 = 19` (`T`). A regra está explícita no código; o valor da chave é um parâmetro separado. A recuperação confirma a conta inversa, mas não avalia a resistência do método.

`calcular_exemplo(indice_claro, chave, modulo=26)` retorna um `ExemploConceitual` com os índices de entrada, saída e recuperação. O índice deve estar no intervalo de `0` a `modulo - 1`; índice, chave e módulo devem ser inteiros, e o módulo maior que 1.

O módulo `missao_cripto2/matematica_missao1.py` é uma cópia identificada de [`aritmetica_modular.py` da Missão 1](https://github.com/ThHSzR/missao-cripto/blob/c7bbf16585cefa2cb1d817da6b1d1c7088e0ccf6/aritmetica_modular.py), na revisão `c7bbf16585cefa2cb1d817da6b1d1c7088e0ccf6`. A autoria desse módulo é atribuída a Nicole Noleto no README da Missão 1. A demonstração chama diretamente `aritmetica_modular` para a soma e a subtração; a cópia local permite executá-la sem depender de outro checkout ou de uma instalação não oferecida pela Missão 1.

Esta contribuição não implementa a cifra de César para mensagens nem os ataques. Essas partes seguem a divisão do grupo.
