const axios = require('axios');
const readline = require('readline');

const BASE_URL = 'http://localhost:8000';

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

function menu() {
  console.log("\n=== MENU CLIENTE JAVASCRIPT ===");
  console.log("1. Cadastrar produto");
  console.log("2. Listar produtos");
  console.log("3. Sair");
  rl.question("Escolha uma opção: ", async (resposta) => {
    switch (resposta.trim()) {
      case '1':
        await cadastrarProduto();
        menu();
        break;
      case '2':
        await listarProdutos();
        menu();
        break;
      case '3':
        console.log("Saindo...");
        rl.close();
        break;
      default:
        console.log("Opção inválida.");
        menu();
    }
  });
}

async function cadastrarProduto() {
  const perguntas = [
    "Nome: ", "Fabricante: ", "Preço: ", "Quantidade: ", "Tipo biológico (vacina): ", "Validade (YYYY-MM-DD): "
  ];

  const respostas = [];

  const perguntar = (i) => {
    return new Promise((resolve) => {
      rl.question(perguntas[i], (resp) => {
        respostas.push(resp.trim());
        resolve();
      });
    });
  };

  for (let i = 0; i < perguntas.length; i++) {
    await perguntar(i);
  }

  const produto = {
    nome: respostas[0],
    fabricante: respostas[1],
    preco: parseFloat(respostas[2]),
    quantidade: parseInt(respostas[3]),
    tipo_biologico: respostas[4],
    validade: respostas[5]
  };

  try {
    const res = await axios.post(`${BASE_URL}/produtos/vacina_perecivel`, produto);
    console.log("Produto cadastrado com sucesso:", res.data);
  } catch (err) {
    console.error("Erro ao cadastrar:", err.response?.data || err.message);
  }
}

async function listarProdutos() {
  try {
    const res = await axios.get(`${BASE_URL}/produtos`);
    console.log("\n=== Produtos ===");
    console.log(res.data);
  } catch (err) {
    console.error("Erro ao listar:", err.response?.data || err.message);
  }
}

menu();
