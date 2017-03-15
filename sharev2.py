import json
from collections import defaultdict

    
def addToTable(table, p,n):
    sp = sorted(p.items(),key=lambda (x,y):y,reverse=True)
    sn = sorted(n.items(),key=lambda (x,y):y,reverse=True)

    for i in range(len(sn)):
        name,toGive  = sn[i]
        if toGive:
            for j in range(len(sp)):
                (otherName,toReceive) = sp[j]
                if toReceive:
                    if toGive>=toReceive:
                        toGive-=toReceive
                        sp[j]=(otherName,0)
                        sn[i]=(name,toGive)
                        table[name][otherName]+=toReceive
#                        print '%s gives %s  Rs. %d, done'%(name,otherName,toReceive)
                    else:
                        sp[j]=(otherName,toReceive-toGive)
                        sn[i]=(name,0)
                        table[name][otherName]+=toGive
#                        print '%s gives %s  Rs. %d, remaining %d'%(name,otherName,toGive,sp[j][1])
                        break






def calc(data):
    all = set()
    table = defaultdict(lambda :defaultdict(lambda: 0))
    for d in data['calc']:
        all |= set(d['participants'])
        all |= set(d['by'])
        nparticipants =  len(d['participants'])
        d['amount'] = float(d['amount'])
        pve = {d['by']:d['amount']}
        nve = dict([(p,d['amount']/nparticipants) for p in d['participants']])
        addToTable(table,pve,nve)

    shouldPay = dict([(i,sum([table[i][l] for l in table[i]])) for i in all])
    shouldGet = dict([(i,sum([l.get(i,0) for l in table.values()]))for i in all])
    for i in all:
        if shouldPay[i] and shouldGet[i]:
            if shouldPay[i]>shouldGet[i]:
                shouldPay[i]-=shouldGet[i]
                shouldGet[i]=0
            else:
                shouldGet[i]-=shouldPay[i]
                shouldPay[i]=0
    table = defaultdict(lambda :defaultdict(lambda: 0))
    addToTable(table,shouldGet,shouldPay)
    return json.dumps(table)

from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        posted = request.json
        return calc(posted)
    else:
        return 'Not Supported !'


if __name__ == '__main__':
    app.run()
