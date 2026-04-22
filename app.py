import base64
import os
from datetime import date

import streamlit as st
import streamlit.components.v1 as components

# ---------------------------------------------------------------------------
# Dados
# ---------------------------------------------------------------------------

CREDENCIAIS: dict[str, date] = {
    "Ravi": date(1996, 4, 28),
    "Bambu": date(1995, 9, 9),
    "Henrique": date(1996, 6, 18),
    "Alfredo": date(1995, 12, 24),
    "Vitor": date(1996, 10, 18),
}

PERGUNTAS: dict[str, list[dict]] = {
    "Ravi": [
        {
            "pergunta": "O que o casal gosta de fazer juntos?",
            "opcoes": [
                "Assistir a missa do Pastor Edir Macêdo.",
                "Comprar calças coloridas no shopping.",
                "Ir pro barzinho e ir pra roda de samba.",
            ],
            "correta": 2,
        },
        {
            "pergunta": "Qual foi o maior perrengue que o casal já passou juntos?",
            "opcoes": [
                "Pagar 200€ de táxi pra chegar a tempo na estação de Milão.",
                "Gaivotas atacarem o drone no Algarve e depois atacarem o casal.",
                "Parar uma festa para procurar um telefone por 30min (estava no bolso da noiva).",
            ],
            "correta": 0,
        },
        {
            "pergunta": "Qual o programa ideal para uma quinta a noite?",
            "opcoes": [
                "Ensaio do bloco Secretinho.",
                "Partidinha de War of the Ring.",
                "Date em casa com queijos e vinhos.",
            ],
            "correta": 2,
        },
        {
            "pergunta": "Se o casal fosse abrir um negócio juntos, qual seria?",
            "opcoes": [
                "Uma livraria com um café dentro.",
                "Um barzinho com jogos de tabuleiro.",
                "Um salão de beleza para pets.",
            ],
            "correta": 1,
        },
        {
            "pergunta": "Qual a hamburgueria favorita do casal em Lisboa?",
            "opcoes": [
                "Street Smash Burger.",
                "Hamburgueria Honorato.",
                "Evaldo.",
            ],
            "correta": 2,
        },
        {
            "pergunta": "Qual o destino da lua de mel dos sonhos do casal?",
            "opcoes": [
                "Tailândia.",
                "Nova York.",
                "Pirenópolis.",
            ],
            "correta": 0,
        },
        {
            "pergunta": "O que o noivo adora fazer quando bebe todas?",
            "opcoes": [
                "Conversar com novas pessoas e fazer amigos.",
                "Deitar e apagar em qualquer superfície existente.",
                "Se retirar da festa pois já está muito tarde para ele.",
            ],
            "correta": 1,
        },
        {
            "pergunta": "O que você (eu-lírico) faz que irrita o noivo?",
            "opcoes": [
                "Demorar 20min pra passar o turno nas noites de jogos.",
                "Falar que está chegando e não ter nem saído de casa.",
                "Sumir quando começava a namorar.",
                "Contar os biscoitos no pacote pra saber quando alguém pegava escondido.",
                "Ficar enchendo o saco do noivo em toda oportunidade possível.",
            ],
            "correta": 1,
        },
        {
            "pergunta": "Por quê você (eu-lírico) é especial para o noivo?",
            "opcoes": [
                "Porque tem uma profissão interessante e é preciso ter amigos que saibam disso.",
                "Porque não tinha mais ninguém para ele ser amigo.",
                "Porque você contou uma piada engraçada uma vez há anos atrás.",
                "Poque você é companheiro, irmão, amigo e pau pra toda obra. Ele sabe que pode contar com você sempre.",
                
            ],
            "correta": 3,
        },
    ],
    "Bambu": [
        {
            "pergunta": "O que o casal gosta de fazer juntos?",
            "opcoes": [
                "Assistir a missa do Pastor Edir Macêdo.",
                "Comprar calças coloridas no shopping.",
                "Ir pro barzinho e ir pra roda de samba.",
            ],
            "correta": 2,
        },
        {
            "pergunta": "Qual foi o maior perrengue que o casal já passou juntos?",
            "opcoes": [
                "Pagar 200€ de táxi pra chegar a tempo na estação de Milão.",
                "Gaivotas atacarem o drone no Algarve e depois atacarem o casal.",
                "Parar uma festa para procurar um telefone por 30min (estava no bolso da noiva).",
            ],
            "correta": 0,
        },
        {
            "pergunta": "Qual o programa ideal para uma quinta a noite?",
            "opcoes": [
                "Ensaio do bloco Secretinho.",
                "Partidinha de War of the Ring.",
                "Date em casa com queijos e vinhos.",
            ],
            "correta": 2,
        },
        {
            "pergunta": "Se o casal fosse abrir um negócio juntos, qual seria?",
            "opcoes": [
                "Uma livraria com um café dentro.",
                "Um barzinho com jogos de tabuleiro.",
                "Um salão de beleza para pets.",
            ],
            "correta": 1,
        },
        {
            "pergunta": "Qual a hamburgueria favorita do casal em Lisboa?",
            "opcoes": [
                "Street Smash Burger.",
                "Hamburgueria Honorato.",
                "Evaldo.",
            ],
            "correta": 2,
        },
        {
            "pergunta": "Qual o destino da lua de mel dos sonhos do casal?",
            "opcoes": [
                "Tailândia.",
                "Nova York.",
                "Pirenópolis.",
            ],
            "correta": 0,
        },
        {
            "pergunta": "O que o noivo adora fazer quando bebe todas?",
            "opcoes": [
                "Conversar com novas pessoas e fazer amigos.",
                "Deitar e apagar em qualquer superfície existente.",
                "Se retirar da festa pois já está muito tarde para ele.",
            ],
            "correta": 1,
        },
        {
            "pergunta": "O que você (eu-lírico) faz que irrita o noivo?",
            "opcoes": [
                "Demorar 20min pra passar o turno nas noites de jogos.",
                "Falar que está chegando e não ter nem saído de casa.",
                "Sumir quando começava a namorar.",
                "Contar os biscoitos no pacote pra saber quando alguém pegava escondido.",
                "Ficar enchendo o saco do noivo em toda oportunidade possível.",
            ],
            "correta": 0,
        },
        {
            "pergunta": "Por quê você (eu-lírico) é especial para o noivo?",
            "opcoes": [
                "Porque tem uma profissão interessante e é preciso ter amigos que saibam disso.",
                "Porque não tinha mais ninguém para ele ser amigo.",
                "Porque você contou uma piada engraçada uma vez há anos atrás.",
                "Poque você é companheiro, irmão, amigo e pau pra toda obra. Ele sabe que pode contar com você sempre.",
                
            ],
            "correta": 3,
        },
    ],
    "Henrique": [
        {
            "pergunta": "O que o casal gosta de fazer juntos?",
            "opcoes": [
                "Assistir a missa do Pastor Edir Macêdo.",
                "Comprar calças coloridas no shopping.",
                "Ir pro barzinho e ir pra roda de samba.",
            ],
            "correta": 2,
        },
        {
            "pergunta": "Qual foi o maior perrengue que o casal já passou juntos?",
            "opcoes": [
                "Pagar 200€ de táxi pra chegar a tempo na estação de Milão.",
                "Gaivotas atacarem o drone no Algarve e depois atacarem o casal.",
                "Parar uma festa para procurar um telefone por 30min (estava no bolso da noiva).",
            ],
            "correta": 0,
        },
        {
            "pergunta": "Qual o programa ideal para uma quinta a noite?",
            "opcoes": [
                "Ensaio do bloco Secretinho.",
                "Partidinha de War of the Ring.",
                "Date em casa com queijos e vinhos.",
            ],
            "correta": 2,
        },
        {
            "pergunta": "Se o casal fosse abrir um negócio juntos, qual seria?",
            "opcoes": [
                "Uma livraria com um café dentro.",
                "Um barzinho com jogos de tabuleiro.",
                "Um salão de beleza para pets.",
            ],
            "correta": 1,
        },
        {
            "pergunta": "Qual a hamburgueria favorita do casal em Lisboa?",
            "opcoes": [
                "Street Smash Burger.",
                "Hamburgueria Honorato.",
                "Evaldo.",
            ],
            "correta": 2,
        },
        {
            "pergunta": "Qual o destino da lua de mel dos sonhos do casal?",
            "opcoes": [
                "Tailândia.",
                "Nova York.",
                "Pirenópolis.",
            ],
            "correta": 0,
        },
        {
            "pergunta": "O que o noivo adora fazer quando bebe todas?",
            "opcoes": [
                "Conversar com novas pessoas e fazer amigos.",
                "Deitar e apagar em qualquer superfície existente.",
                "Se retirar da festa pois já está muito tarde para ele.",
            ],
            "correta": 1,
        },
        {
            "pergunta": "O que você (eu-lírico) faz que irrita o noivo?",
            "opcoes": [
                "Demorar 20min pra passar o turno nas noites de jogos.",
                "Falar que está chegando e não ter nem saído de casa.",
                "Sumir quando começava a namorar.",
                "Contar os biscoitos no pacote pra saber quando alguém pegava escondido.",
                "Ficar enchendo o saco do noivo em toda oportunidade possível.",
            ],
            "correta": 2,
        },
        {
            "pergunta": "Por quê você (eu-lírico) é especial para o noivo?",
            "opcoes": [
                "Porque tem uma profissão interessante e é preciso ter amigos que saibam disso.",
                "Porque não tinha mais ninguém para ele ser amigo.",
                "Porque você contou uma piada engraçada uma vez há anos atrás.",
                "Poque você é companheiro, irmão, amigo e pau pra toda obra. Ele sabe que pode contar com você sempre.",
                
            ],
            "correta": 3,
        },
    ],
    "Alfredo": [
        {
            "pergunta": "O que o casal gosta de fazer juntos?",
            "opcoes": [
                "Assistir a missa do Pastor Edir Macêdo.",
                "Comprar calças coloridas no shopping.",
                "Ir pro barzinho e ir pra roda de samba.",
            ],
            "correta": 2,
        },
        {
            "pergunta": "Qual foi o maior perrengue que o casal já passou juntos?",
            "opcoes": [
                "Pagar 200€ de táxi pra chegar a tempo na estação de Milão.",
                "Gaivotas atacarem o drone no Algarve e depois atacarem o casal.",
                "Parar uma festa para procurar um telefone por 30min (estava no bolso da noiva).",
            ],
            "correta": 0,
        },
        {
            "pergunta": "Qual o programa ideal para uma quinta a noite?",
            "opcoes": [
                "Ensaio do bloco Secretinho.",
                "Partidinha de War of the Ring.",
                "Date em casa com queijos e vinhos.",
            ],
            "correta": 2,
        },
        {
            "pergunta": "Se o casal fosse abrir um negócio juntos, qual seria?",
            "opcoes": [
                "Uma livraria com um café dentro.",
                "Um barzinho com jogos de tabuleiro.",
                "Um salão de beleza para pets.",
            ],
            "correta": 1,
        },
        {
            "pergunta": "Qual a hamburgueria favorita do casal em Lisboa?",
            "opcoes": [
                "Street Smash Burger.",
                "Hamburgueria Honorato.",
                "Evaldo.",
            ],
            "correta": 2,
        },
        {
            "pergunta": "Qual o destino da lua de mel dos sonhos do casal?",
            "opcoes": [
                "Tailândia.",
                "Nova York.",
                "Pirenópolis.",
            ],
            "correta": 0,
        },
        {
            "pergunta": "O que o noivo adora fazer quando bebe todas?",
            "opcoes": [
                "Conversar com novas pessoas e fazer amigos.",
                "Deitar e apagar em qualquer superfície existente.",
                "Se retirar da festa pois já está muito tarde para ele.",
            ],
            "correta": 1,
        },
        {
            "pergunta": "O que você (eu-lírico) faz que irrita o noivo?",
            "opcoes": [
                "Demorar 20min pra passar o turno nas noites de jogos.",
                "Falar que está chegando e não ter nem saído de casa.",
                "Sumir quando começava a namorar.",
                "Contar os biscoitos no pacote pra saber quando alguém pegava escondido.",
                "Ficar enchendo o saco do noivo em toda oportunidade possível.",
            ],
            "correta": 3,
        },
        {
            "pergunta": "Por quê você (eu-lírico) é especial para o noivo?",
            "opcoes": [
                "Porque tem uma profissão interessante e é preciso ter amigos que saibam disso.",
                "Porque não tinha mais ninguém para ele ser amigo.",
                "Porque você contou uma piada engraçada uma vez há anos atrás.",
                "Poque você é companheiro, irmão, amigo e pau pra toda obra. Ele sabe que pode contar com você sempre.",
                
            ],
            "correta": 3,
        },
    ],
    "Vitor": [
        {
            "pergunta": "O que o casal gosta de fazer juntos?",
            "opcoes": [
                "Assistir a missa do Pastor Edir Macêdo.",
                "Comprar calças coloridas no shopping.",
                "Ir pro barzinho e ir pra roda de samba.",
            ],
            "correta": 2,
        },
        {
            "pergunta": "Qual foi o maior perrengue que o casal já passou juntos?",
            "opcoes": [
                "Pagar 200€ de táxi pra chegar a tempo na estação de Milão.",
                "Gaivotas atacarem o drone no Algarve e depois atacarem o casal.",
                "Parar uma festa para procurar um telefone por 30min (estava no bolso da noiva).",
            ],
            "correta": 0,
        },
        {
            "pergunta": "Qual o programa ideal para uma quinta a noite?",
            "opcoes": [
                "Ensaio do bloco Secretinho.",
                "Partidinha de War of the Ring.",
                "Date em casa com queijos e vinhos.",
            ],
            "correta": 2,
        },
        {
            "pergunta": "Se o casal fosse abrir um negócio juntos, qual seria?",
            "opcoes": [
                "Uma livraria com um café dentro.",
                "Um barzinho com jogos de tabuleiro.",
                "Um salão de beleza para pets.",
            ],
            "correta": 1,
        },
        {
            "pergunta": "Qual a hamburgueria favorita do casal em Lisboa?",
            "opcoes": [
                "Street Smash Burger.",
                "Hamburgueria Honorato.",
                "Evaldo.",
            ],
            "correta": 2,
        },
        {
            "pergunta": "Qual o destino da lua de mel dos sonhos do casal?",
            "opcoes": [
                "Tailândia.",
                "Nova York.",
                "Pirenópolis.",
            ],
            "correta": 0,
        },
        {
            "pergunta": "O que o noivo adora fazer quando bebe todas?",
            "opcoes": [
                "Conversar com novas pessoas e fazer amigos.",
                "Deitar e apagar em qualquer superfície existente.",
                "Se retirar da festa pois já está muito tarde para ele.",
            ],
            "correta": 1,
        },
        {
            "pergunta": "O que você (eu-lírico) faz que irrita o noivo?",
            "opcoes": [
                "Demorar 20min pra passar o turno nas noites de jogos.",
                "Falar que está chegando e não ter nem saído de casa.",
                "Sumir quando começava a namorar.",
                "Contar os biscoitos no pacote pra saber quando alguém pegava escondido.",
                "Ficar enchendo o saco do noivo em toda oportunidade possível.",
            ],
            "correta": 4,
        },
        {
            "pergunta": "Por quê você (eu-lírico) é especial para o noivo?",
            "opcoes": [
                "Porque tem uma profissão interessante e é preciso ter amigos que saibam disso.",
                "Porque não tinha mais ninguém para ele ser amigo.",
                "Porque você contou uma piada engraçada uma vez há anos atrás.",
                "Poque você é companheiro, irmão, amigo e pau pra toda obra. Ele sabe que pode contar com você sempre.",
                
            ],
            "correta": 3,
        },
    ],
}

