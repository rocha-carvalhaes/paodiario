// Elemento onde será exibida a frase
const fraseEl = document.getElementById('frase');

// Pega a data atual no formato ano/mês/dia
const hoje = new Date();
const ano = String(hoje.getFullYear());
const mes = String(hoje.getMonth() + 1).padStart(2, '0'); // meses começam em 0
const dia = String(hoje.getDate()).padStart(2, '0');

// Carrega o arquivo JSON e acessa a frase correspondente
fetch('../data/frases.json')
.then(res => {
    if (!res.ok) throw new Error("Falha ao buscar frases.");
    return res.json();
})
.then(frases => {
    const frase = frases?.[ano]?.[mes]?.[dia];
    fraseEl.textContent = frase || "Hoje o padeiro dormiu. Volte amanhã! 💤";
})
.catch(err => {
    console.error("Erro ao carregar frase:", err);
    fraseEl.textContent = "Erro ao carregar a fornada do dia. 😓";
});
