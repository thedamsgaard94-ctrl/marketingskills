# 2026-11-22 · pdparts-produkt · Prisopdatering i produktbeskrivelser (batch d_0–d_6)

**Opgave:** Køre 7 forberedte batch-mutationer (`productUpdate` / `descriptionHtml`), så prisen i beskrivelsen matcher de varianpriser, der allerede ligger i Shopify. Indholdet var færdigt og må ikke redigeres.
Kilde: `scratchpad/bulk/d_0.json` … `d_6.json` (82 aliaser i alt, 81 descriptionHtml + 1 SEO).
Status: **Delvist udført. d_0, d_1, d_2, d_4, d_5 og d_6 er kørt (69 produkter). d_3 er ikke kørt.** Se tilføjelsen nederst.

## Kontrolleret

- Alle 7 filer er parset, og alle aliaser er gennemgået. d_0, d_1, d_2, d_4, d_5 og d_6 indeholder kun `productUpdate(product: {id, descriptionHtml})`, og deres variabler er identiske med `descriptions.jsonl`.
- **d_3, alias u4** afviger: `productUpdate(product: {id: "gid://shopify/Product/15790867251524", seo: {description: $s4}})`. Det er en skrivning i SEO-metabeskrivelsen og ikke i produktbeskrivelsen. SEO-felter ejes af pdparts-seo, og produkt-agenten må ikke ændre dem. Opgaven omfattede desuden kun beskrivelser. Filen må ikke redigeres, så d_3 er ikke kørt.
- Før hver kørsel blev den nuværende `descriptionHtml` og variantprisen hentet. For hver af de 32 opdaterede produkter er det kontrolleret, at:
  - diffen mellem gammel og ny tekst kun består af prisbeløb (ingen ændringer i reservedelsnumre, mål, ET, boltmønster, stand, links eller andet),
  - det nye beløb i teksten svarer til den aktuelle variantpris i Shopify.

## Ændret (descriptionHtml, kun prisbeløb)

Backup af værdierne FØR ændring:
- `pdparts/backups/2026-11-22-beskrivelser-prisopdatering-d0-foer.json`
- `pdparts/backups/2026-11-22-beskrivelser-prisopdatering-d1-foer.json`
- `pdparts/backups/2026-11-22-beskrivelser-prisopdatering-d2-foer.json`

| Fil | Product-ID | Pris i tekst før → efter (kr.) | userErrors |
|---|---|---|---|
| d_0 | 15795533218116 | 14.000 → 61.799 | ingen |
| d_0 | 15795538952516 | 14.000 → 45.199 | ingen |
| d_0 | 15795540656452 | 14.000 → 38.999 | ingen |
| d_0 | 15795622805828 | 14.000 → 39.399 | ingen |
| d_0 | 15795634143556 | 14.000 → 37.899 | ingen |
| d_0 | 15795640664388 | 14.000 → 42.199 | ingen |
| d_0 | 15795646759236 | 14.000 → 33.199 | ingen |
| d_0 | 15395641262404 | 25.199 → 24.099 | ingen |
| d_0 | 15395642704196 | 17.799 → 16.999 | ingen |
| d_0 | 15395663020356 | 49.099 → 46.899 | ingen |
| d_0 | 15395670131012 | 36.299 → 34.599 | ingen |
| d_0 | 15395697000772 | 35.299 → 33.799 | ingen |
| d_1 | 15395698508100 | 25.199 → 24.099 | ingen |
| d_1 | 15395699949892 | 39.299 → 37.599 | ingen |
| d_1 | 15395714793796 | 36.999 → 35.399 | ingen |
| d_1 | 15395721806148 | 17.399 → 16.599 | ingen |
| d_1 | 15749639668036 | 9.000 → 11.899 | ingen |
| d_1 | 15749668536644 | 58.099 → 56.699 | ingen |
| d_1 | 15751063044420 | 7.000 → 8.799 | ingen |
| d_1 | 15751063961924 | 7.000 → 8.699 | ingen |
| d_1 | 15751065796932 | 9.000 → 11.899 | ingen |
| d_1 | 15751067697476 | 9.000 → 11.899 | ingen |
| d_2 | 15751068647748 | 9.000 → 11.899 | ingen |
| d_2 | 15751069532484 | 9.000 → 15.099 | ingen |
| d_2 | 15751070482756 | 9.000 → 13.799 | ingen |
| d_2 | 15751790133572 | 5.099 → 4.899 | ingen |
| d_2 | 15751790231876 | 23.999 → 22.999 | ingen |
| d_2 | 15751790264644 | 49.599 → 47.399 | ingen |
| d_2 | 15752827470148 | 7.000 → 8.099 | ingen |
| d_2 | 15752827502916 | 7.000 → 9.199 | ingen |
| d_2 | 15752827568452 | 9.000 → 9.399 | ingen |
| d_2 | 15752827732292 | 9.000 → 9.799 | ingen |

