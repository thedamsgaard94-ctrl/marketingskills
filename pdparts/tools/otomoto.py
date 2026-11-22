import re,sys,json,subprocess,time,random
def search(q):
    r=subprocess.run(['curl','-s','--max-time','25','-A','Mozilla/5.0 (X11; Linux x86_64) PDParts-sourcing','https://www.otomoto.pl/czesci/q-'+q],capture_output=True)
    h=r.stdout.decode('utf-8','replace')
    m=re.search(r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>',h,re.S)
    if not m: return None,[]
    u=json.loads(m.group(1))['props']['pageProps'].get('urqlState') or {}
    for v in u.values():
        s=v.get('data') if isinstance(v,dict) else None
        if s and 'advertSearch' in s:
            a=json.loads(s)['advertSearch']; out=[]
            for e in a.get('edges') or []:
                n=e['node']; pr=n.get('price') or {}
                amt=(pr.get('amount') or {}).get('units') if isinstance(pr.get('amount'),dict) else pr.get('amount')
                out.append(dict(title=n.get('title'),price=amt,cur=(pr.get('amount') or {}).get('currencyCode') if isinstance(pr.get('amount'),dict) else None,url=n.get('url'),loc=json.dumps(n.get('location'),ensure_ascii=False)[:80]))
            return a.get('totalCount'),out
    return 0,[]
if __name__=='__main__':
    for q in sys.argv[1:]:
        t,o=search(q); print(q,t); [print('   ',x) for x in o[:3]]; time.sleep(2)
