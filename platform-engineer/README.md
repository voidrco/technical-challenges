# AI e Software Engineer de Plataforma — Technical Challenge

Take-home challenge | 5 dias | dedicação estimada de 4–6 horas

## O que este exercício avalia

Componente reutilizável de processamento de eventos. O objetivo é observar decisões, execução, conferência e capacidade de dar continuidade ao trabalho. Um plano convincente sem artefato utilizável ou evidência não é suficiente.

## Contexto e materiais

Duas contas consomem eventos de tickets em formatos diferentes. A plataforma precisa de um contrato estável, isolamento por conta e reprocessamento sem duplicar efeitos.

- [context.md](./case/context.md)
- [input.csv](./case/input.csv)
- [raw-examples.json](./case/raw-examples.json)
- [update.md](./case/update.md)

Todos os dados são fictícios. Este desafio não é trabalho de produção, prestação de serviço ou acesso a sistemas reais. Consulte [a Voidr](https://www.voidr.co) para contexto de produto; não transforme mensagens comerciais em capacidades ou resultados comprovados. Registre o que é evidência, hipótese, proposta ou informação ausente.

## Missão — etapa 1

1. Construa um módulo local que normalize dois formatos de entrada e gere eventos rastreáveis sem duplicar efeitos, respeitando tenant e autorização. Não precisa de cloud ou banco.
2. Defina contrato de entrada/saída e pelo menos quatro testes executáveis: duplicidade, payload inválido, isolamento e evento não autorizado.
3. Documente uma decisão de arquitetura, limite do escopo, observabilidade e procedimento de evolução/reversão.
4. Inclua uma interface fictícia de classificação por IA com saída validada e fallback; use respostas locais determinísticas, sem API paga. Mostre uma sugestão de IA rejeitada.

## Missão — etapa 2: mudança de contexto

Depois de salvar a primeira versão, leia [update.md](./case/update.md). Revise o mesmo trabalho e demonstre a diferença. Explique o que concluiu, o que verificou, o que depende de alguém e a próxima ação. Não faça uma segunda apresentação.

## Entregáveis

1. Um arquivo HTML/PDF de 4–6 páginas ou slides com decisões, evidências, resultado e handover.
2. Um ZIP ou repositório com tabelas, código quando solicitado, entradas/saídas e instruções de reprodução. Cada peça deve aparecer uma vez; organize anexos no mesmo pacote.
3. Vídeo de 10–15 minutos em inglês mostrando o mesmo trabalho e respondendo à etapa 2. Apresentação em inglês; código, tabelas e mensagens operacionais podem ser em português ou inglês. Avaliamos comunicação compreensível e raciocínio, não sotaque.
4. Registro de IA de até meia página: ferramenta, um prompt útil, resultado conferido e uma sugestão corrigida ou rejeitada. Uso de IA é parte do exercício; você deve explicar a própria contribuição.

## Restrições e esforço

- Prazo de cinco dias após o recebimento. Avise se houver conflito de agenda.
- Planeje 4–6h e pare em seis horas; registre o que ficou pendente. Não construa sistema completo, LMS ou infraestrutura em nuvem.
- Nenhuma conta paga, LLM API, dado pessoal real ou integração externa é necessária. Onde há código, execução local é suficiente e linguagem é livre.
- Não contate clientes, não faça pagamentos ou envios reais, não conceda acesso nem declare aprovações inexistentes.
- Mudanças, contratos, publicação e controles em ambiente real exigem responsáveis e alçadas; no exercício são propostas.
- Estética e quantidade de documentos não dão pontos extras. Não incluímos trabalho de candidato na produção.

## Critérios de avaliação

- 30% compreensão do problema e julgamento: evidência, prioridade, limite e alternativa.
- 35% execução verificável: artefato utilizável, cálculos/testes corretos e reprodutibilidade.
- 20% continuidade: responsáveis, exceções, dependências, adaptação e handover.
- 15% comunicação e uso crítico de IA: clareza, contribuição própria e revisão.

A revisão é humana. Uma nota automática não decide avanço. Requisitos específicos seguem o JD; não avaliamos atributos pessoais protegidos.

## Como entregar

Envie para **hiring@jobs.voidr.co**, com cópia para **nathalia@voidr.co**.
Assunto: **[Technical Challenge Voidr] - Seu nome completo - AI e Software Engineer de Plataforma**.
Inclua apresentação, ZIP/repositório e link do vídeo; confira permissões de leitura. Não inclua credenciais.

## Conversa seguinte

Se avançar, teremos uma conversa de 45 minutos sobre o trabalho existente, uma alteração pequena de requisito e sua contribuição própria. Não há novo take-home. A equipe registra evidências, pendências e feedback.
