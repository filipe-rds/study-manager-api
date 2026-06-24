# Study Manager API

Study Manager API é uma aplicação em Python para gerenciamento de estudos, organizada em torno de usuários, disciplinas
e tópicos.

O projeto está sendo construído de forma incremental, com foco em fundamentos sólidos de desenvolvimento de software,
testes automatizados, tipagem estática e evolução arquitetural consciente.

## Objetivo

Este projeto está sendo desenvolvido como parte de um processo de aprendizado técnico em desenvolvimento de software.

A proposta é construir uma API para gerenciamento de estudos, permitindo que usuários organizem disciplinas, cadastrem
tópicos, acompanhem progresso e marquem conteúdos como concluídos.

Além da funcionalidade da aplicação, o projeto tem como objetivo praticar:

* modelagem de domínio;
* testes automatizados;
* organização de projetos Python;
* tipagem estática;
* separação de responsabilidades;
* uso consciente de padrões como Repository e Adapter;
* construção gradual de uma API com FastAPI;
* persistência com banco de dados.

## Tecnologias

* Python
* uv
* pytest
* ty
* Ruff
* FastAPI
* SQLite

## Estrutura planejada

O projeto será evoluído em camadas conforme a necessidade:

```text
domain        → regras de negócio e modelos principais
application   → casos de uso da aplicação
ports         → contratos, como repositórios
adapters      → implementações externas, como banco de dados
api           → entrada HTTP com FastAPI
```

## Execução

Sincronizar dependências:

```bash
uv sync
```

Rodar testes:

```bash
uv run pytest
```

Checar tipagem:

```bash
uv run ty check
```

Formatar código:

```bash
uv run ruff format
```

Verificar lint:

```bash
uv run ruff check
```

## Status

Projeto em construção incremental.

As funcionalidades, camadas e integrações serão adicionadas progressivamente, priorizando simplicidade, testes e clareza
de design antes de expandir a arquitetura.
