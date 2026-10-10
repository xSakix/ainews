+++
title = "rGPU maakt een externe kaart tot een PyTorch-apparaat"
slug = "rgpu-maakt-externe-kaart-tot-pytorch-apparaat"
description = "Het project met Apache-licentie houdt Python en modelcode op een clientmachine terwijl tensors en CUDA-bewerkingen op een externe NVIDIA-GPU draaien."
tags = ["projects", "hardware", "tools"]
date = 2026-10-08T03:55:31+02:00
draft = false
+++

Het open-sourceproject rGPU laat een PyTorch-programma op een laptop blijven draaien terwijl zijn tensors en bewerkingen op een externe NVIDIA-GPU staan.

Het systeem met Apache-licentie biedt twee routes. Nieuwe PyTorch-code kan `device="rgpu"` selecteren, terwijl een bredere CUDA-compatibiliteitslaag aanroepen uit bestaande Linux-programma's onderschept en via een netwerkverbinding naar een server doorstuurt.

Voor een ontwikkelaar met een Mac of bescheiden werkstation en een ongebruikte GPU-machine elders behoudt die scheiding de lokale programmeeromgeving zonder de hele applicatie naar een cloudnotebook of externe shell te verplaatsen. De client kan met gewone PyTorch-syntaxis een tensor op het externe apparaat maken en het meegeleverde startprogramma legt een SSH-tunnel naar de server aan.

De eenvoudige apparaatroute stuurt PyTorch-bewerkingen over TCP. De compatibiliteitsroute implementeert lagen voor de CUDA-driver en runtime, evenals cuBLAS, cuBLASLt en cuDNN, om standaard CUDA-PyTorch-programma's te draaien. De repository beschrijft deze route als breder in compatibiliteit, zodat ondersteuning afhangt van de bibliotheekaanroepen die een applicatie gebruikt.

rGPU bevat een nanoGPT-trainingsvoorbeeld, referenties voor bewerkingen en configuratie, prestatienotities en tests voor zijn Python- en C++-componenten. Experimenteel JAX-werk staat in de repository, maar wordt niet als ondersteunde productroute vermeld.

Netwerkbeveiliging is de belangrijkste operationele beperking. Geen van beide protocollen authenticeert of versleutelt zijn eigen verkeer. De documentatie instrueert gebruikers de bewerkingsserver aan localhost gebonden te houden en via SSH te verbinden; de CUDA-server luistert op alle IPv4-interfaces, zodat poort 9713 ook door host- of cloudfirewallregels moet worden beperkt.

Het project maakt externe versnelling tot een apparaatkeuze in plaats van een afzonderlijke uitvoeringsomgeving, maar zijn prestatie- en compatibiliteitsclaims komen momenteel uit de documentatie van de beheerder. De code, tests en technische verslagen zijn te inspecteren en op de GitHub-pagina staat nog geen getagde release vermeld.

## Verificatie {#verification}

| Bewering | Label | Primaire bron | Onafhankelijke verificatie |
|---|---|---|---|
| rGPU houdt een applicatie op de client terwijl tensors en GPU-werk op een externe NVIDIA-machine draaien | GEVERIFIEERD | [rGPU-repository](https://github.com/ymcrcat/rgpu) | geen |
| Het project biedt een PyTorch-`rgpu`-apparaat en een CUDA-compatibiliteitslaag | GEVERIFIEERD | [rGPU-repository](https://github.com/ymcrcat/rgpu) | geen |
| De compatibiliteitslaag omvat interfaces voor de CUDA-driver, CUDA Runtime, cuBLAS, cuBLASLt en cuDNN | GEVERIFIEERD | [rGPU-repository](https://github.com/ymcrcat/rgpu) | geen |
| Geen van beide protocollen biedt authenticatie of versleuteling; de documentatie schrijft SSH en firewallbeperkingen voor | GEVERIFIEERD | [rGPU-repository](https://github.com/ymcrcat/rgpu) | geen |
| De repository bevat tests, een nanoGPT-voorbeeld en experimenteel JAX-werk | GEVERIFIEERD | [rGPU-repository](https://github.com/ymcrcat/rgpu) | geen |
| Compatibiliteits- en prestatiekenmerken zijn door de projectbeheerder gedocumenteerd | VOLGENS HET BEDRIJF | [rGPU-repository](https://github.com/ymcrcat/rgpu) | geen |
