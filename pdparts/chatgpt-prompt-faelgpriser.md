# Prompt til ChatGPT: indkøbspriser på originale fælgsæt (Polen/Litauen)

Vedhæft filen `chatgpt-faelge-uden-pris.csv`, og indsæt teksten herunder. Slå websøgning til, så ChatGPT kan søge på nettet.

---

Du er indkøber for en dansk webshop, der sælger **originale fælgsæt (4 stk.)**. Du skal finde **aktuelle indkøbspriser i Polen eller Litauen** for fælgene i den vedhæftede CSV-fil.

**Kilder (kun disse lande):**
- Polen: allegro.pl, olx.pl, otomoto.pl, ovoko.pl og polske webshops for brugte/originale fælge
- Litauen: rrr.lt, autoplius.lt, skelbiu.lt, ovoko.lt

Brug linkene i kolonnerne `allegro_soeg` og `olx_soeg` som udgangspunkt. Søg også på reservedelsnummeret (`oem`) med og uden mellemrum, fx "A2924012300" og "A 292 401 23 00". Søg desuden på designnavnet + tommer + "felgi oryginalne".

**Krav til et fund:**
1. Annoncen skal gælde **samme fælg**: samme reservedelsnummer/OEM-nummer, eller samme designnavn/styling-nummer og samme tommestørrelse, hvis der ikke er et OEM-nummer.
2. Den skal være **original** (OEM), ikke kopi eller replika.
3. Notér om prisen gælder **1, 2 eller 4 fælge**. Er det enkeltfælge, skal du skrive stykprisen og "1" i antal.
4. Notér om der følger **dæk** med.
5. Notér **stand**: ny / brugt / renoveret.
6. Notér om sælger er **firma** eller **privat**, hvis det fremgår.
7. Brug kun annoncer, du **faktisk har set**, med et **direkte link**. Gæt aldrig en pris, og opfind aldrig et link.
8. Find gerne det **billigste kvalificerede sæt med 4 stk.**. Findes det ikke, så den billigste enkeltfælg.

**Arbejd i portioner:** tag 25 rækker ad gangen (start med række 1–25), og fortsæt, når jeg skriver "næste".

**Svar KUN med en tabel i dette CSV-format** (semikolon som separator, én linje pr. række, også når der ikke er fundet noget):

```
nr;product_id;oem;fundet;annonce_url;annonce_titel;pris;valuta;antal_faelge;med_daek;stand;saelger_type;land;bemaerkning
```

- `fundet` = JA eller NEJ
- `pris` = kun tal, fx 2999
- `valuta` = PLN eller EUR
- `antal_faelge` = 1, 2 eller 4
- `med_daek` = JA eller NEJ
- `stand` = ny, brugt eller renoveret
- `saelger_type` = firma, privat eller ukendt
- `land` = PL eller LT
- `bemaerkning` = kort note, fx "OEM-nummer set på foto" eller "kun designnavn matcher"

Ved NEJ: udfyld kun `nr;product_id;oem;NEJ` og lad resten være tomt.

---

**Bagefter:** kopiér tabellerne fra ChatGPT ind i en fil, eller indsæt dem her i chatten. Så kontrollerer jeg dem, beregner prisen (kost / 0,45, slutter på 99), lægger dem ind i Shopify og aktiverer produkterne igen.
