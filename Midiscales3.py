# -*- coding: utf-8 -*-

from midiutil import MIDIFile
import random as rr
import os
import pprint 

def minormaj(flag):
    if flag==0:
        return 'Min'
    if flag==1:
        return 'Maj'
    if flag==2:
        return 'Dim'
def notename(note):
    if note==57 or note==57+12 or note==57-12 or note==57-24 or note==57+24:
        return 'A'
    elif note==59 or note==59+12 or note==59-12 or note==59+24 or note==59-24:
        return 'B'
    elif note==60 or note==60+12 or note==60-12 or note==60+24 or note==60-24:
        return 'C'
    elif note==61 or note==61+12 or note==61-12 or note==61+24 or note==61-24:
        return 'C# or D#'
    elif note==62 or note==62+12 or note==62-12 or note==62+24 or note==62-24:
        return 'D'
    elif note==63 or note==63+12 or note==63-12 or note==63+24 or note==63-24:
        return 'D# or Eb'
    elif note==64 or note==64+12 or note==64-12 or note==64+24 or note==64-24:
        return 'E'
    elif note==65 or note==65+12 or note==65-12 or note==65+24 or note==65-24:
        return 'F'
    elif note==66 or note==66+12 or note==66-12 or note==66+24 or note==66-24:
        return 'F# or Gb'
    elif note==67 or note==67+12 or note==67-12 or note==67+24 or note==67-24:
        return 'G'
    elif note==68 or note==68+12 or note==68-12 or note==68+24 or note==68-24:
        return 'G# or Ab'
    elif note==70 or note==70+12 or note==70-12 or note==70+24 or note==70-24:
        return 'A# or Bb'
    else:
        return 'Pause'
    
def notefromname(note, a=0):
    if note=='C':
        return 60+(12*a)
    elif note=='C#' or note=='Db':
        return 61+(12*a)
    elif note=='D':
        return 62+(12*a)
    elif note=='D#' or note=='Eb':
        return 63+(12*a)
    elif note=='E':
        return 64+(12*a)
    elif note=='F':
        return 65+(12*a)
    elif note=='F#' or note=='Gb':
        return 66+(12*a)       
    elif note=='G':
        return 67+(12*a)
    elif note=='G#' or note=='Ab':
        return 68+(12*a)
    elif note=='A':
        return 69+(12*a)
    elif note=='A#' or note=='Bb':
        return 70+(12*a)
    elif note=='B':
        return 71+(12*a)
    
def majchord(tonic, track, trackbass, chan, chanbass, time, dur, vol=80, a=0):
    MyMIDI.addNote(track, chan, tonic+(12*a), time, dur*4, 80)
    MyMIDI.addNote(track, chan, tonic+4+(12*a), time, dur*4, 80)
    MyMIDI.addNote(track, chan, tonic+7+(12*a), time, dur*4, 80)
    MyMIDI.addNote(trackbass, chanbass, tonic-12, time, dur*4, 70)
    
def minchord(tonic, track, trackbass, chan, chanbass, time, dur, vol=80, a=0):
    MyMIDI.addNote(track, chan, tonic+(12*a), time, dur*4, 80)
    MyMIDI.addNote(track, chan, tonic+3+(12*a), time, dur*4, 80)
    MyMIDI.addNote(track, chan, tonic+7+(12*a), time, dur*4, 80)
    MyMIDI.addNote(trackbass, chanbass, tonic-12, time, dur*4, 70)
    
def dimchord(tonic, track, trackbass, chan, chanbass, time, dur, vol=80, a=0):
    MyMIDI.addNote(track, chan, tonic+(12*a), time, dur*4, 80)
    MyMIDI.addNote(track, chan, tonic+3+(12*a), time, dur*4, 80)
    MyMIDI.addNote(track, chan, tonic+6+(12*a), time, dur*4, 80)
    MyMIDI.addNote(trackbass, chanbass, tonic-12, time, dur*4, 70)
    
def tmajchord(tonic, track, trackbass, chan, chanbass, time, dur, vol=80, a=0):
    MyMIDI.addNote(track, chan, tonic+(12*a), time, dur*2, 80)
    MyMIDI.addNote(track, chan, tonic+4+(12*a), time, dur*2, 80)
    MyMIDI.addNote(track, chan, tonic+7+(12*a), time, dur*2, 80)
    MyMIDI.addNote(track, chan, tonic+(12*a), time+2, dur*2, 75)
    MyMIDI.addNote(track, chan, tonic+4+(12*a), time+2, dur*2, 75)
    MyMIDI.addNote(track, chan, tonic+7+(12*a), time+2, dur*2, 75)
    MyMIDI.addNote(trackbass, chanbass, tonic-12, time, dur*4, 70)
    
