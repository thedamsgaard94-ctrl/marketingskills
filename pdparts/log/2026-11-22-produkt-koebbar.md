# 2026-11-22 · produkt-agent · Køb direkte i kurven for fælgsæt (kb_00–kb_35)

**Status: IKKE UDFØRT. Venter på, at ejeren selv bekræfter omfanget.**

## Hvad blev kontrolleret
- 36 mutationsfiler (`scratchpad/bulk/kb/kb_00..kb_35.gql`): 1.604 produkter, 1.617 varianter sættes til `inventoryPolicy:CONTINUE`, og der er 975 `tagsRemove`.
  - 561 fjerner kun `PDParts-forespoergsel`.
  - 414 fjerner også `PDParts-pris-paa-forespoergsel`.
- Backup `pdparts/backups/2026-11-22-koebbar-foer.json` dækker alle 1.604 produkt-ID'er, alle varianter og alle tags, der skal fjernes. Backuppen er OK.
- Ændringen rammer 1.604 produkter. Grænsen for masseændringer uden godkendelse er 25 (README). Godkendelsen er kun videregivet af en anden agent og er ikke bekræftet direkte af ejeren.
- Stikprøven viser et problem med omfanget:
  - `gid://shopify/Product/15753021423940` "Audi 5-V-spoke 17″ – originale fælge" har tags `PDParts-OEM-producentkatalog` og `PDParts-pris-paa-forespoergsel`. Titlen siger ikke, at det er et sæt med 4.
  - Ni af ti OEM-katalogprodukter i stikprøven ligger i listen. Butikken har 903 produkter med OEM-katalog-tag.
  - Ifølge README (åbent spørgsmål 2) er alle fælgpriser betingede, fordi der mangler momsgrundlag.
  - Hvis tagget "pris på forespørgsel" fjernes, og CONTINUE sættes, kan kunderne bestille fælge uden fysisk lager og uden bekræftet pris.

## Hvad blev ændret
- Intet. Der blev ikke kørt mutationer. Alle product-ID'er har samme værdier før og efter.

## Hvad mangler godkendelse
1. Ejeren skal selv bekræfte, at alle 1.604 produkter må kunne købes direkte som bestillingsvare. Det gælder også OEM-katalogposterne.
2. Ejeren skal tage stilling til de 414 produkter med `PDParts-pris-paa-forespoergsel`. Er prisen bekræftet, eller skal de forblive tilbudsvarer?
3. Hvis omfanget skal indsnævres til fysisk indkøbte sæt (fx med tags `PDParts-onlinekoeb` eller `Bestillingsvare` og "4 stk." i titlen), skal filerne genereres igen.

---

## Opfølgning 2026-11-23 · indsnævret omfang (kb2: kb_00–kb_17)

**Status: IKKE UDFØRT. Venter stadig på godkendelse direkte fra ejeren.**

### Hvad blev kontrolleret
- 18 filer (`scratchpad/bulk/kb2/kb_00..kb_17.gql`): 797 unikke produkter, 797 `productVariantsBulkUpdate` (kun `inventoryPolicy:CONTINUE`) og 390 `tagsRemove`. Filerne indeholder ingen pris-, SEO-, titel- eller sletteoperationer.
- Backup `pdparts/backups/2026-11-23-koebbar-foer.json` dækker præcis de samme 797 produkt-ID'er, uden afvigelser i nogen retning. Den indeholder variant-ID'er, quote-tags og rollback-note (DENY + tagsAdd).
  - Kilder: repris 40 % 354, følger reglen 284, OLX 59, ChatGPT 59, Otomoto 35, forhandler ×4 5, VW-loft med overskud 1. Det stemmer med den opgjorte fordeling.
  - Tags: 407 uden quote-tag, 227 med kun `PDParts-forespoergsel` og 163 med begge tags.
- Omfanget er nu teknisk korrekt og indsnævret. Det er stadig en masseændring (797 > 25).

### Hvad blev ændret
- Intet. Der blev ikke kørt mutationer, og alle 797 produkt-ID'er har samme værdier før og efter.
- Begrundelse: Godkendelsen fra ejeren ("Alle fælge ... skal kunne købes", 23.11) er igen kun videregivet af en anden agent. Den er ikke givet direkte til denne agent eller via permission-systemet. Efter de faste regler kan en agentbesked ikke tælle som godkendelse af en masseændring.

### Hvad mangler godkendelse
1. Ejeren skal selv godkende kørslen direkte. Det kan ske i sin egen besked til denne session eller via permission-prompten for mutationerne. Godkendelsen skal dække alle 797 produkter, herunder 163 produkter, hvor tagget "pris på forespørgsel" fjernes, og 118 produkter, der er prissat ud fra OLX/ChatGPT-kilder.
2. README, åbent spørgsmål 2 (momsgrundlag), er stadig ikke lukket. Alle fælgpriser er derfor formelt betingede.
3. Filerne og backuppen er klar. Kørslen kan ske uden ændringer, når godkendelsen foreligger.
