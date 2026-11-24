+++
title = "27B model pre agentov sa zmestí do 10 GB"
slug = "27b-model-pre-agentov-sa-zmesti-do-10-gb"
description = "Nari Labs zmenšila Qwen3.8-27B z 53,8 GB na 10,12 GB a vo viacerých dlhých benchmarkoch agentov sa vyrovnala verzii BF16. Výsledok závisí od kalibračných dát vytvorených agentmi a špecializovaného forku na inferenciu, čo obmedzuje hardvér, na ktorom možno menšie súbory spustiť."
tags = ["models", "agents", "research", "hardware"]
date = 2026-11-24T04:21:00+01:00
draft = false
+++

Sťahovanie sa skončilo na pracovnej stanici so 16 GB grafickej pamäte. Model s 27 miliardami parametrov, ktorý bežne potreboval 53,8 GB, bol uložený v jedinom súbore s veľkosťou 10,12 GB. Vývojár spustil programátorského agenta a sledoval, ako volá nástroje, číta výsledky a pokračuje namiesto toho, aby zlyhal uprostred práce.

*Úvodná a záverečná scéna tohto článku sú ilustračné; osoby v nich sú vymyslené.*

Nari Labs vydala 20. novembra tri zmenšené verzie modelu Qwen3.8-27B od Alibaby. Trojbitový a 2,5-bitový súbor sa v testoch laboratória pri dlhých programátorských a terminálových úlohách vyrovnali pôvodnému modelu BF16. Dvojbitový súbor nie. Vydanie prináša praktické aj metodické tvrdenie: model môže stratiť takmer štyri pätiny priestoru na váhy bez straty správania potrebného pre agentov, ak sa kompresia učí z práce agentov namiesto bežného textu.

## Nesprávny text pre danú úlohu

Kvantizácia nahrádza čísla s vysokou presnosťou vo váhach modelu menšími reprezentáciami. Menej bitov znižuje pamäťové nároky a prenos dát, takže model určený pre server sa môže zmestiť do pracovnej stanice. Cenou je aproximácia. Každá stlačená váha sa odchyľuje od pôvodnej a chyby sa môžu hromadiť, keď model vytvára dlhú odpoveď alebo prechádza mnohými krokmi.

Väčšinu kalibračných sád tvoria krátke pasáže z webu. Kvantizátor sa z nich učí, ktoré chyby sú dôležité a ako rozložiť obmedzenú množinu číselných hodnôt. Doyeob Kim, jediný autor správy o NariQ, tvrdí, že takéto dáta nereprezentujú prácu programátorského agenta. Agent môže pracovať vo viac než 100 000 tokenoch, striedať uvažovanie a volanie nástrojov a počas mnohých kôl reagovať na výstup terminálu.

Tento nesúlad vidno v doterajších výsledkoch. Podľa Kimovho článku sa predchádzajúce kvantizácie Qwen3.8-27B s troma alebo menej bitmi môžu vyrovnať BF16 pri krátkych matematických úlohách AIME, no v DeepSWE vyriešia nanajvýš 72 % počtu úloh verzie BF16. Model, ktorý si vybaví fakty a dokončí samostatné výpočty, sa môže počas dlhej práce so softvérovým repozitárom odchýliť.

NariQ mení kalibračný materiál. Zaznamenáva tokeny, ktoré plný model BF16 vytvoril počas relácií agentov, a tieto záznamy potom využíva pri výbere stlačených váh. Model vidí rovnaký druh sekvencie, ktorý bude neskôr musieť zvládnuť: plány, požiadavky na nástroje, pozorovania a opravy.

## Mriežky a záznamy

Číselný mechanizmus vychádza z QTIP, metódy Jamesa Tsenga a jeho kolegov z roku 2024. QTIP používa kvantizáciu s mriežkovým kódovaním a transformáciu nekoherentnosti, aby skupinám váh priradil kompaktné kódové slová. Mriežka prehľadáva možné sekvencie namiesto nezávislého zaokrúhľovania každej váhy.

NariQ spája tento mechanizmus s kalibráciou podľa cieľovej činnosti. Rozdiel je dôležitý, pretože kvantizátor môže zachovať priemernú pravdepodobnosť ďalšieho tokenu a pritom poškodiť malú skupinu rozhodnutí, ktoré určujú, či sa agent zotaví po neúspešnom príkaze. Dlhé úlohy tieto rozhodnutia odhaľujú opakovane.

Zverejnené súbory používajú tri, 2,5 a dva bity na váhu. Vizuálny enkóder Qwen3.8-27B a KV cache zostávajú vo formáte BF16. Udávaný počet bitov teda opisuje váhy jazykového modelu, nie každý bajt spotrebovaný pri inferencii. Základom je hustý vizuálno-jazykový model so 64 vrstvami a natívnym kontextovým oknom 262 144 tokenov. Podporuje nastaviteľnú úroveň uvažovania a v predvolenom stave zachováva obsah uvažovania medzi kolami.

