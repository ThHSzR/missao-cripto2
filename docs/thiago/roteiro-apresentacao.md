# Roteiro de fala — Thiago

**Tema:** conceitos básicos e princípio de Kerckhoffs.  
**Tempo reservado:** aproximadamente 2 minutos, dentro dos 10 minutos do grupo. Ensaie com cronômetro; as faixas abaixo são uma proposta de distribuição, não uma duração medida.

## 0:00–0:25 — Apresentar o problema

“No SecureDocs, um funcionário enviou a mensagem ‘TRANSFERIR DOCUMENTO PARA SERVIDOR CENTRAL’, e ela foi interceptada. Nossa missão é estudar maneiras de transformar esse conteúdo e investigar as limitações dessas técnicas.”

## 0:25–1:00 — Explicar com o exemplo

“A mensagem original é o texto claro. Aplicamos um algoritmo e uma chave para produzir o texto cifrado. Para recuperar a mensagem, fazemos a decifragem.

Neste exemplo, a regra é deslocar letras, e a chave é três. A letra T vira W. Quando fazemos o caminho inverso, W volta a ser T. Portanto, algoritmo é a regra, e chave é o parâmetro escolhido.”

**Apoio visual sugerido:** mostrar a tabela do exemplo no [resumo](conceitos-e-kerckhoffs.md#3-exemplo-calculado-para-a-missão).

## 1:00–1:40 — Responder à questão central

“Mas deixar a mensagem diferente não basta. Precisamos considerar alguém tentando recuperar seu conteúdo. Shannon analisa justamente o cenário em que o adversário conhece o sistema.

Essa hipótese ajuda a entender o princípio de Kerckhoffs: conhecer o algoritmo não deveria comprometer a proteção, enquanto a chave necessária continua secreta. No exemplo do deslocamento, porém, existem apenas 26 possibilidades. A chave secreta, sozinha, não torna esse método resistente.”

## 1:40–2:00 — Fazer a transição

“Por isso, nosso trabalho precisa explicar os métodos e investigar seus limites. Conseguir cifrar e decifrar é apenas o primeiro passo da avaliação. Agora, a Nicole apresenta César e substituição.”

## Preparação para apresentar

- Leia o resumo e confira a conta T = 19, W = 22 e chave 3.
- Abra a tabela antes da apresentação.
- Ensaie a fala inteira com cronômetro, ajustando as pausas.
- Combine com Nicole a transição e evite repetir a demonstração completa dela.

## Perguntas de apoio

**Por que existem 26 possibilidades?**  
Porque usamos 26 letras e os deslocamentos se repetem módulo 26; há 25 transformações não triviais se excluirmos zero.

**O exemplo já resolve o problema da empresa?**  
Não. Ele demonstra uma transformação reversível e um espaço pequeno de chaves, que pode ser enumerado.

**Qual é a diferença entre decifrar e fazer criptoanálise?**  
Decifrar é aplicar a operação inversa com a chave apropriada; criptoanálise busca contornar a proteção, sem dispor inicialmente do segredo necessário. [2]

## Fontes da fala

O cenário vem do enunciado [1]; o vocabulário, da RFC 4949 [2]; o princípio, do material de Cambridge [3]; e a hipótese de conhecimento do sistema, do artigo de Shannon [4]. As referências completas estão no [resumo](conceitos-e-kerckhoffs.md#referências). Os números do exemplo são calculados no próprio resumo.
