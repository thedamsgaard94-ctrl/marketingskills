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

1. **Prisgrundlag:** De fleste fælge har pris/kostpris ≈ 2,33. Med 1,4 × 1,25 i moms burde forholdet være 1,75. Er kostprisen i Shopify i en anden valuta eller ekskl. fragt, eller gælder der en særregel?
2. **Fast pris 14.000 kr.:** Mange Audi 19″-sæt står til præcis 14.000 kr. Seks af dem ligger under kostprisen. Se `prisavvigelser-faelge-2026-11-22.csv`.