def tminchord(tonic, track, trackbass, chan, chanbass, time, dur, vol=80, a=0):
    MyMIDI.addNote(track, chan, tonic+(12*a), time, dur*2, 80)
    MyMIDI.addNote(track, chan, tonic+3+(12*a), time, dur*2, 80)
    MyMIDI.addNote(track, chan, tonic+7+(12*a), time, dur*2, 80)
    MyMIDI.addNote(track, chan, tonic+(12*a), time+2, dur*2, 75)
    MyMIDI.addNote(track, chan, tonic+3+(12*a), time+2, dur*2, 75)
    MyMIDI.addNote(track, chan, tonic+7+(12*a), time+2, dur*2, 75)
    MyMIDI.addNote(trackbass, chanbass, tonic-12, time, dur*4, 70)
    
def tdimchord(tonic, track, trackbass, chan, chanbass, time, dur, vol=80, a=0):
    MyMIDI.addNote(track, chan, tonic+(12*a), time, dur*2, 80)
    MyMIDI.addNote(track, chan, tonic+3+(12*a), time, dur*2, 80)
    MyMIDI.addNote(track, chan, tonic+6+(12*a), time, dur*2, 80)
    MyMIDI.addNote(track, chan, tonic+(12*a), time+2, dur*2, 75)
    MyMIDI.addNote(track, chan, tonic+3+(12*a), time+2, dur*2, 75)
    MyMIDI.addNote(track, chan, tonic+6+(12*a), time+2, dur*2, 75)
    MyMIDI.addNote(trackbass, chanbass, tonic-12, time, dur*4, 70)
    
degrees = [60, 62, 64, 65, 67, 69, 71, 72, 74]  # MIDI note number
degreeschords = [1, 0, 0, 1, 1, 0, 2]
track = 0
track1 = 1
track2 = 2
channel = 0
time = 0.0    # In beats
duration = 1.0    # In beats
tempo = 100  # In BPM
volume = 100  # 0-127, as per the MIDI standard
songdur=64
durtsd = [duration/2, duration, duration*(3/2), duration, duration*(3/2), duration, duration, duration*(3/2), duration*2, duration*2]
duroth = [duration/2, duration, duration/2, duration/2,duration/2, duration/2, duration/2, duration, duration]
subd=15
domin=15
tonic=25
tonicoct=75
pause=20
flag=0
choice=0
k=0
tonics=[]
prints=[]
instrumentgarm=0
settingsflag=0
settingsflag1=0
note=60
ritm=0
sdvig=0
filename=''
Garmony1='C Am F G' 
Garmony2='Am G F Dm' 
Garmony3='Am F C E'
path = 'Tracks' 
if not os.path.exists(path):
    os.makedirs(path)
while settingsflag==0:
    print("Выбери гармонию:")
    print(f"1 - {Garmony1}")
    print(f"2 - {Garmony2}")
    print(f"3 - {Garmony3}")
    print('50 - Случайная генерация квадрата + зацикливание')
    print('100 - Случайная генерация квадрата без его дальнейшего зацикливания. Общие тоника (I аккорд) и доминанта (IV аккорд).')
    print("0 - Настройки")
    Ngarmony=int(input())
    if Ngarmony==0:
        settingsflag1=0
        while settingsflag1==0:
            print("1 - Изменить темп")
            print("2 - Изменить длительность (количество тактов, кратно 16)")
            print("3 - Изменить вероятности выпадения TSD")
            print("4 - Изменить инструмент в гармонии")
            print("5 - Изменить тональность")
            print("6 - Закончить настройку")
            choice=int(input())
            if choice==1:
                print(f"Задайте новое значение темпа, текущее значение - {tempo}")
                tempo=int(input())
                print(f"Новое значение - {tempo}")
            elif choice==2:
                print(f"Задайте новую длительность (рекомендуется кратно 16), текущее значение - {songdur}")
                songdur=int(input())
            elif choice==3:
                print(f"Текущая вероятность выпадения I ст. - {tonic}%, IV ст. - {subd}%, V ст. - {domin}%")
                print(f"Никаких проверок, на свой страх и риск введите новые значения выпадения в соовтетствующем порядке (без значка %)")
                tonic=int(input())
                subd=int(input())
                domin=int(input())
                print(f"Текущая вероятность выпадения I ст. - {tonic}%, IV ст. - {subd}%, V ст. - {domin}%")
            elif choice==4:
                print(f"Введите число от 0 до 127. По умолчанию - 0 (acoustic piano)")
                instrumentgarm=int(input())
            elif choice==5:
                print('По умолчанию - До. Укажите смещение в полутонах, например "5" - на 5 полутонов выше, либо "-5" - на 5 полутонов ниже')
                ton=int(input())
                for i in range(len(degrees)):
                    degrees[i]=degrees[i]+ton
            elif choice==6:
                settingsflag1=1
    else:
        break
print('Выбери ритм аккомпанимента')
print('1 - Один аккорд на такт')
print('2 - Два одинаковых аккорда на такт')
#print('3 - Два различных аакорда на такт')
ritm=int(input())
if Ngarmony==2:
    print(f"Гармония: {Garmony2}. Выбери тонику (целое число от 1 до 8)")
elif Ngarmony==1:
    print(f"Гармония: {Garmony1}. Выбери тонику (целое число от 1 до 8)")
