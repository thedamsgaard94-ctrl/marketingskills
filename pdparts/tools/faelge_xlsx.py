import json,sys,collections,openpyxl,statistics,shutil
from openpyxl.styles import Font,PatternFill
from openpyxl.utils import get_column_letter
OUT=sys.argv[1]
R=json.load(open('out_aendringsliste.json')); A=[r for r in R if r['status']=='ACTIVE']
F=[r for r in A if r['kontrolstatus'].startswith('FORESL')]
B=[r for r in A if r['kontrolstatus'].startswith('BLOK')]
c=collections.Counter(i for r in A for i in r['kvalitetsfund'].split('; ') if i)
def cnt(s): return sum(n for k,n in c.items() if k.startswith(s))
med=statistics.median(r['nuv_pris_div_kost'] for r in A if r['nuv_pris_div_kost'])
wb=openpyxl.Workbook(); ws=wb.active; ws.title='Oversigt'
rows=[['PDParts – samlet ændringsliste for fælgsæt','',''],['Udtrukket fra Shopify','2026-11-22','Alle produkter med tag "Fælge"'],
['Status-definitioner','','KONTROLLERET = data gennemgået; FORESLÅET = beregnet forslag, ikke skrevet i Shopify; ÆNDRET = skrevet i Shopify; UDGIVET = synligt på pdparts.dk'],
['Ingen priser er ændret i Shopify i denne leverance','',''],[],
['Fælgprodukter i alt',len(R),''],['Aktive',len(A),''],['Kladde / arkiveret',len(R)-len(A),'Kun kontrolleret, intet udgivelsesforslag'],
['Aktive med betinget prisforslag (kost + kilde findes)',len(F),'FORESLÅET (betinget) – kan ikke godkendes før momsgrundlag og faktura er dokumenteret'],
['  heraf prisstigning',sum(1 for r in F if r['aendring_kr']>0),''],['  heraf prisfald',sum(1 for r in F if r['aendring_kr']<0),''],
['Aktive blokeret (mangler kostpris eller kilde)',len(B),'Kræver sourcing før prissætning'],[],
['Kvalitetsfund (aktive)','Antal',''],
['Aktive til 0 kr.',cnt('Aktiv/kladde uden pris'),'Bør skjules eller have et forespørgselsflow'],
['Nuværende pris under kostpris',cnt('NUVÆRENDE PRIS UNDER KOSTPRIS'),'Tabsgivende ved salg'],
['Nuværende pris under kost × 1,75',cnt('Nuværende pris under formel'),''],
['VW: forslag overskrider loft',sum(1 for r in A if r['vw_loft_check'].startswith('LOFT')),'Kræver manuel beslutning'],
['Ikke-VW med loftpris 7/9/14/16 t.kr.',cnt('Ikke-VW'),'Fx Audi-loft registreret 16.11 – bekræft om særreglen gælder'],
['Ingen kilde-URL',cnt('Ingen kilde-URL'),''],['Ingen kostpris i Shopify',cnt('Ingen kostpris'),''],
['Kildeland uden for PL/LT',cnt('Kildeland'),'Kræver afvigelsesgodkendelse'],
['Færre end 2 billeder',cnt('Kun 0')+cnt('Kun 1'),''],['Vejledende modelbilleder',cnt('Vejledende'),''],
['OEM-nummer mangler i tags',cnt('OEM-nummer'),''],['Stand uafklaret',cnt('Stand uafklaret'),''],
['Titel angiver ikke sæt med 4',cnt('Titel angiver'),''],['ET mangler i beskrivelse',cnt('ET ikke'),'Kun de 1.402 aktive med hentet beskrivelse'],['Boltmønster mangler i beskrivelse',cnt('Boltmønster'),''],
['Leverandør-/kildeformulering i tekst',cnt('Beskrivelse indeholder'),''],[],
['VIGTIGT: fortolkningsforskel','','Eksisterende priser er beregnet som salg inkl. moms = kost / 0,43-0,45 (40 procent af omsætningen efter moms og gebyrer). Ny regel: kost x 1,40 x 1,25 = 1,75. Median nuværende pris/kost: '+str(round(med,2))],
['VIGTIGT: kostgrundlag','','Shopify-kostprisen er i de gamle kalkuler brutto inkl. udenlandsk moms, valutabuffer og håndtering. Ved EU-erhvervskøb med omvendt betalingspligt skal kosten være netto, ellers bliver forslaget for højt.']]
for r in rows: ws.append(r)
ws['A1'].font=Font(bold=True,size=14); ws.column_dimensions['A'].width=52; ws.column_dimensions['B'].width=14; ws.column_dimensions['C'].width=110
hdr={'product_id':'Product ID','handle':'Handle','titel':'Titel','status':'Status','maerke':'Mærke','tommer':'Tommer','oem':'OEM','stand':'Stand','lager_egen':'Eget lager','billeder':'Billeder',
'nuv_pris_inkl_moms':'Nuv. pris inkl. moms','shopify_kostpris_dkk':'Shopify-kostpris DKK','nuv_pris_div_kost':'Nuv. pris / kost','kilde_url':'Kilde-URL','saelger':'Sælger','land':'Land','kildepris':'Kildepris','valuta':'Valuta',
'kilde_metafelt':'Kilde-metafelt','kildestatus':'Kildestatus (tidl. audit)','momsgrundlag':'Momsgrundlag','forslag_ex_moms_kost_x1_40':'Forslag ex moms (kost×1,40)','forslag_inkl_moms_normalmoms':'Forslag inkl. moms (normalmoms)',
'aendring_kr':'Ændring kr.','vw_loft':'VW-loft','vw_loft_check':'Loft-check','tekstkontrol':'Tekstkontrol','kvalitetsfund':'Kvalitetsfund','kontrolstatus':'Kontrolstatus'}
def sheet(name,data):
    s=wb.create_sheet(name); keys=list(hdr); s.append([hdr[k] for k in keys])
    for r in data: s.append([r[k] for k in keys])
    for i,k in enumerate(keys,1):
        s.cell(1,i).font=Font(bold=True,color='FFFFFF'); s.cell(1,i).fill=PatternFill('solid',fgColor='1F3A5F')
        s.column_dimensions[get_column_letter(i)].width={'titel':60,'kilde_url':45,'momsgrundlag':50,'kvalitetsfund':70,'kontrolstatus':45}.get(k,14)
    s.freeze_panes='D2'; s.auto_filter.ref=s.dimensions
    red=PatternFill('solid',fgColor='F8D7DA'); ki=keys.index('kvalitetsfund'); pi=keys.index('nuv_pris_inkl_moms')
    for row in s.iter_rows(min_row=2):
        if 'UNDER KOSTPRIS' in (row[ki].value or ''): row[pi].fill=red
