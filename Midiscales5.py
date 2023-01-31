# -*- coding: utf-8 -*-

from midiutil import MIDIFile
import random as rr
import os
import pprint 
import subprocess
abspath = os.path.abspath(os.path.dirname(__file__))
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

def arpmajchord(tonic, track, trackbass, chan, chanbass, time, dur, vol=70, a=-1):
    MyMIDI.addNote(track, chan, tonic+(12*a), time, dur, rr.randint(60,80))
    MyMIDI.addNote(track, chan, tonic+4+(12*a), time+1+rr.uniform(0.98, 1.02), dur, rr.randint(60,80))
    MyMIDI.addNote(track, chan, tonic+7+(12*a), time+1*2+rr.uniform(0.98, 1.02), dur, rr.randint(60,80))
    MyMIDI.addNote(track, chan, tonic+4+(12*a), time+1*3+rr.uniform(0.98, 1.02), dur, rr.randint(60,80))

def arpminchord(tonic, track, trackbass, chan, chanbass, time, dur, vol=70, a=-1):
    MyMIDI.addNote(track, chan, tonic+(12*a), time, dur, rr.randint(60,80))
    MyMIDI.addNote(track, chan, tonic+3+(12*a), time+1+rr.uniform(0.98, 1.02), dur, rr.randint(60,80))
    MyMIDI.addNote(track, chan, tonic+7+(12*a), time+1*2+rr.uniform(0.98, 1.02), dur, rr.randint(60,80))
    MyMIDI.addNote(track, chan, tonic+3+(12*a), time+1*3+rr.uniform(0.98, 1.02), dur, rr.randint(60,80))

def arpdimchord(tonic, track, trackbass, chan, chanbass, time, dur, vol=70, a=-1):
    MyMIDI.addNote(track, chan, tonic+(12*a), time, dur, rr.randint(60,80))
    MyMIDI.addNote(track, chan, tonic+3+(12*a), time+1+rr.uniform(0.98, 1.02), dur, rr.randint(60,80))
    MyMIDI.addNote(track, chan, tonic+6+(12*a), time+1*2+rr.uniform(0.98, 1.02), dur, rr.randint(60,80))
    MyMIDI.addNote(track, chan, tonic+3+(12*a), time+1*3+rr.uniform(0.98, 1.02), dur, rr.randint(60,80))  
    
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
durtsd = [duration, duration, duration*(3/2), duration, duration*(3/2), duration, duration, duration*(3/2), duration*2, duration*2]
duroth = [duration/2, duration/2, duration/2, duration/2,duration/2, duration/2, duration/2, duration, duration]
tonic1=20
subd1=15
domin1=15
subd=15
domin=15
tonic=20
tonicoct=97
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
lastnote=0
streamcheck=0
filename=''
Garmony1='C Am F G' 
Garmony2='Am G F Fm' 
Garmony3='Am F C E'
path = 'Tracks' 
if not os.path.exists(path):
    os.makedirs(path)
print('Choose your language:')
print('1 - English')
print('2 - Russian')
lang=int(input())
if lang!=1 and lang!=2:
    print("Uh... it'll be english anyway")
    lang=1
while settingsflag==0:
    if lang==2:
        print("Выбери гармонию:")
        print(f"1 - {Garmony1}")
        print(f"2 - {Garmony2}")
        print(f"3 - {Garmony3}")
        print('50 - Случайная генерация квадрата + зацикливание')
        print('100 - Случайная генерация квадрата без его дальнейшего зацикливания. Общие тоника (I аккорд) и доминанта (IV аккорд).')
        print('200 - Просто попробовать пример')
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
    if lang==1:
        print("Generated tracks will be created in the same directory as script. You will find it in 'Tracks' folder")
        print("Choose the harmony:")
        print(f"1 - {Garmony1}")
        print(f"2 - {Garmony2}")
        print(f"3 - {Garmony3}")
        print('50 - Random generation of chord square and cycle it')
        print('100 - Random generation of chords without any cycling. Have common chords: tonic (1st chord of square) and dominant (4th chord of square).')
        print('200 - Just try some example.')
        print("0 - Settings")
        Ngarmony=int(input())
        if Ngarmony==0:
            settingsflag1=0
            while settingsflag1==0:
                print("1 - Change tempo")
                print("2 - Change song duration (number of tact, multiple to 16)")
                print("3 - Change probability of getting TSD")
                print("4 - Change instrument in harmony")
                print("5 - Change tone")
                print("6 - Done and go ahead")
                choice=int(input())
                if choice==1:
                    print(f"Set new tempo, current value - {tempo}")
                    tempo=int(input())
                    print(f"New value - {tempo}")
                elif choice==2:
                    print(f"Set new duration (it's highly recomended to be multiple to 16), current value - {songdur}")
                    songdur=int(input())
                elif choice==3:
                    print(f"Current probablity to get I (tonic) - {tonic}%, IV (subdominant) - {subd}%, V (dominant) - {domin}%")
                    print(f"There is no type or value checking, do it as you want. Tonic probability checks first, if you set e.g. 20000 then there is always be tonic, it's like 100%. Set new values in order pressing Enter everytime (without '%')")
                    tonic=int(input())
                    subd=int(input())
                    domin=int(input())
                    print(f"Current probability I - {tonic}%, IV - {subd}%, V - {domin}%")
                elif choice==4:
                    print(f"Type the number from 0 to 127. Default - 0 (acoustic piano). And actually it's the best choice")
                    instrumentgarm=int(input())
                elif choice==5:
                    print('Default - C. Set the bias in semitones, e.g. "5" - 5 semitones higher, or "-5" - 5 semitones lower')
                    ton=int(input())
                    for i in range(len(degrees)):
                        degrees[i]=degrees[i]+ton
                elif choice==6:
                    settingsflag1=1
        else:
            break
