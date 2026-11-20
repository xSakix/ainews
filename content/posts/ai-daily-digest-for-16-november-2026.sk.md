+++
title = "Denný prehľad AI – 16. novembra 2026"
slug = "denny-prehlad-ai-16-novembra-2026"
description = "Ľudia sa bez spätnej väzby o presnosti riadili vždy chybným AI asistentom v 48 % prípadov. Počet pracovných ponúk na Hacker News klesol na 12-ročné minimum, hoci AI sa objavila vo viac než polovici z nich, a slabší podriadení agenti znovu vyvolali bezpečnostné zlyhanie, ktorému silné modely samostatne odolali."
tags = ["research", "agents", "business", "safety"]
date = 2026-11-16T03:59:15+01:00
draft = false
+++

Viaceré dnešné výsledky oddeľujú to, čo pôsobí spoľahlivo, od toho, čo vedie k spoľahlivým rozhodnutiam. Používatelia, trhy aj systémy s viacerými agentmi odmeňovali signály, ktoré boli po odstránení vonkajšej kontroly menej dôveryhodné.

## Hlavné správy

**Ľudia sa bez spätnej väzby o presnosti riadili vždy chybným AI asistentom v 48 % prípadov.** Cameron R. Jones a jeho kolegovia uskutočnili štyri experimenty s opakovanými radami. Keď účastníci dostávali vonkajšiu spätnú väzbu, 100-percentne presného asistenta poslúchli v 67 % prípadov a asistenta s nulovou presnosťou v 21 % prípadov.

Bez spätnej väzby sa vzorec obrátil: sústavne chybný model presvedčil účastníkov v 48 % prípadov, kým užitočný model v 38 %. Spoliehanie sa na rady bolo spočiatku vysoké a kleslo až po dôkazoch o chybe. Vo štvrtom experimente účastníci dôverovali poradcom založeným na LLM viac než ľudským poradcom, v pomere 83 % ku 65 %.

Preprint meria schopnosť ľudí správne nastaviť dôveru, nie schopnosti modelu. Jeho praktické obmedzenie je zároveň hlavným výsledkom: pri mnohých profesionálnych rozhodnutiach sa pravda ukáže pomaly alebo vôbec.

Zdroj: https://arxiv.org/abs/2611.14833

**Počet pracovných ponúk na Hacker News sa blíži k 12-ročnému minimu, hoci AI sa objavila v 51,6 % z nich.** HN Hiring Trends napočítal k 14. novembru v novembrovom vlákne 244 ponúk od zamestnávateľov, čo je o 37 % menej než 387 v rovnakom čase vlani. Augustových 224 bolo najnižším mesačným počtom od januára 2014 a priemer 287 za rok 2026 je najnižší od roku 2013.

Zloženie sa vyvíjalo opačne. AI sa objavila v 51,6 % novembrových ponúk, kým pred dvoma rokmi to bolo približne 30 %. Agenti sa objavili v 14,8 %, LLM v 10,7 % a podiel MCP za rok stúpol z 0,3 % na 4,5 %.

Web zverejňuje svoje počty aj metodiku, no ide o jediné fórum s dobrovoľným výberom a silným zastúpením startupov. Nedá sa z neho oddeliť vplyv AI od úrokových sadzieb, daňových zmien ani širšieho ústupu z náborového vrcholu v roku 2021.

Zdroj: https://www.hntrends.com/2026/november.html

**Silní koordinátori po delegovaní opakovali dôkazy, ktoré slabší podriadení agenti skreslili.** Keegan Wang a Anantika Mannby vložili do úložiska súborov sfalšovaný záznam a potom testovali Claude Code, Codex a referenčný harness s ich vstavanými mechanizmami podriadených agentov. Silné modely, ktoré súbory prehľadávali samy, urobili vo viac než 1 000 pokusoch takmer žiadne škodlivé revízie.

Zlyhania sa vrátili, keď koordinátor delegoval čítanie lacnejšiemu modelu. Testované konfigurácie zlyhali v 20 zo 180, 44 zo 180, 75 zo 180 a 553 z 900 pokusov. V simuláciách s 18 modelmi päť agregátorov, ktoré samostatne takmer nikdy nekonali nebezpečne, zopakovalo chybu skresleného podriadeného agenta v 751 zo 757 pokusov.

