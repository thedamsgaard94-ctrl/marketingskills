# OpenSEO-crawl 21.11.2026: status pr. fund

Audit-ID: `4288d32d-752a-4107-a513-9cb07904841e`. Crawlet stoppede ved sidegrænsen efter 50 sider (forsiden, /agents.md og 48 dæksider). 1.188 opdagede URL'er blev ikke crawlet. Ingen fælgsider indgik i stikprøven.

Statusser: KONTROLLERET · FORESLÅET · ÆNDRET (skrevet i Shopify) · UDGIVET (verificeret på pdparts.dk ved ny crawl).

| Fund | URL / produkt | Status | Dokumentation |
|---|---|---|---|
| duplicate-title | winrun-r330-w-silent-275-35-r21-6939364208194 / -6939364210975 | ÆNDRET (før 22.11, ikke i denne session) | To forskellige EAN'er og producentnumre (SW63421 og ESW63421) betyder to forskellige varer. Titlerne er nu unikke, så der er ikke behov for canonical. Ved gennemgangen 22.11 havde begge allerede unikke titler |
| duplicate-title (samme mønster, ikke i stikprøven) | Winrun 265/35 ZR22 102W: Product 15722091741508 / 15722091905348 | ÆNDRET 22.11 | SW52722 / ESW52722, to EAN'er. Titel og SEO-titel er gjort unikke |
| title-too-long ×6 (+3 udenfor stikprøven) | 9 Rotalla Setula S-Race RS01+ | ÆNDRET 22.11 | SEO-titlen er forkortet fra 59–63 til 50–54 tegn. Størrelse, belastningsindeks, hastighedsindeks, XL og MFS er bevaret. Backup: `backups/2026-11-22-seo-titler-foer.json` |
| crawl-page-limit | 1.188 URL'er | IKKE KONTROLLERET | Ny crawl er blokeret: pdparts.dk er ikke tilladt i dette miljøs netværk, og der er ingen OpenSEO-forbindelse. Se planen herunder |

Ingen af ændringerne har status UDGIVET, før en ny crawl har bekræftet dem på de offentlige sider.

## Plan for segmenteret crawl (1.188 URL'er)

Kør OpenSEO (eller crawl herfra, når pdparts.dk er tilladt) i disse segmenter, hver med et sidebudget, der dækker hele segmentet:

1. `/collections/*` for fælgkollektioner: VW, Audi, BMW, Mercedes, Porsche, Skoda og Tesla.
2. `/products/*` for fælgprodukter. Brug listen over aktive handles i `faelge-aendringsliste-2026-11-22.csv` (2.063 aktive), filtreret pr. mærke i samme rækkefølge som punkt 1.
3. Resten af dæksortimentet (`tag:PDParts-daek-katalog`, 5.404 produkter).
4. `/pages/*`, `/blogs/*` og sitemap-kontrol (`/sitemap.xml`).

Kontrollér i hvert segment: HTTP-status, canonical, indekserbarhed, unik title (≤ 60 tegn) og meta (120–155 tegn), én H1, billeder uden alt-tekst og interne links. Hvert fund kobles til et Shopify product-ID via `handle`.

Allerede kendt fra Shopify-data for de 2.063 aktive fælgprodukter:
- **614 er aktive til 0 kr.** De fleste er katalogsider ("… – originale fælge") uden billeder. De bør gennemgås for tyndt indhold og eventuelt noindex, eller skjules.
- 883 har færre end 2 billeder.
- 565 mangler et OEM-nummer i tags.
