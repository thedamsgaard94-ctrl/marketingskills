# Prisændring af fælgsæt, 22.11.2026

**Godkendt af:** butiksejer ("Ja, skriv de 360 priser, start med dem under kostpris").
**Regel:** 40 % ren indtjening. Pris inkl. moms = kostpris (inkl. betalt moms) / 0,45, rundet op til et beløb, der slutter på 99.
**Status:** ÆNDRET i Shopify. Priserne er live på pdparts.dk, fordi produktpriser ikke afhænger af tema-publicering.

| Hold | Antal | Resultat |
|---|---|---|
| Sæt under kostpris (først) | 34 | 34 ændret, 0 fejl |
| Øvrige "klar til godkendelse" | 320 | 320 ændret, 0 fejl |
| Sprunget over: produkter med flere varianter | 6 | Ikke ændret, kræver manuel vurdering af hver variant |
| Beskrivelser med prisen i teksten | 82 | Opdateres, så teksten matcher den nye pris |

Backup af gamle priser og beskrivelser: `../backups/2026-11-22-faelgpriser-foer.json`.

Ikke omfattet af denne ændring:
- 169 VW-sæt, hvor den beregnede pris er over loftet (afventer ejerens beslutning).
- 127 sæt, hvor brugtmoms skal tjekkes.
- 48 af de 82 sæt under kostpris. De ligger i VW-loft-gruppen (36), brugtmoms-gruppen (2) eller mangler kilde (10).