if Ngarmony!=200:
    if lang==2:
        print('Выбери ритм аккомпанимента')
        print('1 - Один аккорд на такт')
        print('2 - Два одинаковых аккорда на такт')
        print('3 - Арпеджиируй')
    if lang==1:
        print('Choose rythm of harmony. Have only 2 right now, maybe soon')
        print('1 - 1 chord in tact')
        print('2 - 2 same chords in tact')
    #print('3 - Два различных аакорда на такт')
    ritm=int(input())
    if lang==2:
        if Ngarmony==2:
            print(f"Гармония: {Garmony2}. Выбери тонику (целое число от 1 до 8)")
        elif Ngarmony==1:
            print(f"Гармония: {Garmony1}. Выбери тонику (целое число от 1 до 8)")
        elif Ngarmony==3:
            print(f"Гармония: {Garmony3}. Выбери тонику (целое число от 1 до 8)")
        elif Ngarmony==50:
            print(f"Гармония: Случайная с зацикливанием. Выбери тонику (целое число от 1 до 8)")
        elif Ngarmony==100:
            print(f"Гармония: Случайная каждый квадрат. Выбери тонику (целое число от 1 до 8)")
        print(f"1: C - До-мажор")
        print(f"2: D - Ре-дорийский")
        print(f"3: E - Ми-фригийский")
        print(f"4: F - Фа-лидийский")
        print(f"5: G - Соль-микролидийский")
        print(f"6: A - Ля-минор")
        print(f"7: B - Си-локрийский")
        print(f"8: Сгенерировать все вышеперечисленное")
    if lang==1:
        if Ngarmony==2:
            print(f"Harmony: {Garmony2}. Chose the tonic (integer from 1 to 8)")
        elif Ngarmony==1:
            print(f"Harmony: {Garmony1}. Chose the tonic (integer from 1 to 8)")
        elif Ngarmony==3:
            print(f"Harmony: {Garmony3}. Chose the tonic (integer from 1 to 8)")
        elif Ngarmony==50:
            print(f"Harmony: Random with cycle. Chose the tonic (integer from 1 to 8)")
        elif Ngarmony==100:
            print(f"Harmony: Random every square. Chose the tonic (integer from 1 to 8)")
        print(f"1: C-major")
        print(f"2: D-dorian")
        print(f"3: E-phrygian")
        print(f"4: F-lydian")
        print(f"5: G-mixolydian")
        print(f"6: A-minor")
        print(f"7: B-locrian")
        print(f"8: Generate all the stuff")
        
    tonicchose=int(input())
    if tonicchose==8:
        if lang==2:
            print('Можно повышать или понижать результат на полтона с каждой итерацией. Интересует?')
            print('1 - Нет, спасибо')
            print('2 - Повышай')
            print('3 - Понижай')
        if lang==1:
            print('I can generate lower and higher to semitone with every iteration, do you instrested in?')
            print('1 - No, thanks')
            print('2 - Make it higher')
            print('3 - Make it lower')
        sdvig=int(input())
elif Ngarmony==200:
    ritm=1
    tonicchose=8
    sdvig=3      
    Ngarmony=1
