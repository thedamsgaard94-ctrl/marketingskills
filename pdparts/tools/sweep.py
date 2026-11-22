import re,sys,time,json,importlib.util
spec=importlib.util.spec_from_file_location('o','tools/otomoto.py'); o=importlib.util.module_from_spec(spec); spec.loader.exec_module(o)
R=[r for r in json.load(open('out_aendringsliste.json')) if r['status']=='ACTIVE' and r['nuv_pris_inkl_moms']<=0]
out=open('sweep_otomoto.jsonl','a')
done={json.loads(l)['product_id'] for l in open('sweep_otomoto.jsonl')}
def base(x):
    x=x.split(' / ')[0]
    if re.fullmatch(r'\d{11}',x): return x
    if x.startswith('A') and len(x)>11: return x[:11]
    m=re.match(r'^([0-9][A-Z0-9]{2}\d{6}[A-Z]{0,2})',x); return m.group(1) if m else x
for r in R:
    if r['product_id'] in done: continue
    t=r['titel']; qs=[]
    m=re.search(r'A\d{10}',t)
    if r['oem']: qs.append(base(r['oem']))
    elif m: qs.append(m.group(0))
    s=re.search(r'Styling (\d+M?)',t); i=re.search(r'(\d{2})″',t)
    if s and i: qs.append('styling-'+s.group(1)+'-'+i.group(1))
    st=re.search(r'Style (\d{4})',t)
    if st and r['maerke'] in('Jaguar','Land Rover'): qs.append(r['maerke'].lower().replace(' ','-')+'-'+st.group(1))
    found=[]
    for q in qs:
        try: n,ads=o.search(q)
        except Exception as e: n,ads=0,[]
        time.sleep(2)
        if n: found.append(dict(q=q,total=n,ads=ads[:5]))
    out.write(json.dumps(dict(product_id=r['product_id'],titel=t,maerke=r['maerke'],queries=qs,found=found),ensure_ascii=False)+'\n'); out.flush()
print('done')