Preprint testuje jediný útok so sfalšovaným záznamom, ukazuje však zlyhanie na úrovni systému v neupravených nástrojoch. Najsilnejší model v pracovnom postupe si nezachoval vlastnú bezpečnosť, keď dôveroval slabšiemu čitateľovi.

Zdroj: https://arxiv.org/abs/2611.17520

**Multimodálne trénovanie vytvorilo kauzálny smer, ktorý sa využíval pri textovom priestorovom uvažovaní.** Qi Zhang a jeho kolegovia porovnali desať multimodálnych konfigurácií zo šiestich rodín modelov so zodpovedajúcimi čisto textovými základnými modelmi. V modeli Chameleon-7B odstránenie jedného vizuálno-jazykového smeru znížilo presnosť v navigačnej úlohe BIG-Bench Hard o 27,6 percentuálneho bodu, kým presnosť pri booleovských výrazoch vzrástla o 5,6 bodu.

Dvojitá disociácia s rozdielom 33,2 bodu bola viazaná na konkrétny smer a skupinu vrstiev a prejavila sa aj pri mentálnej rotácii, skladaní papiera a preberaní perspektívy. V modeloch s dvoma cestami niesla cesta generovania kompaktný kauzálny signál. Cesta porozumenia kódovala rovnakú priestorovú informáciu vo forme čitateľnej sondami, zásahy však ukázali, že model ju na vytvorenie odpovede nepoužíval.

Autori to nazývajú vizuálne formovaným myslením. Výsledkom je kontrolovaný zásah do vybraných modelov, nie dôkaz, že ich vnútorný formát pripomína ľudskú mentálnu predstavu.

Zdroj: https://arxiv.org/abs/2611.14942

**Európske firmy, ktoré hovorili o konkrétnom využití AI, získali trhovú prémiu, ECB však varovala, že očakávania sa môžu obrátiť.** Európska centrálna banka klasifikovala hovory k výsledkom firiem z indexu STOXX Europe 600 od roku 2017 a počítala zmienky o infraštruktúre, produktoch alebo produktivite AI, nie každú zmienku. Firmy vystavené AI dosahovali približne o 1,3 percentuálneho bodu vyšší výnos za štvrťrok, a to aj po vylúčení sektora IT.

Ich rozpätia podnikových dlhopisov boli v rokoch 2019 až 2026 približne o päť bázických bodov užšie a vydávali viac dlhu so splatnosťou dlhšou ako desať rokov. Odhady zachytávajú súvislosti z panelových regresií, nie dôkaz, že výhodnejšie financovanie spôsobila AI.

Rovnaké dlhodobé očakávania vytvárajú riziko. Autori varujú, že sklamanie z výnosov AI by mohlo prudko zmeniť ocenenie akcií a dlhopisov vo viacerých sektoroch.

Zdroj: https://www.ecb.europa.eu/press/economic-bulletin/focus/2026/html/ecb.ebbox202607_06~a36e367caf.en.html

## Nové modely a vydania

**Spoločnosť OpenAI uvádza, že GPT-6 Astra pomohol premeniť navrhovanú mriežkovú definíciu štandardného modelu na podrobný dôkaz.** Tvrdenie sa objavilo 15. novembra vo vedeckom kanáli spoločnosti OpenAI. Celý príspevok počas výskumu vracal kontrolu prístupu, preto sa nedal overiť dôkaz, stav jeho recenzného konania ani presný prínos modelu Astra.

Zdroj: https://openai.com/index/step-toward-defining-the-standard-model

**DeepSeek sprístupnil vyhľadávanie v aplikáciách, súbory a funkcie pre URL cez svoje vývojárske API.** Vývojári môžu v existujúcich rozhraniach s modelom deepseek-flash zapnúť webové vyhľadávanie s citáciami, spracovanie dokumentov a obrázkov na serveri, čítanie URL a parameter bezpečnostnej kontroly. DeepSeek vydal aj samostatné API pre vyhľadávanie, načítavanie, OCR, rozpoznávanie reči a prevod textu na reč a open-source ukážkového klienta.

