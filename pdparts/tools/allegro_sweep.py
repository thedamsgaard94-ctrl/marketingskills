"""Allegro REST API sweep for drafted PDParts wheel sets.
Auth: client_credentials. The agent proxy injects Basic auth (Client ID/Secret) on allegro.pl,
so the token call sends a dummy Basic header that the proxy replaces."""
import json,re,subprocess,time,sys,urllib.parse
def curl(args):
    r=subprocess.run(['curl','-s','--max-time','30']+args,capture_output=True); return r.stdout.decode('utf-8','replace')
def token():
    out=curl(['-X','POST','-u','dummy:dummy','https://allegro.pl/auth/oauth/token?grant_type=client_credentials'])
    j=json.loads(out); 
    if 'access_token' not in j: sys.exit('token-fejl: '+out[:300])
    return j['access_token']
def search(tok,phrase):
    url='https://api.allegro.pl/offers/listing?'+urllib.parse.urlencode({'phrase':phrase,'limit':30})
    out=curl(['-H','Authorization: Bearer '+tok,'-H','Accept: application/vnd.allegro.public.v1+json',url])
    try: j=json.loads(out)
    except: return None,out[:200]
    if 'items' not in j: return None,out[:300]
    items=j['items'].get('promoted',[])+j['items'].get('regular',[])
    return [dict(id=i['id'],title=i['name'],price=float(i['sellingMode']['price']['amount']),cur=i['sellingMode']['price']['currency'],
                 seller=i.get('seller',{}).get('id'),company=i.get('seller',{}).get('company'),url='https://allegro.pl/oferta/'+i['id']) for i in items],None
if __name__=='__main__':
    tok=token()
    if len(sys.argv)>1 and sys.argv[1]=='test':
        r,err=search(tok,'felgi BMW styling 351 19'); print(err or [(x['title'][:60],x['price']) for x in r[:5]]); sys.exit()
    R=[r for r in json.load(open('out_aendringsliste.json')) if r['product_id'] in set(json.load(open('zero_draft.json')))]
    done=set()
    try: done={json.loads(l)['product_id'] for l in open('allegro_sweep.jsonl')}
    except FileNotFoundError: pass
    priced={x['product_id'] for x in json.load(open('olx_rows.json'))}
    out=open('allegro_sweep.jsonl','a')
    for r in R:
        if r['product_id'] in done or r['product_id'] in priced: continue
        t=r['titel']; inch=(re.search(r'(\d{2})″',t) or [None,''])[1]; qs=[]
        if r['oem']: qs.append(r['oem'].split(' / ')[0][:11])
        m=re.search(r'A\d{10}',t)
        if m and not r['oem']: qs.append(m.group(0))
        s=re.search(r'Styling (\d+M?)',t)
        if s: qs.append(f'felgi BMW styling {s.group(1)} {inch}')
        st=re.search(r'Style (\d{4})',t)
        if st: qs.append(f'felgi {r["maerke"]} style {st.group(1)}')
        if not qs: qs.append(f'felgi {r["maerke"]} {re.sub(r"[–-].*","",t)[:40]} {inch}')
        found=[]
        for q in qs[:2]:
            res,err=search(tok,q); time.sleep(1)
            if res: found+= [dict(x,q=q) for x in res]
        out.write(json.dumps(dict(product_id=r['product_id'],titel=t,maerke=r['maerke'],queries=qs[:2],found=found),ensure_ascii=False)+'\n'); out.flush()
    print('done')