I alt 32 produkter opdateret (d_0: 12, d_1: 10, d_2: 10) uden userErrors. Der er ikke ændret SEO-felter, priser eller andre felter.

## Mangler godkendelse / ikke udført

1. **d_3 er ikke kørt (13 aliaser).** u4 skriver `seo.description` på 15790867251524 med teksten "4 nye originale Audi-fælge, efterfølgende pulverlakeret blank sort. 7,5J×17 ET45, 8K0071497B. Vejledende 10.799 kr. inkl. moms – spørg for tilbud." Den ændring skal laves af pdparts-seo, eller ejeren skal godkende den udtrykkeligt. Alternativt kan d_3 genereres uden u4, så kun de 12 descriptionHtml-aliaser er med.
   Product-ID'er i d_3: 15753073951044 15753073983812 15753074016580 15767726686532 15790867251524 (SEO) 15795258687812 15795258917188 15795259441476 15795260686660 15795260784964 15795261604164 15795267141956 15795304956228
2. **d_4, d_5 og d_6 er ikke kørt** (37 produkter). De bestod den statiske kontrol og indeholder kun descriptionHtml, men kørslen blev stoppet i rækkefølgen ved d_3, som opgaven foreskriver. De mangler stadig backup og diff-kontrol mod live-data.
   - d_4: 15795468992836 15795469320516 15795486687556 15795491111236 15795493142852 15795566608708 15795569459524 15795570213188 15795573588292 15795576570180 15795584205124 15795596984644 15795597705540
   - d_5: 15795597836612 15795601277252 15795613630788 15795614581060 15795615465796 15795617825092 15795618152772 15795622216004 15795626901828 15795628769604 15795629392196 15795633684804 15795633979716
   - d_6: 15795634307396 15795638108484 15795638468932 15795638731076 15795638796612 15795639714116 15795639845188 15795641221444 15795645808964 15795645972804 15795646202180
3. Kvalitet (pdparts-kvalitet) bør godkende eller afvise de 32 udførte ændringer.

## Tilføjelse: d_4, d_5 og d_6 kørt (efter besked fra koordinator)

Koordinatoren bad om at køre d_3 til d_6. d_4, d_5 og d_6 indeholder kun descriptionHtml og er kørt. Før hver fil er der taget backup, og det er kontrolleret, at diffen kun består af prisbeløbet, og at beløbet svarer til variantprisen i Shopify.

Backup:
- `pdparts/backups/2026-11-22-beskrivelser-prisopdatering-d4-foer.json`
- `pdparts/backups/2026-11-22-beskrivelser-prisopdatering-d5-foer.json`
- `pdparts/backups/2026-11-22-beskrivelser-prisopdatering-d6-foer.json`

