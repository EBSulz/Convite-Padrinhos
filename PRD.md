# Product Requirement Document (PRD): Caça ao Tesouro Streamlit

## 1. Visão Geral
Este documento detalha os requisitos para o desenvolvimento de uma aplicação web interativa utilizando **Streamlit**. O objetivo é criar um "Caça ao Tesouro" digital para 5 amigos específicos, onde cada um deve passar por um quiz personalizado para desbloquear uma imagem final.

---

## 2. Objetivos do Produto
* Proporcionar uma experiência personalizada para 5 usuários.
* Validar o acesso através de nome e data de nascimento.
* Apresentar um quiz de 5 perguntas para cada usuário.
* Liberar o "tesouro" (imagem específica) apenas em caso de 100% de aproveitamento.

---

## 3. Requisitos Funcionais

### 3.1. Autenticação (Login)
A tela inicial deve conter:
* **Username (Nome):** Campo de texto livre (`st.text_input`).
* **Senha (Data de Aniversário):** Seletor de data (`st.date_input`).
* **Botão:** "Validar".

**Tabela de Credenciais:**
| Nome | Data de Aniversário |
| :--- | :--- |
| Ravi | 28/04/1996 |
| Bambu | 09/09/1995 |
| Henrique | 18/06/1996 |
| Alfredo | 24/12/1995 |
| Vitor | 18/10/1996 |

**Lógica:**
* Se o par (Nome, Data) for válido, o sistema salva o usuário na sessão (`st.session_state`) e exibe o questionário.
* Se for inválido, exibe uma mensagem de erro: "Credenciais não encontradas. Tente novamente."

### 3.2. O Questionário
Após o login, o usuário visualiza:
* **Introdução:** "Bem-vindo ao Caça ao Tesouro! Responda às 5 perguntas sobre as histórias do noivo. Você precisa acertar **TODAS** para chegar ao tesouro final."
* **Estrutura:** 5 perguntas de múltipla escolha (3 opções cada).
* **Personalização:** Cada um dos 5 usuários recebe 5 perguntas distintas (conforme mapeamento na Seção 4).

### 3.3. Resultado e Tesouro
* **Sucesso (100%):** Exibir a imagem localizada em `imagens/{nome_do_usuario}.png`.
* **Falha ( < 100%):**
    * Exibir mensagem: "Você acertou X% das questões!" (ex: "Você acertou 60% das questões!").
    * Botão "Reiniciar Questionário" para limpar as respostas e tentar novamente.

---

## 4. Conteúdo dos Questionários (Mapping)

As 25 perguntas fornecidas foram divididas em grupos de 5.

### Grupo 1: Ravi
1. **Qual era o estilo de cabelo ou de roupa mais duvidoso que ele já usou?**
   - A) O mullet desproporcional. (Correta)
   - B) A calça colorida Restart.
   - C) O terno dois tamanhos maior.
2. **Qual foi a maior "furada" ou perrengue que vocês já passaram juntos?**
   - A) Ficar sem gasolina no meio da estrada.
   - B) Dormir na rodoviária por perder o ônibus. (Correta)
   - C) Entrar na festa errada achando que era open bar.
3. **Qual é a história de infância ou adolescência dele que ele morre de vergonha de contar?**
   - A) Quando ele chorou no colo do Papai Noel aos 12 anos. (Correta)
   - B) O tombo na apresentação de balé da irmã.
   - C) Quando ele foi expulso da aula de artes.
4. **Quem era o noivo antes de conhecer a noiva?**
   - A) O festeiro incontrolável. (Correta)
   - B) O tímido que não saía do quarto.
   - C) O nerd viciado em RPG.
5. **Qual foi a primeira coisa que vocês pensaram quando ele contou que estava namorando?**
   - A) "Finalmente tomou jeito!" (Correta)
   - B) "É pegadinha, com certeza."
   - C) "Coitada dessa menina..."

### Grupo 2: Bambu
6. **Se ele fosse um personagem de filme, qual seria?**
   - A) Forrest Gump.
   - B) James Bond (versão comédia). (Correta)
   - C) Shrek.
7. **Qual é o talento escondido que ninguém acredita que ele tem?**
   - A) Cantar ópera no chuveiro.
   - B) Fazer embaixadinhas com uvas. (Correta)
   - C) Resolver cubo mágico em 10 segundos.
8. **Qual é a habilidade doméstica em que ele é surpreendentemente bom?**
   - A) Passar camisa social sem deixar vinco.
   - B) Fazer um miojo gourmet inesquecível. (Correta)
   - C) Organizar a despensa por cor.
