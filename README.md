# Dia 2 – Limpador Automático de CSV

Script para limpeza básica de arquivos CSV, removendo espaços em colunas e dados, e excluindo colunas vazias.

## ✅ Funcionalidades

- Remove espaços à esquerda/direita em:
  - Nomes de colunas
  - Valores textuais
- Remove colunas que:
  - Estão 100% nulas
  - Contêm apenas espaços em branco
- Salva arquivos limpos em `./arquivos_limpos`

## 📦 Estrutura

```
clean_csv_automatically/
├── clean_csv.py
├── sujo.csv
├── arquivos_limpos/
└── README.md
```

## 🚀 Como usar

1. Coloque seus arquivos `.csv` na mesma pasta do script
2. Rode o script:
```bash
python Limpeza-de-csv-python.py
```
3. Os arquivos limpos estarão em `./arquivos_limpos`

## 📌 Exemplo

Entrada: `Limpeza-de-csv-python.csv`  
Saída: `clientes_sujos_limpo.csv`

- 
## 👨‍💻 Autor

Desenvolvido por [Welson Viana](https://github.com/Welsonvv)

---

## 🛡️ Licença

MIT License
