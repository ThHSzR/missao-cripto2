# Missão Cripto 2 — A mensagem interceptada

Projeto didático de Criptografia Aplicada sobre a mensagem interceptada no cenário SecureDocs:
`TRANSFERIR DOCUMENTO PARA SERVIDOR CENTRAL`.

## Implementações reunidas na main

| Técnica ou material | Arquivos |
|---|---|
| César e substituição | `cesar.py`, `substituicao.py` |
| Afim e Vigenère | `afim.py`, `vigenere.py`; menu alternativo em `afim_vigenere.py` |
| Hill, transposição colunar e fluxo XOR | `minhas_cifras.py` |
| Matemática modular da Missão 1 | `mdc.py`, `euclides_estendido.py`, `inverso_multiplicativo.py` |
| Criptoanálise e comparação | `forca_bruta.py`, `analise_frequencia.py`, `frequencia_pt.py`, `comparacao_cifras.py` |
| Introdução, Kerckhoffs e exemplo conceitual | `docs/thiago/`, `missao_cripto2/` |

O material do grupo para a apresentação está nos arquivos `Criptografia_Clássica_(2).pdf` e `.pptx`.

## Executar

```bash
python3 -m pip install -r requirements.txt
python3 test_cifras.py            # pede a dimensão 2 a 8 da matriz de Hill
python3 test_cifras.py --padrao   # demonstração automática com matriz 3x3
python3 teste_main.py            # demonstração Afim e Vigenère
python3 afim_vigenere.py         # menu interativo alternativo da branch thiago
python3 -m unittest discover -s tests -v
```

Na demonstração de Hill, escolha a dimensão e use a matriz sugerida ou digite uma matriz inteira de sua preferência. Matrizes sem inversa módulo 26 são rejeitadas e podem ser digitadas novamente. A biblioteca aceita matrizes quadradas inteiras e calcula o determinante sem arredondamento. A interface limita a escolha a 2–8 para manter a entrada manual prática.

Hill e transposição retiram espaços e pontuação e acrescentam `X` para completar blocos; portanto, a saída decifrada pode conter `X` final. A cifra de fluxo recupera o texto original completo. Os métodos clássicos deste projeto são para estudo, não para proteção de documentos reais.

Enunciado da disciplina: *2_M_PBL_Crip_Classica.pdf*, seções “Missão 2 – A mensagem interceptada” e “Produto da missão”.