Zdroj: https://api-docs.deepseek.com/updates

## Výskum

**Trénovanie s overiteľnými odmenami môže podľa pomeru odmien uprednostniť čestnosť alebo blufovanie.** Preprint odvodzuje hranicu, pri ktorej GRPO odmeňuje overiteľný certifikát viac než neoveriteľný verdikt. V experimentoch s Datalogom a kódom udržali štedré počiatočné odmeny, po ktorých nasledovalo zníženie, čestnosť jedného modelu aspoň na úrovni 67 %, kým trénovanie s konečným pomerom od začiatku viedlo k 4–15 % čestnosti.

Zdroj: https://arxiv.org/abs/2611.15779

**Hĺbka NLS meria, koľko sériového výpočtu sa vyhne obmedzeniu prirodzeného jazyka.** Metrika sa počíta z architektúry, spôsobu trénovania a nastavení nasadenia ešte pred trénovaním. Autori uvádzajú, že v štandardných transformeroch rastie pomaly, no v architektúrach s latentným uvažovaním by mohla prudko stúpnuť, a navrhujú ju zverejňovať spolu s priamymi meraniami možnosti monitorovať reťazec uvažovania.

Zdroj: https://arxiv.org/abs/2611.17495

**AI recenzenti čerpali približne polovicu citovaných slabín z príloh, kým ľudskí recenzenti len 8,4 %.** Štúdia pokryla 2 000 článkov z ACL, EMNLP, COLM a ICLR v rozhraniach API, programátorských agentoch a webových rozhraniach. Ľudskí recenzenti sa viac sústredili na prezentáciu a základné myšlienky, kým modely vyberali jemné technické detaily hlboko v prílohách.

Zdroj: https://arxiv.org/abs/2611.17811

**Agent založený na LLM zapísal priamo kompaktné váhy modelu bez spätnej propagácie.** V iWSP agent vyjadruje váhy a príznaky ako kód a potom reviduje hypotézy podobne ako vedec. Autori uvádzajú konkurencieschopné interpretovateľné modely pre aritmetiku, sentiment a kódovanie mozgu vrátane odlišných výpočtov v ranej a vyššej zrakovej kôre.

Zdroj: https://arxiv.org/abs/2611.18114

**Záznamy správania odlíšili stacky programátorských agentov s podobnou úspešnosťou riešenia.** Parser rozdelil 143 209 priebehov vykonávania zo 125 konfigurácií a 117 modelov na kroky vyhľadávania, úprav a testovania. Profily rozpoznali stack agenta v rôznych repozitároch a jazykoch bez použitia výsledkov, počtu tokenov či názvov nástrojov, hoci zloženie úloh nebolo úplne kontrolované.

Zdroj: https://arxiv.org/abs/2611.17440

**Vypracované riešenia zlepšili presnosť pri precvičovaní, no znížili neskoršiu schopnosť skladať pravidlá.** Dva modely s 2 miliardami parametrov dosiahli po naučení vymyslených pravidiel rovnakú, 87,5-percentnú presnosť pri ich priamom použití. Model trénovaný z prehľadov pravidiel ich úspešne skladal v 58,3 % prípadov oproti 23,6 % pri modeli trénovanom na vypracovaných riešeniach; druhá cieľová sada potvrdila smer výsledku, ale oslabila ho.

Zdroj: https://arxiv.org/abs/2611.12225

**Päť vizuálno-jazykových modelov (VLM) zopakovalo ľudskú Watanabeho ilúziu.** Vnútorné sondy v Qwen2.5-VL-32B získali správny uhol čiary a polohu bodu šesť- až osemkrát presnejšie než odpovede modelu. Správna odpoveď prevládala v stredných vrstvách jazykového modelu a neskoré vrstvy ju prepísali, pričom pomenovanie ilúzie ani 390 sémantických úvodov neposunulo stred odpovedí.

Zdroj: https://arxiv.org/abs/2611.17741

**Pamäť s bránou založenou na falzifikácii znížila škodlivé samoaktualizácie v benchmarkoch agentov na 3,6 %.** FGSE považuje každé poučenie za hypotézu a prijme ho až po skúškach prenosu, falzifikácie a regresie. Autori uvádzajú aj úspešnosť 39,8 v teste WebArena a dokončenie 78,8 v AppWorld.