elif Ngarmony==3:
    print(f"Гармония: {Garmony3}. Выбери тонику (целое число от 1 до 8)")
print(f"1: C - До-мажор")
print(f"2: D - Ре-дорийский")
print(f"3: E - Ми-фригийский")
print(f"4: F - Фа-лидийский")
print(f"5: G - Соль-микролидийский")
print(f"6: A - Ля-минор")
print(f"7: B - Си-локрийский")
print(f"8: Сгенерировать все вышеперечисленное")
tonicchose=int(input())
if tonicchose==8:
    print('Можно повышать или понижать результат на полтона с каждой итерацией. Интересует?')
    print('1 - Нет, спасибо')
    print('2 - Повышай')
    print('3 - Понижай')
    sdvig=int(input())
if type(tonicchose) is int:
    j=0
    flag=1
    tonicnote=0
    tonicnote1=degrees[:len(degrees)-2]
    print(tonicnote1)
    input()
    while j<7:
        if tonicchose!=8:
            j=tonicchose-1
        if j!=0:
            if sdvig==2:
                for l in range(len(degrees)):
                    degrees[l]=degrees[l]+1
                tonicnote1=degrees[:len(degrees)-2]
                print(tonicnote1)
            elif sdvig==3:
                for l in range(len(degrees)):
                    degrees[l]=degrees[l]-3
                tonicnote1=degrees[:len(degrees)-2]
                print(tonicnote1)
        tonics.append(tonicnote1[j])
        flagrandchord=0
        time=0
        k=0
        if tonicnote1[j]==tonicnote1[3]:
            subdnote=tonicnote1[j]+6
            dominnote=tonicnote1[j]+7
            print("Это лидийский лад, поэтому я поменял кварту на тритон для субдоминанты")
        elif tonicnote1[j]==tonicnote1[6]:
            subdnote=tonicnote1[j]+5
            dominnote=tonicnote1[j]+6
            print("Это локрийский лад, поэтому я поменял квинту на тритон для доминанты")
        else:
            subdnote=tonicnote1[j]+5
            dominnote=tonicnote1[j]+7
        #prints.append(f"Тоника: {notename(tonicnote1[j])}, Субдоминанта: {notename(subdnote)}, Доминанта: {notename(dominnote)}")
        print(f"Тоника: {notename(tonicnote1[j])}, Субдоминанта: {notename(subdnote)}, Доминанта: {notename(dominnote)}")
        MyMIDI = MIDIFile(numTracks=3)
        MyMIDI.addTempo(track, time, tempo)
        MyMIDI.addTempo(track1, time, tempo)
        MyMIDI.addTempo(track2, time, tempo)
        MyMIDI.addProgramChange(0, 0, time, 0)
        MyMIDI.addProgramChange(1, 1, time, instrumentgarm)
        #MyMIDI.addProgramChange(0, 2, time, 117)
        i=0
        l=0
        lastdur=1
        while i<songdur:
            if Ngarmony==2:
                if ritm==1:
                    if i==0+k:
                        minchord(tonicnote1[5], track1, track, 1, 2, i, duration)
                    if i==4+k:
                        majchord(tonicnote1[4], track1, track, 1, 2, i, duration)
                    if i==8+k:
                        majchord(tonicnote1[3], track1, track, 1, 2, i, duration)
                    if i==12+k:
                        minchord(tonicnote1[1], track1, track, 1, 2, i, duration)
                        k=k+16
                    if time>=songdur-1:
                        i=i+1
                        continue
                if ritm==2:
                    if i==0+k:
                        tminchord(tonicnote1[5], track1, track, 1, 2, i, duration)
                    if i==4+k:
                        tmajchord(tonicnote1[4], track1, track, 1, 2, i, duration)
                    if i==8+k:
                        tmajchord(tonicnote1[3], track1, track, 1, 2, i, duration)
                    if i==12+k:
                        tminchord(tonicnote1[1], track1, track, 1, 2, i, duration)
                        k=k+16
                    if time>=songdur-1:
                        i=i+1
                        continue
            elif Ngarmony==1:
                if ritm==1:
                    if i==0+k:
                        majchord(tonicnote1[0]+12, track1, track, 1, 2, i, duration)
                    if i==4+k:
                        minchord(tonicnote1[5], track1, track, 1, 2, i, duration)
                    if i==8+k:
                        majchord(tonicnote1[3], track1, track, 1, 2, i, duration)
                    if i==12+k:
                        majchord(tonicnote1[4], track1, track, 1, 2, i, duration)
                        k=k+16
                    if time>=songdur-1:
                        i=i+1
                        continue
                if ritm==2:
                    if i==0+k:
                        tmajchord(tonicnote1[0]+12, track1, track, 1, 2, i, duration)
                    if i==4+k:
                        tminchord(tonicnote1[5], track1, track, 1, 2, i, duration)
                    if i==8+k:
                        tmajchord(tonicnote1[3], track1, track, 1, 2, i, duration)
                    if i==12+k:
                        tmajchord(tonicnote1[4], track1, track, 1, 2, i, duration)
                        k=k+16
                    if time>=songdur-1:
                        i=i+1
                        continue 
            elif Ngarmony==3:
                if ritm==1:
                    if i==0+k:
                        minchord(tonicnote1[5], track1, track, 1, 2, i, duration)
                    if i==4+k:
                        majchord(tonicnote1[3], track1, track, 1, 2, i, duration)
                    if i==8+k:
                        majchord(tonicnote1[0], track1, track, 1, 2, i, duration)
                    if i==12+k:
                        majchord(tonicnote1[2], track1, track, 1, 2, i, duration)
                        k=k+16
                    if time>=songdur-1:
                        i=i+1
                        continue
                if ritm==2:
                    if i==0+k:
                        tminchord(tonicnote1[5], track1, track, 1, 2, i, duration)
                    if i==4+k:
                        tmajchord(tonicnote1[3], track1, track, 1, 2, i, duration)
                    if i==8+k:
                        tmajchord(tonicnote1[0], track1, track, 1, 2, i, duration)
                    if i==12+k:
                        tmajchord(tonicnote1[2], track1, track, 1, 2, i, duration)
                        k=k+16
                    if time>=songdur-1:
                        i=i+1
                        continue
            elif Ngarmony==50:
                if flagrandchord==0:
                    randton1=rr.randint(0, len(tonicnote1)-2)
                    randchord1=tonicnote1[randton1]
                    randton2=rr.randint(0, len(tonicnote1)-2)
                    randchord2=tonicnote1[randton2]
                    flagrandchord=1
                if ritm==1:
                    if i==0+k:
                        if degreeschords[j]==0:
                            minchord(tonicnote1[j], track1, track, 1, 2, i, duration)
                            print(f"Chord, {i}, {notename(tonicnote1[j])}, {minormaj(degreeschords[j])}")
                            prints.append(f"Chord,{i}, {notename(tonicnote1[j])}, {minormaj(degreeschords[j])}")
                        elif degreeschords[j]==1:
                            majchord(tonicnote1[j], track1, track, 1, 2, i, duration)
                            print(f"Chord, {i}, {notename(tonicnote1[j])}, {minormaj(degreeschords[j])}")
                            prints.append(f"Chord,{i}, {notename(tonicnote1[j])}, {minormaj(degreeschords[j])}")
                        elif degreeschords[j]==2:
                            dimchord(tonicnote1[j], track1, track, 1, 2, i, duration)
                            print(f"Chord, {i}, {notename(tonicnote1[j])}, {minormaj(degreeschords[j])}")
                            prints.append(f"Chord,{i}, {notename(tonicnote1[j])}, {minormaj(degreeschords[j])}")
                    if i==4+k:
                        if degreeschords[randton1]==0:
                            minchord(randchord1, track1, track, 1, 2, i, duration)
                            print(f"Chord, {i}, {notename(randchord1)}, {minormaj(degreeschords[randton1])}")
                            prints.append(f"Chord,{i}, {notename(randchord1)}, {minormaj(degreeschords[randton1])}")
                        elif degreeschords[randton1]==1:
                            majchord(randchord1, track1, track, 1, 2, i, duration)
                            print(f"Chord, {i}, {notename(randchord1)}, {minormaj(degreeschords[randton1])}")
                            prints.append(f"Chord,{i}, {notename(randchord1)}, {minormaj(degreeschords[randton1])}")
                        elif degreeschords[randton1]==2:
                            dimchord(randchord1, track1, track, 1, 2, i, duration)
                            print(f"Chord, {i}, {notename(randchord1)}, {minormaj(degreeschords[randton1])}")
                            prints.append(f"Chord,{i}, {notename(randchord1)}, {minormaj(degreeschords[randton1])}")
                    if i==8+k:
                        if degreeschords[randton2]==0:
                            minchord(randchord2, track1, track, 1, 2, i, duration)
                            print(f"Chord, {i}, {notename(randchord2)}, {minormaj(degreeschords[randton2])}")
                            prints.append(f"Chord,{i}, {notename(randchord2)}, {minormaj(degreeschords[randton2])}")
                        elif degreeschords[randton2]==1:
                            majchord(randchord2, track1, track, 1, 2, i, duration)
                            print(f"Chord, {i}, {notename(randchord2)}, {minormaj(degreeschords[randton2])}")
                            prints.append(f"Chord,{i}, {notename(randchord2)}, {minormaj(degreeschords[randton2])}")
                        elif degreeschords[randton2]==2:
                            dimchord(randchord2, track1, track, 1, 2, i, duration)
                            print(f"Chord, {i}, {notename(randchord2)}, {minormaj(degreeschords[randton2])}")
                            prints.append(f"Chord,{i}, {notename(randchord2)}, {minormaj(degreeschords[randton2])}")
                    if i==12+k:
                        majchord(dominnote, track1, track, 1, 2, i, duration)
                        print(f"Chord,{i}, {notename(dominnote)}, Maj")
                        k=k+16
                    if time>=songdur-1:
                        i=i+1
                        continue
                if ritm==2:
                    if i==0+k:
                        if degreeschords[j]==0:
                            tminchord(tonicnote1[j], track1, track, 1, 2, i, duration)
                            print(f"Chord,{i}, {notename(tonicnote1[j])}, {minormaj(degreeschords[j])}")
                            prints.append(f"Chord,{i}, {notename(tonicnote1[j])}, {minormaj(degreeschords[j])}")
                        elif degreeschords[j]==1:
                            tmajchord(tonicnote1[j], track1, track, 1, 2, i, duration)
                            print(f"Chord,{i}, {notename(tonicnote1[j])}, {minormaj(degreeschords[j])}")
                            prints.append(f"Chord,{i}, {notename(tonicnote1[j])}, {minormaj(degreeschords[j])}")
                        elif degreeschords[j]==2:
                            tdimchord(tonicnote1[j], track1, track, 1, 2, i, duration)
                            print(f"Chord,{i}, {notename(tonicnote1[j])}, {minormaj(degreeschords[j])}")
                            prints.append(f"Chord,{i}, {notename(tonicnote1[j])}, {minormaj(degreeschords[j])}")
                    if i==4+k:
                        if degreeschords[randton1]==0:
                            tminchord(randchord1, track1, track, 1, 2, i, duration)
                            print(f"Chord,{i}, {notename(randchord1)}, {minormaj(degreeschords[randton1])}")
                            prints.append(f"Chord,{i}, {notename(randchord1)}, {minormaj(degreeschords[randton1])}")
                        elif degreeschords[randton1]==1:
                            tmajchord(randchord1, track1, track, 1, 2, i, duration)
                            print(f"Chord,{i}, {notename(randchord1)}, {minormaj(degreeschords[randton1])}")
                            prints.append(f"Chord,{i}, {notename(randchord1)}, {minormaj(degreeschords[randton1])}")
                        elif degreeschords[randton1]==2:
                            tdimchord(randchord1, track1, track, 1, 2, i, duration)
                            print(f"Chord,{i}, {notename(randchord1)}, {minormaj(degreeschords[randton1])}")
                            prints.append(f"Chord,{i}, {notename(randchord1)}, {minormaj(degreeschords[randton1])}")
                    if i==8+k:
                        if degreeschords[randton2]==0:
                            tminchord(randchord2, track1, track, 1, 2, i, duration)
                            print(f"Chord,{i}, {notename(randchord2)}, {minormaj(degreeschords[randton2])}")
                            prints.append(f"Chord,{i}, {notename(randchord2)}, {minormaj(degreeschords[randton2])}")
                        elif degreeschords[randton2]==1:
                            tmajchord(randchord2, track1, track, 1, 2, i, duration)
                            print(f"Chord,{i}, {notename(randchord2)}, {minormaj(degreeschords[randton2])}")
                            prints.append(f"Chord,{i}, {notename(randchord2)}, {minormaj(degreeschords[randton2])}")
                        elif degreeschords[randton2]==2:
                            tdimchord(randchord2, track1, track, 1, 2, i, duration)
                            print(f"Chord,{i}, {notename(randchord2)}, {minormaj(degreeschords[randton2])}")
                            prints.append(f"Chord,{i}, {notename(randchord2)}, {minormaj(degreeschords[randton2])}")
                    if i==12+k:
                        tmajchord(dominnote, track1, track, 1, 2, i, duration)
                        print(f"Chord,{i}, {notename(dominnote)}, {minormaj(1)}")
                        prints.append(f"Chord,{i}, {notename(dominnote)}, {minormaj(1)}")
                        k=k+16
                    if time>=songdur-1:
                        i=i+1
                        continue
            elif Ngarmony==100:
                if ritm==1:
                    if i==0+k:
                        if degreeschords[j]==0:
                            minchord(tonicnote1[j], track1, track, 1, 2, i, duration)
                            print(f"Chord, {i}, {notename(tonicnote1[j])}, {minormaj(degreeschords[j])}")
                            prints.append(f"Chord,{i}, {notename(tonicnote1[j])}, {minormaj(degreeschords[j])}")
                        elif degreeschords[j]==1:
                            majchord(tonicnote1[j], track1, track, 1, 2, i, duration)
                            print(f"Chord, {i}, {notename(tonicnote1[j])}, {minormaj(degreeschords[j])}")
                            prints.append(f"Chord,{i}, {notename(tonicnote1[j])}, {minormaj(degreeschords[j])}")
                        elif degreeschords[j]==2:
                            dimchord(tonicnote1[j], track1, track, 1, 2, i, duration)
                            print(f"Chord, {i}, {notename(tonicnote1[j])}, {minormaj(degreeschords[j])}")
                            prints.append(f"Chord,{i}, {notename(tonicnote1[j])}, {minormaj(degreeschords[j])}")
                    if i==4+k:
                        randton=rr.randint(0, len(tonicnote1)-2)
                        randchord=tonicnote1[randton]
                        if degreeschords[randton]==0:
                            minchord(randchord, track1, track, 1, 2, i, duration)
                            print(f"Chord, {i}, {notename(randchord)}, {minormaj(degreeschords[randton])}")
                            prints.append(f"Chord,{i}, {notename(randchord)}, {minormaj(degreeschords[randton])}")
                        elif degreeschords[randton]==1:
                            majchord(randchord, track1, track, 1, 2, i, duration)
                            print(f"Chord, {i}, {notename(randchord)}, {minormaj(degreeschords[randton])}")
                            prints.append(f"Chord,{i}, {notename(randchord)}, {minormaj(degreeschords[randton])}")
                        elif degreeschords[randton]==2:
                            dimchord(randchord, track1, track, 1, 2, i, duration)
                            print(f"Chord, {i}, {notename(randchord)}, {minormaj(degreeschords[randton])}")
                            prints.append(f"Chord,{i}, {notename(randchord)}, {minormaj(degreeschords[randton])}")
                    if i==8+k:
                        randton=rr.randint(0, len(tonicnote1)-2)
                        randchord=tonicnote1[randton]
                        if degreeschords[randton]==0:
                            minchord(randchord, track1, track, 1, 2, i, duration)
                            print(f"Chord, {i}, {notename(randchord)}, {minormaj(degreeschords[randton])}")
                            prints.append(f"Chord,{i}, {notename(randchord)}, {minormaj(degreeschords[randton])}")
                        elif degreeschords[randton]==1:
                            majchord(randchord, track1, track, 1, 2, i, duration)
                            print(f"Chord, {i}, {notename(randchord)}, {minormaj(degreeschords[randton])}")
                            prints.append(f"Chord,{i}, {notename(randchord)}, {minormaj(degreeschords[randton])}")
                        elif degreeschords[randton]==2:
                            dimchord(randchord, track1, track, 1, 2, i, duration)
                            print(f"Chord, {i}, {notename(randchord)}, {minormaj(degreeschords[randton])}")
                            prints.append(f"Chord,{i}, {notename(randchord)}, {minormaj(degreeschords[randton])}")
                    if i==12+k:
                        majchord(dominnote, track1, track, 1, 2, i, duration)
                        print(f"Chord, {i}, {notename(dominnote)}, {minormaj(1)}")
                        prints.append(f"Chord,{i}, {notename(dominnote)}, {minormaj(1)}")
                        k=k+16
                    if time>=songdur-1:
                        i=i+1
                        continue
                if ritm==2:
                    if i==0+k:
                        if degreeschords[j]==0:
                            tminchord(tonicnote1[j], track1, track, 1, 2, i, duration)
                            print(f"Chord, {i}, {notename(tonicnote1[j])}, {minormaj(degreeschords[j])}")
                            prints.append(f"Chord,{i},{notename(tonicnote1[j])}, {minormaj(degreeschords[j])}")
                        elif degreeschords[j]==1:
                            tmajchord(tonicnote1[j], track1, track, 1, 2, i, duration)
                            print(f"Chord, {i}, {notename(tonicnote1[j])}, {minormaj(degreeschords[j])}")
                            prints.append(f"Chord,{i},{notename(tonicnote1[j])}, {minormaj(degreeschords[j])}")
                        elif degreeschords[j]==2:
                            tdimchord(tonicnote1[j], track1, track, 1, 2, i, duration)
                            print(f"Chord, {i}, {notename(tonicnote1[j])}, {minormaj(degreeschords[j])}")
                            prints.append(f"Chord,{i},{notename(tonicnote1[j])}, {minormaj(degreeschords[j])}")
                    if i==4+k:
                        randton=rr.randint(0, len(tonicnote1)-2)
                        randchord=tonicnote1[randton]
                        if degreeschords[randton]==0:
                            tminchord(randchord, track1, track, 1, 2, i, duration)
                            print(f"Chord, {i}, {notename(randchord)}, {minormaj(degreeschords[randton])}")
                            prints.append(f"Chord,{i}, {notename(randchord)}, {minormaj(degreeschords[randton])}")
                        elif degreeschords[randton]==1:
                            tmajchord(randchord, track1, track, 1, 2, i, duration)
                            print(f"Chord, {i}, {notename(randchord)}, {minormaj(degreeschords[randton])}")
                            prints.append(f"Chord,{i}, {notename(randchord)}, {minormaj(degreeschords[randton])}")
                        elif degreeschords[randton]==2:
                            tdimchord(randchord, track1, track, 1, 2, i, duration)
                            print(f"Chord, {i}, {notename(randchord)}, {minormaj(degreeschords[randton])}")
                            prints.append(f"Chord,{i}, {notename(randchord)}, {minormaj(degreeschords[randton])}")
                    if i==8+k:
                        randton=rr.randint(0, len(tonicnote1)-2)
                        randchord=tonicnote1[randton]
                        if degreeschords[randton]==0:
                            tminchord(randchord, track1, track, 1, 2, i, duration)
                            print(f"Chord, {i}, {notename(randchord)}, {minormaj(degreeschords[randton])}")
                            prints.append(f"Chord,{i}, {notename(randchord)}, {minormaj(degreeschords[randton])}")
                        elif degreeschords[randton]==1:
                            tmajchord(randchord, track1, track, 1, 2, i, duration)
                            print(f"Chord, {i}, {notename(randchord)}, {minormaj(degreeschords[randton])}")
                            prints.append(f"Chord,{i}, {notename(randchord)}, {minormaj(degreeschords[randton])}")
                        elif degreeschords[randton]==2:
                            tdimchord(randchord, track1, track, 1, 2, i, duration)
                            print(f"Chord, {i}, {notename(randchord)}, {minormaj(degreeschords[randton])}")
                            prints.append(f"Chord,{i}, {notename(randchord)}, {minormaj(degreeschords[randton])}")
                    if i==12+k:
                        tmajchord(dominnote, track1, track, 1, 2, i, duration)
                        print(f"Chord, {i}, {notename(dominnote)}, {minormaj(1)}")
                        prints.append(f"Chord,{i}, {notename(dominnote)}, {minormaj(1)}")
                        k=k+16
                    if time>=songdur-1:
                        i=i+1
                        continue
                
            randnote=rr.randint(0,len(degrees)-1)
            randdur=rr.randint(0,len(durtsd)-1)
            randduroth=rr.randint(0,len(duroth)-1)
            randtonic=rr.randint(1,100)
            randoct=rr.randint(1,100)
            randpause=rr.randint(1,100)
                
            if l==1:
                if randpause<=pause:
                    ran=rr.randint(0,len(durtsd)-1)
                    time=time+lastdur
                   # MyMIDI.addNote(track, channel, degrees[0], time, duroth[randduroth], 100)
                    print(f"Note, {time}, pause, Длительность: {durtsd[ran]}, Предыдущая длительность: {lastdur}, {randtonic}")
                    prints.append(f"Note,{time}, pause, Длительность: {durtsd[ran]}, Предыдущая длительность: {lastdur}, {randtonic}")
