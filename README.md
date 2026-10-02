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

## Prova de conceito inicial

A branch `thiago` contém uma demonstração didática da cifra de César, com a mensagem do enunciado e chave 3. Os módulos `missao_cripto2/alfabeto.py` e `missao_cripto2/cesar.py` podem ser reaproveitados nas próximas contribuições. Execute na raiz do repositório, com Python 3:

```bash
python -m missao_cripto2.demo
python -m unittest discover -s tests -v
```

A demonstração aceita letras A–Z (maiúsculas ou minúsculas) e espaços; outros caracteres são recusados explicitamente. O texto devolvido fica em maiúsculas. Esta cifra é apenas uma prova de conceito: o pequeno conjunto de deslocamentos permite recuperar a mensagem testando as possibilidades.

A biblioteca matemática da Missão 1 ainda não está neste repositório. O cálculo modular usa, por ora, o operador `%` do Python; quando a interface dessa biblioteca for definida, o grupo poderá integrá-la. Os demais algoritmos e a criptoanálise seguem com seus responsáveis.
