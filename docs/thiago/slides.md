# Conteúdo dos slides — parte de Thiago

Proposta de **dois slides** para integrar à apresentação de 10 minutos do grupo. A fala detalhada está no [roteiro](roteiro-apresentacao.md); o conteúdo abaixo cabe na abertura reservada a Thiago.

## Slide 1 — A mensagem interceptada

**Na tela:**

> TRANSFERIR DOCUMENTO PARA SERVIDOR CENTRAL

| Termo | No exemplo |
|---|---|
| Texto claro | Mensagem original |
| Algoritmo | Regra pública de transformação |
| Chave | Parâmetro escolhido para a regra |
| Texto cifrado | Resultado da transformação |
| Decifragem | Recuperação do texto claro |

**Fala:** apresentar o problema e distinguir regra, chave e mensagem. Mostrar `T = 19`, `k = 3`, `W = 22` se houver tempo. Os cálculos podem ser exibidos pelo comando `python3 -m missao_cripto2.exemplo_conceitual`.

## Slide 2 — Princípio de Kerckhoffs

**Na tela:**

> O método deve ser avaliado mesmo quando o adversário conhece a regra; a chave é o parâmetro que se tenta manter secreto.

- Exemplo: `c = (m + k) mod 26`; `T (19) → W (22)` com `k = 3`.
- Reverter o exemplo comprova a conta, não a segurança.
- Pergunta para o grupo: o que acontece quando tentamos recuperar a mensagem sem conhecer a chave?

**Fala:** explicar por que depender do sigilo do algoritmo não sustenta a segurança e passar para a demonstração de César e substituição da Nicole.

**Fontes:** cenário e produtos no [enunciado da missão](conceitos-e-kerckhoffs.md#referências); conceitos e princípio nas referências [2]–[4] do [resumo](conceitos-e-kerckhoffs.md#referências). O cálculo numérico está na seção 3 do resumo.
