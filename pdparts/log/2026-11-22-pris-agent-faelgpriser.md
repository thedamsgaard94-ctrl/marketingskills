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