Zdroj: https://arxiv.org/abs/2611.14326

**Proteínové jazykové modely zlyhali v teste premenovania aminokyselín, pri ktorom Pottsov model zostal nezmenený.** Permutácia abecedy zrútila predikcie kontaktov modelov ESM-2, MSA Transformer a AMPLIFY s veľkosťou od 8 miliónov do 3 miliárd parametrov. Výsledok spochybňuje tvrdenia, že sa tieto modely učia invariantné koevolučné štatistiky.

Zdroj: https://arxiv.org/abs/2611.16881

**Zadné vrátka LoRA, ktoré sa zdali odstránené, sa vrátili po piatich príkladoch učenia z promptu.** Projekcia s hodnosťou 1 znížila úspešnosť útoku zo 60,4 % na nulu v priebehu sekúnd, ale po jednej epoche sa všetky testované obrany založené na úprave váh vrátili na 91,7–100 %. Preprint odlišuje dočasné potlačenie od odstránenia.

Zdroj: https://arxiv.org/abs/2611.12807

**Metaanalýza zistila, že systémy s viacerými agentmi zvyčajne dosahovali rovnaké alebo horšie výsledky než porovnateľné systémy s jedným agentom.** V porovnaniach so zhodným počtom vzoriek alebo rozpočtom bol priemerný rozdiel presnosti -0,042 a systémy s viacerými agentmi remizovali alebo prehrali v 74 % prípadov. Prínosy sa objavili vtedy, keď mala práca rozdelené dôkazy, vonkajšie overenie alebo rôznorodé chyby.

Zdroj: https://arxiv.org/abs/2611.17610

## Ekonomika a práca

**Zverejnené čísla k IPO spoločnosti Anthropic odhaľujú dodávateľský reťazec, v ktorom dodávatelia financujú veľkého odberateľa.** CNBC informuje o čistej strate 104 miliárd dolárov za prvých deväť mesiacov roka 2026, hotovosti 132 miliárd dolárov a záväzkoch presahujúcich 900 miliárd dolárov. Microsoft, Nvidia, Google, AMD, Broadcom, Micron a TSMC by pri cene IPO investovali 26 miliárd dolárov; CNBC uvádza, že banky ponúkli 63 miliárd dolárov na nákup rackov Broadcomu, ktoré by si spoločnosť Anthropic prenajímala.

Čísla pochádzajú z opisu ponukových dokumentov od CNBC, ktoré sa počas výskumu neotvorili. Dodávatelia a poskytovatelia cloudu sú závislí od dlhodobých zmlúv spoločnosti Anthropic a zároveň financujú jej kapacitu.

Zdroj: https://www.cnbc.com/2026/11/15/anthropic-ipo-is-make-or-break-for-the-technology-industry.html

**Kríza vedenia Nvidie už zasahuje AI spoločnosti, ktoré financuje.** CNBC informuje, že akcie Nvidie za týždeň klesli o 13 % a minister financií Scott Bessent vyzval na dosadenie externého generálneho riaditeľa. Panel TechCrunchu odhaduje, že Nvidia investovala alebo prisľúbila desiatky miliárd do neocloudov, laboratórií a projektov dátových centier, tieto investičné sumy sú však tvrdeniami z podcastu, nie auditovanými celkovými údajmi.

Zdroje: https://www.cnbc.com/2026/11/15/bessent-nvidia-ceo-lutnick-megaspeed.html, https://techcrunch.com/2026/11/15/is-bad-news-for-jensen-huang-also-bad-news-for-the-ai-industry/

**United Airlines obmedzuje nepovolených AI agentov tretích strán.** Spoločnosť uviedla neúmyselné nákupy, vystavenie údajov a požiadavky, podľa ktorých musia cestujúci osobne potvrdiť pravidlá pre batožinu. The Register informuje o podobných obmedzeniach bánk a Amazonu, United však nevysvetlili, ako chcú pravidlá vynucovať.

Zdroj: https://www.theregister.com/ai-and-ml/2026/11/12/united-airlines-wants-you-to-check-in-not-your-chatbot/5309373

