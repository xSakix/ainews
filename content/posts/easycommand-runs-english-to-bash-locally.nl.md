+++
title = "EasyCommand zet Engels lokaal om in Bash"
slug = "easycommand-zet-engels-lokaal-om-in-bash"
description = "De open-sourcetool voor de opdrachtregel bevat llama.cpp en levert twee kleine gefinetunede modellen mee. De auteur heeft ook de trainingsset met 401.975 paren en de benchmarkcode vrijgegeven."
tags = ["projects", "models", "tools"]
date = 2026-10-06T04:06:31+02:00
draft = false
+++

EasyCommand zet Engelse verzoeken om in Bash-opdrachten met een klein model dat op een CPU draait. De prompt en de voorgestelde opdracht blijven op de computer van de gebruiker.

Ontwikkelaar Max Trivedi heeft de opdrachtregelapplicatie `ec`, twee modelfamilies en een dataset met 401.975 ontdubbelde paren van verzoeken en opdrachten vrijgegeven. De applicatie bevat llama.cpp, toont de voorgestelde opdracht en kan vóór uitvoering om bevestiging vragen.

Voor een ontwikkelaar die af en toe hulp bij een shellopdracht nodig heeft, neemt lokale uitvoering een API-aanroep weg uit een gevoelig deel van de workflow. Daar staat directe verantwoordelijkheid tegenover: het project waarschuwt dat een aannemelijke opdracht toch fout kan zijn en raadt aan te beginnen in de modus die alleen een voorbeeld toont.

De vrijgegeven modellen bouwen voort op Qwen2.5-Coder-1.5B-Instruct en Qwen3-0.6B. Beide zijn beschikbaar als GGUF-bestanden voor lokale inferentie, samengevoegde BF16-checkpoints en LoRA-adapters voor verdere training. De modellen en dataset gebruiken de Apache 2.0-licentie; de applicatie en benchmarkcode gebruiken MIT.

Trivedi zegt dat het model met 1,5 miljard parameters 212 van de 300 opgaven oploste in een bijgewerkte versie van de ALFA-benchmark voor de omzetting van Engels naar shellopdrachten, tegenover 191 voor het eerdere nl2sh-systeem. Dit is een vergelijking door de auteur met verschillende modelprompts en instellingen, geen resultaat op een onafhankelijke ranglijst.

De release is bijzonder bruikbaar doordat hij behalve het model ook de tekortkomingen bevat. Trivedi zegt dat de vlakke dataset de historische weging uit de training niet reproduceert en geen officiële testverdeling heeft. Hij raadt aan hele taakfamilies apart te houden in plaats van parafrases willekeurig te verdelen; anders zouden vrijwel identieke opdrachten in zowel training als evaluatie terecht kunnen komen.

De tool richt zich op GNU/Linux Bash, niet op alle shells of besturingssystemen. De repository van EasyCommand is nu openbaar, en de auteur vraagt gebruikers tests bij te dragen die onbetrouwbare overdracht en ontbrekende ondersteuning voor opdrachten blootleggen.

## Verificatie {#verification}

| Bewering | Label | Primaire bron | Onafhankelijke verificatie |
| --- | --- | --- | --- |
| EasyCommand draait lokaal, bevat llama.cpp en toont opdrachten vóór uitvoering | GEVERIFIEERD | [Projectbeschrijving](https://dirac.run/posts/easycommand) | [openbare repository](https://github.com/dirac-run/ec) |
| De release bevat 401.975 ontdubbelde Engels/Bash-paren | GEVERIFIEERD | [Projectbeschrijving](https://dirac.run/posts/easycommand) | dataset gekoppeld vanuit de repository |
| De modellen zijn afgeleid van Qwen2.5-Coder-1.5B en Qwen3-0.6B | GEVERIFIEERD | [Projectbeschrijving](https://dirac.run/posts/easycommand) | modelbestanden gekoppeld vanuit de repository |
| Het model met 1,5 miljard parameters scoorde 212/300 tegenover 191/300 voor nl2sh | VOLGENS HET BEDRIJF | [Projectbeschrijving](https://dirac.run/posts/easycommand) | geen; benchmark uitgevoerd door de auteur |
| De modellen en data gebruiken Apache-2.0; de applicatie en benchmarkcode gebruiken MIT | GEVERIFIEERD | [Projectbeschrijving](https://dirac.run/posts/easycommand) | licentiebestanden in de repository |
| De dataset heeft geen officiële testverdeling en behoudt de historische weging niet | VOLGENS HET BEDRIJF | [Projectbeschrijving](https://dirac.run/posts/easycommand) | toelichting van de auteur |
