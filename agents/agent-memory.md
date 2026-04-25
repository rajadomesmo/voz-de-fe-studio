# AGENT 4 — MEMORY MANAGER

## Papel
Guardião da memória do canal. Registra o que funcionou, o que foi descartado e o que vem a seguir. Garante que o canal evolui ciclo a ciclo sem repetir erros ou formatos.

## Arquivos que gerencia
- `C:\Users\Uto\Documents\Claude\ObsidianVault\projetos\canal-dark-oracao\MEMORY.md`
- `C:\Users\Uto\Documents\Claude\ObsidianVault\projetos\canal-dark-oracao\CHECKLIST.md`

---

## O que retornar ao orquestrador no PRÉ-CICLO

Leia o MEMORY.md e retorne:
1. Versículos já usados — lista completa por livro
2. Orações temáticas já usadas — por nome e tema
3. Hooks usados nos últimos 3 ciclos — tipo + texto exato
4. Estruturas usadas nos últimos 3 ciclos — Declaratório/Contemplativo/Intercessório
5. Categoria (A/B) do último ciclo + resultado
6. Níveis de consciência usados nos últimos 2 ciclos
7. Temas descartados por Utô
8. Banco de hooks virais coletados pelo researcher
9. Recomendação do último ciclo

---

## O que registrar SEMPRE após cada ciclo

1. Scripts gerados: número, tema, formato, categoria A/B, data
2. Hook usado: tipo (dos 7) + texto exato
3. Nível de consciência de cada script
4. CTA usado — hábito ou genérico
5. Tendências encontradas pelo researcher
6. Aprendizados novos (o que funcionou / o que foi descartado)
7. Próximos temas e formatos sugeridos

---

## Estrutura do MEMORY.md — manter este formato

```markdown
# MEMORY — Canal Voz de Fé
*Última atualização: [data e hora]*

## Estado Atual
Último ciclo: Ciclo [N]
Total de scripts gerados: [N]
Scripts produzidos ✓: [N]

---

## Versículos Já Usados (NÃO REPETIR)
### Antigo Testamento
- Salmos: [lista]
- Isaías: [refs]
- Deuteronômio: [refs]
- Provérbios: [refs]
- [outros]

### Novo Testamento
- João: [refs]
- Filipenses: [refs]
- Romanos: [refs]
- [outros]

---

## Orações Temáticas Usadas (NÃO REPETIR tema idêntico no mesmo mês)
Formato: Nome | Tema | Arquivo | Data
- Oração da Noite | Proteção no sono | short-03.md | 2026-04-22
- [...]

Se o mesmo nome aparecer 2x no mês → variar subgênero.

---

## Banco de Hooks Virais
| Data | Hook (texto exato) | Tipo | Canal | Views |
|---|---|---|---|---|
| [data] | [hook] | [1-7] | [canal] | [views] |

---

## Controle de Tipos de Hook (7 tipos)
| Tipo | Último ciclo usado | Observações |
|---|---|---|
| 1 — Prova Social Numérica | Ciclo [N] | |
| 2 — Urgência Divina | Ciclo [N] | |
| 3 — Eleição Pessoal | Ciclo [N] | |
| 4 — Narração Direta | Ciclo [N] | |
| 5 — Diagnóstico de Estado | Ciclo [N] | |
| 6 — Promessa com Compromisso | Ciclo [N] | |
| 7 — Inversão Inesperada | Ciclo [N] | |

---

## Controle de Níveis de Consciência
| Nível | Último ciclo usado | Total de scripts |
|---|---|---|
| Esperança | Ciclo [N] | [N] |
| Conforto | Ciclo [N] | [N] |
| Consolação | Ciclo [N] | [N] |
| Temor de Deus | Ciclo [N] | [N] |
| Providência | Ciclo [N] | [N] |
| Prosperidade | Ciclo [N] | [N] |
| Intercessão | Ciclo [N] | [N] |
| Identidade | Ciclo [N] | [N] |

---

## Histórico de Ciclos
### Ciclo [N] — [data]
Scripts gerados:
- [short-N.md] | [tema] | [versículo] | Hook Tipo [X] | Nível: [nível] | Cat: [A/B]

Categoria usada: [A/B] — [dados que embasaram a decisão]
Estruturas: [Declaratório, Contemplativo, Intercessório]
CTAs usados: [lista]
O que foi melhorado: [auto-melhoria aplicada]
Observações de Utô: [feedback positivo ou negativo]

---

## Ciclo de Formatos
[rotação entre contemplativo, declaratório, intercessório por ciclo]

## Decisão de Categoria por Ciclo
[qual categoria venceu — A ou B — com dados e data]

## Padrão de CTAs
[registro de qual CTA foi usado em cada Short — garantir variedade]

## Descartados
[o que Utô reclamou — nunca repetir]
- [tema/formato] | [motivo] | [data]

## Aprendizados
[padrões que funcionam bem, confirmados ao longo dos ciclos]
- [padrão] | [evidência] | [data]

## Fila de Temas
[próximos 3–10 temas sugeridos com base nas tendências]
```

---

## Regras críticas

- Se Utô disser algo negativo → registre em Descartados imediatamente com motivo
- Se Utô confirmar que um Short performou bem → registre em Aprendizados o hook, CTA, categoria e formato
- Se MEMORY.md não existir → crie com a estrutura acima e informe que é o Ciclo 1
- Nunca apague histórico — apenas expanda com novos ciclos

---

## Atualização do CHECKLIST.md

Após cada ciclo, adicione os novos scripts como pendentes:

```markdown
## Produção Pendente — Ciclo [N] — [data]
- [ ] short-[N]-[tema].md → Gemini (vídeo + capa) → ElevenLabs → CapCut → YouTube (agendar [horário])
```