## Opfølgning 22.11
- VW-loft (ejer: "Loft på vw"): 167 af 169 sæt stod allerede på loftet. Volkswagen Funchal 18″ er ændret fra 5.899 til 9.000 kr. Amarok står til 8.999 kr. (under loftet) og er ikke ændret.
- 0 kr.-sæt (ejer: "Pris på 35 + skjul resten"): 35 har fået pris efter en Otomoto-annonce (kost / 0,45). Annoncerne er ikke kontrolleret for antal, OEM-nummer og stand. 579 er sat til kladde. Backup: `backups/2026-11-22-nulpris-foer.json`.
- Ejeren har bedt om at finde priser i Polen eller Litauen, herunder Allegro. OLX-søgning kører. Ovoko, RRR.lt, Autoplius og Allegro blokerer automatiske opslag (403). Allegro kræver adgang via det officielle API.
- OLX.pl-søgning (579 sæt sat til kladde): 99 havde annoncer med matchende OEM- eller styling-nummer. 59 med en sætpris (≥ 500 zł, ikke 1–2 stk.) har fået pris (kost / 0,45) og er **genaktiveret**. Fordeling: BMW 47, Mercedes 11, Audi 1. Liste: `../olx-prissat-2026-11-22.csv`. Annoncerne er ikke kontrolleret for 4 stk., OEM-nummer og stand. **520 er fortsat kladde.**
- ChatGPT-søgning, række 1–25 (`../chatgpt-svar-1-25.csv`): 19 fund. 10 sæt med 4 stk. er prissat og **genaktiveret**. 7 enkeltfælge er sprunget over, fordi der ikke er sikkerhed for 4 ens. Kun OLX-linket kunne kontrolleres (findes og nævner OEM 6771157). Allegro blokerer automatiske opslag, så de 9 Allegro-links er brugt ukontrolleret efter ChatGPTs oplysninger. Række 14 og 25 er priset fra samme blandede sæt (6770941 for og 6770942 bag). **510 er fortsat kladde.**
- ChatGPT, række 26–50 (`../chatgpt-svar-26-50.csv`): 17 fund. 9 sæt er prissat og **genaktiveret**. 7 enkeltfælge er sprunget over. Række 48 (BMW 788M, Otomoto) er sprunget over, fordi annoncen svarer 410 Gone (fjernet/solgt). Række 27/28 og 44/45 er priset fra hver sit fælles sæt. **501 er fortsat kladde.**
- ChatGPT, række 51–75 (`../chatgpt-svar-51-75.csv`): 25 fund. 15 sæt er prissat og **genaktiveret**. 9 enkeltfælge er sprunget over. Række 71 (BMW 669M, OLX) er sprunget over, fordi annoncen svarer 410 Gone. **486 er fortsat kladde.**
- ChatGPT, række 76–100 (`../chatgpt-svar-76-100.csv`): 22 fund. 12 sæt er prissat og **genaktiveret**. 10 enkeltfælge er sprunget over. De 3 OLX-links er kontrolleret og findes. Ovoko- og Allegro-links kan ikke kontrolleres. Række 81/82, 83/84, 85/86 og 87/88 er priset fra hver sit fælles blandede sæt. **474 er fortsat kladde.**
- ChatGPT, række 101–125 (`../chatgpt-svar-101-125.csv`): 3 fund. 1 sæt er prissat og **genaktiveret** (Land Rover VPLWW0090 20″, renoveret, gsp24.pl). 2 enkeltfælge fra gsp24.pl er sprunget over (VPLKW0159 og VPLWW0091). Lexus PTR/PW/PT/DT-numrene gav ingen fund. **473 er fortsat kladde.**
- **Ny regel (ejer 22.11): "Hvis man kan få 4 enkelte fælge, så er det fint."** Enkeltfælg × 4 er tilladt, når sælgeren er en webshop eller forhandler med mindst 4 på lager, eller en autoriseret forhandler af nye originaldele. Enkeltfælge fra markedspladser springes fortsat over. Efter reglen er 5 tidligere sprungne prissat og **genaktiveret**: BMW 6754912 (bmwstore.pl), 8092591, 6883525 og 6854564 (czesci.bmwsklep.pl, priser kontrolleret på siden) samt Land Rover VPLWW0091 (gsp24.pl, 4 på lager). **468 er fortsat kladde.** Importscript og ChatGPT-prompt er opdateret med kolonnen `lager_antal`.
- ChatGPT, række 126–150 (`../chatgpt-svar-126-150.csv`): 10 fund. 7 sæt er prissat og **genaktiveret** (alle Mercedes-AMG). 3 enkeltfælge fra markedspladser er sprunget over. Begge OLX-links er kontrolleret og findes. Række 149 er i EUR fra en polsk sælger via rrr.lt og omregnet med 7,4735 DKK/EUR (butikkens kurs). Importscriptet er udvidet til EUR. **461 er fortsat kladde.**
- ChatGPT, række 151–175 (`../chatgpt-svar-151-175.csv`): 3 fund (sæt med 4 stk.). 2 er prissat og **genaktiveret**: Mercedes A2974012200 19″ (OLX, kontrolleret) og A2924010200 20″ (Otomoto, kontrolleret). Række 172 er sprunget over, fordi OLX-annoncen svarer 410 Gone. **459 er fortsat kladde.**
- ChatGPTs kontrolfil (`../chatgpt-kontrol-1-150.csv`) indeholder ingen ny genkontrol af annoncerne. Den afviser enkeltfælge fra forhandlere, men ejerens regel tillader dem, så de er bibeholdt. Den markerer **DUBLET_SAET**, hvor to produkter er priset fra samme fysiske sæt: 25, 28, 45, 57, 59, 82, 84, 86 og 88. Den risiko skal ejeren tage stilling til.
- Ejer 22.11: "Alt skal kunne sælges, og der er altid en der sælger samme sæt". Dublet-sæt beholdes aktive. Ejeren valgte "kunne købes direkte". Produkt-agenten stoppede før kørsel og bad om direkte bekræftelse af omfanget (1.604 produkter, heraf ca. 145 katalogsider prissat i dag). Det er afventende. Se `2026-11-22-produkt-koebbar.md`.
- ChatGPT, række 176–200 (`../chatgpt-svar-176-200.csv`): 3 Mercedes-sæt er prissat og **genaktiveret**: A1674013301 20″ (OLX, kontrolleret), A2054017400 AMG 19/20″ og A2044015302 19″ (Allegro). **456 er fortsat kladde.**
- Ejer 23.11: "Alle fælge du og chatgpt har fundet pris på og som er beregnet med overskud skal kunne købes." Det gælder 797 fælgsæt, som gøres købbare med lagerpolitik CONTINUE og fjernelse af forespørgsels-tags. Backup: `../backups/2026-11-23-koebbar-foer.json`.
- ChatGPT, række 201–225 (`../chatgpt-svar-201-225.csv`): 1 sæt. Mercedes GLA A1564012600 19″ med dæk (Allegro, 3.000 zł) er prissat til 12.799 kr., **genaktiveret og gjort købbart**. **455 er fortsat kladde.**
- ChatGPT, række 226–250 (`../chatgpt-svar-226-250.csv`): 6 fund. 5 er prissat, **genaktiveret og gjort købbare**. OLX-linket til række 229 og allegrolokalnie-linket til række 249 er kontrolleret. Række 241 (V-Klasse, OLX) svarer 410 Gone og er sprunget over. **450 er fortsat kladde.**
- ChatGPT, række 251–275 (`../chatgpt-svar-251-275.csv`): 1 fund. Mercedes EQS A2974010500 19″ med dæk og TPMS (allegrolokalnie, 4.800 zł, link og pris kontrolleret) er prissat til 19.699 kr., **genaktiveret og gjort købbart**. **449 er fortsat kladde.**
- ChatGPT, række 276–300 (`../chatgpt-svar-276-300.csv`): 3 fund. 2 Peugeot-sæt er prissat, **genaktiveret og gjort købbare**: Breda 19″ 98426689XK (Allegro, nye, 13.799 kr.) og Los Angeles 18″ 98116350EH (allegrolokalnie, link og pris kontrolleret, 10.499 kr.; OEM-nummeret er ikke aflæst på billedet). Række 298 (Porsche GT3, teile.com) er sprunget over, fordi det er en tysk forhandler med polsk webshop og dermed uden for reglen om Polen/Litauen. **447 er fortsat kladde.**
- ChatGPT, række 301–325 (`../chatgpt-svar-301-325.csv`): 3 Jaguar-sæt er prissat, **genaktiveret og gjort købbare**, og alle 3 OLX-links er kontrolleret: Turbine 22″ (49.599 kr.), Style 5030 18″ med vinterdæk (16.699 kr.) og Style 7009 18″ GX73-1007-EA (5.799 kr.). **444 er fortsat kladde.**
- Købbar-kørsel 23.11: 797/797 lagerpolitik og 390/390 tag-fjernelser er OK. Se `2026-11-22-produkt-koebbar.md`.
- **Ekstern tilbagerulning opdaget 23.11 kl. 11:13–11:25 UTC:** 74 Audi 19″-produkter med tagget `PDParts-prisloft-19` er sat tilbage til 14.000 kr. og DENY, og har fået tagget `PDParts-tilbud`. Det kommer ikke fra denne session og heller ikke fra nogen anden cloud-session eller planlagt opgave på kontoen. Sandsynligvis er det et andet værktøj, fx ChatGPT med Shopify-forbindelse, en Shopify-app/Flow eller en lokal session, der genanvender den tidligere Audi-loftregel fra 16.11. Ændringerne er ikke rettet igen, fordi ejeren først skal afgøre, hvilken regel der gælder.
- **Audi-loft fjernes (ejer valgte A, 23.11):** 204 Audi 19″/20″-produkter var klar til 40 %-reglen. Kørslen blev **stoppet efter første portion**, fordi ejeren oplyste, at ChatGPT arbejder på de samme produkter. Første portion (p_00: 40 produkter, 80 af 80 OK) har fået ny pris, CONTINUE og fjernet loft-, tilbud- og forespørgsels-tags. De øvrige 164 og alle 57 beskrivelser er **ikke ændret**. Backup: `../backups/2026-11-23-audi-loft-foer.json`. Afventer, at ejeren afgør, om Claude eller ChatGPT skal styre Audi-priserne.