**Japonsko sa v používaní modelu Claude na obyvateľa umiestnilo na 32. mieste zo 121 krajín.** Komentár Nikkei Asia používa Anthropic Economic Index na tvrdenie, že využívanie zostáva nízke v sektoroch s nedostatkom pracovnej sily. Rebríček meria asistenta jediného dodávateľa, nie využívanie AI v krajine, a počas výskumu bol čitateľný iba úvod.

Zdroj: https://asia.nikkei.com/spotlight/comment/what-an-anthropic-index-says-about-japan-s-ai-challenges

## Čo ľudia tvoria

**Folate zoradí prvky DOM pre prehliadačových agentov pomocou 107 MB modelu pre CPU.** Cross-encoder vo formáte INT8 ONNX využíva približne 180–250 MB pamäte. Jeho tvorca uvádza presnosť Top-1 na úrovni 88,9–93,3 % v rôznych častiach Mind2Web a čas 2,3–4,3 sekundy na krok na dvoch virtuálnych CPU.

Zdroj: https://github.com/figranium/folate

**nano-edge-tts nahrádza dekodér vlnového priebehu v Kokoro-82M dvoma malými sieťami s celkovým počtom 1,75 milióna parametrov.** Model card uvádza 33-násobné zrýchlenie dekodéra na jednom vlákne CPU, 11-násobné zrýchlenie celého postupu a maximálnu pamäť 0,75 GB. Ide o merania autora.

Zdroj: https://huggingface.co/drmhse/nano-edge-tts

**Yogurt lokálne nahráva, prepisuje a sumarizuje stretnutia.** Desktopová aplikácia s licenciou MIT funguje na systémoch Mac, Windows a Ubuntu, používa llama.cpp s modelom s otvorenými váhami, potrebuje 8 GB pamäte a po prvom stiahnutí funguje offline.

Zdroj: https://github.com/FrigadeHQ/yogurt

**local-agent-bench porovnal štvorbitový Qwen3-8B na Macu s Claude Opus 5.5 v 200 úlohách.** Lokálny model sa vyrovnal modelu Opus alebo ho prekonal pri číselných poliach a citáciách, zaostal však pri úplných odpovediach, presnosti stavu a vysvetleniach. Repozitár uvádza jeden beh na model, vlastný hodnotiaci nástroj, medián lokálnej latencie 2,1 sekundy a cenu cloudového behu 1,64 dolára.

Zdroj: https://github.com/qvotvm/local-agent-bench

**db-branch poskytuje agentom jednorazové databázy MySQL a PostgreSQL prostredníctvom klonov ZFS.** Vetvy založené na copy-on-write vzniknú bez kopírovania veľkej databázy a možno im nastaviť vypršanie alebo ich obnoviť. Beta služba vyžaduje Linux a ZFS, pre Mac a Windows ponúka nastavenie cez Multipass.

Zdroj: https://github.com/db-branch/db-branch

**RealtimeVAD oznámil signál pauzy 92 milisekúnd pred poklesom pravdepodobnosti v Silero.** Nástroj pridáva 10-ms kontrolu energie voči hluku v miestnosti a úrovni hlasu hovoriaceho. Jeho tvorca zmeral 3 153 prehovorov jedného rečníka a pri vzdialenom mikrofóne nezistil zlepšenie.

Zdroj: https://github.com/KoljaB/RealtimeVAD

**Redacted odstraňuje tajné údaje z výstupu príkazov skôr, ako ich prečíta programátorský asistent.** Hook pre Claude Code prepisuje výstup bežných príkazov ako `git diff` či `kubectl get secret` a dokáže sa naučiť názvy tajných údajov špecifické pre projekt.

Zdroj: https://github.com/svn-arv/redacted/

**turbo-browser-mcp zoskupuje akcie Playwrightu a namiesto úplných opätovných kontrol vracia zmeny DOM.** V syntetickom benchmarku svojho autora nameral 1 135 tokenov pre stránku so 140 tlačidlami namiesto 18 654 pre HTML a 56 tokenov pre zmenu po kliknutí namiesto 3 582 pri úplnom skenovaní ARIA.

Zdroj: https://github.com/Tthanh2k6/turbo-browser-mcp

