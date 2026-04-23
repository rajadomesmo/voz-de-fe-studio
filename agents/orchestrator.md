# ORQUESTRADOR — Voz e Fé

## Papel do Agent Team
100% pré-produção e mentoria. A produção (áudio, vídeo, upload) é sempre manual.

---

## Regra universal — SEMPRE antes de qualquer ciclo

Independente do que o usuário pedir, execute SEMPRE estas 2 etapas antes:

PRÉ-CICLO obrigatório:
1. agent-memory → leia MEMORY. Identifique: últimos temas, hooks usados, o que foi descartado, formatos recentes
2. agent-researcher → faça varredura rápida de incremento:
   - Leia knowledge\canais-referencia\shorts-referencia.md
   - Leia seo\tendencias.md (se existir)
   - Via Chrome MCP, busque no YouTube os 3 Shorts de oração mais recentes (últimos 7 dias)
   - Identifique se há tema novo em alta não explorado ainda
   - Salve achados novos em seo\tendencias.md (append, não sobrescrever)

Só depois do PRÉ-CICLO inicia o ciclo solicitado.

---

## CICLO SHORTS

Ativado quando: usuário pedir shorts, vídeos curtos, novos conteúdos

Etapa 1 — PRÉ-CICLO (obrigatório — ver acima)

Etapa 2 — Roteiros
agent-scriptwriter → com base no PRÉ-CICLO, gere os scripts solicitados:
- Hook de prova social obrigatório (0-3s)
- Versículo bíblico real — priorizar Salmos
- Corpo com [pausa curta] e marcadores de ênfase
- CTA de hábito obrigatório — não apenas "se inscreva"
- Prompt de imagem em inglês para Gemini (dark, cinematic, 9:16, no text)
- Nunca repetir Salmo ou estrutura dos últimos 3 gerados

Etapa 3 — SEO
agent-seo → gere pacote SEO completo para cada Short:
- 3 opções de título (máx 60 caracteres)
- Descrição curta com keyword na 1ª linha
- 5 hashtags
- Horário sugerido de postagem

Etapa 4 — Memória
agent-memory → atualize MEMORY com temas, Salmos, hooks e CTAs usados. Sugira próximos 3 temas.

Salvar em:
- shorts\scripts\short-[N]-[tema].md
- seo\seo-short-[N].md

---

## CICLO LIVE

Ativado quando: usuário pedir live, conteúdo longo, roteiro para Gyre

Etapa 1 — PRÉ-CICLO (obrigatório — ver acima)

Etapa 2 — Roteiro longo
agent-scriptwriter → gere roteiro de 30-60 min:
- Formato: SLEEP PRAYER ou SALMO GUIADO
- Versículos reais com leitura lenta
- Marcadores [pausa longa] entre blocos
- Prompt de imagem de fundo para loop no Gyre

Etapa 3 — SEO
agent-seo → título, descrição 300+ palavras, tags, horário

Etapa 4 — Memória
agent-memory → registre no MEMORY

Salvar em:
- live\playlist\oracao-loop-[N].md
- seo\seo-live-[N].md

---

## CICLO PESQUISA

Ativado quando: usuário pedir tendências, o que está em alta, análise de mercado

Etapa 1 — PRÉ-CICLO (obrigatório — ver acima)

Etapa 2 — Pesquisa profunda
agent-researcher → pesquisa completa:
- Busque Shorts de oração dos últimos 30 dias
- Identifique 5 temas com maior potencial não explorado ainda
- Compare com histórico de MEMORY para garantir novidade
- Sugira próximos 10 temas em ordem de prioridade

Etapa 3 — Memória
agent-memory → atualize Fila de Temas no MEMORY com os 10 sugeridos

---

## RESUMO DO PROJETO

Ativado quando: usuário perguntar o que foi feito, status, histórico

- Leia MEMORY completo
- Liste: roteiros gerados, Salmos usados, temas descartados, próximos sugeridos
- Mostre o que ainda falta produzir manualmente

---

## FEEDBACK NEGATIVO

Ativado quando: usuário disser que não gostou, descartar algo, reclamar

- Registre imediatamente em MEMORY seção Descartados com motivo
- Nunca repita aquilo em nenhum ciclo futuro

---

## RELATÓRIO FINAL obrigatório após qualquer ciclo

Sempre exiba ao final:

O que foi gerado: [lista de arquivos criados]
Salmos usados neste ciclo: [lista]
Tendência identificada no pré-ciclo: [achado]
Próximos 3 temas sugeridos: [lista]

Seus próximos passos manuais:
1. Gemini → colar prompts de imagem de shorts\scripts\
2. ElevenLabs → colar roteiro e gerar .mp3
3. CapCut → imagem + áudio + legenda automática → exportar 9:16
4. YouTube Studio → colar SEO de seo\ → postar nos horários: 5h, 18h ou 0h

---

## O que o agent team NUNCA FAZ
- Chamar API do ElevenLabs ou gerar áudio automaticamente
- Fazer upload no YouTube automaticamente
- Montar vídeo automaticamente
- Baixar arquivos de plataformas externas automaticamente
