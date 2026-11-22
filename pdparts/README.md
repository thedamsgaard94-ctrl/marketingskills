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
- Pris: indkøbspris + 40 %, medmindre der er en dokumenteret særregel (se åbne spørgsmål).
- Reservedele: originale udvendige dele og udstyrsdele med indkøbspris over 1.000 DKK. Angiv model, årgang, facelift, højre/venstre og variant.
- Mindst 2 billeder pr. produkt, kun billeder vi har rettigheder til, og ingen leverandørlogoer.

## Åbne spørgsmål til ejeren

1. **Prisgrundlag (afklaret 22.11):** Den gældende regel er salg ekskl. moms = dokumenteret direkte kost × 1,40, og salg inkl. moms = × 1,25 ved normal moms. De eksisterende priser er beregnet som kost / 0,43–0,45. Det er fortolkningen "40 % ren indtjening", og den skal godkendes eller forkastes, før nye priser udgives.
2. **Momsgrundlag:** Ingen fælgsæt har en dokumenteret faktura eller momsordning. Alle prisforslag er derfor betingede. Se `faelge-aendringsliste-2026-11-22.xlsx`.
3. **Audi-loft:** Der ligger en registreret Audi-loftregel fra 16.11 (`pdparts_internal.audi_price_cap_20261116`). Skal den gælde fremover?
