# Study Manager API

Study Manager API é uma aplicação em Python para gerenciamento de estudos, organizada em torno de usuários, disciplinas e tópicos.

O projeto está sendo construído de forma incremental, com foco em fundamentos sólidos de desenvolvimento de software, testes automatizados, tipagem estática, arquitetura serverless e evolução consciente do design.

## Objetivo

Este projeto está sendo desenvolvido como parte de um processo de aprendizado técnico em desenvolvimento de software e cloud.

A proposta é construir uma aplicação serverless para gerenciamento de estudos, permitindo que usuários organizem disciplinas, cadastrem tópicos, acompanhem progresso e marquem conteúdos como concluídos.

Além da funcionalidade da aplicação, o projeto tem como objetivo praticar:

* modelagem de domínio;
* testes automatizados;
* organização de projetos Python;
* tipagem estática;
* separação de responsabilidades;
* arquitetura serverless;
* uso consciente de padrões como Repository e Adapter;
* integração com serviços AWS em ambiente local;
* evolução incremental orientada por casos de uso.

## Tecnologias

* Python
* uv
* pytest
* ty
* Ruff
* Makefile
* AWS local stack / ministack
* AWS API Gateway
* AWS Lambda
* DynamoDB

## Arquitetura planejada

O projeto seguirá uma arquitetura serverless, mantendo o domínio independente de frameworks, serviços externos e detalhes de infraestrutura.

A evolução será feita em camadas conforme a necessidade:

```text
domain        → regras de negócio e modelos principais
application   → casos de uso da aplicação
ports         → contratos, como repositórios
adapters      → implementações externas, como DynamoDB local
entrypoints   → handlers serverless acionados por API Gateway/Lambda
```

Fluxo arquitetural planejado:

```text
API Gateway
    ↓
AWS Lambda
    ↓
Application Use Case
    ↓
Domain
    ↓
Repository Port
    ↓
DynamoDB Adapter
```

## Decisões arquiteturais

### Domínio independente

As entidades de domínio não devem depender de AWS, DynamoDB, Lambda handlers, API Gateway ou qualquer detalhe de infraestrutura.

O domínio deve permanecer simples, testável e isolado.

### Serverless como modelo de entrada

A entrada HTTP da aplicação será feita por AWS API Gateway, que encaminhará eventos para funções AWS Lambda.

A aplicação não utilizará um framework web tradicional como camada principal de entrada. Os handlers Lambda serão responsáveis apenas por interpretar eventos, chamar casos de uso e montar respostas HTTP compatíveis com API Gateway.

### Persistência como adapter

A persistência será tratada como detalhe de infraestrutura.

O domínio e os casos de uso dependerão de contratos, enquanto a implementação concreta poderá usar serviços locais da AWS, como DynamoDB.

### Evolução incremental

O projeto será desenvolvido por etapas.

Novas camadas, adapters e integrações serão adicionados apenas quando houver necessidade clara no fluxo da aplicação.

## Execução

Sincronizar dependências:

```bash
uv sync
```

Formatar código:

```bash
uv run ruff format
```

Verificar lint:

```bash
uv run ruff check
```

Checar tipagem:

```bash
uv run ty check
```

Rodar todos os testes:

```bash
uv run pytest tests
```

## Validação com Makefile

Em ambientes com `make` disponível, é possível executar as validações do projeto com:

```bash
make check
```

Esse comando executa:

```text
format
lint
typecheck
test
```

## Status

Projeto em construção incremental.

As funcionalidades, camadas e integrações serão adicionadas progressivamente, priorizando simplicidade, testes, clareza de design e independência entre domínio, aplicação e infraestrutura.
