import json,sys,glob,re,csv,collections,math
W,OUT=sys.argv[1],sys.argv[2]
P=[]
for f in sorted(glob.glob(W+'/page*.json'), key=lambda s:int(re.search(r'page(\d+)',s).group(1))):
    P+=json.load(open(f))['data']['products']['nodes']
PRIMARY=['pdparts_internal.sourcing_audit','pdparts.sourcing_audit','pdparts.sourcing','pdparts.pricing_policy','pdparts_internal.oe_priskandidater','pdparts.wheel_cost_review_20261106']
MARKET=r'olx\.|kleinanzeigen|ebay\.|allegro\.|otomoto|facebook\.|vinted|autoplius|skelbiu|marktplaats|subito|mobile\.de'
VWCAP={17:7000,18:9000,19:14000,20:16000}
FORBID=r'leverandør|ifølge (sælger|kilde|annonce)|sælger(en)? oplyser|allegro|olx|kleinanzeigen|ebay|\bkilden\b'
def mfs(p):
    d={}
    for ns,name in (('a','pdparts'),('b','pdparts_internal')):
        for m in p[ns]['nodes']:
            try: d[name+'.'+m['key']]=json.loads(m['value'])
            except: d[name+'.'+m['key']]=m['value']
    return d
def walk(o,skip=('rejected_sources','alternatives','alternatives_private','candidates','rejected')):
    if isinstance(o,dict):
        for k,v in o.items():
            if k in skip: continue
            yield k,v
            yield from walk(v,skip)
    elif isinstance(o,list):
        for x in o: yield from walk(x,skip)
def first(o,keys,pred=lambda v:True):
    for k,v in walk(o):
        if k in keys and v not in (None,'',[]) and not isinstance(v,(dict,list)) and pred(v): return v
def anyurl(o):
    for k,v in walk(o):
        if isinstance(v,str) and v.startswith('http') and 'pdparts' not in v and 'shopify' not in v and not re.search(r'\.(jpg|jpeg|png|webp)(\?|$)',v,re.I): return v
