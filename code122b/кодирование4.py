def f4():
    import math 
    def otvet(a):
        print(str(a)+" бит")
        print(str(a/2**3)+" байт")
        print(str(a/2**13)+" килобайт")
        print(str(a/2**23)+" мегабайт")      
        print(str(a/2**33)+" гигабайт")
    def perevod(a,b):
        if b== "1":
            a=a*2**3
        elif b== "2":
            a=a*2**13
        elif b== "3":
            a=a*2**23
        elif b== "4":
            a=a*2**33
        return a 
    def it(N):
        T = int(math.log2(2*N-1))
        return T
    def pamyat():
        N ="1 - Мощность алфавита(N), "
        K ="2 - колво символов в тексте(K), "
        I ="3 - инф объём текста(I), "
        i ="0 - инф  символа(i), "
        print("что нужно найти? \n",i,"\n",N,"\n",K,"\n",I,"\n")
        G=input()
        if G=="0":
            N=input("N-?\n")
            K=int(input("K-?\n"))
            I,V=float(input("I-?\n")),input("в чём данные? \n 0 - бит\n 1 - байт\n 2 - килобайт\n 3 - мегабайт\n 4 - гигабайт\n")
            if N=="":
                otvet(K*perevod(I,V))
            else: 
                otvet(it(int(N)))
        if G=="1":
            i,v=float(input("i-?\n"))
            print(2**perevod(i,v))
        if G=="3":
            K=int(input("K-?\n"))
            N=input("N-?\n")
            i,V=input("i-?\n"),input("в чём данные? \n 0 - бит\n 1 - байт\n 2 - килобайт\n 3 - мегабайт\n 4 - гигабайт\n")
            if i=="":
                I=it(int(N))*K
            else:
                I=perevod(float(i),V)*K
            otvet(I)
        if G=="2":
            I,V1=float(input("I-?\n")),input("в чём данные? \n 0 - бит\n 1 - байт\n 2 - килобайт\n 3 - мегабайт\n 4 - гигабайт\n")
            i,V2=input("i-?\n"),input("в чём данные? \n 0 - бит\n 1 - байт\n 2 - килобайт\n 3 - мегабайт\n 4 - гигабайт\n")
            N=input("N-?\n")
            if i=="":
                K=perevod(I,V1)/it(int(N))
            else:
                K=perevod(I,V1)/perevod(float(i),V2)
            print(K)
    def zvuk():
        N ="0 - количество уровней сигнала(N), "
        D ="1 - частота дискретизации(D), "
        V ="2 - объём звуковоо файла(V), "
        i ="3 - глубина звука(i), "
        T ="4 - длительность звукового файла(T)"
        print("Что нужно найти? ","\n",N,"\n",D,"\n",V,"\n",i,"\n",T,"\n")
        G=input()
        if G=="0":
            i,b=float(input("i-?\n")),input("в чём данные? \n 0 - бит\n 1 - байт\n 2 - килобайт\n 3 - мегабайт\n 4 - гигабайт\n")
            print(2**perevod(i,b))
        if G=="1":
            N=input("N-?\n")
            i,b1=input("i-?\n"),input("в чём данные? \n 0 - бит\n 1 - байт\n 2 - килобайт\n 3 - мегабайт\n 4 - гигабайт\n")
            T=float(input("T-?\n"))
            V,b2=float(input("V-?\n")),input("в чём данные? \n 0 - бит\n 1 - байт\n 2 - килобайт\n 3 - мегабайт\n 4 - гигабайт\n")
            if i =="":
                print(perevod(V,b2)/(it(int(N))*T))
            else:
                print(perevod(V,b2)/(perevod(i,b1)*T))
        if G=="2":
            D=float(input("D-?\n"))
            i,b1=input("i-?\n"),input("в чём данные? \n 0 - бит\n 1 - байт\n 2 - килобайт\n 3 - мегабайт\n 4 - гигабайт\n")
            N=input("N-?\n")
            T=float(input("T-?\n"))
            if i =="":
                print(D*(it(int(N))*T))
            else:
                print(D*(perevod(i,b1)*T))
        if G=="3":
            N=input("N-?\n")
            T=float(input("T-?\n"))
            V,b2=float(input("V-?\n")),input("в чём данные? \n 0 - бит\n 1 - байт\n 2 - килобайт\n 3 - мегабайт\n 4 - гигабайт\n")
            D=float(input("D-?\n"))
            if N=="":
                otvet(perevod(V,b2)/(D*T))
            else:
                otvet(it(int(N)))
        if G=="4":
            N=input("N-?\n")
            i,b1=input("i-?\n"),input("в чём данные? \n 0 - бит\n 1 - байт\n 2 - килобайт\n 3 - мегабайт\n 4 - гигабайт\n")
            V,b2=float(input("V-?\n")),input("в чём данные? \n 0 - бит\n 1 - байт\n 2 - килобайт\n 3 - мегабайт\n 4 - гигабайт\n")
            D=float(input("D-?\n"))
            if i =="":
                otvet(perevod(V,b2)/(perevod(i,b1)*D))
            else:
                otvet(perevod(V,b2)/(it(int(N))*D))
    def isobr():
        N ="0 - количество цветов в политре(N), "
        H ="1 - высота изображения(H), "
        W ="2 - ширина изображения(W), "
        i ="3 - глубина текста(i), "
        I ="4 - инф объём изобр(ажения(I), "
        print("Что нужно найти?\n",N,"\n",H,"\n",W,"\n",i,"\n",I,"\n")
        G=input()
        if G=="0":
            i,b1=input("i-?\n"),input("в чём данные? \n 0 - бит\n 1 - байт\n 2 - килобайт\n 3 - мегабайт\n 4 - гигабайт\n")
            print(2**perevod(i,b1))
        if G=="1":
            i,b1=input("i-?\n"),input("в чём данные? \n 0 - бит\n 1 - байт\n 2 - килобайт\n 3 - мегабайт\n 4 - гигабайт\n")
            N=input("N-?\n")
            W=int(input("W-?\n"))
            I,b2=float(input("I-?\n")),input("в чём данные? \n 0 - бит\n 1 - байт\n 2 - килобайт\n 3 - мегабайт\n 4 - гигабайт\n")
            if i=="":
                print(perevod(I,b2)/(it(int(N))*W))
            else:
                print(perevod(I,b2)/(perevod(i,b1)*W))
        if G=="2":
            i,b1=input("i-?\n"),input("в чём данные? \n 0 - бит\n 1 - байт\n 2 - килобайт\n 3 - мегабайт\n 4 - гигабайт\n")
            N=input("N-?\n")
            H=int(input("H-?\n"))
            I,b2=float(input("I-?\n")),input("в чём данные? \n 0 - бит\n 1 - байт\n 2 - килобайт\n 3 - мегабайт\n 4 - гигабайт\n")
            if i=="":
                print(perevod(I,b2)/(it(int(N))*H))
            else:
                print(perevod(I,b2)/(perevod(i,b1)*H))
        if G=="3":
            N=input("N-?\n")
            W=int(input("W-?\n"))
            I,b2=float(input("I-?\n")),input("в чём данные? \n 0 - бит\n 1 - байт\n 2 - килобайт\n 3 - мегабайт\n 4 - гигабайт\n")
            N=input("N-?\n")
            if N=="":
                otvet(perevod(I,b2)/(H*W))
            else:
                otvet(it(int(N)))
        if G=="4":
            N=input("N-?\n")
            H=int(input("H-?\n"))
            W=int(input("W-?\n"))
            i,b1=input("i-?\n"),input("в чём данные? \n 0 - бит\n 1 - байт\n 2 - килобайт\n 3 - мегабайт\n 4 - гигабайт\n")
            if i =="":
                otvet(W*(it(int(N))*H))
            else:
                otvet(W*(perevod(i,b1)*H))
    print("Введите тип задачи,которую нужно решить? \n 1 - звук\n 2 - текст\n 3 - изображение")
    A=input()
    if A=="1":
        zvuk()
    if A=="2":
        pamyat()
    if A=="3":
        isobr()
f4()
