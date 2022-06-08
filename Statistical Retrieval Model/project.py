from flask import Flask , render_template,request 

import random
 
app = Flask(__name__)

@app.route('/')
def index():
    char=['a','b','c','d','e','f']
    for i in range(1,11):
        file=open('files/f%i'%i,'w')
        file.write(' '.join(random.choice(char)for i in range(1,random.randint(15,40))))
        file.close()
    return render_template('index.html')

@app.route('/result',methods = [ 'POST'])
def data():
    dic={'f1':0,'f2':0,'f3':0,'f4':0,'f5':0,'f6':0,'f7':0,'f8':0,'f9':0,'f10':0}
    freq=[]

    wa=float(request.form["a_field"])
    wb=float(request.form["b_field"])
    wc=float(request.form["c_field"])
    wd=float(request.form["d_field"])
    we=float(request.form["e_field"])
    wf=float(request.form["f_field"])
    a=0
    b=0
    c=0
    d=0
    e=0
    f=0

    for i in range(1,11):
        file=open('files/f%i'%i,'r')
        l=file.readline()
        a=0
        b=0
        c=0
        d=0
        e=0
        f=0
        
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

        ca=(a/len(l))*wa
        cb=(b/len(l))*wb
        cc=(c/len(l))*wc
        cd=(d/len(l))*wd
        ce=(e/len(l))*we
        cf=(f/len(l))*wf
        s=ca+cb+cc+cd+ce+cf

        freq.append(s) #score
        

   
    dic={'f1':freq[0],'f2':freq[1],'f3':freq[2],'f4':freq[3],'f5':freq[4],'f6':freq[5],'f7':freq[6],'f8':freq[7],'f9':freq[8],'f10':freq[9]}
    
    sorted_dic = {k: v for k, v in sorted(dic.items(), key=lambda item: item[1], reverse=True)}
    
    return render_template("result.html", data=sorted_dic)

if __name__=="__main__":
    app.run(debug=True)