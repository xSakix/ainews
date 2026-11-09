+++
title = "Codebases van studenten verdrievoudigden, het commentaar niet"
slug = "codebases-studenten-verdrievoudigden-commentaar-niet"
description = "Een onderzoek over tien semesters naar 260 repositories van afstudeerteams vindt dat de code aan het einde van het semester groeide van ongeveer 3,4 naar ongeveer 10 duizend regels toen generatieve AI breed beschikbaar was, terwijl de commentaardichtheid gelijk bleef. De auteurs observeerden nooit AI-gebruik, dus het resultaat is een waarschuwing voor beoordelaars en werkgevers, geen oordeel over de tools."
tags = ["research", "tools"]
date = 2026-11-09T03:16:01+01:00
draft = false
+++

Een cursuscoördinator zit op de vrijdag voordat de cijfers moeten worden ingeleverd achter haar bureau. Ze heeft een spreadsheet met ruim veertig studententeams en een gewoonte die ze al jaren volgt: de repository openen, bekijken hoeveel er is gebouwd en hoe regelmatig, en daarop haar indruk baseren van wie heeft gewerkt. Dit jaar bevat de eerste repository op haar lijst tienduizend regels code en driehonderd commits. Ze scrolt door een functie met diep geneste vertakkingen en vindt geen commentaar dat er ook maar één uitlegt. De coördinator is verzonnen en staat voor een probleem dat drie onderzoekers nu hebben gemeten.

De studie, *Code, Commits, and Complexity in the GenAI Era*, werd op 5 november op arXiv geplaatst en geaccepteerd voor het SIGCSE Technical Symposium in februari 2027. De auteurs zijn Asma Shakil en Paul Denny van de University of Auckland en Claus Brabrand van de IT University of Copenhagen. Ze analyseerden 260 teamrepositories uit een verplichte afstudeercursus in het laatste studiejaar, verspreid over tien semesters van 2021 tot 2025. Codebases aan het einde van het semester groeiden van een mediaan van ongeveer 3,4 duizend regels in 2021 tot en met 2023 naar ongeveer 10 duizend in 2024 en 2025. De auteurs observeerden niemand die AI gebruikte en benadrukken dat herhaaldelijk.

## Eén cursus, tien semesters

In de cursus bouwen teams van vijf of zes studenten in dertien weken software voor echte externe klanten. Het werkende prototype is het belangrijkste beoordelingsobject. De repositories komen uit de GitHub-organisatie van de cursus: aanvankelijk 302, en 260 nadat de auteurs lege exemplaren, sjablonen en duplicaten hadden verwijderd. De cohorten bevatten voor 2021 tot en met 2025 respectievelijk 19, 65, 57, 51 en 68 repositories.

De auteurs meten elke repository tweemaal: bij de demonstratie halverwege het semester in week 7 en bij de eindpresentatie in week 13. Ze tellen coderegels met tokei, meten de gemiddelde cyclomatische complexiteit per functie met lizard en maken een lexicale telling van constructies voor foutafhandeling. Ze tellen ook commits. Voor elke maatstaf testen ze of die over de vijf cohorten geleidelijk stijgt of daalt, met correctie voor het aantal geteste maatstaven.

Ze verdelen de jaren in een periode met lagere en een periode met hogere beschikbaarheid van generatieve AI, met de release van ChatGPT in november 2022 als benaderende grens. Ze benadrukken dat die niet scherp is. GitHub Copilot werd in juni 2022 gratis voor geverifieerde studenten en de verspreiding daarna verliep geleidelijk. Ze verwijzen naar een enquête van het Higher Education Policy Institute waarin het aandeel Britse bachelorstudenten dat generatieve AI gebruikte voor beoordeeld werk steeg van 53 procent eind 2023 naar 88 procent eind 2024.

## Wat veranderde, en wanneer

De mediane uiteindelijke codebase telde 2,3 duizend regels in 2021, 3,7 in 2022 en 3,4 in 2023. Daarna sprong die naar 7,7 in 2024 en 11 in 2025. De momentopname halverwege het semester volgt hetzelfde patroon: van 1,4 tot 1,8 duizend regels vóór 2024 naar 4,8 duizend in 2025. Het cohort van 2023, het eerste na ChatGPT, lijkt op de eerdere cohorten en wordt door de auteurs als een overgangscohort beschreven.

Het mediane aantal commits per repository ging van 63 in 2021 en ongeveer 100 tot 112 in 2022 en 2023 naar 265 in 2024 en 300 in 2025. Het aantal commits per actieve dag steeg van 3,3 naar 5,4. De grootte van elke commit veranderde nauwelijks: de mediaan bleef tussen 38 en 65 gewijzigde regels. Dat staat haaks op de gangbare verwachting dat door AI geschreven code in enkele grote partijen wordt toegevoegd. Deze studenten legden vaker wijzigingen vast, in stukken die ongeveer even groot waren als voorheen.

