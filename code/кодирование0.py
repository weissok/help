def f0():
    import math

    def menu11_resh(I,K,i,N,sel):
        otvet=0
        if sel==1:
            
            if K>0 and i>0:
                I=K*i
                form='I= K * i'
            elif K>0 and N>0:
                I=K*math.log2(N)
                form='I= K * log2(N)'
            otvet=I
            ed_izm='бит'

            
        if sel==2:
            if I>0 and i>0:
                K=I/i
                form='K=I/i'
            elif I>0 and N>0:
                K=I/math.log2(N)
                form='K=I/log2(N)'
            otvet=K
            ed_izm='символов'

        
        if sel==3:
            if I>0 and K>0:
                i=I/K
                form='i=I/K'
            elif N>0:
                i=math.log2(N)
                form='i=log2(N)'
            otvet=i
            ed_izm='бит'


        if sel==4:
            if I>0 and K>0:
                N=2**(I/K)
                form='N=2^(I/K)'
            elif i>0:
                N=2**i
                form='N=2^i'
            otvet=N
            ed_izm='символов'


        print(f'\nОтвет: {form}={otvet} {ed_izm}\nЗадача решена. Хотите решить еще одну? Для этого нажмите 1')
        if input()=='1':
            f0()
        else:
            print('выход')
            exit()
        

    def menu21_resh(V,p,N,sel):
        
        otvet=0
        if sel==1:
            if K>0 and i>0:
                I=K*i
                form='I= K * i'
            elif K>0 and N>0:
                I=K*math.log2(N)
                form='I= K * log2(N)'
            otvet=I
            ed_izm='бит'

        ed_izm='бит'
        print(f'\nОтвет: {form}={otvet} {ed_izm}\nЗадача решена. Хотите решить еще одну? Для этого нажмите 1')

    def menu31_resh(I,H,i,t,sel):
        
        otvet=20
        ed_izm='бит'
        print(f'\nОтвет: {form}={otvet} {ed_izm}\nЗадача решена. Хотите решить еще одну? Для этого нажмите 1')


    def menu11(m1,m2,m3,m4,sel):
        sel2=0
        m5='Закончить ввод данных'
        if sel==1 or sel==3:
            menu=[m1,m2,m3,m4,m5]
        if sel==2:
            menu=[m1,m2,m3,m5],
          
        I=K=i=N=H=t=p=V=-1

        if sel==1 or sel==3:  crit=5
        elif sel==2: crit=4
            
        while sel2!=crit:
            print('\nВыберите, что вам известно (если вы ошибетесь с вводом данных, можно будет ввести их заново)\n')
            
            for n in range(crit):
                if n!=sel-1: print (f'{n+1}. {menu[n]}')
                else: print(f'{n+1}.Пункт активирован')

            sel2=int(input('Ваш выбор-'))
            velich1=['I=','K=','i=','N=']
            txt='Введите значение '
            n=int(1)
            
            if sel2!=sel:
                if sel2==n:  I=int(input(f'{txt} {velich1[0]}'))
                if sel2==n+1:K=int(input(f'{txt} {velich1[n]}'))
                if sel2==n+2:i=int(input(f'{txt} {velich1[n+1]}'))
                if sel2==n+3:N=int(input(f'{txt} {velich1[n+2]}'))
                if sel2==n+4:menu11_resh(I,K,i,N,sel)
            else:
                print('Этот пункт уже активирован!')
                input('Нажмите любую клавишу')
            

                
    def menu1():
        print(text)
        m1='I - информационный объем сообщения'
        m2='K - количество символов'
        m3='i - информационный вес символа'
        m4='N - мощность алфавита'
        
        print(f'''
    1. {m1}
    2. {m2}
    3. {m3}
    4. {m4}''')

        sel=int(input(vibor))
        print(f'Вы выбрали {select1[sel-1]}')
        menu11(m1,m2,m3,m4,sel)
            
        
    def menu2():
        print(text)
        m1='V - информационный объем изображения'
        m2='p (x,y) - количество пикселей'
        m3='n - информационный вес цвета (разрядность)'
        print(f'''
    1. {m1}
    2. {m2}
    3. {m3}''')
        sel=int(input(vibor))
        print(f'Вы выбрали {sel}')
        menu11(m1,m2,m3,m4,sel)

    def menu3():
        print(text)
        m1='I - информационный объем звукового файла'
        m2='H - частота дискретизации'
        m3='i - битовая губина кодирования'
        m4='t - время звучания'
        print(f'1. {m1}')
        print(f'2. {m2}')
        print(f'3. {m3}')
        print(f'4. {m4}')

        sel=int(input(vibor))
        print(f'Вы выбрали {sel}')
        menu11(m1,m2,m3,m4,sel)

    text='\nВыберите, что вам нужно найти\n'
    vibor='Ваш выбор-'
    otv='\nОтвет: {form}={otvet} {ed_izm}\nЗадача решена. Хотите решить еще одну? Для этого нажмите 1'
    m1=m2=m3=m4=''
    select1=['I','K','i','N']
    I=K=i=N=-1
    print('1. Кодирование информации\n2. Кодирование изображения\n3. Кодирование аудио')
    sel=int(input('Ваш выбор-'))
    if sel==1:
        menu1()
    if sel==2:
        menu2()
    if sel==3:
        menu3()

f0()





