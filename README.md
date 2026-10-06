# Missão Cripto 2 — A mensagem interceptada

Repositório da **Missão 2** do projeto SecureDocs, da disciplina de Criptografia Aplicada. A atividade investiga como transformar uma mensagem em texto claro para que seu conteúdo não seja compreendido diretamente por quem a interceptar.

## Contexto

No cenário proposto, um funcionário envia a mensagem:

> TRANSFERIR DOCUMENTO PARA SERVIDOR CENTRAL

A transmissão é interceptada. A equipe deve pesquisar, experimentar e comparar técnicas de criptografia clássica, além de analisar como algumas delas podem ser quebradas por força bruta ou análise de frequência.

## Objetivos da missão

- Estudar texto claro, texto cifrado, cifragem, decifragem, chaves e criptoanálise.
- Experimentar cifras clássicas, como César, substituição, Afim, Vigenère, Hill, transposição e cifras de fluxo, conforme as técnicas escolhidas pelo grupo.
- Implementar uma biblioteca com as técnicas estudadas, preferencialmente em Python e com apoio da biblioteca matemática da Missão 1.
- Testar as implementações e discutir suas limitações.
- Explicar por que ocultar o algoritmo não basta para garantir segurança, à luz do princípio de Kerckhoffs.

## Entregáveis previstos no enunciado

1. Resumo dos conceitos básicos de criptografia e dos algoritmos estudados.
2. Biblioteca com as implementações das técnicas criptográficas clássicas estudadas.
3. Apresentação de 10 minutos dos artefatos produzidos até o momento.

## Estado do projeto

Repositório iniciado. As implementações, testes e demais artefatos serão adicionados ao longo da missão.

> **Nota:** cifras clássicas são estudadas aqui para fins didáticos. Este repositório ainda não representa uma solução de segurança pronta para proteger os documentos do SecureDocs.

## Referência

Enunciado da disciplina: *2_M_PBL_Crip_Classica.pdf*, seções “Missão 2 – A mensagem interceptada” e “Produto da missão”.

## Parte de Thiago — conceitos e Kerckhoffs

A branch `thiago` contém o [resumo conceitual](docs/thiago/conceitos-e-kerckhoffs.md), o [roteiro](docs/thiago/roteiro-apresentacao.md), [dois slides sugeridos](docs/thiago/slides.md) e uma [demonstração executável](docs/thiago/implementacao.md) do exemplo numérico. A demonstração usa uma cópia identificada do módulo de aritmética modular da [Missão 1](https://github.com/ThHSzR/missao-cripto/blob/c7bbf16585cefa2cb1d817da6b1d1c7088e0ccf6/aritmetica_modular.py).

Na raiz do repositório, com Python 3.10 ou superior:

```bash
python3 -m missao_cripto2.exemplo_conceitual
python3 -m unittest discover -s tests -v
```

Este código ilustra texto claro, chave, regra pública, resultado e recuperação em um único símbolo. As implementações das cifras completas e dos ataques cabem aos respectivos responsáveis na divisão do grupo.