if type(tonicchose) is int:
    j=0
    flag=1
    tonicnote=0
    tonicnote1=degrees[:len(degrees)-2]
    print(tonicnote1)
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
            #print("Это лидийский лад, поэтому я поменял кварту на тритон для субдоминанты")
        elif tonicnote1[j]==tonicnote1[6]:
            subdnote=tonicnote1[j]+5
            dominnote=tonicnote1[j]+6
            #print("Это локрийский лад, поэтому я поменял квинту на тритон для доминанты")
        else:
            subdnote=tonicnote1[j]+5
            dominnote=tonicnote1[j]+7
        #prints.append(f"Тоника: {notename(tonicnote1[j])}, Субдоминанта: {notename(subdnote)}, Доминанта: {notename(dominnote)}")
        if lang==2:
            print(f"Тоника: {notename(tonicnote1[j])}, Субдоминанта: {notename(subdnote)}, Доминанта: {notename(dominnote)}")
        if lang==1:
            print(f"Tonic: {notename(tonicnote1[j])}, Subdominant: {notename(subdnote)}, Dominant: {notename(dominnote)}")
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
                        minchord(tonicnote1[3], track1, track, 1, 2, i, duration)
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
                        tminchord(tonicnote1[3], track1, track, 1, 2, i, duration)
                        k=k+16
                    if time>=songdur-1:
                        i=i+1
                        continue
                if ritm==3:
                    if i==0+k:
                        arpminchord(tonicnote1[5], track1, track, 1, 2, i, duration)
                    if i==4+k:
                        arpmajchord(tonicnote1[4], track1, track, 1, 2, i, duration)
                    if i==8+k:
                        arpmajchord(tonicnote1[3], track1, track, 1, 2, i, duration)
                    if i==12+k:
                        arpminchord(tonicnote1[3], track1, track, 1, 2, i, duration)
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
                if ritm==3:
                    if i==0+k:
                        arpmajchord(tonicnote1[0]+12, track1, track, 1, 2, i, duration)
                    if i==4+k:
                        arpminchord(tonicnote1[5], track1, track, 1, 2, i, duration)
                    if i==8+k:
                        arpmajchord(tonicnote1[3], track1, track, 1, 2, i, duration)
                    if i==12+k:
                        arpmajchord(tonicnote1[4], track1, track, 1, 2, i, duration)
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
                if ritm==2:
                    if i==0+k:
                        arpminchord(tonicnote1[5], track1, track, 1, 2, i, duration)
                    if i==4+k:
                        arpmajchord(tonicnote1[3], track1, track, 1, 2, i, duration)
                    if i==8+k:
                        arpmajchord(tonicnote1[0], track1, track, 1, 2, i, duration)
                    if i==12+k:
                        arpmajchord(tonicnote1[2], track1, track, 1, 2, i, duration)
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
                            prints.append(f"Chord,{i}, {tonicnote1[j]}-{notename(tonicnote1[j])}, {minormaj(degreeschords[j])}")
                        elif degreeschords[j]==1:
                            majchord(tonicnote1[j], track1, track, 1, 2, i, duration)
                            print(f"Chord, {i}, {notename(tonicnote1[j])}, {minormaj(degreeschords[j])}")
                            prints.append(f"Chord,{i}, {tonicnote1[j]}-{notename(tonicnote1[j])}, {minormaj(degreeschords[j])}")
                        elif degreeschords[j]==2:
                            dimchord(tonicnote1[j], track1, track, 1, 2, i, duration)
                            print(f"Chord, {i}, {notename(tonicnote1[j])}, {minormaj(degreeschords[j])}")
                            prints.append(f"Chord,{i}, {tonicnote1[j]}-{notename(tonicnote1[j])}, {minormaj(degreeschords[j])}")
                    if i==4+k:
                        if degreeschords[randton1]==0:
                            minchord(randchord1, track1, track, 1, 2, i, duration)
                            print(f"Chord, {i}, {notename(randchord1)}, {minormaj(degreeschords[randton1])}")
                            prints.append(f"Chord,{i}, {randchord1}-{notename(randchord1)}, {minormaj(degreeschords[randton1])}")
                        elif degreeschords[randton1]==1:
                            majchord(randchord1, track1, track, 1, 2, i, duration)
                            print(f"Chord, {i}, {notename(randchord1)}, {minormaj(degreeschords[randton1])}")
                            prints.append(f"Chord,{i}, {randchord1}-{notename(randchord1)}, {minormaj(degreeschords[randton1])}")
                        elif degreeschords[randton1]==2:
                            dimchord(randchord1, track1, track, 1, 2, i, duration)
                            print(f"Chord, {i}, {notename(randchord1)}, {minormaj(degreeschords[randton1])}")
                            prints.append(f"Chord,{i}, {randchord1}-{notename(randchord1)}, {minormaj(degreeschords[randton1])}")
                    if i==8+k:
                        if degreeschords[randton2]==0:
                            minchord(randchord2, track1, track, 1, 2, i, duration)
                            print(f"Chord, {i}, {notename(randchord2)}, {minormaj(degreeschords[randton2])}")
                            prints.append(f"Chord,{i}, {randchord2}-{notename(randchord2)}, {minormaj(degreeschords[randton2])}")
                        elif degreeschords[randton2]==1:
                            majchord(randchord2, track1, track, 1, 2, i, duration)
                            print(f"Chord, {i}, {notename(randchord2)}, {minormaj(degreeschords[randton2])}")
                            prints.append(f"Chord,{i}, {randchord2}-{notename(randchord2)}, {minormaj(degreeschords[randton2])}")
                        elif degreeschords[randton2]==2:
                            dimchord(randchord2, track1, track, 1, 2, i, duration)
                            print(f"Chord, {i}, {notename(randchord2)}, {minormaj(degreeschords[randton2])}")
                            prints.append(f"Chord,{i}, {randchord2}-{notename(randchord2)}, {minormaj(degreeschords[randton2])}")
                    if i==12+k:
                        majchord(dominnote, track1, track, 1, 2, i, duration)
                        print(f"Chord,{i}, {notename(dominnote)}, Maj")
                        prints.append(f"Chord,{i}, {dominnote}-{notename(dominnote)}, {minormaj(1)}")
                        k=k+16
                    if time>=songdur-1:
                        i=i+1
                        continue
                if ritm==2:
                    if i==0+k:
                        if degreeschords[j]==0:
                            tminchord(tonicnote1[j], track1, track, 1, 2, i, duration)
                            print(f"Chord,{i}, {notename(tonicnote1[j])}, {minormaj(degreeschords[j])}")
                            prints.append(f"Chord,{i}, {tonicnote1[j]}-{notename(tonicnote1[j])}, {minormaj(degreeschords[j])}")
                        elif degreeschords[j]==1:
                            tmajchord(tonicnote1[j], track1, track, 1, 2, i, duration)
                            print(f"Chord,{i}, {notename(tonicnote1[j])}, {minormaj(degreeschords[j])}")
                            prints.append(f"Chord,{i}, {tonicnote1[j]}-{notename(tonicnote1[j])}, {minormaj(degreeschords[j])}")
                        elif degreeschords[j]==2:
                            tdimchord(tonicnote1[j], track1, track, 1, 2, i, duration)
                            print(f"Chord,{i}, {notename(tonicnote1[j])}, {minormaj(degreeschords[j])}")
                            prints.append(f"Chord,{i}, {tonicnote1[j]}-{notename(tonicnote1[j])}, {minormaj(degreeschords[j])}")
                    if i==4+k:
                        if degreeschords[randton1]==0:
                            tminchord(randchord1, track1, track, 1, 2, i, duration)
                            print(f"Chord,{i}, {notename(randchord1)}, {minormaj(degreeschords[randton1])}")
                            prints.append(f"Chord,{i}, {randchord1}-{notename(randchord1)}, {minormaj(degreeschords[randton1])}")
                        elif degreeschords[randton1]==1:
                            tmajchord(randchord1, track1, track, 1, 2, i, duration)
                            print(f"Chord,{i}, {notename(randchord1)}, {minormaj(degreeschords[randton1])}")
                            prints.append(f"Chord,{i}, {randchord1}-{notename(randchord1)}, {minormaj(degreeschords[randton1])}")
                        elif degreeschords[randton1]==2:
                            tdimchord(randchord1, track1, track, 1, 2, i, duration)
                            print(f"Chord,{i}, {notename(randchord1)}, {minormaj(degreeschords[randton1])}")
                            prints.append(f"Chord,{i}, {randchord1}-{notename(randchord1)}, {minormaj(degreeschords[randton1])}")
                    if i==8+k:
                        if degreeschords[randton2]==0:
                            tminchord(randchord2, track1, track, 1, 2, i, duration)
                            print(f"Chord,{i}, {notename(randchord2)}, {minormaj(degreeschords[randton2])}")
                            prints.append(f"Chord,{i}, {randchord2}-{notename(randchord2)}, {minormaj(degreeschords[randton2])}")
                        elif degreeschords[randton2]==1:
                            tmajchord(randchord2, track1, track, 1, 2, i, duration)
                            print(f"Chord,{i}, {notename(randchord2)}, {minormaj(degreeschords[randton2])}")
                            prints.append(f"Chord,{i}, {randchord2}-{notename(randchord2)}, {minormaj(degreeschords[randton2])}")
                        elif degreeschords[randton2]==2:
                            tdimchord(randchord2, track1, track, 1, 2, i, duration)
                            print(f"Chord,{i}, {notename(randchord2)}, {minormaj(degreeschords[randton2])}")
                            prints.append(f"Chord,{i}, {randchord2}-{notename(randchord2)}, {minormaj(degreeschords[randton2])}")
                    if i==12+k:
                        tmajchord(dominnote, track1, track, 1, 2, i, duration)
                        print(f"Chord,{i}, {notename(dominnote)}, {minormaj(1)}")
                        prints.append(f"Chord,{i}, {dominnote}-{notename(dominnote)}, {minormaj(1)}")
                        k=k+16
                    if time>=songdur-1:
                        i=i+1
                        continue
                if ritm==3:
                    if i==0+k:
                        if degreeschords[j]==0:
                            arpminchord(tonicnote1[j], track1, track, 1, 2, i, duration)
                            print(f"Chord,{i}, {notename(tonicnote1[j])}, {minormaj(degreeschords[j])}")
                            prints.append(f"Chord,{i}, {tonicnote1[j]}-{notename(tonicnote1[j])}, {minormaj(degreeschords[j])}")
                        elif degreeschords[j]==1:
                            arpmajchord(tonicnote1[j], track1, track, 1, 2, i, duration)
                            print(f"Chord,{i}, {notename(tonicnote1[j])}, {minormaj(degreeschords[j])}")
                            prints.append(f"Chord,{i}, {tonicnote1[j]}-{notename(tonicnote1[j])}, {minormaj(degreeschords[j])}")
                        elif degreeschords[j]==2:
                            arpdimchord(tonicnote1[j], track1, track, 1, 2, i, duration)
                            print(f"Chord,{i}, {notename(tonicnote1[j])}, {minormaj(degreeschords[j])}")
                            prints.append(f"Chord,{i}, {tonicnote1[j]}-{notename(tonicnote1[j])}, {minormaj(degreeschords[j])}")
                    if i==4+k:
                        if degreeschords[randton1]==0:
                            arpminchord(randchord1, track1, track, 1, 2, i, duration)
                            print(f"Chord,{i}, {notename(randchord1)}, {minormaj(degreeschords[randton1])}")
                            prints.append(f"Chord,{i}, {randchord1}-{notename(randchord1)}, {minormaj(degreeschords[randton1])}")
                        elif degreeschords[randton1]==1:
                            arpmajchord(randchord1, track1, track, 1, 2, i, duration)
                            print(f"Chord,{i}, {notename(randchord1)}, {minormaj(degreeschords[randton1])}")
                            prints.append(f"Chord,{i}, {randchord1}-{notename(randchord1)}, {minormaj(degreeschords[randton1])}")
                        elif degreeschords[randton1]==2:
                            arpdimchord(randchord1, track1, track, 1, 2, i, duration)
                            print(f"Chord,{i}, {notename(randchord1)}, {minormaj(degreeschords[randton1])}")
                            prints.append(f"Chord,{i}, {randchord1}-{notename(randchord1)}, {minormaj(degreeschords[randton1])}")
                    if i==8+k:
                        if degreeschords[randton2]==0:
                            arpminchord(randchord2, track1, track, 1, 2, i, duration)
                            print(f"Chord,{i}, {notename(randchord2)}, {minormaj(degreeschords[randton2])}")
                            prints.append(f"Chord,{i}, {randchord2}-{notename(randchord2)}, {minormaj(degreeschords[randton2])}")
                        elif degreeschords[randton2]==1:
                            arpmajchord(randchord2, track1, track, 1, 2, i, duration)
                            print(f"Chord,{i}, {notename(randchord2)}, {minormaj(degreeschords[randton2])}")
                            prints.append(f"Chord,{i}, {randchord2}-{notename(randchord2)}, {minormaj(degreeschords[randton2])}")
                        elif degreeschords[randton2]==2:
                            arpdimchord(randchord2, track1, track, 1, 2, i, duration)
                            print(f"Chord,{i}, {notename(randchord2)}, {minormaj(degreeschords[randton2])}")
                            prints.append(f"Chord,{i}, {randchord2}-{notename(randchord2)}, {minormaj(degreeschords[randton2])}")
                    if i==12+k:
                        arpmajchord(dominnote, track1, track, 1, 2, i, duration)
                        print(f"Chord,{i}, {notename(dominnote)}, {minormaj(1)}")
                        prints.append(f"Chord,{i}, {dominnote}-{notename(dominnote)}, {minormaj(1)}")
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
                            prints.append(f"Chord,{i}, {tonicnote1[j]}-{notename(tonicnote1[j])}, {minormaj(degreeschords[j])}")
                        elif degreeschords[j]==1:
                            majchord(tonicnote1[j], track1, track, 1, 2, i, duration)
                            print(f"Chord, {i}, {notename(tonicnote1[j])}, {minormaj(degreeschords[j])}")
                            prints.append(f"Chord,{i}, {tonicnote1[j]}-{notename(tonicnote1[j])}, {minormaj(degreeschords[j])}")
                        elif degreeschords[j]==2:
                            dimchord(tonicnote1[j], track1, track, 1, 2, i, duration)
                            print(f"Chord, {i}, {notename(tonicnote1[j])}, {minormaj(degreeschords[j])}")
                            prints.append(f"Chord,{i}, {tonicnote1[j]}-{notename(tonicnote1[j])}, {minormaj(degreeschords[j])}")
                    if i==4+k:
                        randton=rr.randint(0, len(tonicnote1)-2)
                        randchord=tonicnote1[randton]
                        if degreeschords[randton]==0:
                            minchord(randchord, track1, track, 1, 2, i, duration)
                            print(f"Chord, {i}, {notename(randchord)}, {minormaj(degreeschords[randton])}")
                            prints.append(f"Chord,{i}, {randchord}-{notename(randchord)}, {minormaj(degreeschords[randton])}")
                        elif degreeschords[randton]==1:
                            majchord(randchord, track1, track, 1, 2, i, duration)
                            print(f"Chord, {i}, {notename(randchord)}, {minormaj(degreeschords[randton])}")
                            prints.append(f"Chord,{i}, {randchord}-{notename(randchord)}, {minormaj(degreeschords[randton])}")
                        elif degreeschords[randton]==2:
                            dimchord(randchord, track1, track, 1, 2, i, duration)
                            print(f"Chord, {i}, {notename(randchord)}, {minormaj(degreeschords[randton])}")
                            prints.append(f"Chord,{i}, {randchord}-{notename(randchord)}, {minormaj(degreeschords[randton])}")
                    if i==8+k:
                        randton=rr.randint(0, len(tonicnote1)-2)
                        randchord=tonicnote1[randton]
                        if degreeschords[randton]==0:
                            minchord(randchord, track1, track, 1, 2, i, duration)
                            print(f"Chord, {i}, {notename(randchord)}, {minormaj(degreeschords[randton])}")
                            prints.append(f"Chord,{i}, {randchord}-{notename(randchord)}, {minormaj(degreeschords[randton])}")
                        elif degreeschords[randton]==1:
                            majchord(randchord, track1, track, 1, 2, i, duration)
                            print(f"Chord, {i}, {notename(randchord)}, {minormaj(degreeschords[randton])}")
                            prints.append(f"Chord,{i}, {randchord}-{notename(randchord)}, {minormaj(degreeschords[randton])}")
                        elif degreeschords[randton]==2:
                            dimchord(randchord, track1, track, 1, 2, i, duration)
                            print(f"Chord, {i}, {notename(randchord)}, {minormaj(degreeschords[randton])}")
                            prints.append(f"Chord,{i}, {randchord}-{notename(randchord)}, {minormaj(degreeschords[randton])}")
                    if i==12+k:
                        majchord(dominnote, track1, track, 1, 2, i, duration)
                        print(f"Chord, {i}, {notename(dominnote)}, {minormaj(1)}")
                        prints.append(f"Chord,{i}, {dominnote}-{notename(dominnote)}, {minormaj(1)}")
                        k=k+16
                    if time>=songdur-1:
                        i=i+1
                        continue
                if ritm==2:
                    if i==0+k:
                        if degreeschords[j]==0:
                            tminchord(tonicnote1[j], track1, track, 1, 2, i, duration)
                            print(f"Chord, {i}, {notename(tonicnote1[j])}, {minormaj(degreeschords[j])}")
                            prints.append(f"Chord,{i}, {tonicnote1[j]}-{notename(tonicnote1[j])}, {minormaj(degreeschords[j])}")
                        elif degreeschords[j]==1:
                            tmajchord(tonicnote1[j], track1, track, 1, 2, i, duration)
                            print(f"Chord, {i}, {notename(tonicnote1[j])}, {minormaj(degreeschords[j])}")
                            prints.append(f"Chord,{i}, {tonicnote1[j]}-{notename(tonicnote1[j])}, {minormaj(degreeschords[j])}")
                        elif degreeschords[j]==2:
                            tdimchord(tonicnote1[j], track1, track, 1, 2, i, duration)
                            print(f"Chord, {i}, {notename(tonicnote1[j])}, {minormaj(degreeschords[j])}")
                            prints.append(f"Chord,{i}, {tonicnote1[j]}-{notename(tonicnote1[j])}, {minormaj(degreeschords[j])}")
                    if i==4+k:
                        randton=rr.randint(0, len(tonicnote1)-2)
                        randchord=tonicnote1[randton]
                        if degreeschords[randton]==0:
                            tminchord(randchord, track1, track, 1, 2, i, duration)
                            print(f"Chord, {i}, {notename(randchord)}, {minormaj(degreeschords[randton])}")
                            prints.append(f"Chord,{i}, {randchord}-{notename(randchord)}, {minormaj(degreeschords[randton])}")
                        elif degreeschords[randton]==1:
                            tmajchord(randchord, track1, track, 1, 2, i, duration)
                            print(f"Chord, {i}, {notename(randchord)}, {minormaj(degreeschords[randton])}")
                            prints.append(f"Chord,{i}, {randchord}-{notename(randchord)}, {minormaj(degreeschords[randton])}")
                        elif degreeschords[randton]==2:
                            tdimchord(randchord, track1, track, 1, 2, i, duration)
                            print(f"Chord, {i}, {notename(randchord)}, {minormaj(degreeschords[randton])}")
                            prints.append(f"Chord,{i}, {randchord}-{notename(randchord)}, {minormaj(degreeschords[randton])}")
                    if i==8+k:
                        randton=rr.randint(0, len(tonicnote1)-2)
                        randchord=tonicnote1[randton]
                        if degreeschords[randton]==0:
                            tminchord(randchord, track1, track, 1, 2, i, duration)
                            print(f"Chord, {i}, {notename(randchord)}, {minormaj(degreeschords[randton])}")
                            prints.append(f"Chord,{i}, {randchord}-{notename(randchord)}, {minormaj(degreeschords[randton])}")
                        elif degreeschords[randton]==1:
                            tmajchord(randchord, track1, track, 1, 2, i, duration)
                            print(f"Chord, {i}, {notename(randchord)}, {minormaj(degreeschords[randton])}")
                            prints.append(f"Chord,{i}, {randchord}-{notename(randchord)}, {minormaj(degreeschords[randton])}")
                        elif degreeschords[randton]==2:
                            tdimchord(randchord, track1, track, 1, 2, i, duration)
                            print(f"Chord, {i}, {notename(randchord)}, {minormaj(degreeschords[randton])}")
                            prints.append(f"Chord,{i}, {randchord}-{notename(randchord)}, {minormaj(degreeschords[randton])}")
                    if i==12+k:
                        tmajchord(dominnote, track1, track, 1, 2, i, duration)
                        print(f"Chord, {i}, {notename(dominnote)}, {minormaj(1)}")
                        prints.append(f"Chord,{i}, {dominnote}-{notename(dominnote)}, {minormaj(1)}")
                        k=k+16
                    if time>=songdur-1:
                        i=i+1
                        continue
                if ritm==3:
                    if i==0+k:
                        if degreeschords[j]==0:
                            arpminchord(tonicnote1[j], track1, track, 1, 2, i, duration)
                            print(f"Chord, {i}, {notename(tonicnote1[j])}, {minormaj(degreeschords[j])}")
                            prints.append(f"Chord,{i}, {tonicnote1[j]}-{notename(tonicnote1[j])}, {minormaj(degreeschords[j])}")
                        elif degreeschords[j]==1:
                            arpmajchord(tonicnote1[j], track1, track, 1, 2, i, duration)
                            print(f"Chord, {i}, {notename(tonicnote1[j])}, {minormaj(degreeschords[j])}")
                            prints.append(f"Chord,{i}, {tonicnote1[j]}-{notename(tonicnote1[j])}, {minormaj(degreeschords[j])}")
                        elif degreeschords[j]==2:
                            arpdimchord(tonicnote1[j], track1, track, 1, 2, i, duration)
                            print(f"Chord, {i}, {notename(tonicnote1[j])}, {minormaj(degreeschords[j])}")
                            prints.append(f"Chord,{i}, {tonicnote1[j]}-{notename(tonicnote1[j])}, {minormaj(degreeschords[j])}")
                    if i==4+k:
                        randton=rr.randint(0, len(tonicnote1)-2)
                        randchord=tonicnote1[randton]
                        if degreeschords[randton]==0:
                            arpminchord(randchord, track1, track, 1, 2, i, duration)
                            print(f"Chord, {i}, {notename(randchord)}, {minormaj(degreeschords[randton])}")
                            prints.append(f"Chord,{i}, {randchord}-{notename(randchord)}, {minormaj(degreeschords[randton])}")
                        elif degreeschords[randton]==1:
                            arpmajchord(randchord, track1, track, 1, 2, i, duration)
                            print(f"Chord, {i}, {notename(randchord)}, {minormaj(degreeschords[randton])}")
                            prints.append(f"Chord,{i}, {randchord}-{notename(randchord)}, {minormaj(degreeschords[randton])}")
                        elif degreeschords[randton]==2:
                            arpdimchord(randchord, track1, track, 1, 2, i, duration)
                            print(f"Chord, {i}, {notename(randchord)}, {minormaj(degreeschords[randton])}")
                            prints.append(f"Chord,{i}, {randchord}-{notename(randchord)}, {minormaj(degreeschords[randton])}")
                    if i==8+k:
                        randton=rr.randint(0, len(tonicnote1)-2)
                        randchord=tonicnote1[randton]
                        if degreeschords[randton]==0:
                            arpminchord(randchord, track1, track, 1, 2, i, duration)
                            print(f"Chord, {i}, {notename(randchord)}, {minormaj(degreeschords[randton])}")
                            prints.append(f"Chord,{i}, {randchord}-{notename(randchord)}, {minormaj(degreeschords[randton])}")
                        elif degreeschords[randton]==1:
                            arpmajchord(randchord, track1, track, 1, 2, i, duration)
                            print(f"Chord, {i}, {notename(randchord)}, {minormaj(degreeschords[randton])}")
                            prints.append(f"Chord,{i}, {randchord}-{notename(randchord)}, {minormaj(degreeschords[randton])}")
                        elif degreeschords[randton]==2:
                            arpdimchord(randchord, track1, track, 1, 2, i, duration)
                            print(f"Chord, {i}, {notename(randchord)}, {minormaj(degreeschords[randton])}")
                            prints.append(f"Chord,{i}, {randchord}-{notename(randchord)}, {minormaj(degreeschords[randton])}")
                    if i==12+k:
                        arpmajchord(dominnote, track1, track, 1, 2, i, duration)
                        print(f"Chord, {i}, {notename(dominnote)}, {minormaj(1)}")
                        prints.append(f"Chord,{i}, {dominnote}-{notename(dominnote)}, {minormaj(1)}")
                        k=k+16
                    if time>=songdur-1:
                        i=i+1
                        continue    

            elif Ngarmony==150:
                if ritm==1:
                    if i==0+k:
                        if degreeschords[j]==0:
                            minchord(tonicnote1[j], track1, track, 1, 2, i, duration)
                            print(f"Chord, {i}, {notename(tonicnote1[j])}, {minormaj(degreeschords[j])}")
                            prints.append(f"Chord,{i}, {tonicnote1[j]}-{notename(tonicnote1[j])}, {minormaj(degreeschords[j])}")
                        elif degreeschords[j]==1:
                            majchord(tonicnote1[j], track1, track, 1, 2, i, duration)
                            print(f"Chord, {i}, {notename(tonicnote1[j])}, {minormaj(degreeschords[j])}")
                            prints.append(f"Chord,{i}, {tonicnote1[j]}-{notename(tonicnote1[j])}, {minormaj(degreeschords[j])}")
                        elif degreeschords[j]==2:
                            dimchord(tonicnote1[j], track1, track, 1, 2, i, duration)
                            print(f"Chord, {i}, {notename(tonicnote1[j])}, {minormaj(degreeschords[j])}")
                            prints.append(f"Chord,{i}, {tonicnote1[j]}-{notename(tonicnote1[j])}, {minormaj(degreeschords[j])}")
                    if i==4+k or i == 8+k or i == 12+k or i == 16+k or i == 20+k or i == 24+k:
                        randton=rr.randint(0, len(tonicnote1)-1)
                        randchord=tonicnote1[randton]
                        if degreeschords[randton]==0:
                            minchord(randchord, track1, track, 1, 2, i, duration)
                            print(f"Chord, {i}, {notename(randchord)}, {minormaj(degreeschords[randton])}")
                            prints.append(f"Chord,{i}, {randchord}-{notename(randchord)}, {minormaj(degreeschords[randton])}")
                        elif degreeschords[randton]==1:
                            majchord(randchord, track1, track, 1, 2, i, duration)
                            print(f"Chord, {i}, {notename(randchord)}, {minormaj(degreeschords[randton])}")
                            prints.append(f"Chord,{i}, {randchord}-{notename(randchord)}, {minormaj(degreeschords[randton])}")
                        elif degreeschords[randton]==2:
                            dimchord(randchord, track1, track, 1, 2, i, duration)
                            print(f"Chord, {i}, {notename(randchord)}, {minormaj(degreeschords[randton])}")
                            prints.append(f"Chord,{i}, {randchord}-{notename(randchord)}, {minormaj(degreeschords[randton])}")
                    if i==28+k:
                        if j==0 or j==3 or j==4:
                            majchord(dominnote, track1, track, 1, 2, i, duration)
                        if j==1 or j==2 or j==5 or j==6:
                            minchord(dominnote, track1, track, 1, 2, i, duration)
                        print(f"Chord, {i}, {notename(dominnote)}, {minormaj(1)}")
                        prints.append(f"Chord,{i}, {dominnote}-{notename(dominnote)}, {minormaj(1)}")
                        k=k+32
                    if time>=songdur-1:
                        i=i+1
                        continue
                if ritm==2:
                    if i==0+k:
                        if degreeschords[j]==0:
                            tminchord(tonicnote1[j], track1, track, 1, 2, i, duration)
                            print(f"Chord, {i}, {notename(tonicnote1[j])}, {minormaj(degreeschords[j])}")
                            prints.append(f"Chord,{i}, {tonicnote1[j]}-{notename(tonicnote1[j])}, {minormaj(degreeschords[j])}")
                        elif degreeschords[j]==1:
                            tmajchord(tonicnote1[j], track1, track, 1, 2, i, duration)
                            print(f"Chord, {i}, {notename(tonicnote1[j])}, {minormaj(degreeschords[j])}")
                            prints.append(f"Chord,{i}, {tonicnote1[j]}-{notename(tonicnote1[j])}, {minormaj(degreeschords[j])}")
                        elif degreeschords[j]==2:
                            tdimchord(tonicnote1[j], track1, track, 1, 2, i, duration)
                            print(f"Chord, {i}, {notename(tonicnote1[j])}, {minormaj(degreeschords[j])}")
                            prints.append(f"Chord,{i}, {tonicnote1[j]}-{notename(tonicnote1[j])}, {minormaj(degreeschords[j])}")
                    if i==4+k or i == 8+k or i == 12+k or i == 16+k or i == 20+k or i == 24+k:
                        randton=rr.randint(0, len(tonicnote1)-2)
                        randchord=tonicnote1[randton]
                        if degreeschords[randton]==0:
                            tminchord(randchord, track1, track, 1, 2, i, duration)
                            print(f"Chord, {i}, {notename(randchord)}, {minormaj(degreeschords[randton])}")
                            prints.append(f"Chord,{i}, {randchord}-{notename(randchord)}, {minormaj(degreeschords[randton])}")
                        elif degreeschords[randton]==1:
                            tmajchord(randchord, track1, track, 1, 2, i, duration)
                            print(f"Chord, {i}, {notename(randchord)}, {minormaj(degreeschords[randton])}")
                            prints.append(f"Chord,{i}, {randchord}-{notename(randchord)}, {minormaj(degreeschords[randton])}")
                        elif degreeschords[randton]==2:
                            tdimchord(randchord, track1, track, 1, 2, i, duration)
                            print(f"Chord, {i}, {notename(randchord)}, {minormaj(degreeschords[randton])}")
                            prints.append(f"Chord,{i}, {randchord}-{notename(randchord)}, {minormaj(degreeschords[randton])}")
                    if i==28+k:
                        if j==0 or j==3 or j==4:
                            tmajchord(dominnote, track1, track, 1, 2, i, duration)
                        if j==1 or j==2 or j==5 or j==6:
                            tminchord(dominnote, track1, track, 1, 2, i, duration)
                        print(f"Chord, {i}, {notename(dominnote)}, {minormaj(1)}")
                        prints.append(f"Chord,{i}, {dominnote}-{notename(dominnote)}, {minormaj(1)}")
                        k=k+32
                    if time>=songdur-1:
                        i=i+1
                        continue
                if ritm==3:
                    if i==0+k:
                        if degreeschords[j]==0:
                            arpminchord(tonicnote1[j], track1, track, 1, 2, i, duration)
                            print(f"Chord, {i}, {notename(tonicnote1[j])}, {minormaj(degreeschords[j])}")
                            prints.append(f"Chord,{i}, {tonicnote1[j]}-{notename(tonicnote1[j])}, {minormaj(degreeschords[j])}")
                        elif degreeschords[j]==1:
                            arpmajchord(tonicnote1[j], track1, track, 1, 2, i, duration)
                            print(f"Chord, {i}, {notename(tonicnote1[j])}, {minormaj(degreeschords[j])}")
                            prints.append(f"Chord,{i}, {tonicnote1[j]}-{notename(tonicnote1[j])}, {minormaj(degreeschords[j])}")
                        elif degreeschords[j]==2:
                            arpdimchord(tonicnote1[j], track1, track, 1, 2, i, duration)
                            print(f"Chord, {i}, {notename(tonicnote1[j])}, {minormaj(degreeschords[j])}")
                            prints.append(f"Chord,{i}, {tonicnote1[j]}-{notename(tonicnote1[j])}, {minormaj(degreeschords[j])}")
                    if i==4+k or i == 8+k or i == 12+k or i == 16+k or i == 20+k or i == 24+k:
                        randton=rr.randint(0, len(tonicnote1)-1)
                        randchord=tonicnote1[randton]
                        if degreeschords[randton]==0:
                            arpminchord(randchord, track1, track, 1, 2, i, duration)
                            print(f"Chord, {i}, {notename(randchord)}, {minormaj(degreeschords[randton])}")
                            prints.append(f"Chord,{i}, {randchord}-{notename(randchord)}, {minormaj(degreeschords[randton])}")
                        elif degreeschords[randton]==1:
                            arpmajchord(randchord, track1, track, 1, 2, i, duration)
                            print(f"Chord, {i}, {notename(randchord)}, {minormaj(degreeschords[randton])}")
                            prints.append(f"Chord,{i}, {randchord}-{notename(randchord)}, {minormaj(degreeschords[randton])}")
                        elif degreeschords[randton]==2:
                            arpdimchord(randchord, track1, track, 1, 2, i, duration)
                            print(f"Chord, {i}, {notename(randchord)}, {minormaj(degreeschords[randton])}")
                            prints.append(f"Chord,{i}, {randchord}-{notename(randchord)}, {minormaj(degreeschords[randton])}")
                    if i==28+k:
                        if j==0 or j==3 or j==4:
                            arpmajchord(dominnote, track1, track, 1, 2, i, duration)
                        if j==1 or j==2 or j==5 or j==6:
                            arpminchord(dominnote, track1, track, 1, 2, i, duration)
                        print(f"Chord, {i}, {notename(dominnote)}, {minormaj(1)}")
                        prints.append(f"Chord,{i}, {dominnote}-{notename(dominnote)}, {minormaj(1)}")
                        k=k+32
                    if time>=songdur-1:
                        i=i+1
                        continue                
            randpause=rr.randint(1,100)    
            tonic = 0
            flagtonicrep=0
            randrep = 0
            while streamcheck<=100000000:
                randnote=rr.randint(0,len(degrees)-1)
                randdur=rr.randint(0,len(durtsd)-1)
                randduroth=rr.randint(0,len(duroth)-1)
                randtonic=rr.randint(1,100)
                randoct=rr.randint(1,100)
                print(note, lastnote,"<<<<")
                if randtonic<=tonic:
                    note=tonicnote1[j]
                elif randtonic>tonic and randtonic<=(tonic+domin):
                    note=dominnote
                elif randtonic>(tonic+domin) and randtonic<=(tonic+domin+subd):
                    note=subdnote
                else:
                    while degrees[randnote]==tonicnote1[j] or degrees[randnote]==subdnote or degrees[randnote]==dominnote:
                        randnote=rr.randint(0,len(degrees)-1)
                        note=degrees[randnote]
                if streamcheck==0 or abs(note-lastnote)<=5:
                    if abs(note-lastnote)==0:
                        randrep=rr.randint(1,100)
                        if randrep<=95:
                            continue
                        else:
                            print("Да-да, я пропустил")
                            pass
                    print('Разница:', abs(note-lastnote), randrep, streamcheck)
                    streamcheck+=1
                    tonic=tonic1
                    subd=subd1
                    domin=domin1
                    break
                tonic-=5
                subd-=5
                domin-=5
                streamcheck+=1
            if l==1:
                if randpause<=pause:
                    ran=rr.randint(0,len(durtsd)-1)
                    time=time+lastdur
                   # MyMIDI.addNote(track, channel, degrees[0], time, duroth[randduroth], 100)
                    print(f"Pause, {time}, pause, Duration: {durtsd[ran]}, Last duration: {lastdur}, rand: {randtonic}")
                    prints.append(f"Pause,{time}, pause, Duration: {durtsd[ran]}, Last duration: {lastdur}")
