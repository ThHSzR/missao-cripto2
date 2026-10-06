# Conceitos básicos e princípio de Kerckhoffs

**Responsável:** Thiago  
**Atividade:** SecureDocs — Missão 2: A mensagem interceptada

## 1. Situação-problema

No enunciado, a TechSecure identifica a interceptação da mensagem “TRANSFERIR DOCUMENTO PARA SERVIDOR CENTRAL”. Esta parte apresenta o vocabulário necessário para discutir as cifras e responde à questão: por que esconder o algoritmo não é suficiente para garantir segurança? [1]

## 2. Vocabulário essencial

As definições abaixo são sínteses didáticas dos verbetes da RFC 4949. [2]

| Conceito | Significado |
|---|---|
| Criptografia | Estudo e aplicação de técnicas matemáticas para proteger informações. |
| Texto claro | Dados de entrada da cifragem; neste exercício, a mensagem original legível. |
| Texto cifrado | Resultado da cifragem, cujo significado não fica diretamente disponível. |
| Cifragem | Transformação do texto claro em texto cifrado. |
| Decifragem | Operação que recupera o texto claro a partir do texto cifrado. |
| Algoritmo | Procedimento que define as operações realizadas. |
| Chave criptográfica | Parâmetro que determina uma transformação específica do algoritmo. |
| Criptoanálise | Análise de um sistema criptográfico para contornar a proteção oferecida. |

No modelo simétrico, podemos escrever `C = Eₖ(M)` e `Dₖ(C) = M`: M é a mensagem, C é o resultado cifrado e k é a chave compartilhada. Recuperar M demonstra correção; não demonstra, por si só, resistência a ataques. [3]

## 3. Exemplo calculado para a missão

Para visualizar os conceitos, usamos um deslocamento de três posições sobre A–Z, com A = 0, B = 1, …, Z = 25. Os espaços permanecem inalterados. Trata-se de um exemplo de César para introdução; o estudo e a implementação dessa cifra pertencem à parte da Nicole.

- Algoritmo de cifragem: `c = (m + k) mod 26`.
- Chave escolhida para o exemplo: `k = 3`.
- Decifragem: `m = (c - k) mod 26`.

| Etapa | Resultado |
|---|---|
| Texto claro | TRANSFERIR DOCUMENTO PARA SERVIDOR CENTRAL |
| Texto cifrado | WUDQVIHULU GRFXPHQWR SDUD VHUYLGRU FHQWUDO |
| Texto recuperado | TRANSFERIR DOCUMENTO PARA SERVIDOR CENTRAL |

Conferência da primeira letra: T = 19; `(19 + 3) mod 26 = 22`, que representa W. Na volta: `(22 - 3) mod 26 = 19`, recuperando T.

Há 26 deslocamentos distintos, de 0 a 25. Descartando o deslocamento 0, que mantém o texto, sobram 25. Assim, neste exemplo, enumerar todos os deslocamentos é suficiente para incluir a mensagem original entre os candidatos. O segredo da chave não compensa esse espaço pequeno de possibilidades.

## 4. Princípio de Kerckhoffs

O princípio orienta a avaliar o sistema supondo que o adversário conheça seu funcionamento. A proteção deve resistir à divulgação do algoritmo, mantendo secreta a chave necessária. Publicar o algoritmo não prova que ele seja seguro: ainda é preciso analisar sua resistência. [3]

Shannon também adota o conhecimento do sistema pelo adversário como hipótese de análise. Isso permite discutir segurança sem depender da esperança de que o método permaneça desconhecido. [4]

**Resposta à questão norteadora:** esconder o algoritmo é insuficiente porque sua descoberta não deveria destruir a proteção. No nosso exemplo, esconder a regra de deslocamento não elimina suas 26 possibilidades; quando a regra é conhecida, a enumeração continua viável. Precisamos avaliar o método e suas chaves diante de ataques.

## 5. Aplicação ao SecureDocs

A missão permite experimentar confidencialidade. Cifrar, isoladamente, não assegura a integridade ou a origem da mensagem; esses objetivos requerem mecanismos apropriados. [3]

Como encaminhamento para o grupo, propomos documentar cada algoritmo, explicitar suas chaves e testar sua resistência considerando o método conhecido. Os resultados dos demais membros completarão a comparação. Este exemplo introdutório não constitui proteção adequada para os documentos reais descritos no cenário.

## Referências

[1] **Enunciado da disciplina.** *2_M_PBL_Crip_Classica.pdf*. Seções “Missão 2 – A mensagem interceptada”, “Problema adicional” e “Produto da missão”. Arquivo fornecido à equipe.

[2] **SHIREY, R.** *Internet Security Glossary, Version 2*. RFC 4949, 2007. Seção 4, verbetes “cryptography”, “plain text”, “cipher text”, “encryption”, “decryption”, “cryptographic key” e “cryptanalysis”. Glossário informativo, utilizado para terminologia, não como recomendação atual de algoritmos.  
https://www.rfc-editor.org/rfc/rfc4949.txt

[3] **KUHN, Markus.** *Cryptography*. University of Cambridge, 2025. Slides numerados 6, 7 e 12–13: esquemas de cifragem, integridade e princípios de Kerckhoffs.  
https://www.cl.cam.ac.uk/teaching/2425/Crypto/crypto-slides.pdf

[4] **SHANNON, Claude E.** *Communication Theory of Secrecy Systems*. Bell System Technical Journal, 1949. Parte I, seção 2; hipótese sobre o conhecimento do sistema pelo adversário. Cópia do artigo:  
https://all.net/refs/shannon1949.pdf

Fontes online consultadas em 29/09/2026. O exemplo numérico foi calculado e sua reversão foi conferida em Python.