Nari Labs porovnala stlačené súbory s 53,8 GB checkpointom BF16. DeepSWE v1.1 obsahuje 113 úloh spustených trikrát. BF16 dosiahol pass@1 na úrovni 39,8, trojbitový súbor 41,0 a 2,5-bitový 41,9. Terminal-Bench 2.1 priniesol 62,6 bodu pre BF16, 63,8 pre tri bity a 60,2 pre 2,5 bitu.

Rovnaký vzorec sa objavil v matematických sadách AIME 2025 a 2026. BF16 dosiahol 97,7, trojbitová verzia 98,3 a 2,5-bitová 96,5 bodu. Vo vizuálnom benchmarku RealWorldQA dosiahli BF16 aj trojbitová verzia 82,4 bodu. Takéto malé rozdiely nedokazujú, že kompresia model zlepšuje. Výsledok agentického benchmarku môže posunúť opakované vzorkovanie. Podporujú však užší záver, že dve väčšie verzie NariQ v týchto testoch merateľne nezaostali.

## Hranica dvoch bitov

Najmenší súbor ukazuje, kde sa tvrdenie končí. Pri dvoch bitoch na váhu klesol DeepSWE na 28,6, Terminal-Bench na 52,4 a AIME na 86,0 bodu. Kompresia prekročila hranicu, pri ktorej už kalibrácia nedokázala obnoviť správanie pôvodného modelu.

Aj benchmarky patria vývojárovi. Nari Labs vybrala model, kalibračné záznamy, implementáciu aj nastavenia hodnotenia. Správa má jedného autora a neprešla recenzným konaním. Nezávislé behy s inými agentmi, repozitármi a hardvérom by ukázali, či sa rovnaký výsledok zopakuje mimo zverejnenej tabuľky.

Medzi malým súborom a dostupným modelom je ešte jedna hranica. NariQ vyžaduje fork llama.cpp od firmy, pretože formát váh a jadrá nie sú v štandardnom projekte. Bežné llama.cpp, Ollama ani LM Studio súbory nenačítajú. Fork je vyladený pre architektúru Nvidia SM120. Nari Labs uvádza, že na kartách Ampere, Ada a Hopper beží pomalšie, GPU od AMD a Intelu nepodporuje a cez Apple Metal zostáva pomalý.

Táto podmienka mení význam slova „lokálny“. Desať gigabajtov dostáva váhy do pamäťového rozpočtu mnohých spotrebiteľských grafických kariet, no softvérová cesta zatiaľ mnohým z nich neslúži dobre. Model card nestlačeného Qwen naopak uvádza zavedené frameworky na prevádzku, napríklad Transformers, vLLM a SGLang. Súbory NariQ vymieňajú širokú kompatibilitu za malú veľkosť.

## Čo súbor meria

Práca navrhuje iný spôsob hodnotenia modelov s nízkym počtom bitov. Perplexita a krátke skúšky sú praktické, pretože sú lacné a opakovateľné. Nezaťažujú však slučky, vďaka ktorým je agent užitočný: udržanie cieľa, výber nástrojov, čítanie chýb a nový pokus. Kalibračné dáta môžu mať rovnakú slepú škvrnu ako hodnotenie.

NariQ nerobí z 27B modelu univerzálne lacný systém. Celý kontext naďalej spotrebúva pamäť pre kľúče a hodnoty, vizuálny enkóder zostáva vo vysokej presnosti a rýchlosť inferencie závisí od jadier pre konkrétne zariadenie. Ukazuje však, že pri troch alebo 2,5 bitoch nemusia pri testovaných úlohách klesať úložný priestor pre váhy a schopnosti agenta súčasne.

Agent na pracovnej stanici dokončil terminálovú úlohu. Súbor s veľkosťou 10,12 GB sa zmestil hneď na začiatku. To, či ho spustí ďalší počítač, závisí menej od súboru a viac od názvu na jeho grafickom čipe.

## Použité zdroje

- Kim, D. (2026). *NariQ: Sub-3-Bit Quantization for Long-Horizon Agentic Tasks*. https://arxiv.org/abs/2611.26157
- Nari Labs (2026). *Qwen3.8-27B-NariQ-GGUF model card*. https://huggingface.co/nari-labs/Qwen3.8-27B-NariQ-GGUF
- Qwen Team (2026). *Qwen3.8-27B model card*. https://huggingface.co/Qwen/Qwen3.8-27B
- Tseng, J., et al. (2024). *QTIP: Quantization with Trellises and Incoherence Processing*. https://arxiv.org/abs/2406.11235
