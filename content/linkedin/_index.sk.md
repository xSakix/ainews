+++
title = "Newsletter Svet AI tvorený AI"
description = "Denné vydania newslettra na LinkedIne, pripravené na vloženie do editora. Stránka nie je určená čitateľom ani vyhľadávačom."
outputs = ["html"]
robotsNoIndex = true
ShowBreadCrumbs = false
[build]
  list = "never"
[sitemap]
  disable = true

# Editions (YYYY-MM-DD.sk.md, written by prompts/linkedin-run.md) are listed
# here but kept out of the home page, feeds, search, archives, llms.txt and
# the sitemap: build.list = "local" leaves them out of site.RegularPages.
[[cascade]]
  outputs = ["html"]
  robotsNoIndex = true
  searchHidden = true
  [cascade.build]
    list = "local"
  [cascade.sitemap]
    disable = true
+++

Každé ráno z denného prehľadu vznikne vydanie newslettra [Svet AI tvorený AI](https://www.linkedin.com/newsletters/svet-ai-tvoren%C3%BD-ai-7349186484307951619/). LinkedIn nemá rozhranie na zverejňovanie newslettrov, preto ho do LinkedInu vkladá vydavateľ ručne. Na stránke vydania má každá časť vlastné tlačidlo na kopírovanie a postup je uvedený priamo tam.
