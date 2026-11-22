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
