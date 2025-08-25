const container = document.getElementById("cardsContainer");

const API_URL = "https://paodiario.onrender.com/todas-frases";

fetch(API_URL)
  .then(res => {
    if (!res.ok) throw new Error("Falha ao carregar frases");
    return res.json();
  })
  .then(data => {
    const frases = [];

    for (const key in data) {
    const item = data[key];
    const ano = String(item.ano);
    const mes = String(item.mes).padStart(2, '0');
    const dia = String(item.dia).padStart(2, '0');
    const texto = item.texto;

    const dateStr = `${ano}-${mes}-${dia}`;

    frases.push({
        date: dateStr,
        phrase: texto
    });
    }

    // Ordena da mais recente para mais antiga
    frases.sort((a, b) => new Date(b.date) - new Date(a.date));

    // Gera os cards
    frases.forEach(frase => {
      const card = document.createElement("div");
      card.className = "card";

      const dataDiv = document.createElement("div");
      dataDiv.className = "date";
      dataDiv.textContent = frase.date;

      const texto = document.createElement("div");
      texto.className = "phrase-preview";
      texto.textContent = frase.phrase;

      card.appendChild(dataDiv);
      card.appendChild(texto);
      container.appendChild(card);

      card.addEventListener("click", () => {
        window.location.href = `reflexao-antiga.html?data=${frase.date}`;
      });
    });
  })
  .catch(err => {
    const erro = document.createElement("div");
    erro.textContent = "Erro ao carregar frases.";
    erro.style.color = "red";
    container.appendChild(erro);
    console.error(err);
  });