rows=[];stats=collections.Counter()
for p in P:
    d=mfs(p); src=None;srckey=''
    for k in PRIMARY:
        if k in d and isinstance(d[k],(dict,list)): src=d[k];srckey=k;break
    allm=[v for v in d.values() if isinstance(v,(dict,list))]
    url=None
    for o in ([src] if src else [])+allm:
        url=url or anyurl(o)
    seller=None;country=None;sprice=None;cur=None;srcstatus=None;divisor=None
    for o in ([src] if src else [])+allm:
        seller=seller or first(o,{'seller','source_name','seller_name','supplier_name','shop','name'} if o is src else {'seller','source_name','seller_name','supplier_name'},lambda v:isinstance(v,str) and len(v)<120)
        country=country or first(o,{'country','country_code','countryCode','land'},lambda v:isinstance(v,str) and len(v)<=3)
        if sprice is None:
            for k,v in walk(o):
                m=re.match(r'^(price|price_pln|price_eur|gross_source_set_pln|saet_pln|supplier_full_gross|source_price|set_price_pln|purchase_gross_budget_pln)$',k)
                if m and isinstance(v,(int,float,str)) and re.match(r'^\d+(\.\d+)?$',str(v)):
                    sprice=float(v); cur='PLN' if 'pln' in k else ('EUR' if 'eur' in k else None); break
        cur=cur or first(o,{'currency','supplier_currency'},lambda v:isinstance(v,str) and len(v)==3)
        srcstatus=srcstatus or (o.get('status') if isinstance(o,dict) and isinstance(o.get('status'),str) and len(o.get('status'))<40 else None)
    vatinv=any(re.search(r'vat_invoice|invoice_vat|faktura',k,re.I) and (v is True or (isinstance(v,(str,list)) and re.search(r'VAT|faktur',str(v),re.I))) for o in allm for k,v in walk(o))
    tags=p['tags']; tl=' '.join(tags).lower(); title=p['title']; low=(title+' '+tl).lower()
    inch=next((int(m.group(1)) for t in tags for m in [re.match(r'^(\d{2}) tommer$',t)] if m),None)
    if inch is None:
        m=re.search(r'(\d{2})\s*(″|"|tommer|”)',title); inch=int(m.group(1)) if m else None
    oem=[t for t in tags if re.fullmatch(r'[0-9A-Z]{9,14}',t) and re.search(r'\d',t) and re.search(r'[A-Z]',t) or re.fullmatch(r'\d{11}',t)]
    if 'brugt' in low or 'demontage' in low: stand='Brugt'
    elif 'demo' in low: stand='Demo'
    elif 'renover' in low: stand='Renoveret'
    elif re.search(r'\bnye?\b',low) or 'som nyt' in low: stand='Ny'
    else: stand='Uafklaret'
    four=bool(re.search(r'\b4\b|fire ',title.lower()) or '4 fælge' in tl or 'sæt' in title.lower())
    v=p['variants']['nodes'][0]; price=float(v['price']); uc=v['inventoryItem']['unitCost']; cost=float(uc['amount']) if uc else None
    vendor=p['vendor'] or ''
    isvw=bool(re.search(r'volkswagen|^vw$',vendor,re.I) or re.match(r'vw ',title,re.I))
    cap=VWCAP.get(inch) if isvw else None
    desc=p.get('descriptionHtml')
    # VAT basis
    if not url: moms='INGEN DOKUMENTERET KILDE'
    elif re.search(MARKET,url): moms='UAFKLARET – markedsplads, sælgerstatus (privat/erhverv) og faktura ikke dokumenteret'+(' (mulig brugtmoms/privatkøb)' if stand in('Brugt','Demo') else '')
    else: moms='UAFKLARET – erhvervssælger; faktura og evt. omvendt betalingspligt (EU-erhvervskøb) ikke dokumenteret'
    if vatinv and url: moms+='; VAT-faktura tilbudt i kilde'
    issues=[]
    if not country and url:
        m=re.search(r'https?://[^/]+\.(pl|lt|de|lv|sk|cz|nl|it|at|dk)(/|$)',url); country=m.group(1).upper() if m else None
    if price<=0: issues.append('Aktiv/kladde uden pris (0 kr.)')
    if not isvw and price in (7000.0,9000.0,14000.0,16000.0): issues.append('Ikke-VW med loftpris (7/9/14/16 t.kr.) – særregel skal bekræftes')
    if not cost or cost<=0: issues.append('Ingen kostpris i Shopify')
    if not url: issues.append('Ingen kilde-URL')
    if country and country.upper() not in ('PL','LT'): issues.append(f'Kildeland {country} (ikke PL/LT – kræver afvigelsesgodkendelse)')
    if not four: issues.append('Titel angiver ikke tydeligt sæt med 4')
    if not oem: issues.append('OEM-nummer mangler i tags')
    if inch is None: issues.append('Tommer mangler')
    if stand=='Uafklaret': issues.append('Stand uafklaret')
    if p['mediaCount']['count']<2: issues.append(f"Kun {p['mediaCount']['count']} billede(r)")
    if 'pdparts-vejledende-modelbillede' in tl: issues.append('Vejledende modelbilleder, ikke fotos af sættet')
    if desc is None: dq='ikke hentet'
    else:
        dq='ok'
        if re.search(FORBID,re.sub(r'<[^>]+>',' ',desc),re.I): dq='leverandør-/kildeformulering'; issues.append('Beskrivelse indeholder leverandør-/kildeformulering')
        if re.search(r'href="https?://(?!pdparts)',desc): dq+='; eksternt link'; issues.append('Eksternt link i beskrivelse')
        if desc and not re.search(r'ET\s?-?\d',desc): issues.append('ET ikke angivet i beskrivelse')
        if desc and not re.search(r'\d\s?[x×]\s?\d{3}',desc): issues.append('Boltmønster ikke angivet i beskrivelse')
    if srcstatus and re.search(r'blocked|reject|unavailable|sold|archiv',srcstatus,re.I): issues.append(f'Kildestatus: {srcstatus}')
    prop=None;prop_ex=None;diff=None
    if cost and cost>0:
        prop_ex=round(cost*1.40,2); prop=math.ceil(cost*1.40*1.25); diff=round(prop-price,2)
    capflag=''
    if cap:
        capflag='Under loft' if prop and prop<=cap else ('LOFT OVERSKREDET – kræver godkendelse' if prop else '')
        if price>cap: issues.append(f'Nuværende pris over VW-loft {cap}')
    ratio=round(price/cost,3) if cost else None
    if ratio and ratio<1.75-0.01: issues.append('Nuværende pris under formel (kost×1,75)')
    if ratio and ratio<1: issues.append('NUVÆRENDE PRIS UNDER KOSTPRIS')
    # kontrolstatus
    if p['status']!='ACTIVE': ks='KONTROLLERET – ikke aktiv ('+p['status']+'); intet forslag til udgivelse'
    elif not cost or not url: ks='BLOKERET – mangler kost/kilde'
    else: ks='FORESLÅET (betinget) – kan ikke godkendes før momsgrundlag og faktura er dokumenteret'
    stats[ks.split(' –')[0]]+=1
    rows.append(dict(product_id=p['id'],handle=p['handle'],titel=title,status=p['status'],maerke=vendor,tommer=inch,oem=' / '.join(oem),stand=stand,
        lager_egen=p['totalInventory'],billeder=p['mediaCount']['count'],nuv_pris_inkl_moms=price,shopify_kostpris_dkk=cost,nuv_pris_div_kost=ratio,
        kilde_url=url,saelger=seller,land=country,kildepris=sprice,valuta=cur,kilde_metafelt=srckey,kildestatus=srcstatus,momsgrundlag=moms,
        forslag_ex_moms_kost_x1_40=prop_ex,forslag_inkl_moms_normalmoms=prop,aendring_kr=diff,vw_loft=cap,vw_loft_check=capflag,
        tekstkontrol=dq,kvalitetsfund='; '.join(issues),kontrolstatus=ks))
cols=list(rows[0].keys())
with open(OUT+'.csv','w',newline='',encoding='utf-8-sig') as f:
    w=csv.DictWriter(f,cols,delimiter=';'); w.writeheader(); w.writerows(rows)
json.dump(rows,open(OUT+'.json','w'),ensure_ascii=False)
print(len(rows),dict(stats))
