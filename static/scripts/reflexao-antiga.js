const fraseEl = document.getElementById('frase');
const dataEl = document.getElementById('data');

// Pega a data da URL no formato YYYY-MM-DD
const params = new URLSearchParams(window.location.search);
const dataStr = params.get('data');

if (!dataStr) {
  fraseEl.textContent = "Data inválida.";
} else {
  const [ano, mes, dia] = dataStr.split('-');
  const baseURL = "https://paodiario.onrender.com";
  const url = `${baseURL}/frases?ano=${ano}&mes=${mes}&dia=${dia}`;

  fetch(url)
    .then(res => {
      if (!res.ok) throw new Error("Frase não encontrada");
      return res.json();
    })
    .then(data => {
      dataEl.textContent = `🗓️ ${dataStr}`;
      fraseEl.textContent = data.texto || "Hoje o padeiro dormiu. Volte amanhã! 💤";
    })
    .catch(err => {
      console.error("Erro ao carregar frase:", err);
      fraseEl.textContent = "Erro ao carregar a fornada do dia. 😓";
    });
}
