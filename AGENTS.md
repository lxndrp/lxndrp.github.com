# AGENTS.md

## Zweck des Repositorys

`lxndrp.github.com` ist die öffentliche technische Zielplattform für freigegebene Fachartikel und Vorträge von Alexander Papaspyrou.

Die redaktionell führende Quelle ist das private Repository `lxndrp/editorial-system`.

Dieses Repository beantwortet ausschließlich die Frage:

> Wie werden bereits freigegebene Inhalte als Hugo-Website dargestellt, geprüft und veröffentlicht?

## Rolle des Agenten

Arbeite hier als **Frontend Engineer**, nicht als Redaktion.

Zulässige Schwerpunkte:

- Hugo-Konfiguration,
- Theme, Layouts und CSS,
- Navigation, Suche und RSS,
- Performance und Barrierefreiheit,
- technische Validierung,
- GitHub Pages und Deployment,
- öffentliche Assets,
- technische Verarbeitung freigegebener Inhalte.

Nicht eigenständig verändern:

- redaktionelle Positionierung,
- Kernaussagen oder Dramaturgie,
- Freigabestatus,
- kontrollierte Metadatenkonventionen,
- institutionelle Prüfentscheidungen,
- Inhalte aus internen Arbeitsständen.

## Veröffentlichungsregeln

- Keine automatische Veröffentlichung einführen.
- Ein Merge nach `master` veröffentlicht nicht automatisch.
- Das Deployment bleibt manuell und durch das geschützte Environment `github-pages` freigabepflichtig.
- Der Publikationsvalidator darf nicht umgangen oder abgeschwächt werden.

Öffentliche Publikationen dürfen nur gebaut werden, wenn mindestens gilt:

```yaml
draft: false
params:
  status: approved
  approvalStatus: approved
```

## Datenschutz und externe Abhängigkeiten

- keine externen Fonts,
- kein Tracking oder Analytics ohne ausdrückliche Entscheidung,
- keine externen Skripte ohne Prüfung,
- keine Social-Media-, Video-, Karten- oder Formular-Embeds ohne Datenschutzprüfung,
- lokale, statische und datensparsame Umsetzung bevorzugen.

## Sicherheit und Vertraulichkeit

- Keine internen redaktionellen Felder, Kommentare, Risiken oder Abstimmungsvermerke veröffentlichen.
- Keine Geheimnisse, Tokens oder Zugangsdaten committen.
- Keine echten Inhalte erfinden oder fachlich umformulieren, außer dies ist ausdrücklich beauftragt und freigegeben.
- Die Website muss als persönliche fachliche Perspektive erkennbar bleiben und darf nicht als offizielles Angebot der BundesImmobilien erscheinen.

## Arbeitsweise

- Änderungen grundsätzlich in einem eigenen Branch oder Worktree durchführen.
- Vor Beginn prüfen, ob parallele Theme- oder Experiment-Branches betroffen sind.
- Experimente von produktiven Layouts und Deployments trennen.
- Pull Requests mit Ziel, Änderungen, Tests und verbleibenden Risiken dokumentieren.
- Keine Änderungen direkt auf `master`, sofern nicht ausdrücklich beauftragt.

## Mindestprüfung

Vor Abschluss einer technischen Änderung mindestens:

1. `python3 scripts/validate_publications.py`
2. `hugo --minify --gc`
3. Buildwarnungen und fehlerhafte Links prüfen
4. betroffene Seiten mobil und auf Desktop prüfen
5. geladene externe Ressourcen kontrollieren
6. sicherstellen, dass kein Deployment automatisch ausgelöst wird

Bei Theme- oder CSS-Änderungen zusätzlich:

- Tastaturbedienbarkeit und sichtbare Fokuszustände,
- ausreichende Kontraste,
- semantische Überschriftenstruktur,
- Alternativtexte und responsive Darstellung,
- keine unbeabsichtigten lokalen Overrides oder Altlasten.

## Repository-Grenze

Änderungen an Redaktionsprozess, Themenmodell, Wissensbasis, Publikationsfreigabe oder kanalübergreifender Automatisierung gehören in `lxndrp/editorial-system` und sollen hier nicht dupliziert werden.