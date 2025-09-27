// Elemento onde será exibida a frase
const fraseElemento = document.getElementById('frase');

// Pega a data atual no formato ano/mês/dia
const hoje = new Date();
const ano = String(hoje.getFullYear());
const mes = String(hoje.getMonth() + 1).padStart(2, '0');
const dia = String(hoje.getDate()).padStart(2, '0');

// Monta a URL da API
const BASE_API = "https://paodiario.onrender.com";  // substitua pela URL real
const API_URL = `${BASE_API}/frases?ano=${ano}&mes=${mes}&dia=${dia}`;

// Busca a frase do dia via API
fetch(API_URL)
  .then(res => {
    if (!res.ok) throw new Error("Frase não encontrada");
    return res.json();
  })
  .then(data => {
    fraseElemento.textContent = data.texto || "Reflexão não disponível para hoje. Tente novamente mais tarde.";
  })
  .catch(err => {
    console.error("Erro ao carregar frase:", err);
    fraseElemento.textContent = "Erro ao carregar a reflexão do dia. Tente novamente mais tarde.";
  });