#                    lastdur=durtsd[randdur]
                    lastdur=durtsd[ran]                    
                l=0
            if randtonic<=tonic:
                note=tonicnote1[j]
                if randoct<=tonicoct:
                    note1=tonicnote1[j]
                else:
                    note1=tonicnote1[j]+12
                time=time+lastdur
                ran=rr.randint(0,len(durtsd)-1)
                MyMIDI.addNote(track, channel, note1, time, durtsd[ran], rr.randint(80,95))
                print(f"Note, {time}, Note: {notename(note1)}, Duration: {durtsd[ran]}, Last duration: {lastdur}, rand: {randtonic}")
                prints.append(f"Note,{time}, Note: {note1}-{notename(note1)}, Duration: {durtsd[ran]}, Last duration: {lastdur}")
#                    lastdur=durtsd[randdur]
                lastdur=durtsd[ran]
                lastnote=note
                l=1              
            else:
                if randtonic>tonic and randtonic<=(tonic+domin):
                    note=dominnote
                    time=time+lastdur
                    ran=rr.randint(0,len(durtsd)-1)
                    MyMIDI.addNote(track, channel, note, time, durtsd[ran], rr.randint(80,95))
                    print(f"Note, {time}, Note: {notename(note)}, Duration: {durtsd[ran]}, Last duration: {lastdur}, {randtonic}")
                    prints.append(f"Note,{time}, Note: {note}-{notename(note)}, Duration: {durtsd[ran]}, Last duration: {lastdur}")
                    lastdur=durtsd[ran]
                    lastnote=note
                    l=1
                    
                    
                else:
                    if randtonic>(tonic+domin) and randtonic<=(tonic+domin+subd):
                        note=subdnote
                        time=time+lastdur
                        ran=rr.randint(0,len(durtsd)-1)
                        MyMIDI.addNote(track, channel, note, time, durtsd[ran], rr.randint(80,95))
                        print(f"Note, {time}, Note: {notename(note)}, Duration: {durtsd[ran]}, Last duration: {lastdur}, {randtonic}")
                        prints.append(f"Note,{time}, Note: {note}-{notename(note)}, Duration: {durtsd[ran]}, Last duration: {lastdur}")
                        lastdur=durtsd[ran]
                        lastnote=note
                        
                    else:
                        time=time+lastdur
                        while degrees[randnote]==tonicnote1[j] or degrees[randnote]==subdnote or degrees[randnote]==dominnote:
                            randnote=rr.randint(0,len(degrees)-1)
                        MyMIDI.addNote(track, channel, degrees[randnote], time, duroth[randduroth], rr.randint(70,90)) 
                        print(f"Note, {time}, Note: {notename(degrees[randnote])}, Duration: {duroth[randduroth]}, Last duration: {lastdur}, {randtonic}")
                        prints.append(f"Note,{time}, Note: {degrees[randnote]}-{notename(degrees[randnote])}, Duration: {duroth[randduroth]}, Last duration: {lastdur}")
                        lastdur=duroth[randduroth]
                        lastnote=degrees[randnote]
                                  
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
            elif Ngarmony==100 or Ngarmony==50 or Ngarmony == 150:
                if degreeschords[j]==0:
                    minchord(tonicnote1[j], track1, track, 1, 2, i, duration)
                    print(f"Chord, {i}, {notename(tonicnote1[j])}, {minormaj(degreeschords[j])}")
                    prints.append(f"Chord,{i}, {tonicnote1[j]}-{notename(tonicnote1[j])}, {minormaj(degreeschords[j])}")
                elif degreeschords[j]==1:
                    majchord(tonicnote1[j], track1, track, 1, 2, i, duration)
                    print(f"Chord, {i}, {notename(tonicnote1[j])}, {minormaj(degreeschords[j])}")
                    prints.append(f"Chord,{i}, {tonicnote1[j]}-{notename(tonicnote1[j])}, {minormaj(degreeschords[j])}")
                elif degreeschords[j]==2:
                    minchord(tonicnote1[j]-2, track1, track, 1, 2, i, duration)
                    print(f"Chord, {i}, {notename(tonicnote1[j])}, {minormaj(degreeschords[j])}")
                    prints.append(f"Chord,{i}, {tonicnote1[j]}-{notename(tonicnote1[j])}, {minormaj(degreeschords[j])}")
                i=i+1
        for l in range(len(prints)):
            prints[l] = prints[l].split(',')
        prints.sort(key= lambda x: float(x[1]))
        for l in range(len(prints)):
            prints[l][0]=prints[l][0]+' '
        #pprint.pprint(prints)
        #print(prints)
        if j==0:
            with open(f"Tracks/{j} - {notename(tonicnote1[j])}-major.mid", "wb") as output_file:
                MyMIDI.writeFile(output_file)
            midfile = f'Tracks/{str(j)} - {notename(tonicnote1[j])}-major.mid'
            wavefile = f'Tracks/{str(j)} - {notename(tonicnote1[j])}-major.wav'
            subprocess.call(f'fluidsynth -F "{wavefile}" "1961 Kawai 600-Stereo.sf2" "{midfile}"')
            with open(f"Tracks/{j} - {notename(tonicnote1[j])}-major.txt", "w") as textfile:
                for l in range(len(prints)):
                    textfile.writelines(prints[l])
                    textfile.write('\n')
            prints=[]
        elif j==1:
            with open(f"Tracks/{j} - {notename(tonicnote1[j])}-dorian.mid", "wb") as output_file:
                MyMIDI.writeFile(output_file)
            midfile = f'Tracks/{str(j)} - {notename(tonicnote1[j])}-dorian.mid'
            wavefile = f'Tracks/{str(j)} - {notename(tonicnote1[j])}-dorian.wav'
            subprocess.call(f'fluidsynth -F "{wavefile}" "1961 Kawai 600-Stereo.sf2" "{midfile}"')
            with open(f"Tracks/{j} - {notename(tonicnote1[j])}-dorian.txt", "w") as textfile:
                for l in range(len(prints)):
                    textfile.writelines(prints[l])
                    textfile.write('\n')
            prints=[]
        elif j==2:
            with open(f"Tracks/{j} - {notename(tonicnote1[j])}-phrygian.mid", "wb") as output_file:
                MyMIDI.writeFile(output_file)
            midfile = f'Tracks/{str(j)} - {notename(tonicnote1[j])}-phrygian.mid'
            wavefile = f'Tracks/{str(j)} - {notename(tonicnote1[j])}-phrygian.wav'
            subprocess.call(f'fluidsynth -F "{wavefile}" "1961 Kawai 600-Stereo.sf2" "{midfile}"')
            with open(f"Tracks/{j} - {notename(tonicnote1[j])}-phrygian.txt", "w") as textfile:
                for l in range(len(prints)):
                    textfile.writelines(prints[l])
                    textfile.write('\n')
            prints=[]
        elif j==3:
            with open(f"Tracks/{j} - {notename(tonicnote1[j])}-lydian.mid", "wb") as output_file:
                MyMIDI.writeFile(output_file)
            midfile = f'Tracks/{str(j)} - {notename(tonicnote1[j])}-lydian.mid'
            wavefile = f'Tracks/{str(j)} - {notename(tonicnote1[j])}-lydian.wav'
            subprocess.call(f'fluidsynth -F "{wavefile}" "1961 Kawai 600-Stereo.sf2" "{midfile}"')
            with open(f"Tracks/{j} - {notename(tonicnote1[j])}-lydian.txt", "w") as textfile:
                for l in range(len(prints)):
                    textfile.writelines(prints[l])
                    textfile.write('\n')
            prints=[]
        elif j==4:
            with open(f"Tracks/{j} - {notename(tonicnote1[j])}-mixolydian.mid", "wb") as output_file:
                MyMIDI.writeFile(output_file)
            midfile = f'Tracks/{str(j)} - {notename(tonicnote1[j])}-mixolydian.mid'
            wavefile = f'Tracks/{str(j)} - {notename(tonicnote1[j])}-mixolydian.wav'
            subprocess.call(f'fluidsynth -F "{wavefile}" "1961 Kawai 600-Stereo.sf2" "{midfile}"')
            with open(f"Tracks/{j} - {notename(tonicnote1[j])}-mixolydian.txt", "w") as textfile:
                for l in range(len(prints)):
                    textfile.writelines(prints[l])
                    textfile.write('\n')
            prints=[]
        elif j==5:
            with open(f"Tracks/{j} - {notename(tonicnote1[j])}-minor.mid", "wb") as output_file:
                MyMIDI.writeFile(output_file)
            midfile = f'Tracks/{str(j)} - {notename(tonicnote1[j])}-minor.mid'
            wavefile = f'Tracks/{str(j)} - {notename(tonicnote1[j])}-minor.wav'
            subprocess.call(f'fluidsynth -F "{wavefile}" "1961 Kawai 600-Stereo.sf2" "{midfile}"')
            with open(f"Tracks/{j} - {notename(tonicnote1[j])}-minor.txt", "w") as textfile:
                for l in range(len(prints)):
                    textfile.writelines(prints[l])
                    textfile.write('\n')
            prints=[]
        elif j==6:
            with open(f"Tracks/{j} - {notename(tonicnote1[j])}-locrian.mid", "wb") as output_file:
                MyMIDI.writeFile(output_file)
            midfile = f'Tracks/{str(j)} - {notename(tonicnote1[j])}-locrian.mid'
            wavefile = f'Tracks/{str(j)} - {notename(tonicnote1[j])}-locrian.wav'
            subprocess.call(f'fluidsynth -F "{wavefile}" "1961 Kawai 600-Stereo.sf2" "{midfile}"')
            with open(f"Tracks/{j} - {notename(tonicnote1[j])}-locrian.txt", "w") as textfile:
                for l in range(len(prints)):
                    textfile.writelines(prints[l])
                    textfile.write('\n')
            prints=[]
        j=j+1
        if tonicchose!=8:
            break
if lang==2:
    print('Не забудь проверить папку Tracks')
if lang==1:
    print('Dont forget to check Tracks folder out threre')
input()