# PDParts AI-workflow

Styringsdokument for de seks PDParts-agenter i `.claude/agents/`. Butik: pdparts.dk (Shopify Basic, DKK).

## Arbejdsfordeling (ejerskab pr. felt, så ingen overskriver hinanden)

| Agent | Skriver i Shopify | Ejer |
|---|---|---|
| pdparts-seo | Ja | SEO-titel, metabeskrivelse, kollektionstekst, tema-SEO-snippets |
| pdparts-produkt | Ja | Produkttitel, beskrivelse, tags, varianter, kollektioner |
| pdparts-pris | Nej (forslag i CSV) | Prisregler, avancekontrol |
| pdparts-kvalitet | Nej (godkender/afviser) | Billeder, alt-tekst, tekstregler, mobil/desktop-kontrol |
| pdparts-marketing | Nej (udkast) | LinkedIn, nyhedsbreve, B2B-materiale i `pdparts/marketing/` |
| pdparts-analyse | Nej | Trafik-, salgs- og konverteringsrapporter |

## Flow

1. Analyse og SEO finder problemer, og hvert fund registreres i `pdparts/log/`.
2. Produkt og SEO retter inden for deres egne felter. De gamle værdier gemmes først i `pdparts/backups/`.
3. Pris foreslår ændringer i en CSV, som ejeren godkender, før de lægges ind.
4. Kvalitet kontrollerer og markerer opgaven som godkendt eller afvist i loggen.
5. Temaændringer laves på en kopi af temaet. Kopien publiceres kun efter godkendelse.

Masseændringer over 25 produkter kræver godkendelse.

## Faste produktregler

- Professionelt dansk i PDParts' eget navn. Ingen formuleringer som "leverandøren oplyser" og ingen eksterne salgslinks.
- EU-dækmærket på dæk er lovpligtigt og bevares, også når det ligger på en ekstern billed-URL.
- Fælge er altid originale og sælges som sæt med 4. Kontrollér reservedelsnummer, størrelse, ET, boltmønster, farve og stand. Sourcing prioriteres fra Polen og Litauen.
- **Pris (bekræftet af ejer 22.11):** 40 % skal være ren indtjening. Kostpris = indkøbspris inkl. betalt moms + indgående fragt + håndtering. Salgspris inkl. moms = kost / 0,45, rundet op til et beløb, der slutter på 99. Formlen giver 40 % af salgsprisen ekskl. moms efter kost og 3 % betalingsgebyr. VW-lofter (17″ 7.000 · 18″ 9.000 · 19″ 14.000 · 20″ 16.000 inkl. moms) gælder stadig. Overskrides et loft, skal ejeren beslutte. Produkter må ikke stå til 0 kr.
- Reservedele: originale udvendige dele og udstyrsdele med indkøbspris over 1.000 DKK. Angiv model, årgang, facelift, højre/venstre og variant.
- Mindst 2 billeder pr. produkt, kun billeder vi har rettigheder til, og ingen leverandørlogoer.

## Åbne spørgsmål til ejeren

1. **Prisgrundlag:** Afklaret 22.11, se de faste produktregler.
2. **Momsgrundlag:** Ingen fælgsæt har en dokumenteret faktura eller momsordning. Alle prisforslag er derfor betingede. Se `faelge-aendringsliste-2026-11-22.xlsx`.
3. **Audi-loft:** Der ligger en registreret Audi-loftregel fra 16.11 (`pdparts_internal.audi_price_cap_20261116`). Skal den gælde fremover?

## Ansvarsfordeling (ejer 23.11)
- **Audi-fælge med prisloft-tags** (`PDParts-prisloft-19`/`-20`): håndteres af ChatGPT. Claude-agenter ændrer dem ikke.
- **Audi har intet prisloft** (ejer 23.11). Audi følger 40 %-reglen: kost / 0,45, slutter på 99. VW-loftet gælder stadig.
