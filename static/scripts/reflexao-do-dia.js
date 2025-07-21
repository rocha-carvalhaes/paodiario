// Elemento onde será exibida a frase
const fraseEl = document.getElementById('frase');

// Pega a data atual no formato ano/mês/dia
const hoje = new Date();
const ano = String(hoje.getFullYear());
const mes = String(hoje.getMonth() + 1).padStart(2, '0');
const dia = String(hoje.getDate()).padStart(2, '0');

// Monta a URL da API
const baseURL = "https://paodiario.onrender.com";  // substitua pela URL real
const url = `${baseURL}/frases?ano=${ano}&mes=${mes}&dia=${dia}`;

// Busca a frase do dia via API
fetch(url)
  .then(res => {
    if (!res.ok) throw new Error("Frase não encontrada");
    return res.json();
  })
  .then(data => {
    fraseEl.textContent = data.texto || "Hoje o padeiro dormiu. Volte amanhã! 💤";
  })
  .catch(err => {
    console.error("Erro ao carregar frase:", err);
    fraseEl.textContent = "Erro ao carregar a fornada do dia. 😓";
  });