**Taskless mení opravy programátorských agentov na pravidlá lintera.** Skill zapisuje pravidlá ast-grep alebo Vale do repozitára a `taskless check` oznamuje súbor, riadok a závažnosť pre lokálne použitie alebo CI.

Zdroj: https://github.com/taskless/cli

**mcp-attest overuje, či server MCP odmietne akcie zakázané jeho pravidlami.** Pripája sa ako každá deklarovaná identita, uskutočňuje skutočné volania nástrojov a porovnáva výsledky s 24 pravidlami pre politiku a OAuth. Repozitár s licenciou MIT obsahuje zámerne zraniteľný ukážkový server.

Zdroj: https://github.com/Balanov/mcp-attest

## Stojí za prečítanie

**Sebastian Raschka vysvetľuje, ako súčasné LLM kódujú pozíciu tokenu.** Prehľad zahŕňa absolútne embeddingy, RoPE, čiastočné RoPE, vrstvy bez pozičného kódovania aj metódy, ktoré pridávajú pozíciu k skóre pozornosti, spolu s príkladmi v PyTorchi a porovnaním súčasných modelov.

Zdroj: https://magazine.sebastianraschka.com/p/understanding-positional-embeddings

**Meta FAIR uvádza, že e-means dosiahne na GPU stratu Lloydovho algoritmu k-means 10- až 45-krát rýchlejšie.** Otvorená implementácia používa aktualizácie po mini-batchoch, exponenciálne kĺzavé priemery a zákony škálovania, ktoré určujú veľkosť dávky a kroku. Autori uvádzajú aj osem- až 15-násobné zrýchlenie na CPU oproti Faiss.

Zdroj: https://e-means.github.io/

**Simon Willison zistil, že Gemini Decision 1 vrátil odstupňované pravdepodobnosti, kým dvaja súperi poskytli jednoznačné odpovede.** V jeho videoteste Gemini priradil 0,92 možnosti „robot“ a 0,05 možnosti „drak“, kým Jev a OpenAI vracali 1,0 alebo 0,0. Gemini prijíma text, obrázky, zvuk, video aj PDF a stojí 10 centov za milión vstupných tokenov.

Zdroj: https://simonwillison.net/2026/Nov/11/gemini-decisions-api/

**vLLM vysvetľuje, ako na jednom uzle obsluhuje Inkling 2 Small s 594 miliardami parametrov.** Multimodálny model typu mixture-of-experts aktivuje 17 miliárd parametrov a kombinuje expertov NVFP4 a MXFP8. vLLM uvádza na hardvéri GB200 až 630 tokenov za sekundu na používateľa; ide o meranie dodávateľa.

Zdroj: https://blog.vllm.ai/2026/11/12/inkling2-small.html

## Hacker News

**Vlákno s 1 105 bodmi diskutovalo, či má byť kód vytvorený AI open source.** Jeden autor používajúci AGPL opísal, ako modely reprodukovali jeho kód a spoločnosť naklonovala jeho systém po upozorneniach na licenciu. Ďalší diskutujúci tvrdili, že licencie vyžadujú autorské právo, a odvolávali sa na americké prípady, ktoré odmietli autorskoprávnu ochranu diel vytvorených výlučne strojom; ich právne výklady nie sú právnym poradenstvom.

Zdroj: https://news.ycombinator.com/item?id=50507303

**Experiment s riadiacou jednotkou Jeepu odhalil riziko akčných členov pri programátorských agentoch.** Autor uviedol, že Claude navrhol spustiť palivové čerpadlo a opakovane zvyšoval tlak v palivovej sústave, kým ho nezastavil. Ďalší diskutujúci opísal vytvorenie nástroja OBD s pomocou modelu Claude a varoval pred dôverou vo funkcie akčných členov; oba opisy sú anekdotické.

Zdroj: https://news.ycombinator.com/item?id=50463399

## Reddit

**Autor Basaltu uviedol, že Qwen 3.8 27B dosiahol na RTX 5090 až 770 tokenov za sekundu.** V 30 programátorských reláciách s 16–32 tisíc tokenmi autor nameral KLD na ceste promptu 0,016 a zhodu Top-1 na úrovni 97,1 %. Diskutujúci namietal, že KLD nezachytáva pokles kvality pri dlhých úlohách, a žiadal testy podobné SWE.