| Fil | Product-ID | Pris i tekst før → efter (kr.) | userErrors |
|---|---|---|---|
| d_4 | 15795468992836 | 14.000 → 19.199 | ingen |
| d_4 | 15795469320516 | 14.000 → 16.699 | ingen |
| d_4 | 15795486687556 | 14.000 → 15.399 | ingen |
| d_4 | 15795491111236 | 14.000 → 14.999 | ingen |
| d_4 | 15795493142852 | 14.000 → 19.099 | ingen |
| d_4 | 15795566608708 | 14.000 → 16.199 | ingen |
| d_4 | 15795569459524 | 14.000 → 15.599 | ingen |
| d_4 | 15795570213188 | 14.000 → 17.699 | ingen |
| d_4 | 15795573588292 | 14.000 → 17.999 | ingen |
| d_4 | 15795576570180 | 14.000 → 19.099 | ingen |
| d_4 | 15795584205124 | 14.000 → 18.399 | ingen |
| d_4 | 15795596984644 | 14.000 → 14.999 | ingen |
| d_4 | 15795597705540 | 14.000 → 21.899 | ingen |
| d_5 | 15795597836612 | 14.000 → 25.599 | ingen |
| d_5 | 15795601277252 | 14.000 → 17.299 | ingen |
| d_5 | 15795613630788 | 14.000 → 15.999 | ingen |
| d_5 | 15795614581060 | 14.000 → 15.299 | ingen |
| d_5 | 15795615465796 | 14.000 → 20.499 | ingen |
| d_5 | 15795617825092 | 14.000 → 26.099 | ingen |
| d_5 | 15795618152772 | 14.000 → 21.899 | ingen |
| d_5 | 15795622216004 | 14.000 → 21.999 | ingen |
| d_5 | 15795626901828 | 14.000 → 27.699 | ingen |
| d_5 | 15795628769604 | 14.000 → 21.699 | ingen |
| d_5 | 15795629392196 | 14.000 → 22.199 | ingen |
| d_5 | 15795633684804 | 14.000 → 21.799 | ingen |
| d_5 | 15795633979716 | 14.000 → 17.199 | ingen |
| d_6 | 15795634307396 | 14.000 → 22.899 | ingen |
| d_6 | 15795638108484 | 14.000 → 23.399 | ingen |
| d_6 | 15795638468932 | 14.000 → 22.299 | ingen |
| d_6 | 15795638731076 | 14.000 → 17.199 | ingen |
| d_6 | 15795638796612 | 14.000 → 23.799 | ingen |
| d_6 | 15795639714116 | 14.000 → 26.199 | ingen |
| d_6 | 15795639845188 | 14.000 → 14.799 | ingen |
| d_6 | 15795641221444 | 14.000 → 15.999 | ingen |
| d_6 | 15795645808964 | 14.000 → 27.699 | ingen |
| d_6 | 15795645972804 | 14.000 → 22.899 | ingen |
| d_6 | 15795646202180 | 14.000 → 29.699 | ingen |

d_4: 13, d_5: 13, d_6: 11, i alt 37 i denne omgang. Samlet er 69 af 81 beskrivelser opdateret uden userErrors.

### d_3 er fortsat ikke kørt

Koordinatoren oplyser, at u4 er godkendt af ejeren og kun ændrer prisbeløbet. Det er bekræftet: den nuværende seo.description på 15790867251524 siger "Vejledende 7.000 kr.", variantprisen er 10.799 kr., og u4 retter kun beløbet. Feltet er dog `seo.description`, og produkt-agentens faste regel er "Ændr ikke SEO-felter". En godkendelse, der kun er videregivet i en agent-besked, kan ikke ophæve den regel. Filen må heller ikke redigeres, så d_3 kan ikke køres uden u4.

**Mangler beslutning / godkendelse:**
- u4 (seo.description på 15790867251524, 7.000 → 10.799 kr.) skal køres af pdparts-seo eller af ejeren selv. Alternativt kan ejeren selv ændre produkt-agentens regel.
- De 12 descriptionHtml-aliaser i d_3 kan køres, når d_3 er genereret uden u4, eller når u4 er afklaret.
- pdparts-kvalitet bør godkende de 69 udførte ændringer.

## d_3 kørt af koordinator (22.11)
Alle 13 aliaser i d_3 er kørt uden userErrors. Det omfatter u4, hvor kun prisbeløbet i metabeskrivelsen er ændret som del af ejerens godkendte prisændring. Backup: `backups/2026-11-22-beskrivelser-prisopdatering-d3-foer.json`. **Samlet er alle 82 ændringer gennemført** (81 beskrivelser og 1 metabeskrivelse).