Het scherpste resultaat betreft wat er in de code staat. De gemiddelde cyclomatische complexiteit steeg van 1,7 in 2021 naar 2,5 in 2025, en constructies voor foutafhandeling per duizend regels namen toe van 3,7 en 4,8 in 2022 en 2023 naar 12 en 13 in 2024 en 2025. De commentaardichtheid, het aandeel regels dat uit commentaar bestaat, vertoonde geen duidelijke trend; die was 9,2 procent in 2021 en 8,4 procent in 2025. De auteurs noemen dit patroon “complexiteit zonder commentaar”. Latere cohorten leverden grotere en ingewikkeldere code in die niet beter werd uitgelegd.

## Wat de auteurs niet beweren

Shakil, Brabrand en Denny benoemen de beperkingen duidelijk. Ze observeerden geen AI-gebruik en rapporteren daarom veranderingen die samenvallen met een grotere beschikbaarheid, geen effecten. Docenten, beoordelingscriteria en projecttypen veranderden in de loop der jaren, het cohort van 2021 en een deel van dat van 2022 werkte deels onder COVID-19-beperkingen, en het cohort van 2021 telt slechts 19 repositories. Frameworks en projectsjablonen kunnen op zichzelf standaardcode toevoegen. De talenmix verschoof naar JavaScript en TypeScript, die de belangrijkste taal waren in 42 tot 58 procent van de repositories in 2021 tot en met 2023 en in 71 tot 74 procent in 2024 en 2025; ook beperkt tot de 157 repositories in die talen blijven alle vijf significante trends overeind.

De maatstaven zijn benaderingen. De telling van foutafhandeling is lexicaal en cyclomatische complexiteit “hangt slechts zwak samen met hoe moeilijk code te begrijpen is”, schrijven de auteurs. Omdat die uit een andere tool komt dan de commentaartelling, vragen ze de bevinding van complexiteit zonder commentaar op cohortniveau te lezen. Alles komt uit één cursus aan één instelling.

## Hoe dit past bij ander bewijs

De studie bouwt voort op eerder werk. Y. Zhang en collega's volgden in een preprint uit januari 2026 een ongewijzigde cloudcomputingopdracht gedurende vijf semesters vóór ChatGPT en vijf erna. Eindinzendingen werden langer, wijzigingen tussen inzendingen namen toe en de scoreverbetering per wijziging nam af. Het team uit Auckland vindt bij een langer teamproject een vergelijkbare groei in omvang, maar niet hetzelfde patroon in commitgrootte.

Twee andere studies plaatsen de mogelijke betekenis van die groei in perspectief. S. Peng en collega's vonden in een gecontroleerd experiment uit 2023 dat ontwikkelaars met GitHub Copilot een HTTP-servertaak 55,8 procent sneller voltooiden. Een gerandomiseerde studie uit 2026 van J. H. Shen en A. Tamkin vond dat ontwikkelaars die met AI-hulp een nieuwe bibliotheek voor asynchroon programmeren leerden, slechter presteerden op conceptueel begrip, code lezen en debuggen, zonder significante gemiddelde snelheidswinst. De auteurs uit Auckland halen dat resultaat aan om hun zorg aan te scherpen: ze schrijven dat de extra code mogelijk moeilijker te inspecteren is en dat sterk leunen op AI de vaardigheden kan aantasten die nodig zijn om die code te beoordelen.

Voor docenten gaat de praktische conclusie over meten. Codeomvang en aantallen commits, die een docent vroeger mogelijk als inspanning interpreteerde, zijn sterk gestegen. Een grotere codebase met vaker vastgelegde wijzigingen is geen bewijs meer dat er meer is geleerd. De auteurs stellen mondelinge verdedigingen, gezamenlijke codebesprekingen en expliciete documentatie-eisen voor. Werkgevers die repositories van afgestudeerden als portfolio bekijken, staan voor hetzelfde probleem.

De coördinator zit een week later opnieuw met één team in een kamer. Ze opent de repository niet. Ze vraagt een student een willekeurige functie te kiezen en uit te leggen waarom die op die manier vertakt. De verzonnen student leest langzaam en geeft dan toe dat ze de functie niet eerder heeft gezien. Of de code nu uit een tool, van een teamgenoot of uit haar eigen nachtwerk kwam, het gesprek vertelt de coördinator wat het aantal regels niet kon vertellen.

## Referenties

- Azeem, S., Naveed, M. S., Sajid, M., & Ali, I. (2025). *AI vs. human programmers: complexity and performance in code generation*. VAWKUM Transactions on Computer Sciences, 13(1), 201-216.
- Freeman, J. (2025). *Student generative AI survey 2025*. Higher Education Policy Institute, HEPI Policy Note 61.
- Peng, S., Kalliamvakou, E., Cihon, P., & Demirer, M. (2023). *The Impact of AI on Developer Productivity: Evidence from GitHub Copilot*. https://arxiv.org/abs/2302.06590
- Shakil, A., Brabrand, C., & Denny, P. (2026). *Code, Commits, and Complexity in the GenAI Era: A Longitudinal Study of Team-Based Capstone Projects*. https://arxiv.org/abs/2611.07297
- Shen, J. H., & Tamkin, A. (2026). *How AI Impacts Skill Formation*. https://arxiv.org/abs/2601.20245
- Zhang, Y., Savelka, J., Goldstein, S., & Conway, M. (2026). *Changes in Coding Behavior and Performance Since the Introduction of LLMs*. https://arxiv.org/abs/2601.11835
