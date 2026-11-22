import csv,json,glob,math,sys
P={}
for f in glob.glob('wheels/page*.json'):
    for p in json.load(open(f))['data']['products']['nodes']: P[p['id'].split('/')[-1]]=p
rows=[];skip=[]
for r in csv.DictReader(open(sys.argv[1],encoding='utf-8-sig'),delimiter=';'):
    if r['fundet']!='JA': continue
    if r['antal_faelge']!='4' or r['valuta']!='PLN' or r['land'] not in('PL','LT'): skip.append((r['nr'],r['antal_faelge'])); continue
    p=P[r['product_id']]; v=p['variants']['nodes']
    if len(v)!=1: skip.append((r['nr'],'varianter')); continue
    cost=float(r['pris'])/0.589*1.02+150+(400 if r['med_daek']=='JA' else 0)
    raw=cost/0.45; pr=int(math.ceil((raw+1)/100)*100-1)
    if pr-100>=raw: pr-=100
    rows.append(dict(nr=r['nr'],product_id='gid://shopify/Product/'+r['product_id'],variant_id=v[0]['id'],titel=p['title'],pris_pln=r['pris'],kost=round(cost),ny_pris=pr,url=r['annonce_url']))
print('skip',skip)
for x in rows: print(x['nr'],x['titel'][:55],x['pris_pln'],'->',x['ny_pris'])
json.dump(rows,open(sys.argv[2],'w'),ensure_ascii=False)
print('mutation{'+''.join(f'p{j}:productVariantsBulkUpdate(productId:"{x["product_id"]}",variants:[{{id:"{x["variant_id"]}",price:"{x["ny_pris"]}.00"}}]){{userErrors{{message}}}} s{j}:productUpdate(product:{{id:"{x["product_id"]}",status:ACTIVE}}){{userErrors{{message}}}} ' for j,x in enumerate(rows))+'}')