sheet('Forslag aktive',sorted(F,key=lambda r:r['aendring_kr'])); sheet('Blokeret aktive',B); sheet('Alle fælge',R)
rs=wb.create_sheet('Prisregler')
for r in [['Regel','Værdi'],['Salgspris ex moms','(verificeret indkøbspris ex fradragsberettiget moms + indgående fragt + klargøring + direkte gebyrer) × 1,40'],['Salgspris inkl. moms','ex-pris × 1,25 (kun normal moms), rundet op til hel krone'],
 ['Forslag i dette ark','Shopify-kostpris × 1,40 × 1,25. Indgående fragt er ikke dokumenteret særskilt og kan mangle eller være indregnet'],['Udgående fragt','Faktureres separat'],
 ['VW-lofter inkl. moms','17″ 7.000 · 18″ 9.000 · 19″ 14.000 · 20″ 16.000. Overskridelse flagges og sænkes ikke automatisk'],['Andre mærker','Intet standardloft'],
 ['Brugtmoms / privatkøb','Normalformlen må ikke bruges før fakturakrav er kontrolleret (skat.dk, brugtmomsordningen)'],['Kilder','https://skat.dk/erhverv/moms/andre-momsemner/brugtmoms/brugtmomsordningen ; https://skat.dk/erhverv/moms/moms-ved-handel-med-udlandet/moms-ved-handel-med-virksomheder/moms-ved-handel-med-lande-i-eu/moms-ved-koeb-af-varer-og-ydelser-i-eu']]: rs.append(r)
rs.column_dimensions['A'].width=28; rs.column_dimensions['B'].width=130
wb.save(OUT+'/faelge-aendringsliste-2026-11-22.xlsx'); shutil.copy('out_aendringsliste.csv',OUT+'/faelge-aendringsliste-2026-11-22.csv')
for r in rows[5:31]:
    if r: print(r[0],'|',r[1])