# ---------------------------------------------------------------------------
# Audio player
# ---------------------------------------------------------------------------
# st.audio(autoplay) runs after a server round-trip, so the browser no longer
# treats it as a direct user gesture — autoplay is blocked. This iframe calls
# audio.play() from an onclick handler in the same document, which every
# browser allows.
# Streamlit static serving is not used for this file: .mp4 is not in the
# list of content types that get a correct MIME (others get text/plain), so
# <audio src="/app/static/..."> would break. A data: URL with base64 is used.

@st.cache_data(show_spinner=False)
def _data_url_audio() -> str:
    musica = os.path.join("song", "The Lord of the Rings Music - The Fellowship.mp4")
    with open(musica, "rb") as f:
        b64 = base64.b64encode(f.read()).decode("ascii")
    return f"data:audio/mp4;base64,{b64}"


_AUDIO_HTML = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8"/>
<style>
  body {{ margin:0; font-family: system-ui, sans-serif; background: transparent; }}
  .bar {{
    display:flex; flex-wrap:wrap; align-items:center; gap:10px 14px;
    padding:10px 14px;
    background: linear-gradient(90deg, #1a1a2e, #16213e);
    color: #e8e8e8; border-radius: 10px; font-size: 14px; max-width: 100%;
  }}
  button {{
    background: #c9a227; color: #1a1a1a; border: none;
    padding: 9px 18px; border-radius: 8px; font-weight: 600; cursor: pointer;
  }}
  button:hover {{ filter: brightness(1.08); }}
  .ok {{ color: #a8d5a2; font-size: 13px; }}
  .hint {{ color: #9aa0a6; font-size: 12px; }}
  .hidden {{ display: none !important; }}
</style>
</head>
<body>
<audio id="bg" src="__SRC__" preload="none"></audio>
<div class="bar" id="wrap">
  <span id="line1">Para uma experiência completa, ative a</span>
  <button type="button" id="playBtn">Trilha Sonora</button>
  <span class="ok hidden" id="ok">!</span>
</div>
<script>
(function() {{
  var a = document.getElementById("bg");
  var POS = "padrinhos_audio_time";
  // Limpa posições antigas (gravadas quando havia play automático no canplay)
  try {{
    if (!localStorage.getItem("padrinhos_player_v2")) {{
      localStorage.removeItem(POS);
      localStorage.setItem("padrinhos_player_v2", "1");
    }}
  }} catch (e) {{}}
  // 3:17 — só o clique inicia; sem play ao carregar (evita avanço em segundo plano)
  var START_SEC = 197;
  var btn = document.getElementById("playBtn");
  var line1 = document.getElementById("line1");
  var ok = document.getElementById("ok");

  function setPlayingUi() {{
    line1.classList.add("hidden");
    btn.classList.add("hidden");
    ok.classList.remove("hidden");
  }}

  a.addEventListener("ended", function() {{
    try {{ localStorage.removeItem(POS); }} catch (e) {{}}
    a.currentTime = 0;
    a.play().catch(function(){{}});
  }});

  setInterval(function() {{
    if (!a.paused && !a.ended) {{
      try {{ localStorage.setItem(POS, String(a.currentTime)); }} catch (e) {{}}
    }}
  }}, 400);

  function seekAndPlay(seconds) {{
    a.currentTime = seconds;
    return a.play();
  }}

  // Primeiro clique: 3:17 (197 s). Clicar de novo o mesmo botão: — sem botão após o primeiro
  // Se o iframe for recriado a meio da jornada, POS guarda a posição para retomar.
  btn.addEventListener("click", function() {{
    var saved = localStorage.getItem(POS);
    var sec = (saved !== null && !isNaN(parseFloat(saved)))
      ? parseFloat(saved)
      : START_SEC;
    seekAndPlay(sec)
      .then(function() {{ setPlayingUi(); }})
      .catch(function() {{}});
  }});
}})();
</script>
</body>
</html>"""


def injetar_player_audio() -> None:
    src = _data_url_audio()
    html = _AUDIO_HTML.replace("__SRC__", src)
    components.html(html, height=100)


# ---------------------------------------------------------------------------
# State management
# ---------------------------------------------------------------------------

_CHAVES_PADRAO: dict = {
    "usuario_logado": None,
    "respostas": {},
    "submetido": False,
}


def init_state() -> None:
    for chave, valor in _CHAVES_PADRAO.items():
        if chave not in st.session_state:
            st.session_state[chave] = valor


def reiniciar_questionario() -> None:
    st.session_state.respostas = {}
    st.session_state.submetido = False


def fazer_logout() -> None:
    for chave, valor in _CHAVES_PADRAO.items():
        st.session_state[chave] = valor


# ---------------------------------------------------------------------------
# Telas
# ---------------------------------------------------------------------------

def tela_login() -> None:
    st.title("O Pergaminho Oculto")
    st.write("Saudações, nobres viajantes!")
    st.write("Preparem o fôlego e ajustem suas capas, pois uma convocação vinda das terras distantes acaba de chegar. Se você está lendo isto, é porque seu nome foi sussurrado entre os sábios e sua lealdade é conhecida além das fronteiras do Condado.")
    st.write("📜 A Prova de Merecimento")
    st.write("Para alcançar o que está oculto no final desta busca, você deve provar que é um verdadeiro aliado da nossa Sociedade.")
    st.write("• O Desafio: Acerte todas as perguntas do quiz.")
    st.write("• A Recompensa: O acesso a uma mensagem destinada apenas aos mais honrados.")
    st.write('"Até a menor das pessoas pode mudar o curso do futuro."')
    st.write("Você aceita o desafio desta jornada?")


    _, col, _ = st.columns([1, 2, 1])
    with col:
        with st.form("login"):
            nome = st.text_input("Como o noivo te chama")
            data = st.date_input(
                "Sua data de aniversário",
                value=None,
                min_value=date(1990, 1, 1),
                max_value=date(2005, 12, 31),
                format="DD/MM/YYYY",
            )
            enviado = st.form_submit_button("Validar", use_container_width=True)

        if enviado:
            nome_normalizado = nome.strip().title()
            if nome_normalizado in CREDENCIAIS and data == CREDENCIAIS[nome_normalizado]:
                st.session_state.usuario_logado = nome_normalizado
                st.rerun()
            else:
                st.error("Credenciais não encontradas. Tente novamente.")


def tela_questionario() -> None:
    usuario = st.session_state.usuario_logado
    perguntas = PERGUNTAS[usuario]

    col_titulo, col_sair = st.columns([4, 1])
    with col_titulo:
        st.title(f"Olá, {usuario}!")
    with col_sair:
        st.write("")
        if st.button("Sair", use_container_width=True):
            fazer_logout()
            st.rerun()

    st.info(
        "Bem-vindo ao Quizz do PArgaminho Oculto! Responda às perguntas sobre as histórias "
        "dos noivos. Você precisa acertar **TODAS** para chegar ao final."
    )
    st.divider()

    with st.form("quiz"):
        respostas_form: dict[int, int] = {}
        for i, item in enumerate(perguntas):
            st.markdown(f"**{i + 1}. {item['pergunta']}**")
            escolha = st.radio(
                label=f"Pergunta {i + 1}",
                options=range(len(item["opcoes"])),
                format_func=lambda x, opts=item["opcoes"]: opts[x],
                index=None,
                key=f"q_{i}",
                label_visibility="collapsed",
            )
            respostas_form[i] = escolha
            st.write("")

        enviado = st.form_submit_button("Enviar respostas", use_container_width=True)

    if enviado:
        nao_respondidas = [i + 1 for i, v in respostas_form.items() if v is None]
        if nao_respondidas:
            st.warning(
                f"Responda todas as perguntas antes de enviar. "
                f"Faltam: {', '.join(str(n) for n in nao_respondidas)}."
            )
        else:
            st.session_state.respostas = respostas_form
            st.session_state.submetido = True
            st.rerun()


def tela_resultado() -> None:
    usuario = st.session_state.usuario_logado
    perguntas = PERGUNTAS[usuario]
    respostas = st.session_state.respostas

    acertos = sum(
        respostas[i] == perguntas[i]["correta"] for i in range(len(perguntas))
    )
    percentual = acertos / len(perguntas) * 100

    col_titulo, col_sair = st.columns([4, 1])
    with col_titulo:
        st.title(f"Resultado de {usuario}")
    with col_sair:
        st.write("")
        if st.button("Sair", use_container_width=True):
            fazer_logout()
            st.rerun()

    st.divider()

    if acertos == len(perguntas):
        st.success("Parabéns! Você acertou tudo e encontrou o seu Pergaminho Oculto!")
        caminho_imagem = os.path.join("imagens", f"{usuario}.png")
        if os.path.exists(caminho_imagem):
            st.image(caminho_imagem, use_container_width=True)
        else:
            st.error("Imagem do tesouro não encontrada.")

        if st.button("Jogar de novo", use_container_width=True):
            reiniciar_questionario()
            st.rerun()
    else:
        st.warning(f"Voce acertou {percentual:.0f}% das questões! Tente novamente!")
        if st.button("Reiniciar Questionário", use_container_width=True):
            reiniciar_questionario()
            st.rerun()


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    st.set_page_config(
        page_title="Caca ao Tesouro",
        page_icon="assets/icon.png" if os.path.exists("assets/icon.png") else None,
        layout="centered",
    )
    init_state()
    # Same block order on every run so the iframe is not needlessly remounted.
    injetar_player_audio()

    if st.session_state.usuario_logado is None:
        tela_login()
    elif not st.session_state.submetido:
        tela_questionario()
    else:
        tela_resultado()


if __name__ == "__main__":
    main()
