# PluralAlert

![GitHub repo size](https://img.shields.io/github/repo-size/iuricode/README-template?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/iuricode/README-template?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/iuricode/README-template?style=for-the-badge)
![Bitbucket open issues](https://img.shields.io/bitbucket/issues/iuricode/README-template?style=for-the-badge)
![Bitbucket open pull requests](https://img.shields.io/bitbucket/pr-raw/iuricode/README-template?style=for-the-badge)

> Linha adicional de texto informativo sobre o que o projeto faz. Sua introdução deve ter cerca de 2 ou 3 linhas. Não exagere, as pessoas não vão ler.

## 💻 Pré-requisitos

Antes de começar, verifique se você atendeu aos seguintes requisitos:

- Você instalou a versão mais recente de `uv`
- Você tem uma máquina `Linux, Mac e Windows não é garantido`
- 
## ☕ Rodando PluralAlert

Linux: 
```
curl -LsSf https://astral.sh/uv/install.sh | sh (para instalação do uv)
git clone https://github.com/NerdSystem0228/PluralAlert
cd PluralAlert
uv sync
uv run main.py
```

With docker:
```
git clone https://github.com/NerdSystem0228/PluralAlert
cd PluralAlert
docker build . -t <nome do seu bot>
nano docker-compose.yml.example (modifique com seu gosto)
docker-compose up -d
```

## 📝 Licença

Esse projeto está sob licença. Veja o arquivo [LICENÇA](LICENSE.md) para mais detalhes.