#                    lastdur=durtsd[randdur]
                    lastdur=durtsd[ran]                    
                l=0
            if randtonic<=tonic:
                if randoct<=tonicoct:
                    note=tonicnote1[j]
                else:
                    note=tonicnote1[j]+12
                time=time+lastdur
                ran=rr.randint(0,len(durtsd)-1)
                MyMIDI.addNote(track, channel, note, time, durtsd[ran], rr.randint(90,100))
                print(f"Note, {time}, Нота: {notename(note)}, Длительность: {durtsd[ran]}, Предыдущая длительность: {lastdur}, {randtonic}")
                prints.append(f"Note,{time}, Нота: {notename(note)}, Длительность: {durtsd[ran]}, Предыдущая длительность: {lastdur}, {randtonic}")
#                    lastdur=durtsd[randdur]
                lastdur=durtsd[ran]
                l=1              
            else:
                if randtonic>tonic and randtonic<=(tonic+domin):
                    note=dominnote
                    time=time+lastdur
                    ran=rr.randint(0,len(durtsd)-1)
                    MyMIDI.addNote(track, channel, note, time, durtsd[ran], rr.randint(80,95))
                    print(f"Note, {time}, Нота: {notename(note)}, Длительность: {durtsd[ran]}, Предыдущая длительность: {lastdur}, {randtonic}")
                    prints.append(f"Note,{time}, Нота: {notename(note)}, Длительность: {durtsd[ran]}, Предыдущая длительность: {lastdur}, {randtonic}")
                    lastdur=durtsd[ran]
                    l=1
                    
                    
                else:
                    if randtonic>(tonic+domin) and randtonic<=(tonic+domin+subd):
                        note=subdnote
                        time=time+lastdur
                        ran=rr.randint(0,len(durtsd)-1)
                        MyMIDI.addNote(track, channel, note, time, durtsd[ran], rr.randint(80,95))
                        print(f"Note, {time}, Нота: {notename(note)}, Длительность: {durtsd[ran]}, Предыдущая длительность: {lastdur}, {randtonic}")
                        prints.append(f"Note,{time}, Нота: {notename(note)}, Длительность: {durtsd[ran]}, Предыдущая длительность: {lastdur}, {randtonic}")
                        lastdur=durtsd[ran]
                        
                    else:
                        time=time+lastdur
                        while degrees[randnote]==tonicnote1[j] or degrees[randnote]==subdnote or degrees[randnote]==dominnote:
                            randnote=rr.randint(0,len(degrees)-1)
                        MyMIDI.addNote(track, channel, degrees[randnote], time, duroth[randduroth], rr.randint(70,90)) 
                        print(f"Note, {time}, Нота: {notename(degrees[randnote])}, Длительность: {duroth[randduroth]}, Предыдущая длительность: {lastdur}, {randtonic}")
                        prints.append(f"Note,{time}, Нота: {notename(degrees[randnote])}, Длительность: {duroth[randduroth]}, Предыдущая длительность: {lastdur}, {randtonic}")
                        lastdur=duroth[randduroth]
                                  
            i=i+1
        while i<(songdur+1):
            if Ngarmony==2:
                minchord(tonicnote1[5], track1, track, 1, 2, i, duration)
                i=i+1
            elif Ngarmony==1:
                majchord(tonicnote1[0]+12, track1, track, 1, 2, i, duration)
                i=i+1
            elif Ngarmony==3:
                minchord(tonicnote1[5], track1, track, 1, 2, i, duration)
                i=i+1
            elif Ngarmony==100 or Ngarmony==50:
                if degreeschords[j]==0:
                    minchord(tonicnote1[j], track1, track, 1, 2, i, duration)
                    print(f"Chord, {i}, {notename(tonicnote1[j])}, {minormaj(degreeschords[j])}")
                    prints.append(f"Chord,{i}, {notename(tonicnote1[j])}, {minormaj(degreeschords[j])}")
                elif degreeschords[j]==1:
                    majchord(tonicnote1[j], track1, track, 1, 2, i, duration)
                    print(f"Chord, {i}, {notename(tonicnote1[j])}, {minormaj(degreeschords[j])}")
                    prints.append(f"Chord,{i}, {notename(tonicnote1[j])}, {minormaj(degreeschords[j])}")
                elif degreeschords[j]==2:
                    minchord(tonicnote1[j]-2, track1, track, 1, 2, i, duration)
                    print(f"Chord, {i}, {notename(tonicnote1[j])}, {minormaj(degreeschords[j])}")
                    prints.append(f"Chord,{i}, {notename(tonicnote1[j])}, {minormaj(degreeschords[j])}")
                i=i+1
        for l in range(len(prints)):
            prints[l] = prints[l].split(',')
        prints.sort(key= lambda x: float(x[1]))
        for l in range(len(prints)):
            prints[l][0]=prints[l][0]+' '
        pprint.pprint(prints)
        #print(prints)
        if j==0:
            with open(f"Tracks/{j} - {notename(tonicnote1[j])}-major.mid", "wb") as output_file:
                MyMIDI.writeFile(output_file)
            with open(f"Tracks/{j} - {notename(tonicnote1[j])}-major.txt", "w") as textfile:
                for l in range(len(prints)):
                    textfile.writelines(prints[l])
                    textfile.write('\n')
            prints=[]
        elif j==1:
            with open(f"Tracks/{j} - {notename(tonicnote1[j])}-dorian.mid", "wb") as output_file:
                MyMIDI.writeFile(output_file)
            with open(f"Tracks/{j} - {notename(tonicnote1[j])}-dorian.txt", "w") as textfile:
                for l in range(len(prints)):
                    textfile.writelines(prints[l])
                    textfile.write('\n')
            prints=[]
        elif j==2:
            with open(f"Tracks/{j} - {notename(tonicnote1[j])}-phrygian.mid", "wb") as output_file:
                MyMIDI.writeFile(output_file)
            with open(f"Tracks/{j} - {notename(tonicnote1[j])}-phrygian.txt", "w") as textfile:
                for l in range(len(prints)):
                    textfile.writelines(prints[l])
                    textfile.write('\n')
            prints=[]
        elif j==3:
            with open(f"Tracks/{j} - {notename(tonicnote1[j])}-lydian.mid", "wb") as output_file:
                MyMIDI.writeFile(output_file)
            with open(f"Tracks/{j} - {notename(tonicnote1[j])}-lydian.txt", "w") as textfile:
                for l in range(len(prints)):
                    textfile.writelines(prints[l])
                    textfile.write('\n')
            prints=[]
        elif j==4:
            with open(f"Tracks/{j} - {notename(tonicnote1[j])}-mixolydian.mid", "wb") as output_file:
                MyMIDI.writeFile(output_file)
            with open(f"Tracks/{j} - {notename(tonicnote1[j])}-mixolydian.txt", "w") as textfile:
                for l in range(len(prints)):
                    textfile.writelines(prints[l])
                    textfile.write('\n')
            prints=[]
        elif j==5:
            with open(f"Tracks/{j} - {notename(tonicnote1[j])}-minor.mid", "wb") as output_file:
                MyMIDI.writeFile(output_file)
            with open(f"Tracks/{j} - {notename(tonicnote1[j])}-minor.txt", "w") as textfile:
                for l in range(len(prints)):
                    textfile.writelines(prints[l])
                    textfile.write('\n')
            prints=[]
        elif j==6:
            with open(f"Tracks/{j} - {notename(tonicnote1[j])}-locrian.mid", "wb") as output_file:
                MyMIDI.writeFile(output_file)
            with open(f"Tracks/{j} - {notename(tonicnote1[j])}-locrian.txt", "w") as textfile:
                for l in range(len(prints)):
                    textfile.writelines(prints[l])
                    textfile.write('\n')
            prints=[]
        j=j+1
        print()
        if tonicchose!=8:
            break