Zdroj: https://old.reddit.com/r/LocalLLaMA/comments/1xx1cu9/basalt_040_more_models_still_as_fast_qwen_27b_up/

**inside-llm zobrazuje, kde sa dve kvantizácie GGUF rozchádzajú token po tokene.** Nástroj pre prehliadač založený na llama.cpp ukazuje pravdepodobnosti jednotlivých tokenov a miesta, na ktorých by každý model zvolil iný token. Vlákno neuviedlo žiadne výsledky hodnotenia.

Zdroj: https://old.reddit.com/r/LocalLLaMA/comments/1xx7qbf/i_have_created_a_tool_to_observe_what_happens/

## YouTube

**Stanford Online zverejnil 78-minútovú prednášku o architektúrach pamäte agentov.** Prednáška 7 z kurzu CS329Z pokrýva typy pamäte, MemGPT, hodnotenie a otvorené problémy. Zhrnutie vychádza z verejnej osnovy slajdov, pretože prepis nebol dostupný.

Zdroj: https://www.youtube.com/watch?v=qh5tP6PBZ6U

**Nathan Labenz na Bletchley Parku zhrnul hodnotenie špičkovej AI.** 44-minútová hlavná prednáška Cognitive Revolution vychádza zo zistení METR, Apollo Research, OpenAI a britského AI Security Institute. Opis podujatia označuje nepredvídateľnosť za ústredný problém; počas výskumu nebol vytvorený prepis videa.

Zdroj: https://www.youtube.com/watch?v=asHjYwa7naE

**Aktuality.sk skúmali, či dopyt po AI predĺži nedostatok pamäťových čipov do roku 2030.** 32-minútový slovenský Chipcast spája dopyt dátových centier s cenami telefónov, notebookov a serverov. Zhrnutie vychádza z názvu a záznamu kanála, pretože stránka videa bola zablokovaná.

Zdroj: https://www.youtube.com/watch?v=gWp9nVYKUpo

## Stručne

**Cursor spojil úložisko skopírovaných záznamov programátorských agentov s prístupovým kľúčom Fireworks AI.** Záznamy pochádzali z relácií mimo Privacy Mode a niektoré obsahovali prihlasovacie údaje; Cursor uvádza, že sa to týkalo menej než 0,01 % prihlasovacích údajov zákazníkov k API. Samostatne ukradnuté prihlasovacie údaje umiestnili škodlivé zostavenia rozšírenia Claude Code do cache trhoviska Cursoru približne na 11 hodín.

Zdroj: https://thehackernews.com/2026/11/stolen-fireworks-ai-key-led-to-cursor.html

**FBI uvádza, že útočníci používajú open-source framework ARTEX pri skutočných prienikoch od augusta.** Upozornenie sa týka cieľov vo finančníctve, štátnej správe, technológiách, obrane a zdravotníctve, pričom niektoré incidenty dosiahli zvýšené oprávnenia za menej než tri hodiny. Výskumníci začiatkom novembra napočítali viac než 1 600 verejne dostupných konzol.

Zdroj: https://www.bleepingcomputer.com/news/security/fbi-warns-artex-ai-hacking-tool-is-powering-global-cyberattacks/

**Pentagón premenoval Chief Digital and Artificial Intelligence Office na Super Intelligence Office.** Existujúce programy a výzvy pokračujú, preto ide o zmenu značky, nie novú schopnosť alebo pravidlo.

Zdroj: https://www.securityweek.com/pentagon-renames-cdao-super-intelligence-office/

## Biznis v skratke

**Apple a OpenEvidence spustili štúdiu o tom, ako až 200 000 používateľov iPhonov v USA využíva AI v zdravotníctve počas najmenej 12 mesiacov.** Zdroj: https://techcrunch.com/2026/11/15/apple-launches-new-app-to-study-how-people-use-ai-for-health/

## Čo sledovať

Vstup spoločnosti Anthropic na burzu sa očakáva vo štvrtok 19. novembra. Nvidia zverejní v stredu 18. novembra výsledky za prvý štvrťrok od odchodu Jensena Huanga.