9. **Em uma situação de sobrevivência na selva, ele seria:**
   - A) O líder que salva a todos.
   - B) O primeiro a ser resgatado (ou devorado). (Correta)
   - C) O que tenta fazer fogo com dois gelos.
10. **Qual é a frase ou bordão que ele repete o tempo todo?**
    - A) "Segue o jogo." (Correta)
    - B) "Isso é loucura."
    - C) "Confia no pai."

### Grupo 3: Henrique
11. **Qual é o nível de lealdade dele em uma escala de 1 a 10?**
    - A) 11 (fiel até debaixo d'água). (Correta)
    - B) 5 (depende do churrasco).
    - C) 10 (mas cobra juros).
12. **O que é algo que só os amigos sabem que o deixa irritado?**
    - A) Atrasos de mais de 5 minutos.
    - B) Ficar com fome. (Correta)
    - C) Perder no videogame.
13. **Se tivéssemos que descrevê-lo em uma palavra, qual seria?**
    - A) Imprevisível. (Correta)
    - B) Sistemático.
    - C) Dorminhoco.
14. **Qual é o pedido de comida que ele nunca troca?**
    - A) Pizza de calabresa sem cebola.
    - B) Hambúrguer com o dobro de bacon. (Correta)
    - C) Sushi de salmão.
15. **Como ele se comporta em um grupo: faz rir, organiza ou observa?**
    - A) O que faz todo mundo rir até passar mal. (Correta)
    - B) O mestre da planilha e organização.
    - C) O observador silencioso.

### Grupo 4: Alfredo
16. **Qual foi o momento em que viram que ele estava "perdido de amores"?**
    - A) Quando ele parou de ir ao futebol para ver série. (Correta)
    - B) Quando ele começou a usar perfume caro.
    - C) Quando ele aprendeu a cozinhar para ela.
17. **O que mudou no comportamento dele depois que começou a namorar?**
    - A) Ficou muito mais caseiro. (Correta)
    - B) Ficou mais estressado.
    - C) Começou a gostar de plantas.
18. **Quem é o melhor conselheiro para o noivo?**
    - A) Os amigos (com certeza).
    - B) A noiva (sem dúvidas). (Correta)
    - C) O Google.
19. **O que ele mais gosta de fazer com a noiva que nunca faria com os amigos?**
    - A) Ir ao shopping num sábado à tarde. (Correta)
    - B) Assistir jogo de futebol.
    - C) Comer pizza com as mãos.
20. **Qual conselho vocês dariam para a noiva para lidar com ele nos dias difíceis?**
    - A) Dê comida e um controle de videogame. (Correta)
    - B) Deixe ele falando sozinho até cansar.
    - C) Leve ele para uma caminhada de 10km.

### Grupo 5: Vitor
21. **Qual foi o maior mico que ele já pagou em público?**
    - A) Rasgar a calça na pista de dança. (Correta)
    - B) Chamar a sogra de "mãe" no primeiro dia.
    - C) Cair da cadeira no restaurante.
22. **Qual é a lembrança de infância que ele mais gosta de compartilhar?**
    - A) O gol de bicicleta no campeonato da escola. (Correta)
    - B) Quando ele se perdeu no supermercado.
    - C) O dia que ganhou o primeiro cachorro.
23. **Qual foi o presente mais criativo (ou sem noção) que ele já deu?**
    - A) Uma pedra decorativa de estimação. (Correta)
    - B) Meias com a cara dele estampada.
    - C) Um vale-abraço escrito à mão.
24. **Qual é a viagem que ele não cansa de contar as histórias?**
    - A) O mochilão passando perrengue na Europa. (Correta)
    - B) A ida para a praia no ano novo.
    - C) A viagem de formatura.
25. **Qual é a fase da vida dele que ele mais sente falta?**
    - A) Da época da faculdade e festas. (Correta)
    - B) Da infância na casa da avó.
    - C) Do primeiro emprego.

---

## 5. Requisitos Não Funcionais e Design
* **Interface:** Utilizar `st.columns` para centralizar os campos.
* **State Management:** O estado do login e as respostas devem ser armazenados no `st.session_state` para evitar que o Streamlit resete os dados a cada interação.
* **Segurança:** Embora simples, a validação de data deve ser exata.
* **Assets:** As imagens devem estar no diretório `/imagens` com o formato `{Nome}.png` (ex: `Ravi.png`).

---

## 6. Estrutura de Arquivos Proposta
```text
/
├── app.py              # Código principal em Python/Streamlit
├── PRD.md              # Este documento
├── imagens/
│   ├── Ravi.png
│   ├── Bambu.png
│   ├── Henrique.png
│   ├── Alfredo.png
│   └── Vitor.png
└── requirements.txt    # streamlit