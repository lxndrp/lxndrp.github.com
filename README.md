# Alexander Papaspyrou – Publikationsplattform

Dieses Repository enthält die öffentliche Hugo-Website für freigegebene Fachartikel und Vorträge.

## Lokale Vorschau

Voraussetzung: Hugo Extended.

```bash
hugo server -D
```

## Produktionsbuild

```bash
hugo --minify
```

Die erzeugten Dateien liegen anschließend unter `public/`.

## Veröffentlichungsregel

Öffentliche Inhalte müssen mindestens folgende Metadaten tragen:

```yaml
draft: false
params:
  status: approved
  approvalStatus: approved
```

Interne Felder wie `communicationRisk`, `reviewLevel`, `knowledgeRefs` oder `sourceTopics` werden nicht im Layout ausgegeben.

## Trennung der Systeme

- `lxndrp/editorial-system`: internes Redaktions- und Wissenssystem
- `lxndrp/lxndrp.github.com`: ausschließlich öffentliche, freigegebene Inhalte

Die Domain ist über `CNAME` auf `stage.papaspyrou.name` vorbereitet.

## Phase 4

Enthalten sind Hugo-Konfiguration, Inhaltsbereiche, minimale eigene Layouts, responsive Grundgestaltung und lokale Build-Anleitung. Die automatisierte GitHub-Pages-Pipeline folgt in Phase 5.
