from flask import Flask, render_template,request

import random,math

appa=Flask(__name__)

@appa.route('/')
def index2():
    char=['a','b','c','d','e','f']
    for i in range(1,11):
        file=open('files2/d%i'%i,'w')
        file.write(' '.join(char[random.randint(0,5)] for i in range(1,random.randint(3,10))))
        file.close()
    return render_template('index2.html')

@appa.route('/result2',methods=['POST'])
def data():
    dic={'d1':0,'d2':0,'d3':0,'d4':0,'d5':0,'d6':0,'d7':0,'d8':0,'d9':0,'d10':0}
    a=0;b=0;c=0;d=0;e=0;f=0;all=0
    arr=[];arrA=[];arrB=[];arrC=[];arrD=[];arrE=[];arrF=[]
    Adoc=0;Bdoc=0;Cdoc=0;Ddoc=0;Edoc=0;Fdoc=0
    maximum=0

    for i in range(1,11):
        file=open('files2/d%i'%i,'r')
        l=file.readline()
        a=0;b=0;c=0;d=0;e=0;f=0
        
        for i in range(len(l)):
            if l[i]=='a':
                a=a+1
            if l[i]=='b':
                b=b+1
            if l[i]=='c':
                c=c+1
            if l[i]=='d':
                d=d+1  
            if l[i]=='e':
                e=e+1
            if l[i]=='f':
                f=f+1  
        arr=[a,b,c,d,e,f]
        maximum=max(arr)
        tfA=a/maximum
        arrA.append(tfA)
        tfB=b/maximum
        arrB.append(tfB)
        tfC=c/maximum
        arrC.append(tfC)
        tfD=d/maximum
        arrD.append(tfD)
        tfE=e/maximum
        arrE.append(tfE)
        tfF=f/maximum
        arrF.append(tfF)
    for i in range(1,11):
        file=open('files2/d%i'%i,'r')
        l=file.readline()
        if 'a' in l:
            Adoc=Adoc+1
        if 'b' in l:
            Bdoc=Bdoc+1
        if 'c' in l:
            Cdoc=Cdoc+1
        if 'd' in l:
            Ddoc=Ddoc+1
        if 'e' in l:
            Edoc=Edoc+1
        if 'f' in l:
            Fdoc=Fdoc+1
    idfA=math.log(10/Adoc,2)
    idfB=math.log(10/Bdoc,2)
    idfC=math.log(10/Cdoc,2)
    idfD=math.log(10/Ddoc,2)
    idfE=math.log(10/Edoc,2)
    idfF=math.log(10/Fdoc,2)
    wAD1=arrA[0]*idfA;wAD2=arrA[1]*idfA;wAD3=arrA[2]*idfA;wAD4=arrA[3]*idfA;wAD5=arrA[4]*idfA;wAD6=arrA[5]*idfA;wAD7=arrA[6]*idfA;wAD8=arrA[7]*idfA;wAD9=arrA[8]*idfA;wAD10=arrA[9]*idfA
    wBD1=arrB[0]*idfB;wBD2=arrB[1]*idfB;wBD3=arrB[2]*idfB;wBD4=arrB[3]*idfB;wBD5=arrB[4]*idfB;wBD6=arrB[5]*idfB;wBD7=arrB[6]*idfB;wBD8=arrB[7]*idfB;wBD9=arrB[8]*idfB;wBD10=arrB[9]*idfB
    wCD1=arrC[0]*idfC;wCD2=arrC[1]*idfC;wCD3=arrC[2]*idfC;wCD4=arrC[3]*idfC;wCD5=arrC[4]*idfC;wCD6=arrC[5]*idfC;wCD7=arrC[6]*idfC;wCD8=arrC[7]*idfC;wCD9=arrC[8]*idfC;wCD10=arrC[9]*idfC
    wDD1=arrD[0]*idfD;wDD2=arrD[1]*idfD;wDD3=arrD[2]*idfD;wDD4=arrD[3]*idfD;wDD5=arrD[4]*idfD;wDD6=arrD[5]*idfD;wDD7=arrD[6]*idfD;wDD8=arrD[7]*idfD;wDD9=arrD[8]*idfD;wDD10=arrD[9]*idfD
    wED1=arrE[0]*idfE;wED2=arrE[1]*idfE;wED3=arrE[2]*idfE;wED4=arrE[3]*idfE;wED5=arrE[4]*idfE;wED6=arrE[5]*idfE;wED7=arrE[6]*idfE;wED8=arrE[7]*idfE;wED9=arrE[8]*idfE;wED10=arrE[9]*idfE
    wFD1=arrF[0]*idfF;wFD2=arrF[1]*idfF;wFD3=arrF[2]*idfF;wFD4=arrF[3]*idfF;wFD5=arrF[4]*idfF;wFD6=arrF[5]*idfF;wFD7=arrF[6]*idfF;wFD8=arrF[7]*idfF;wFD9=arrF[8]*idfF;wFD10=arrF[9]*idfF
    strQuery=request.form["QueryStr"]
    aq=0;bq=0;cq=0;dq=0;eq=0;fq=0
    for i in range(len(strQuery)):
        if strQuery[i]=='a':
            aq=aq+1
        if strQuery[i]=='b':
            bq=bq+1
        if strQuery[i]=='c':
            cq=cq+1
        if strQuery[i]=='d':
            dq=dq+1  
        if strQuery[i]=='e':
            eq=eq+1
        if strQuery[i]=='f':
            fq=fq+1  
    arrq=[aq,bq,cq,dq,eq,fq]
    maximumq=max(arrq)
    tfaQ=aq/maximumq
    tfbQ=bq/maximumq
    tfcQ=cq/maximumq
    tfdQ=dq/maximumq
    tfeQ=eq/maximumq
    tffQ=fq/maximumq
    waq=tfaQ*idfA
    wbq=tfbQ*idfB
    wcq=tfcQ*idfC
    wdq=tfdQ*idfD
    weq=tfeQ*idfE
    wfq=tffQ*idfF
    cosSimd1q=(wAD1*waq+wBD1*wbq+wCD1*wcq+wDD1*wdq+wED1*weq+wFD1*wfq)/math.sqrt((wAD1*wAD1+wBD1*wBD1+wCD1*wCD1+wDD1*wDD1+wED1*wED1+wFD1*wFD1)*(waq*waq+wbq*wbq+wcq*wcq+wdq*wdq+weq*weq+wfq*wfq))
    cosSimd2q=(wAD2*waq+wBD2*wbq+wCD2*wcq+wDD2*wdq+wED2*weq+wFD2*wfq)/math.sqrt((wAD2*wAD2+wBD2*wBD2+wCD2*wCD2+wDD2*wDD2+wED2*wED2+wFD2*wFD2)*(waq*waq+wbq*wbq+wcq*wcq+wdq*wdq+weq*weq+wfq*wfq))
    cosSimd3q=(wAD3*waq+wBD3*wbq+wCD3*wcq+wDD3*wdq+wED3*weq+wFD3*wfq)/math.sqrt((wAD3*wAD3+wBD3*wBD3+wCD3*wCD3+wDD3*wDD3+wED3*wED3+wFD3*wFD3)*(waq*waq+wbq*wbq+wcq*wcq+wdq*wdq+weq*weq+wfq*wfq))
    cosSimd4q=(wAD4*waq+wBD4*wbq+wCD4*wcq+wDD4*wdq+wED4*weq+wFD4*wfq)/math.sqrt((wAD4*wAD4+wBD4*wBD4+wCD4*wCD4+wDD4*wDD4+wED4*wED4+wFD4*wFD4)*(waq*waq+wbq*wbq+wcq*wcq+wdq*wdq+weq*weq+wfq*wfq))
    cosSimd5q=(wAD5*waq+wBD5*wbq+wCD5*wcq+wDD5*wdq+wED5*weq+wFD5*wfq)/math.sqrt((wAD5*wAD5+wBD5*wBD5+wCD5*wCD5+wDD5*wDD5+wED5*wED5+wFD5*wFD5)*(waq*waq+wbq*wbq+wcq*wcq+wdq*wdq+weq*weq+wfq*wfq))
    cosSimd6q=(wAD6*waq+wBD6*wbq+wCD6*wcq+wDD6*wdq+wED6*weq+wFD6*wfq)/math.sqrt((wAD6*wAD6+wBD6*wBD6+wCD6*wCD6+wDD6*wDD6+wED6*wED6+wFD6*wFD6)*(waq*waq+wbq*wbq+wcq*wcq+wdq*wdq+weq*weq+wfq*wfq))
    cosSimd7q=(wAD7*waq+wBD7*wbq+wCD7*wcq+wDD7*wdq+wED7*weq+wFD7*wfq)/math.sqrt((wAD7*wAD7+wBD7*wBD7+wCD7*wCD7+wDD7*wDD7+wED7*wED7+wFD7*wFD7)*(waq*waq+wbq*wbq+wcq*wcq+wdq*wdq+weq*weq+wfq*wfq))
    cosSimd8q=(wAD8*waq+wBD8*wbq+wCD8*wcq+wDD8*wdq+wED8*weq+wFD8*wfq)/math.sqrt((wAD8*wAD8+wBD8*wBD8+wCD8*wCD8+wDD8*wDD8+wED8*wED8+wFD8*wFD8)*(waq*waq+wbq*wbq+wcq*wcq+wdq*wdq+weq*weq+wfq*wfq))
    cosSimd9q=(wAD9*waq+wBD9*wbq+wCD9*wcq+wDD9*wdq+wED9*weq+wFD9*wfq)/math.sqrt((wAD9*wAD9+wBD9*wBD9+wCD9*wCD9+wDD9*wDD9+wED9*wED9+wFD9*wFD9)*(waq*waq+wbq*wbq+wcq*wcq+wdq*wdq+weq*weq+wfq*wfq))
    cosSimd10q=(wAD10*waq+wBD10*wbq+wCD10*wcq+wDD10*wdq+wED10*weq+wFD10*wfq)/math.sqrt((wAD10*wAD10+wBD10*wBD10+wCD10*wCD10+wDD10*wDD10+wED10*wED10+wFD10*wFD10)*(waq*waq+wbq*wbq+wcq*wcq+wdq*wdq+weq*weq+wfq*wfq))

    dic={'d1':cosSimd1q,'d2':cosSimd2q,'d3':cosSimd3q,'d4':cosSimd4q,'d5':cosSimd5q,'d6':cosSimd6q,'d7':cosSimd7q,'d8':cosSimd8q,'d9':cosSimd9q,'d10':cosSimd10q}
    
    sorted_dic = {k: v for k, v in sorted(dic.items(), key=lambda item: item[1], reverse=True)}

    return render_template("result2.html", data=sorted_dic)

if __name__=='__main__':
    appa.run(debug=True)