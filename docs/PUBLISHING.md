# Veröffentlichungsprozess

## Grundsatz

Ein Merge nach `master` veröffentlicht die Website nicht automatisch. Das Deployment wird ausschließlich manuell über den Workflow **Publish website** ausgelöst.

## Voraussetzungen für öffentliche Inhalte

Eine Publikation unter `content/articles/`, `content/talks/` oder `content/podcast/` darf nur mit folgenden Werten öffentlich gebaut werden:

```yaml
draft: false

params:
  status: approved
  approvalStatus: approved
```

Der Validierungsschritt `scripts/validate_publications.py` bricht den Build ab, wenn `draft: false` ohne beide Freigabewerte gesetzt ist.

## Prüfung

Pull Requests und Änderungen auf `master` führen automatisch einen Hugo-Build aus. Diese Prüfung veröffentlicht nichts.

## Veröffentlichung

1. Freigegebene Änderungen nach `master` mergen.
2. Unter **Actions** den Workflow **Publish website** öffnen.
3. **Run workflow** auswählen.
4. Als Bestätigung exakt `publish` eingeben.
5. Den erfolgreichen Build und das Deployment in der Umgebung `github-pages` prüfen.

Der Workflow checkt ausdrücklich den aktuellen Stand von `master` aus. Ein anderer Branch kann dadurch nicht versehentlich veröffentlicht werden.

## GitHub-Pages-Einstellung

Im Repository muss unter **Settings → Pages → Build and deployment → Source** die Option **GitHub Actions** ausgewählt sein. Diese Repository-Einstellung wird nicht durch die Workflow-Datei selbst geändert.

## Domain

Hugo übernimmt `static/CNAME` in das Build-Ergebnis. Die veröffentlichte Website verwendet dadurch weiterhin `stage.papaspyrou.name`, sofern der DNS-Eintrag auf GitHub Pages zeigt.

## Rücknahme

Eine fehlerhafte Veröffentlichung wird durch einen korrigierenden Commit oder Revert auf `master` und ein erneutes manuelles Deployment zurückgenommen. GitHub Pages selbst wird nicht als führende Inhaltsquelle behandelt.
