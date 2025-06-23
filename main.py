import random
import time
import inspect
import sys
from datetime import datetime

# === SETTINGS ===
_DEBUG = True

# === DATA ===
DATA = [
	"DIAMANT","DIAMA","DIAMA","diamanten",15,  # 90300
	"GURKA","GURKA","ILLAL","gurkan",0,  # 90302
	"SILVERTACKA","SILVE","TACKA","silvertackan",31,  # 90304
	"HILLEBARD","HILLE","JUVEL","hillebarden",2,  # 90306
	"DÖDSKALLE","DÖDSK","SKALL","dödskallen",0,  # 90308
	"KLOCKA","VÄCKA","KLOCK","klockan",59,  # 90310
	"GULDMYNT","GULD","MYNT","guldmynten",0,  # 90312
	"TRILOGI","TRILO","SAGAN","trilogin",36,  # 90314
	"KONTRAKT","KONTR","SKÄRT","kontraktet",0,  # 90316
	"LAGERKRANS","LAGER","KRANS","lagerkransen",53,  # 90318
	"PÄRLHALSBAND","PÄRL","HALSB","pärlhalsbandet",0,  # 90320
	"FAUNSKO","FAUN","SKO","faunskon",0,  # 90322
	"KOFOT","KOFOT","KOFOT","kofoten",0,  # 90330
	"CYKELPUMP","CYKEL","PUMP","cykelpumpen",0,  # 90332
	"STEGE","STEGE","STEGE","stegen",4,  # 90334
	"BRÄNNVINSFLASKA","BRÄNN","BRÄNN","brännvinsflaskan",97,  # 90336
	"VATTENFLASKA","VATTENF","VATTENF","vattenflaskan",0,  # 90338
	"BOLL","BOLL","BOLL","bollen",8,  # 90340
	"SPADE","SPADE","SPADE","spaden",61,  # 90342
	"LIK","LIK","LIK","liket",0,  # 90344
	"KATALOG","KATAL","TELEFONK","katalogen",0,  # 90346
	"LAMPA","LAMPA","LAMPA","lampan",0,  # 90348
	"TELEFON","TELEF","TELEF","telefonen",100,  # 90350
	"NYCKLAR","NYCKL","NYCKE","nycklarna",54,  # 90352
	"SAX","SAX","SAX","saxen",2,  # 90354
	"SLÄGGA","SLÄGG","SLÄGG","släggan",2,  # 90356
	"VAKT","VAKT","VAKT","vakten",58,  # 90357
	"FÖRLÄNGNINGSSLADD","FÖRLÄ","SLADD","förlängningssladden",26,  # 90358
	# Data för Fozzis berättelse  # 90400
	"Dodge City","Boot Hill","en by i Montana","fantomengrottan",  # 90402
	"fängelsechefen i Råå","Trondheim",  # 90404
	"bröderna Dalton","Sven Olssons kvintett","bröderna Brothers",  # 90406
	"Kimmo, den gamle fyllbulten,","Curt Nicolin","Jesse James",  # 90408
	"fängelset","San Franciscos hem för tankspridda","sin limosin",  # 90410
	"burarna i Bronx Zoo","en labyrint i Småland","riksdagshuset",  # 90412
	"fritidsorganet GLAD OCH NAKEN","sheriffen","guldlasten",  # 90414
	"några glada flickor","en aktie i Kuben","en illaluktande gurka",  # 90416
	"fruktans demoner","ett bankrån","Butch Cassidys hustru",  # 90418
	"jultomten","en hjärnskakningsepidemi","kvarterspolisen",  # 90420
	"ett bakhåll","ett fel på Malmös TV 2-sändare","en taxi",  # 90422
	"att toaletten ska bli ledig","att sheriffen ska göra något","Lucky Luke",  # 90424
	"skjuta sönder stan","störa indianerna","varsla om lockout",  # 90426
	"väcka guvernören","ta gisslan på Norges ambassad","dra sej tillbaka",  # 90428
	"rädda","lätt berusade","måna om sitt utseende","allt färre",  # 90430
	"svårflörtade","sömniga",  # 90432
	"på ett helt annat ställe","för sent","i grevens tid",  # 90434
	"en liten aning för tidigt","samtidigt","inte",  # 90436
]

# === TEMP ===
def goto(instruction_number: int) -> None:
    """Make a jump to a specific BASIC instruction number"""
    module = sys.modules["__main__"]
    source_lines, _ = inspect.getsourcelines(module)
    line = -1
    for idx, content in enumerate(source_lines):
        if content.strip().endswith(f"# {instruction_number:05d}"):
            line = idx + 1
            break
    assert line != -1
    scope = []
    for idx, source_line in enumerate(source_lines[:line]):
        if source_line.startswith(('import ', 'from ')):
            scope.insert(0, source_lines[idx])
        if source_line.startswith("def "):
            scope.append(source_line)
            while source_lines[idx + 1].startswith(" "):
                idx += 1
                scope.append(source_lines[idx])
    source_lines = source_lines[line - 1 :]
    first_indentation_level = len(source_lines[0]) - len(source_lines[0].lstrip())
    for index, source_line in enumerate(source_lines):
        indentation_level = len(source_line) - len(source_line.lstrip())
        if indentation_level == 0:
            break
        indentation_start = min(indentation_level, first_indentation_level)
        source_lines[index] = source_lines[index][indentation_start:]
    source_code = "".join(scope + source_lines)
    if _DEBUG:
        print(f"goto({instruction_number}) -> line={line}")
        time.sleep(1)
    exec(source_code, module.__dict__)
    sys.exit(0)

# === UTILS ===
def INSTR(X1: str, X2: str) -> int:
    """
    Returns 0 if not found. Starting index is 1
    See: https://www.c64-wiki.com/wiki/INSTR
    """
    return X1.find(X2) + 1


def FNL_(X1_: str, X: int) -> str:  # 90800
    """Returns substring from left"""
    return X1_[:X]  # 90810


def FNC_(A_: str) -> str:  # 90700
    """Converts to upper case"""
    return A_[:130].upper()  # 90760


def FNA_(I1: int) -> str:  # 90600
    """Returns proper 'no' for item"""
    if I1 == 7 or I1 == 26:
        return "inga "
    if I1 == 9 or I1 == 11 or I1 == 22:
        return "inget "
    return "ingen "  # 90602


def busy(n: int, msg: str):
    """Busy wait that captures keypress"""
    start = time.time()
    try:
        # Windows
        import msvcrt
        while True:
            if msvcrt.kbhit():
                msvcrt.getch()
                print(msg)
                break
            if time.time() - start >= n:
                break
    except ImportError:
        # Unix
        import select
        import termios
        import tty
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setcbreak(fd)
            while True:
                if select.select([sys.stdin], [], [], 0)[0]:
                    sys.stdin.read(1)
                    print(msg)
                if time.time() - start >= n:
                    break
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)


def FNS_(X1_: str, X: int):  # 90650
    busy(X, f"Tyst, jag {X1_}!")


def FNR_(X1_: str, X: int) -> str:  # 90820
    """Trims str from right"""
    if X <= 0:
        return ""
    if X > len(X1_):
        return f"{X1_}"
    return X1_[X:]  # 90830


def FNM_(X1_: str, X: int) -> str:  # 90840
    """Returns middle part of a str"""
    if X > len(X1_) or X <= 0:
        return ""
    return X1_[X-1:len(X1_) - X]  # 90850


def FNF_(xi):  # 90900
    #? maybe incorrect, if data pointer must persist
    return DATA[X[xi] + 1]


def FNI_(X1_) -> str:  # 90950
    #? only partially fixed
    #if M2_ = 1 and W_ != CHR_(3):
    #    print()#2,W_ #&&&&&  # 90960
    # print(X1_)  # 90970
    # ? if M3%==0%:  # 90980
    W_ = input(X1_)
    return W_
    # if END#3:
    # ?     M3%=0%
    goto(90980)  # &&&&&  # 90982
    _ = input()  # LINE #3,W_
    print(W_)  # &&&&&  )# 90984
    return W_  # 90990


# == SKIPPED ==
"""
Modul med metoder för spara och återskapa,
logga och läs från logg, som inte är implementerade än.
"""

def call_method_80000():
    print('TODO: Detta är inte implementerat än.')
    return

    # *** SPARA *** &&&&& DEC-10 SPECIELL KOD PÅ 80000-80565  # 80000
    if ERROR:  # 80005
        goto(80500)  # &&&&&
    # ?OPEN "STUGA.SPA" FOR OUTPUT AS FILE #1 #&&&&&  # 80100
    if ERROR:  # 80102
        goto(97000)  # &&&&&
    # ?MARGIN #1,132
    # ?QUOTE #1
    X = 0  # &&&&&  # 80105
    print()  # 1,A[I]; FOR I=0 TO A[0] #&&&&&  # 80110
    for i in range(0, A[0]):
        X = X + A[I] / (PI)  # &&&&&  # 80115
    print()  # 1 #&&&&&  # 80120
    print()  # 1,S(I); FOR I=0 TO S[0] #&&&&&  # 80125
    for i in range(0, S[0]):
        X = X + S[I] / (PI - 1)  # &&&&&  # 80127
    print()  # 1 #&&&&&  # 80130
    print()  # 1,G/2,Z*7,X+G+Z #&&&&&  # 80131
    for I in range(0, S[24]):  # &&&&&):# 80132
        if W_(I) == "":
            print()  # 1,"-----"
        else:
            print()  # 1,W_(I) #&&&&&  # 80135

    print()  # 1,J(I); FOR I=0 TO J[0] #&&&&&  # 80140
    # ? CLOSE 1 #&&&&&  # 80150
    print("Det nuvarande läget är sparat på filen STUGA.SPA.")  # &&&&&  )# 80155
    goto(12210)  # &&&&&  # 80160  # 80000


def call_method_80200():
    print('TODO: Detta är inte implementerat än.')
    return

    # *** ÅTERSKAPA *** #&&&&&  # 80200
    if ERROR:  # 80202
        goto(80500)  # &&&&&
    # ? OPEN "STUGA.SPA" FOR_ = input() # AS FILE #1 #&&&&&  # 80205
    if ERROR:  # 80210
        goto(80520)  # &&&&&
    MARGIN  # 1,132
    X = 0  # &&&&&  # 80300
    _ = input()  # #1,A[0] #&&&&&  # 80305
    _ = input()  # #1,A[I] FOR I=1 TO A[0] #&&&&&  # 80310
    for i in range(0, A[0]):
        X = X + A[I] / (PI)  # &&&&&  # 80315
    # ?_ = input() # #1,S[0] #&&&&&  # 80318
    if S[0] == 0:
        S[0] = 53  # _____ Standardvärde. Raden bör tas bort småningom #&&&&&  # 80319
    # ?_ = input() # #1,S(I) FOR I=1 TO S[0] #&&&&&  # 80320
    for i in range(0, S[0]):
        X = X + S(I) / (PI - 1)  # &&&&&  # 80325
    if S[24] == 0:
        S[24] = 6  # _____ #&&&&&  # 80326
    if ERROR:  # 80327
        goto(80540)  # _____ Koll om gammal fil. Raden bör tas bort. #&&&&&
    # ?_ = input() # #1,G,Z,I1 #&&&&&  # 80329
    # ?_ = input() # #1,W_(I) FOR I=0 TO S[24] #&&&&&  # 80330
    for i in range(0, S[24]):
        if FNL_(W_[I], 5) == "-----":
            W_[I] = ""  # &&&&&  # 80332
    # ?IF END#1:
    # ?      goto(80340) #_____ #&&&&&  # 80336
    _ = input()  # #1,J[0]  # 80337
    _ = input()  # #1,J(I) FOR I=1 TO 100  # 80338
    G = G * 2
    Z = Z / 7  # &&&&&  # 80340
    X = X + G + Z  # &&&&&  # 80341
    # ? CLOSE 1 #&&&&&  # 80342
    if ERROR:  # 80343
        goto(97000)  # &&&&&
    if ABS(X - I1) > 0.03:
        print("Fel på STUGA.SPA!")
    STOP  # &&&&&  )# 80345
    S2 = 1  # Återskapaflagga #&&&&&  # 80347
    if Z == 4:
        goto(41000)  # &&&&&  # 80350
    if Z < 8 or Z > 100:
        print("Fel i STUGA.SPA!")
    STOP  # &&&&&  )# 80355
    if Z < 20:
        goto(
            [
                9991,
                15050,
                15000,
                15300,
                16000,
                16500,
                17000,
                25000,
                10020,
                40000,
                9300,
                2044,
            ][Z - 7]
        )  # &&&&&  # 80360
    if Z < 31:
        goto(
            [2115, 9000, 9035, 9065, 9145, 2075, 9175, 9100, 9020, 9190, 21100][Z - 19]
        )  # &&&&&  # 80365
    if Z < 41:
        goto(
            [21340, 7570, 2066, 1909, 7556, 8300, 8330, 8071, 8095, 8365][Z - 30]
        )  # &&&&&  # 80370
    if Z < 51:
        goto(
            [8381, 8400, 8000, 8020, 8035, 15350, 15370, 15386, 9361, 2200][Z - 40]
        )  # &&&&&  # 80375
    if Z < 61:
        goto(
            [2241, 8420, 1500, 9490, 9510, 9545, 9558, 13000, 13235, 9528][Z - 50]
        )  # &&&&&  # 80380
    if Z < 71:
        goto(
            [36000, 13173, 36050, 14000, 14100, 20180, 20240, 20255, 2019, 20000][Z - 60]
        )  # &&&&&  # 80385
    if Z < 81:
        goto(
            [20020, 20030, 20040, 20055, 20070, 20085, 20107, 9390, 20155, 20143][Z - 70]
        )  # &&&&&  # 80390
    if Z < 91:
        goto(
            [20200, 20165, 20270, 20285, 20300, 20315, 20330, 9424, 1929, 15432][Z - 80]
        )  # &&&&&  # 80395
    goto(
        [2033, 1919, 1950, 1960, 1970, 25130, 8148, 2150, 2127, 35000][Z - 90]
    )  # &&&&&  # 80400
    print("? Kan inte öppna STUGA.SPA.")  # &&&&&  )# 80500
    # ? #? RESUME 80510 #&&&&&  # 80505
    if ERROR:  # 80510
        goto(97000)  # &&&&&
    goto(12210)  # &&&&&  # 80515
    print("Fel inuti STUGA.SPA!")  # &&&&&  )# 80520
    # ? CLOSE 1 #&&&&&  # 80525
    # ? #? RESUME 99999 #&&&&&  # 80530
    # ? #? RESUME 80545 #_____ Raderna 80540-80565 bör tas bort småningom. #&&&&&  # 80540
    if ERROR:  # 80545
        goto(80520)  # &&&&&
    _ = input()  # #1,W_(I) FOR I=0 TO 6 #&&&&&  # 80550
    _ = input()  # #1,W_(3) #Starttid #&&&&&  # 80552
    _ = input()  # #1,A1_ FOR I=8 TO 14 #&&&&&  # 80555
    _ = input()  # #1,G,Z,I1 #&&&&&  # 80560
    goto(80332)  # _____ #&&&&&  # 80565


# == MAIN ==

def call_method_12200():
    if _DEBUG:
        time.sleep(0.5)
        print('call_method_12200')
    #  #XXXXX ALLMÄN GOSUBRUTIN XXXXXX  # 12200
    call_method_6000()  # 12201
    print()  # 12202
    if S1 < 2:
        A_ = FNI_("")
    print()  # 12203
    call_method_12000()  # 12204
    # ? return  # 12208
    print()  # XXXX INMATNINGSRUTIN XXXX  )# 12210
    if S[49] == 0 and S[30] == Z and Z != 96:
        X1 = 1
    goto(30000)  # 12211
    if S < 9 and Z == 60:
        goto(12999)  # 12212
    A_ = FNI_("")  # 12213
    print()  # 12214
    if S[36] == 1:
        goto(8600)
    else:
        call_method_12000()  # 12215
    if A[10] == 5 or A[10] == 53:
        print("Ingenting händer.")
    goto(12210)  # 12220
    if A[10] == 1:
        goto(12226)  # 12223
    if Z == 53:
        print("Nu hänger lagerkransen på väggen.")
    else:
        print("Ok.")  # 12224
    A[10] = 53
    goto(12210)  # 12225
    S[1] = S[1] - 1
    A[10] = 53  # 12226
    if Z == 53:
        goto(12224)  # 12227
    print("Lagerkransen försvinner.")
    goto(12210)  # 12228
    if A[21] != 1:
        print("Du har ingenting du kan gräva med.")
    goto(12210)  # 12230
    if Z != 77:
        print("Marken är för hård.")
    goto(12210)  # 12232
    if S[20] == 1:
        print("Platsen är redan helt utgrävd.")
    goto(12210)  # 12234
    X = 13
    goto(12999)  # 12236
    if FNL_(C_, 5) == "GUBBE" or (C_ == "" and S[30] == Z):
        goto(30050)  # 12240
    if FNL_(C_, 4) == "VAKT" or (C_ == "" and (A[29] == Z or A[29] == 1)):
        goto(28010)  # 12242
    print("Det finns inget du kan döda här.")
    goto(12210)  # 12248
    if C_ != "":
        A_ = C_
    goto(12214)  # 12255
    print("Åt vilket håll?")  # 12260
    A_ = FNI_("")  # 12261
    goto(12214)  # 12262
    if FNL_(C_, 5) == "BRÄNN":
        goto(12280)  # 12270
    if FNL_(C_, 5) == "VATTE":
        goto(12282)  # 12272
    if C_ != "":
        call_method(11000)
    goto(12210)  # 12274
    C_ = FNI_("Drick vad ?")  # 12276
    C_ = FNC_(C_)
    goto(12270)  # 12278
    if A[18] == 1 and S[31] == 0:
        goto(12310)
    else:
        goto(12306)  # 12280
    if A[19] == 1 and S[32] == 0:
        goto(12292)  # 12282
    if Z == 25 or Z == 33 or Z == 49 or Z == 50 or Z == 66 or Z == 70:
        goto(12296)  # 12284
    if Z == 72 or Z == 74 or Z == 78 or Z == 79 or Z == 83 or Z == 87 or Z == 88:
        goto(12296)  # 12286
    if Z == 91:
        print("Du dricker ur vattenfallet.")
    goto(12300)  # 12288
    print("Jag ser inget VATTEN här.")
    goto(12210)  # 12290
    print("Du dricker ur vattenflaskan.")  # 12292
    S[32] = 1
    goto(12300)  # 12294
    print("Du dricker ur sjön.")  # 12296
    print("Klunk...klunk...klunk......AHHHH!")  # 12300
    goto(12210)  # 12302
    print("Jag ser inget BRÄNNVIN här.")
    goto(12210)  # 12306
    print("Du dricker ur brännvinsflaskan.")  # 12310
    print("Klunk...klunk...klunk......HICK    !")  # 12312
    for I in range(1, 9):  # 12314
        S = time.sleep(3)  # 12316
        print(TAB(random.randint(0, 6) + 1) + "HICK    !")  # 12318
    print()
    S[31] = 1  # 12322
    print("Nu hoppas jag att vi har nyktrat till så pass att vi kan fortsätta!")  # 12324
    goto(12210)  # 12326
    if FNL_(C_, 5) == "GUBBE" or (C_ == "" and S[30] == Z):
        goto(30010)  # 12340
    if FNL_(C_, 4) == "VAKT" or (C_ == "" and (A[29] == Z or A[29] == 1)):
        goto(12360)  # 12341
    if INSTR(C_, "BRÄNN") > 0:
        goto(12306)  # 12342
    if INSTR(C_, "VATTE") > 0:
        goto(12380)  # 12344
    if C_ == "FYLL" or INSTR(C_, "FLASKA") > 0:
        goto(12350)  # 12346
    call_method(11000)
    goto(12210)  # 12348
    if A[18] == 1 or A[19] == 1:
        C_ = FNI_("Fyll med vad ?")
    C_ = FNC_(C_)
    goto(12340)  # 12350
    print("Du har ju ingen flaska!")
    goto(12210)  # 12354
    if A[29] != Z and A[29] != 1:
        print("Jag ser ingen VAKT här.")
    goto(12210)  # 12360
    if S[6] == 2:
        print("Vakten är ju död.")
    goto(12210)  # 12361
    if S[6] == 3:
        print("Han sover för djupt.")
    goto(12210)  # 12362
    if A[18] != 1:
        print("Du har inget att fylla honom med.")
    goto(12210)  # 12364
    if S[31] == 1:
        print("Din brännvinsflaska är tom.")
    goto(12210)  # 12366
    S[31] = 1
    S[51] = S[50]  # 12368
    print("Vakten dricker upp ditt brännvin i en enda klunk.")  # 12370
    if S[6] == 0:
        S[6] = 1
    goto(12210)  # 12372
    print("Den nu redlöst fulle vakten ramlar ihop i en hög på golvet och somnar.")  # 12374
    S[6] = 3
    A[29] = Z  # 12376
    goto(12210)  # 12378
    if A[19] != 1:
        print("Du bär ingen vattenflaska som du kan fylla.")
    goto(12210)  # 12380
    if S[32] == 0:
        print("Din vattenflaska är så full den kan bli.")
    goto(12210)  # 12382
    if Z == 25 or Z == 33 or Z == 49 or Z == 50 or Z == 66 or Z == 70 or Z == 72:
        goto(12390)  # 12384
    if Z == 74 or Z == 78 or Z == 79 or Z == 83 or Z == 87 or Z == 88 or Z == 91:
        goto(12390)  # 12386
    goto(12290)  # 12388
    print("Du fyller vattenflaskan med vatten från ")  # 12390
    if Z == 91:
        print("vattenfallet.")
    else:
        print("sjön.")  # 12392
    S[32] = 0
    goto(12210)  # 12394
    if Z == 81:
        X = 3  # 12400
    if Z == 50:
        X = 4  # 12402
    if Z == 99 or Z == 55:
        X = 5  # 12404
    if Z == 30:
        S[23] = 1
    print("I garderoben hittar du ett kassaskåp.")
    goto(12210)  # 12406
    if X > 0:
        goto(12999)
    else:
        goto(12089)  # 12408
    if Z == 8 or Z == 51 or Z == 100:
        X = 6  # 12420
    if X > 0:
        goto(12999)
    else:
        goto(12082)  # 12428
    if Z == 81 or Z == 8:
        goto(12450)  # 12440
    if Z == 30:
        goto(12456)  # 12442
    if Z == 62 and S[7] == 0:
        print("Porten är låst.")
    goto(12210)  # 12444
    goto(12083)  # 12448
    if S[19] == 1:
        print("Dörren är ju redan öppen!")  # 12450
    if S[19] != 1:
        print("Dörren öppnas med ett gnäll    .")  # 12452
    S[19] = 1
    X = 19
    goto(12999)  # 12454
    if INSTR(A_, "GARDE") > 0 or (C_ == "" and S[23] == 0):
        goto(12466)  # 12456
    if INSTR(A_, "KASSA") == 0 and C_ != "":
        goto(12083)  # 12458
    if Z == 31:
        print("Kassaskåpet är redan öppet.")
    goto(12210)  # 12460
    print("Dörren är utan handtag och lås.")
    goto(12210)  # 12464
    if S[23] == 1:
        print("Garderoben är redan öppen.")
    goto(12210)  # 12466
    print("Du öppnar garderoben och hittar ett litet kassaskåp där.")  # 12468
    S[23] = 1
    goto(12210)  # 12469
    if Z == 30:
        goto(12480)  # 12470
    if Z == 31:
        goto(12486)  # 12472
    goto(12084)  # 12478
    if S[23] == 0:
        print("Garderoben är redan stängd.")
    goto(12210)  # 12480
    print("Ok.")
    S[23] = 0
    goto(12210)  # 12482
    if INSTR(A_, "GARDE") > 0 or (C_ == "" and S[23] == 1):
        goto(12494)  # 12486
    if INSTR(A_, "KASSA") == 0 and C_ != "":
        goto(12084)  # 12488
    print("Kassaskåpet stängs sakta.")  # 12490
    Z = 30
    goto(12999)  # 12492
    print("Kassaskåpet och garderoben stängs.")  # 12494
    S[23] = 0
    goto(12492)  # 12496
    if Z != 63 and Z != 61:
        print("Marken är för hård!")
        goto(12210)  # 12510
    if FNL_(C_, 3) != "LIK" and FNL_(C_, 4) != "VAKT" and (C_ == "" and A[22] != 1):
        goto(12526)  # 12512
    if A[29] == 1 or A[29] == Z:
        print("Du kan inte begrava en levande!")
        goto(12210)  # 12514
    if A[22] != 1 and A[22] != Z:
        print("Du har inget sånt att begrava!")
        goto(12210)  # 12516
    if A[22] == 63:
        print("Liket är redan begravt!")
        goto(12210)  # 12518
    if A[22] == 1:
        S[1] -= 1  # 12520
    A[22] = 63
    S[2] = S[2] + 25
    S[52] = S[50]  # 12522
    print("Ok.")
    goto(12210)  # 12524
    print("Man kan bara begrava lik!")
    goto(12210)  # 12526
    I = INSTR(A_, " ")  # ============ SKRIK  # 12550
    if I == 0 or I == len(A_):
        print("AAAAAAARRRRRRRRRR    GHHHHH    H!")
    else:
        print("Ok. " + FNM_(A_, I + 1))  # 12551
    goto(12210)  # 12553
    # ===================================SVÄRORD========  # 12555
    print("Vilket språk!")  # 12557
    goto(12210)  # 12559
    # ============================VÄNTA========STANNA=====  # 12570
    print("Ok." + FNS_("väntar", 10))  # 12572
    if Z == 37:
        goto(12999)
    else:
        print("Så där ja!")  # 12574
    goto(12210)  # 12576
    if S[21] > 0:
        print("Du kan inte sparka något med vrickade fötter!")
    goto(12210)  # 12580
    if (FNL_(C_, 4) == "BOLL" or C_ == "") and (A[20] == Z or A[20] == 1):
        goto(12120)  # 12582
    print("AJ! Du vrickar dina fötter.")  # 12584
    S[21] = S[50]  # 12586
    goto(12210)  # 12588
    if Z != 23:
        print("Ok.")
    goto(12210)  # 12590
    print("Oj! Du ramlar själv ner i toaletten.")
    A_ = "SPOLA"  # 12592
    goto(12999)  # 12594
    print("Vad vill du göra med " + A_(I, 4) + "?")  # 12600
    A1_ = FNI_("")
    A_ = A1_ + " " + A_(I, 1)  # 12601
    goto(12214)  # 12610
    if INSTR(A_, "KATAL") > 0:
        goto(12670)  # 12650
    if INSTR(A_, "KONTR") > 0:
        goto(12700)  # 12652
    if INSTR(A_, "TRILO") > 0:
        goto(12710)  # 12654
    if INSTR(A_, "LOGGF") > 0:
        goto(12975)  # &&&&&  # 12655
    if INSTR(A_, "KLOCK") > 0:
        goto(12740)  # 12656
    if INSTR(A_, "GRAV") > 0 or INSTR(A_, "STEN") > 0:
        goto(12750)  # 12657
    if A_ != "LÄS":
        call_method(11000)
    goto(12210)  # 12658
    A_ = FNI_("Vad vill du läsa ?")
    A_ = FNC_(A_)
    goto(12650)  # 12660
    if A[23] != 1 and A[23] != Z:
        print("Jag ser ingen KATALOG här.")
    goto(12210)  # 12670
    print()  # 12672
    print("    TELEFONKATALOG ÖVER STUGAN")  # 12674
    print("Telefonnr:    Abonnent:")  # 12676
    print("   000        Stugas televerk")  # 12678
    print("   100        Stugan")  # 12680
    print("   307        Hissreparatören")  # 12682
    print("   323        Glasmästaren")  # 12684
    print("   405        Personalköket")  # 12686
    print("   481        Vakten")  # 12688
    print("   999        Larmcentralen")  # 12690
    goto(12210)  # 12698
    if A[9] != 1 and A[9] != Z:
        print("Jag ser inget KONTRAKT här.")
    goto(12210)  # 12700
    print("Tyvärr är kontraktet skrivet med Kermits oläsliga handstil.")  # 12702
    print()
    goto(12210)  # 12704
    if A[8] != 1 and A[8] != Z:
        print("Jag ser ingen TRILOGI här.")
    goto(12210)  # 12710
    print()  # 12712
    print("Tre ringar för älvkungarnas makt högt i det blå,")  # 12714
    print("sju för dvärgarnas furstar i salarna av sten,")  # 12716
    print("nio för de dödliga, som köttets väg skall gå,")  # 12718
    print("en för Mörkrets herre i ondskans dunkla sken")  # 12720
    print("i Mordorslandets hisnande gruva.")  # 12722
    print()
    print("En ring att sämja dem,")  # 12724
    print("en ring att främja dem,")  # 12726
    print("en ring att djupt i mörkrets")  # 12728
    print("vida riken tämja dem -")  # 12730
    print("i Mordors land, där skuggorna ruva...")  # 12732
    print()  # 12734
    goto(12210)  # 12736
    if A[6] != 1 and A[6] != Z:
        print("Jag ser ingen KLOCKA här.")
    goto(12210)  # 12740
    print(TIME_)  # 12742
    goto(12210)  # 12744
    if Z != 61:
        print("Jag ser ingen GRAVSTEN här.")
    goto(12210)  # 12750
    if len(W_(6)) == 0:
        print("Gravstenen är tom.")
    goto(12210)  # 12752
    print("Här vilar sej " + W_(6) + ".")  # 12754
    print(W_(6) + " försvann in i ett okänt hus klockan " + W_(3))  # 12756
    if W_(4) == DATE_:
        print()
    else:
        print(" " + W_(4))  # 12757
    print("och sågs aldrig mer.")  # 12758
    print()
    goto(12210)  # 12760
    print("INFORMATION OM VISSA KOMMANDON:")  # 12770
    print("Förflyttning inomhus:")  # 12772
    print("UPPÅT, NERÅT, FRAMÅT, BAKÅT, VÄNSTER, HÖGER (U, N, F, B, V, H)")  # 12774
    print("Förflyttning utanför huset:")  # 12776
    print("NORR, SÖDER, VÄSTER, ÖSTER (N, S, V, Ö) NV, NÖ, SV, SÖ")  # 12778
    print("INVENT skriver allt man bär på")  # 12780
    print("HJÄLP  ger ibland hjälp")  # 12781
    print("POÄNG  visar hur många poäng man har fått")  # 12782
    print("TITTA  ger hela rumsbeskrivningen")  # 12783
    print("SPARA  sparar spelat på fil")  #                         &&&&&  )# 12784
    print("ÅTERSKAPA  hämtar tillbaka spelet")  #                   &&&&&  )# 12785
    print("LOGGA  skriver en loggfil med alla kommandon man ger")  # &&&&&  )# 12787
    print("LÄS LOGGFIL  utför kommandona i en loggfil")  #          &&&&&  )# 12788
    print("SLUTA  slutar")
    goto(12210)  # 12789
    if A[25] == 1 and (J[Z] == 1 or S[44] == Z):
        print("Du HÅLLER ju i telefonsladden.")  # 12800
    if A[25] != 1 and A[25] != Z:
        print("Jag ser ingen TELEFON här.")  # 12802
    if J[Z] != 1 and S[44] != Z:
        print("Jag ser ingen TELEFONJACK här.")  # 12804
    if (J[Z] != 1 and S[44] != Z) or A[25] != Z:
        goto(12210)  # 12806
    if C_ == "":
        C_ = FNI_("Ring vart:")  # 12808
    if INSTR(C_, "000") > 0:
        goto(27250)  # 12810
    if INSTR(C_, "100") > 0:
        goto(27600)  # 12812
    if INSTR(C_, "307") > 0 or INSTR(C_, "323") > 0:
        goto(27620)  # 12814
    if INSTR(C_, "405") > 0:
        goto(27200)  # 12816
    if INSTR(C_, "481") > 0:
        goto(27630)  # 12818
    if INSTR(C_, "900") > 0:
        goto(27400)  # 12821
    if FNC_(C_) == "HEM":
        goto(12835)  # 12822
    print("Du hör en röst säja:")  # 12826
    print("- Ingen abonnent på det numret.")  # 12828
    goto(12210)  # 12830
    if W_(6) == "":
        print("Du hör din egen röst:  - Jag är inte hemma än!")
    goto(12210)  # 12835
    print("Du hör en röst säja:")  # 12836
    print("- Detta är ", W_(6), "s telefonsvarare. ", W_(6), " är inte hemma.")  # 12837
    goto(12210)  # 12838
    if S[30] != Z:
        print("Du kan inte ge något till någon här.")
        goto(12210)  # 12840
    if I == 10 or I == 19:
        goto(7030)  # 12842
    if INSTR(C_, "VATTE") > 0:
        goto(30010)  # 12844
    print("Gubben tar inte emot det.")
    goto(12210)  # 12846
    if A[24] != 1:
        print("Du har inget att blända med.")
    goto(12210)  # 12850
    if FNL_(C_, 5) == "GUBBE" or (C_ == "" and S[30] == Z):
        goto(12860)  # 12851
    if FNL_(C_, 4) == "VAKT" or (C_ == "" and (A[29] == Z or A[29] == 1)):
        goto(12880)  # 12852
    print("Du kan inte blända någon här.")
    goto(12210)  # 12854
    if S[30] != Z:
        print("Jag ser ingen GUBBE här.")
    goto(12210)  # 12860
    if A[19] == 0:
        print("Du försöker blända gubben men han häller")  # 12864
    if A[19] == 0:
        print("vattenflaskan som skydd.")
    goto(12210)  # 12866
    if S[49] == 0 or S[49] == 2 or S[30] == 96:
        goto(30002)  # 12868
    S[49] = 2
    print("Du bländar den stackars gubben med lampan.")
    goto(12210)  # 12870
    if (A[29] == Z or A[29] == 1) and S[6] != 2:
        print("Du klarar inte av att blända vakten.")
    goto(12210)  # 12880
    if S[6] == 2:
        print("Vakten är död.")
    else:
        print("Jag ser ingen VAKT här.")  # 12881
    goto(12210)  # 12882
    if Z == 25 or Z == 33 or Z == 49 or Z == 50 or Z == 66 or Z == 70:
        X = 10
    goto(12999)  # 12890
    if Z == 72 or Z == 74 or Z == 78 or Z == 79 or Z == 83 or Z == 87 or Z == 88:
        X = 10
    goto(12999)  # 12892
    if Z == 91:
        print("Vattenfallets vatten är alldeles för kallt.")
    goto(12210)  # 12893
    print("Här finns det inget vatten.")
    goto(12210)  # 12894
    if A[20] != 1:
        print("Du har inget att pumpa.")  # 12900
    if A[16] != 1:
        print("Du har inget att pumpa med.")  # 12902
    if A[20] == 1 and S[33] == 0:
        print("Din boll är redan pumpad.")  # 12904
    if A[16] == 1 and A[20] == 1 and S[33] == 1:
        print("Ok.")
    S[33] = 0  # 12906
    goto(12210)  # 12908
    if INSTR(A_, "RÖVAR") > 0:
        print("Jag ser ingen RÖVARE här.")
    goto(12210)  # 12910
    if INSTR(A_, "GUBBE") > 0:
        goto(12920)  # 12912
    if INSTR(A_, "EFTER") > 0:
        print("Jag ser ingen du kan följa efter.")
    goto(12210)  # 12914
    if (INSTR(A_, "RÅD") > 0 or INSTR(A_, "THORVALD") > 0) and Z == 59:
        goto(12924)  # 12916
    goto(12088)  # 12918
    if S[30] == Z:
        print("Gubben sitter ju här!")
    goto(12210)  # 12920
    print("Jag ser ingen GUBBE här.")
    goto(12210)  # 12922
    print("Du ska inte ha någon fördel bara för att Stugrådet råkar ha samman-")  # 12924
    print("träde när du ramlar in. Du får försöka hitta skattkammaren själv.")  # 12926
    print("(Förresten har dom redan försvunnit!)")
    goto(12210)  # 12928
    # ?if M2%==1%:
    # ?     goto(12970) #&&&&&  # 12950
    print("Vad heter loggfilen")
    # ?_ = input() # LINE M2_ #&&&&&  )# 12951
    if ERROR:
        goto(12962)  # &&&&&  # 12952
    # ?OPEN M2_ FOR OUTPUT AS FILE #2 #&&&&&  # 12954
    if ERROR:
        goto(97000)  # &&&&&  # 12956
    print("Nu loggas alla kommandon på filen " + M2_)  # &&&&&  )# 12958
    # ?M2%=1%
    W_ = CHR_(3)
    goto(12210)  # &&&&&  # 12960
    # ?#? RESUME 12964 #&&&&&  # 12962
    if ERROR:
        goto(97000)  # &&&&&  # 12964
    print("? Jag kan inte öppna " + M2_)  # &&&&&  )# 12966
    goto(12210)  # &&&&&  # 12968
    # ?M2%=0%
    # ?CLOSE 2 #&&&&&  # 12970
    print("Loggningen på " + M2_ + " avslutad.")  # &&&&&  )# 12972
    goto(12210)  # &&&&&  # 12974
    print("Vad heter loggfilen")
    # ?_ = input() # LINE M3_ #&&&&&  )# 12975
    # ?if M3_=="":
    # ?      goto(12210)
    # ?else:
    # ?  if M3%=1%:
    # ?     CLOSE 3
    # ?M3%=0% #&&&&&  # 12976
    if ERROR:
        goto(12985)  # &&&&&  # 12977
    # ?OPEN M3_ FOR_ = input() # AS FILE #3 #&&&&&  # 12979
    if ERROR:
        goto(97000)  # &&&&&  # 12981
    # ?M3%=1%
    goto(12210)  # &&&&&  # 12983
    # ?#? RESUME 12987 #&&&&&  # 12985
    print("? Jag kan inte öppna " + M3_)  # &&&&&  )# 12987
    if ERROR:
        goto(97000)  # &&&&&  # 12988
    goto(12210)  # &&&&&  # 12989
    if S[30] == Z:  # 12999
        goto(30000)
    else:
        pass  # ? return
    Z = 58  # XXX FARSTUN XXXXX  # 13000
    print("Du är i farstun, ett litet rum med en dörr bakom dej")  # 13002
    print("och en stor portal rakt fram.")  # 13003
    call_method_12200()  # 13004
    if X1 == 1:
        goto(13000)  # 13005
    if X > 4:
        goto([13173, 7570, 13010][X - 4])  # 13006
    call_method(11000)  # 13008
    goto(13000)  # 13009
    if S[6] > 0 or A[29] != Z:
        goto(13008)  # 13010
    print("Det finns en sak som kan påverka vakten.")  # 13012
    S[2] = S[2] - 10  # 13014
    goto(13000)  # 13016
    call_method(11000)  # 13172
    Z = 62  # XXX PORTEN XXX  # 13173
    print("Du står vid en jättelik, utsmyckad port.")  # 13175
    call_method_12200()  # 13176
    if X > 5:
        goto([13000, 13195][X - 5])  # 13177
    if X == 5 and S[7] == 1:
        goto(13220)  # 13178
    if X == 5:
        print("Porten är låst.")
    goto(13173)  # 13179
    if X1 == 1:
        goto(13173)  # 13180
    if FNL_(A_, 3) != "LÅS":
        goto(13172)  # 13184
    if INSTR(A_, "UPP") > 0:
        goto(13200)  # 13186
    if S[7] == 0:
        print("Porten är redan låst.")
    goto(13173)  # 13188
    print("Det går inte utan nycklar.")
    goto(13173)  # 13190
    if S[7] != 0 or S[26] == 1:
        goto(13172)  # 13195
    if A[26] != 2:
        print("Vakten orkar låsa upp porten, men han har inga nycklar.")  # 13196
    if A[26] == 2:
        print("Ta hit vakten och lås upp porten.")  # 13197
    S[2] = S[2] - 15
    goto(13173)  # 13198
    if S[7] == 1:
        print("Porten är redan upplåst.")
    goto(13173)  # 13200
    if A[26] == 1:
        print("Du orkar inte vrida om nyckeln själv.")
    goto(13173)  # 13202
    if A[29] != 1 or A[26] != 2:
        print("Det går inte.")
    goto(13173)  # 13204
    print("Vakten låser upp porten.")  # 13206
    print("Han tittar på nycklarna ett slag, innan han äter upp dom.")  # 13208
    S[7] = 1
    A[26] = 0
    S[2] = S[2] + 10
    goto(13173)  # 13218
    if S[26] == 1:
        goto(13235)
    else:
        S[26] = 1  # 13220
    print("Du har kommit in i matrummet. Här har Stugrådet sammanträde.")  # 13222
    print("Just nu pratar ordföranden, Thorvald:")  # 13223
    call_method(700)  # 13224
    print(" - Vi har samlats till detta krismöte för att diskutera den")  # 13225
    print("   allvarliga frågan om stugforskarnas kvalitet. Jag, och många")  # 13226
    print("   med mej, anser att stugforskarnas kvalitet genomgående har")  # 13227
    print("   försämrats.")  # 13228
    print("Kimmo:")  # 13229
    print(" - Jag håller med dej. Titta bara på den som kom in nu! Jag")  # 13230
    print("   föreslår att vi fortsätter vårt sammanträde i skattkammaren.")  # 13231
    print("Hela församlingen reser sej och ger sej iväg.")  # 13232
    print()  # 13233
    Z = 59
    print("Du är i husets matrum. Väggarna är målade i rött och guld.")  # 13235
    if S[15] == 0:
        print("En trappa leder uppåt.")  # 13237
    if S[15] == 1:
        print("En trappa har gått uppåt, men är nu obrukbar.")  # 13238
    call_method_12200()  # 13241
    if X != 0:
        goto([13247, 13245, 13245, 13245, 13245, 13173, 13245][X])  # 13244
    call_method(11000)  # 13245
    goto(13235)  # 13246
    if S[15] == 0 and A[1] != 1:
        goto(40000)  # 13247
    if S[15] == 1:
        goto(13252)  # 13248
    print("Trappan rasar ihop.")  # 13249
    S[15] = 1  # 13250
    goto(13235)  # 13251
    print("Trappan är avspärrad av stugas gatukontor.")  # 13252
    goto(13235)  # 13253
    Z = 64  # XXXXX MÖRKA GÅNGEN XXXXX  # 14000
    print("Du är i en mörk gång. Framåt är en öppning.")  # 14004
    print("Till vänster skymtar man en grind och till höger en panna.")  # 14008
    print("Det finns ett hål i golvet och en gång går snett bakåt-uppåt.")  # 14010
    call_method_12200()  # 14012
    if X1 == 1:
        goto(14000)  # 14018
    if X != 0:
        goto([9490, 1909, 14030, 14100, 8000, 9490, 14022][X])  # 14020
    call_method(11000)  # 14022
    print("Du är i en mörk gång.")
    goto(14012)  # 14024
    print("Du går genom en grind som går i lås bakom dej.")  # 14030
    goto(20040)  # 14032
    print("Grinden öppnar sej och du går in.")  # 14034
    print("BA    NG!!  Grinden stängs bakom dej!")  # 14036
    goto(14000)  # 14038
    call_method(11000)  # 14099
    Z = 65  # XXXXX PANNRUMMET XXXXX  # 14100
    print("Du är i Pannrummet, en trång gång går snett uppåt-framåt")  # 14106
    print("och en går åt vänster. Till höger fortsätter Pannrummet.")  # 14107
    call_method_12200()  # 14112
    if X == 0:
        goto(14099)  # 14121
    goto([14139, 14099, 15050, 2008, 14139, 14099, 14099][X])  # 14124
    if A[1] != 1:
        goto(14000)  # 14139
    print("Nå #nting du bär på tar emot. Skriv INVENT och släpp det.")  # 14142
    goto(14100)  # 14145
    call_method(11000)  # 14998
    Z = 10
    S[10] = S[10] + 1  # XXXXX KÄLLAREN XXXXX  # 15000
    if S[10] < 3 or S[10] > 7:
        goto(15018)  # 15004
    print("Du är i källaren.")  # 15006
    call_method_12200()  # 15008
    if X1 == 1:
        goto(15018)  # 15012
    if X == 0:
        goto(14998)  # 15013
    goto([16000, 14998, 15300, 16500, 1500, 14998, 14998][X])  # 15014
    print("Du är i källaren. Ett kallt och rått rum med tre dörrar")  # 15018
    print("(vänster,höger och framåt) och en gång uppåt.")  # 15020
    if S[10] > 8:
        S[10] = 4  # 15024
    goto(15008)  # 15026
    Z = 9
    S[9] = S[9] + 1
    S[45] = 2  # XXXXX ÅP-RUMMET XXXXX  # 15050
    if S[9] < 3 or S[9] > 7:
        goto(15066)  # 15056
    print("Du är i ÅP-rummet.")  # 15058
    call_method_12200()  # 15060
    if X != 0:
        goto([15076, 15064, 15386, 14100, 1500, 15078, 15064][X])  # 15062
    call_method(11000)  # 15064
    if S[9] > 8:
        S[9] = 4  # 15066
    print("Du är i ett stort rum som heter ÅP-rummet.")  # 15068
    print("Dörrar leder till vänster och höger men")  # 15070
    print("man kan också gå framåt.")  # 15072
    goto(15060)  # 15074
    print("Tror du att du kan flyga?")
    goto(15058)  # 15076
    print("Du kan inte gå bakåt!")
    goto(15058)  # 15078


def call_method_15200():
    if _DEBUG:
        time.sleep(0.5)
        print('call_method_15200')
    # XXXXX ALLMÄN GOSUBRUTIT XXXXX  # 15200
    call_method_6000()
    print()  # 15202
    if S1 < 2:
        A_ = FNI_("")
    print()  # 15203
    call_method(8600)  # 15204
    # ? return  # 15205
    call_method(11000)  # 15299
    Z = 11  # XXX Hilbertrummet XXX  # 15300
    print(
        "Du är i Hilbertrummet, ett rum med fyra dörrar och hål i taket och golvet."
    )  # 15302
    if A[17] == 11:
        print("En stege är uppställd mot hålet i taket.")  # 15304
    call_method_12200()  # 15306
    if X == 0 or X > 6:
        goto(15299)  # 15308
    goto([15312, 17000, 16000, 15000, 9145, 16500][X])  # 15310
    if A[17] == 11:
        goto(25000)  # 15312
    print("Du når inte upp till hålet.")
    goto(15300)  # 15314
    call_method(11000)  # 15349
    Z = 46  # XXX TRAPPRUM 1 XXXXXZ=46 XXX  # 15350
    print("Du är i ett rum med två rulltrappor.")  # 15351
    print("Det finns en dörr bakom dej.")  # 15352
    if S[17] == 1:
        print("Den nedåtgående rulltrappan är avspärrad av Stugas gatukontor.")  # 15354
    if S[18] == 1:
        print("Den uppåtgående rulltrappan är avspärrad av Stugas satukontor.")  # 15355
    call_method_12200()  # 15356
    if X == 6:
        goto(9991)  # 15357
    if X == 1 and S[18] == 0:
        goto(15370)  # 15358
    if X == 2 and S[17] == 0:
        goto(15386)
    else:
        goto(15349)  # 15359
    call_method(11000)  # 15369
    Z = 47  # XXX TRAPPRUM 2 XXX  # 15370
    print("Du är i ett rum med en nedåtgående rulltrappa och en dörr åt höger.")  # 15372
    if S[18] == 1:
        print("Rulltrappan är avspärrad av Stugas gatukontor.")  # 15373
    call_method_12200()  # 15374
    if X == 4:
        goto(9035)  # 15375
    if A[1] == 1 and X == 2 and S[18] == 0:
        goto(15382)  # 15376
    if X == 2 and S[18] == 0:
        goto(15350)
    else:
        goto(15369)  # 15377
    print("Just när du går fram mot rulltrappan, stannar den och en")  # 15382
    print("gubbe springer fram och spärrar av den.")  # 15383
    S[18] = 1
    goto(15370)  # 15384
    call_method(11000)  # 15385
    Z = 48  # XXX TRAPPRUM 3 XXXXX  # 15386
    print("Du är i ett rum med en uppåtgående rulltrappa och en dörr framåt.")  # 15388
    if S[17] == 1:
        print("Rulltrappan är avspärrad av Stugas gatukontor.")  # 15390
    call_method_12200()  # 15392
    if X == 5:
        goto(15050)  # 15394
    if X != 1 or S[17] != 0:
        goto(15385)
    else:
        if A[1] != 1:
            goto(15350)  # 15396
    print("Just när du går fram mot rulltrappan, stannar den och en")  # 15398
    print("gubbe springer fram och spärrar av den.")  # 15399
    S[17] = 1
    goto(15386)  # 15400
    Z = 90  # XXXXX TRAPPRUM 4 XXXXX  # 15425
    print("Dörren öppnar sej och du går in i ett rum")  # 15427
    print("med två trappor och en dörr bakåt.")  # 15428
    call_method_12200()  # 15429
    if X > 0:
        goto([16000, 9145, 15431, 15431, 15431, 15434, 15438][X])  # 15430
    call_method(11000)  # 15431
    print("Du är i trapprummet.")
    Z = 90  # 15432
    goto(15429)  # 15433
    if A[1] != 1:
        goto(9991)  # 15434
    print("Dörren har gått i baklås.")  # 15435
    if A[26] == 1 or A[26] == 90:
        print("Din nyckel passar inte i låset!")  # 15436
    goto(15432)  # 15437
    if A[1] == 1:
        print("TIPS!! Något du bär hindrar dej att gå bakåt!")
    goto(15432)  # 15438
    goto(15431)  # 15439
    Z = 12
    S[12] = S[12] + 1  # XXXXX VINDEN XXXXX  # 16000
    if S[12] > 2 and S[12] < 8:
        print("Du är på vinden.")
    goto(16055)  # 16012
    print("Du är på vinden, ett litet skrymsle högst ner i huset.")  # 16020
    print("Härifrån kan man gå överallt.")  # 16030
    print("På väggen står det: SESAM")  # 16032
    if random.random() < 0.5:
        print("Någon säjer:  - Du kom hit klockan " + W_(3) + " " + W_(4))  # 16040
    if S[12] > 8:
        S[12] = 4  # 16045
    call_method_12200()  # 16055
    if X1 == 1:
        goto(16020)  # 16057
    if X > 0:
        goto([15000, 15432, 9000, 15300, 17000, 16500, 16060][X])  # 16058
    call_method(11000)  # 16060
    print("Du är på vinden.")
    goto(16055)  # 16065
    Z = 13
    S[13] = S[13] + 1  # XXXXX TOMMA RUMMET XXXXX  # 16500
    if S[13] > 2 and S[13] < 8:
        print("Du är i Tomma rummet.")
    goto(16530)  # 16512
    print("Du är i ett tomt rum. Det finns ett hål i taket och en ribbstol")  # 16515
    print("som leder dit. Dörrar leder åt höger och åt vänster.")  # 16517
    if S[13] > 8:
        S[13] = 4  # 16525
    call_method_12200()  # 16530
    if X1 == 1:
        goto(16515)  # 16535
    if X > 0:
        goto([16000, 16545, 15000, 15300, 16545, 16545, 16545][X])  # 16540
    call_method(11000)  # 16545
    print("Du är i Tomma rummet.")
    goto(16530)  # 16550
    Z = 14
    S[14] = S[14] + 1  # XXXXX UNDERLIGA RUMMET XXXXX  # 17000
    if S[14] < 3 or S[14] > 8:
        goto(17100)  # 17005
    print("Du är i Underliga rummet.")  # 17010
    call_method_12200()  # 17020
    if X < 7 and X > 0:
        goto([17150, 17180, 17185, 17195, 17220, 17240][X])  # 17025
    if X1 == 1:
        goto(17100)  # 17031
    call_method(11000)  # 17032
    goto(17010)  # 17033
    print("Du är i ett underligt rum. Dimslöjor sveper kring dina fötter")  # 17100
    print("och du ser gångar i alla riktningar.")  # 17101
    if S[14] > 8:
        S[14] = 4  # 17110
    goto(17020)  # 17120
    print("Jag är ledsen, men det tar lång tid att komma fram här.")  # 17150
    print(FNS_("tar mej fram", 15))  # 17155
    D = random.randint(0, 6) + 1  # 17160
    if D == 1:
        goto(20040)  # 17165
    if D == 3:
        goto(15050)  # 17172
    goto(17182)  # 17175
    D = random.randint(1, 5)  # 17180
    if D == 4:
        goto(40000)  # 17181
    print("Du har vindlat runt i en trång gång och kommer tillbaka.")  # 17182
    goto(17010)  # 17183
    D = random.randint(1, 7)  # 17185
    if D < 3:
        print("Du har en rutten tomat i handen, men den försvinner.")  # 17186
    if D == 5:
        if A[1] != 1:
            goto(9991)
    else:
        goto(14100)  # 17190
    if D == 6:
        goto(14100)  # 17191
    goto(17182)  # 17192
    D = random.randint(1, 10)  # 17195
    if D > 5 and S[2] > 50:
        goto(18000)  # 17197
    if D == 2:
        goto(14100)  # 17205
    if D == 3:
        goto(8000)  # 17210
    goto(17182)  # 17215
    if S[3] > 0 and S[41] == 1:
        goto(9035)  # 17220
    if S[40] == 4:
        goto(1500)  # 17230
    goto(9190)  # 17235
    D = random.randint(0, 9)  # 17240
    if D == 2:
        goto(15370)  # 17245
    goto(17182)  # 17250
    print("Du är i ZZZZ-rummet. Ett stort schackbräde är ritat på golvet.")  # 18000
    if random.random() < 0.3 or A[18] != 1 or S[31] != 1:
        goto(18120)  # 18020
    print("Fozzi kommer fram ur dunklet, utklädd till kung.")  # 18030
    print("Han ser din brännvinsflaska och säjer:")  # 18080
    print("- Det är väl synd att gå omkring här med en tom brännvinsflaska.")  # 18081
    print()
    print("Han tar fram en fickplunta ur kostymen och fyller på")  # 18090
    S[31] = 0  # 18095
    print("din brännvinsflaska.")  # 18100
    print("Fozzi mumlar något om en faun och knuffar ut dej ur rummet.")  # 18105
    goto([40000, 1960, 1960][random.randint(0, 2)])  # 18110
    print("Du trampas på tårna av en faun, så du springer ut igen.")  # 18120
    goto(18110)  # 18125
    if S[2] > 50: # 20000
        print("Du är på bryggan och ser ett hus rakt fram.")  # 20005
    else:
        print("Du står på en brygga någonstans i Småland. Bakom din solvärmda rygg")  # 20001
        print("åker man vattenskidor. En kyrkklocka (som du inte ser) slår tolv.")  # 20002
        print("Du ser ett hus rakt fram.")  # 20003
    pass # 20004
    Z = 70  # 20006
    call_method_15200()  # 20007
    if S1 > 0:  # 20008
        goto(20007)
    if X1 == 1:  # 20009
        goto(20000)
    if X != 0:  # 20010
        goto(
            [20030, 9361, 20200, 20013, 20020, 20013, 20011, 20013, 20070, 2107][X]
        )
    call_method(11000)  # 20011
    goto(20005)  # 20012
    print("Du kan väl inte gå på vattnet?")  # 20013
    goto(20005)  # 20014
    Z = 71  # XXXXX SKOG 1 XXXXX  # 20020
    print("Du är i skogen.")  # 20021
    call_method_15200()  # 20024
    if X != 0:
        goto([20040, 20200, 20028, 20030, 20028, 20055, 20026, 20005, 20028][X])  # 20025
    call_method(11000)  # 20026
    goto(20020)  # 20027
    print("Ett staket hindrar dej att gå ditåt.")  # 20028
    goto(20020)  # 20029
    Z = 72  # XXXX STRAND 1 XXX Z=72 XXXXX  # 20030
    print("Du är på stranden väster om bryggan.")  # 20031
    if S[53] == 1:
        goto(20350)
    else:
        S[53] = S[53] + 1  # 20032
    call_method_15200()  # 20033
    if X != 0:
        goto(
            [20055, 20000, 20020, 20037, 20040, 20037, 20035, 20037, 20200, 2107][X]
        )  # 20034
    call_method(11000)  # 20035
    goto(20030)  # 20036
    print("Du kan väl inte gå på vattnet?")  # 20037
    goto(20030)  # 20038
    Z = 73  # XXXXX SKOG MED GRIND XXXXX  # 20040
    print("Du är i skogen, framför en låst grind.")  # 20041
    if A[26] == 1:
        print("Dina nycklar passar inte i grinden.")  # 20042
    call_method_15200()  # 20043
    if A_ == "IN":
        print("Grinden är ju låst!")
    goto(20040)  # 20044
    if FNL_(A_, 3) == "LÅS":
        if A[26] == 1:
            goto(20042)
    else:
        print("Det går inte!")
    goto(20040)  # 20045
    if A_ == "SESAM":
        goto(14034)  # 20046
    if X != 0:
        goto([20050, 20020, 20050, 20055, 20050, 20050, 20048, 20030, 20050][X])  # 20047
    call_method(11000)  # 20048
    goto(20040)  # 20049
    print("Ett staket hindrar dej att gå ditåt!")  # 20050
    goto(20040)  # 20051
    call_method(11000)  # 20054
    Z = 74  # XXX STRAND 2 XXXX Z=74 XXXXX  # 20055
    print("Du är på stranden nordväst om sjön.")  # 20056
    call_method_15200()  # 20057
    if X1 == 1:
        goto(20061)  # 20058
    if X == 0:
        goto(20054)  # 20059
    goto([20063, 20030, 20040, 20155, 20063, 20063, 20054, 20065, 20020, 2107][X])  # 20060
    print("Du är på en strand som fortsätter åt öster. Långt bort i öster")  # 20061
    print("skymtar man en brygga. Åt norr och söder är det skog.")  # 20062
    print("Ett staket hindrar dej att gå åt väster, nordväst eller sydväst.")  # 20063
    goto(20055)  # 20064
    print("Du kan väl inte gå på vattnet?")
    goto(20055)  # 20065
    Z = 75  # XXXXX SKOG 2 XXXXX  # 20070
    print("Du är i skogen. Åt väster ser du ett hus.")  # 20071
    call_method_15200()  # 20073
    if X != 0:
        goto([20200, 20085, 20077, 9361, 20077, 20000, 20075, 9424, 20077][X])  # 20074
    call_method(11000)  # 20075
    goto(20070)  # 20076
    print("Ett staket hindrar dej att gå ditåt.")  # 20077
    goto(20070)  # 20078
    Z = 76  # XXXXX SKOG 3 XXXXX  # 20085
    print("Du är i skogen.")  # 20086
    call_method_15200()  # 20088
    if X != 0:
        goto([20070, 20092, 20094, 9424, 20092, 9361, 20090, 20105, 20092][X])  # 20089
    call_method(11000)  # 20090
    goto(20085)  # 20091
    print("Ett elektriskt stängsel hindrar dej att gå ditåt.")  # 20092
    goto(20085)  # 20093
    print("Du går runt, runt. Efter ett tag märker du att du gått vilse.")  # 20094
    print("Du går över en äng och ett högt berg.")  # 20095
    print()  # 20096
    print("Plötsligt hittar du ")  # 20097
    D = random.randint(0, 5)  # 20098
    if D < 4:
        goto(20102)  # 20099
    print("en stig som du följer tillbaka.")  # 20100
    goto(20085)  # 20101
    print("ett hål som du hoppar ner genom.")  # 20102
    print()
    goto(8000)  # 20103
    print("Du kryper igenom ett hål i staketet.")  # 20105
    Z = 77  # XXX OVANFÖR RÖVARGÖMSTÄLLET XXX  # 20107
    print("Du är i skogen.")  # 20108
    if S[20] < 1:
        print("Det ser ut som något har grävt här tidigare.")  # 20110
    if S[20] == 1:
        print("Det finns en grop här.")  # 20112
    call_method(20500)  # 20114
    if X == 2 and S[20] == 1:
        goto(20143)  # 20116
    if X1 == 1:
        goto(20107)  # 20117
    if X < 13:
        goto(20085)  # 20118
    if S[20] < 0:
        S[2] = S[2] + 10  # 20120
    S[20] = 1  # 20122
    print("Du gräver och gräver..." + FNS_("gräver", 10))  # 20124
    Z = 80  # XXXX RÖVARGÖMSTÄLLET XXXX  # 20143
    print("Du är längst ner i en grop och kan bara gå uppåt.")  # 20145
    call_method_12200()  # 20147
    if X == 1:
        S[3] = 1
    goto(20107)  # 20149
    call_method(11000)
    goto(20143)  # 20151
    Z = 79  # XXXXX SKOG 4 XXXXX Z=79 XXX  # 20155
    print("Du är i skogen, väster om sjön.")  # 20156
    call_method_15200()  # 20158
    if X != 0:
        goto(
            [20197, 2115, 20055, 20165, 20197, 20197, 20162, 20180, 20195, 2107][X]
        )  # 20161
    call_method(11000)  # 20162
    goto(20155)  # 20163
    Z = 82  # XXXXX SKOG 5 XXXXX Z=82 XXX  # 20165
    print("Du är i skogen, sydväst om sjön.")  # 20166
    call_method_15200()  # 20168
    if X != 0:
        goto([20178, 20180, 20155, 20240, 20178, 20178, 20173, 20255, 20176][X])  # 20172
    call_method(11000)  # 20173
    goto(20165)  # 20174
    print("Kan du gå på vattnet?")  # 20176
    goto(20165)  # 20177
    print("Ett staket hindrar dej att gå ditåt.")  # 20178
    goto(20165)  # 20179
    Z = 66  # XXXXX SKOG 6 XXXXX Z=66 XXX  # 20180
    print("Du är söder om sjön. En grotta leder åt ÖSTER.")  # 20181
    call_method_15200()  # 20183
    if X != 0:
        goto(
            [20165, 2075, 20191, 20255, 20155, 20240, 20188, 2200, 20191, 2107][X]
        )  # 20187
    call_method(11000)  # 20188
    goto(20180)  # 20189
    print("Kan du gå på vattnet?")  # 20191
    goto(20180)  # 20192
    print("Kan du gå på vattnet?")  # 20195
    goto(20155)  # 20196
    print("Ett staket hindrar dej att gå ditåt.")  # 20197
    goto(20155)  # 20198
    call_method(11000)  # 20199
    Z = 81  # XXXXX FRAMFÖR HUSET XXXX Z=81 XXX  # 20200
    print("Du står framför husets väldiga port.")  # 20202
    call_method_15200()  # 20204
    if X1 == 1:
        goto(20232)  # 20206
    if X == 19:
        call_method(15202)
    goto(20206)  # 20208
    if X == 0:
        goto(20199)  # 20210
    goto([20020, 20070, 20225, 20230, 20214, 20030, 20199, 9361, 20214][X])  # 20212
    print("Huset är i vägen.")
    goto(20200)  # 20214
    if S[19] == 1:
        print("Porten stängs bakom dej.")
    S[19] = 0
    goto(9991)  # 20225
    print("Porten är stängd!")  # 20226
    goto(20200)  # 20227
    print("En avskyvärd stank driver dej tillbaka!")  # 20230
    goto(20200)  # 20231
    print("Du står på en trappa framför ett stort hus. En stor port")  # 20232
    print("prydd med ett familjevapen i guld och silver finns bredvid")  # 20233
    print("dej. I söder ser du en brygga. Åt väster och öster står")  # 20234
    print("skogen tät.")  # 20235
    goto(20204)  # 20239
    Z = 67  # XXXXX SKOG 7 XXXXX Z=67 XXX  # 20240
    print("Du är i skogen.")  # 20241
    call_method_15200()  # 20243
    if X != 0:
        goto([20251, 20255, 20165, 20251, 20251, 20251, 20248, 20251, 20180][X])  # 20247
    call_method(11000)  # 20248
    goto(20240)  # 20249
    print("Ett staket hindrar dej att gå ditåt.")  # 20251
    goto(20240)  # 20252
    Z = 68  # XXXXX SKOG 8 XXXXX Z=68 XXX  # 20255
    print("Du är i skogen. En grotta leder åt NORDOST.")  # 20256
    call_method_15200()  # 20258
    if X != 0:
        goto([20240, 2200, 20180, 20266, 20165, 20266, 20263, 20266, 2075][X])  # 20262
    call_method(11000)  # 20263
    goto(20255)  # 20264
    print("Ett staket hindrar dej att gå ditåt.")  # 20266
    goto(20256)  # 20267
    Z = 83  # XXXXX SKOG 9 XXXXX Z=83 XXX  # 20270
    print("Du är söder om sjön. En grotta leder åt VÄSTER.")  # 20271
    call_method_15200()  # 20273
    if X != 0:
        goto(
            [2066, 20285, 20281, 20300, 20281, 2200, 20278, 20315, 20330, 2107][X]
        )  # 20277
    call_method(11000)  # 20278
    goto(20270)  # 20279
    print("Kan du gå på vattnet?")  # 20281
    goto(20270)  # 20282
    Z = 84  # XXXXX SKOG 10 XXXX Z=84 XXX  # 20285
    print("Du är i skogen, sydost om sjön.")  # 20286
    call_method_15200()  # 20288
    if X != 0:
        goto([20270, 20297, 20330, 20315, 20295, 20300, 20293, 20297, 20297][X])  # 20292
    call_method(11000)  # 20293
    goto(20285)  # 20294
    print("Kan du gå på vattnet?")  # 20295
    goto(20285)  # 20296
    print("Ett staket hindrar dej att gå ditåt.")  # 20297
    goto(20285)  # 20298
    Z = 85  # XXXXX SKOG 11 XXXX Z=85 XXX  # 20300
    print("Du är i skogen. En grotta leder åt NORDVÄST.")  # 20301
    call_method_15200()  # 20303
    if X != 0:
        goto([2200, 20315, 20270, 20312, 2066, 20312, 20309, 20312, 20285][X])  # 20307
    call_method(11000)  # 20309
    goto(20300)  # 20310
    print("Ett staket hindrar dej att gå ditåt.")  # 20312
    goto(20300)  # 20313
    Z = 86  # XXXXX SKOG 12 XXXX Z=86 XXX  # 20315
    print("Du är i skogen.")  # 20316
    call_method_15200()  # 20318
    if X != 0:
        goto([20300, 20327, 20285, 20327, 20270, 20327, 20324, 20327, 20327][X])  # 20322
    call_method(11000)  # 20324
    goto(20315)  # 20325
    print("Ett staket hindrar dej att gå ditåt.")  # 20327
    goto(20315)  # 20328
    Z = 87  # XXXXX SKOG 13 XXXX Z=87 XXX  # 20330
    print("Du är i skogen, öster om sjön.")  # 20331
    call_method_15200()  # 20333
    if X != 0:
        goto(
            [20340, 20342, 9424, 20285, 20340, 20270, 20338, 20342, 20342, 2107][X]
        )  # 20336
    call_method(11000)  # 20338
    goto(20330)  # 20339
    print("Kan du gå på vattnet?")  # 20340
    goto(20330)  # 20341
    print("Ett staket hindrar dej att gå ditåt.")  # 20342
    goto(20330)  # 20343
    S[53] = 2  # 20350
    print("Plötsligt hoppar ett konstigt, blått litet djur fram")  # 20352
    print("ur skogen och ropar:")  # 20354
    print(" - Hjälp    ! Jag vet inte om jag är en bug eller en feature!")  # 20356
    print("Det springer rätt ut i sjön och simmar bort.")  # 20358
    print()
    goto(20033)  # 20360
    call_method_6000()  # SABBAR 6000,_ = input() #TAR, KOLLAR BÅDE 8600 OCH 12000  # 20500
    print()  # 20502
    if S1 < 2:
        A_ = FNI_("")
    print()  # 20504
    X = 0  # 20506
    call_method(8600)  # 20508
    if X1 == 1:
        goto(20520)  # 20510
    if X > 0 and X < 5:
        X = X + 2
    else:
        call_method_12000()  # 20512
    S[36] = 2
    # ? return  # 20520
    Z = 30  # XXXXX DIMMIGT BERGSRUM XXXXX  # 21100
    print("Du är i ett dimmigt bergsrum. Kall rå luft blåser dej i")  # 21120
    print("ansiktet. Här finns")  # 21122
    if S[23] == 0:
        print(" en garderob.")  # 21130
    if S[23] == 1:
        print(" ett kassaskåp i en garderob.")  # 21140
    print("En gång leder uppåt och nedåt.")  # 21155
    call_method_12200()  # 21160
    if X1 == 1:
        goto(21120)  # 21180
    if X == 0 or X > 6:
        goto(21220)  # 21190
    goto([25000, 25130, 36000, 21230, 21230, 10020][X])  # 21200
    if INSTR(A_, "KORKSKRUV") > 0:
        goto(21300)  # 21220
    call_method(11000)  # 21230
    print("Du är i ett dimmigt bergsrum.")  # 21240
    goto(21160)  # 21250
    if S[23] == 1:
        goto(21330)  # 21300
    goto(21230)  # 21310
    print("Kassaskåpet öppnas.")  # 21330
    Z = 31  # 21340
    call_method_12200()  # 21350
    if X > 0 and X < 7:
        goto(21500)  # 21380
    if S[23] == 0 or Z == 30:
        goto(21240)  # 21390
    call_method(11000)  # 21410
    print("Kassaskåpet är öppet.")  # 21415
    goto(21350)  # 21420
    print("Kassaskåpet stängs.")  # 21500
    Z = 30
    goto(21180)  # 21510
    Z = 15  # XXX THORVALDS RUM X  # 25000
    print("Du är i Thorvalds rum. Vid väggen står en stor förseglad")  # 25001
    if A[1] == 0:
        A[1] = 15  # 25004
    print("kista. I taket finns en taklucka och i golvet finns ett hål.")  # 25005
    if A[3] == 31:
        print("På väggen står det: KORKSKRUV HJÄLPER TILL MED KASS...")  # 25008
    call_method_12200()  # 25010
    if X > 0:
        goto([25050, 15300, 25100, 10020, 40000, 21100, 25060][X])  # 25012
    if X1 == 1:
        goto(25000)  # 25014
    if INSTR(A_, "ÖPPNA") > 0:
        goto(25045)  # 25016
    if INSTR(A_, "KISTA") > 0:
        goto(25035)  # 25019
    if INSTR(A_, "LÅS UPP KIST") > 0:
        print("Det finns inget lås.")
    goto(25025)  # 25020
    call_method(11000)  # 25023
    print("Du är i Thorvalds rum.")
    goto(25010)  # 25025
    if A[15] != 1:
        print("Du kan inte öppna kistan.")
    goto(25025)  # 25035
    print("Du bänder upp kistan med din kofot och ser att det ligger en")  # 25036
    print("cykelpump där!")  # 25037
    print("Slarvig som du är lyckas du tappa kofoten i kistan när du tar")  # 25038
    print("pumpen. Kistlocket smäller igen.")  # 25039
    A[16] = 1
    A[15] = 5
    goto(25000)  # 25040
    if A_ == "ÖPPNA":
        A_ = FNI_("Öppna vad")
    A_ = FNC_(A_)  # 25045
    if INSTR(A_, "KIST") > 0:
        goto(25035)  # 25046
    if INSTR(A_, "TAKLU") == 0 and INSTR(A_, "LUCK") == 0:
        goto(25023)  # 25047
    if A[17] != 1 and A[17] != Z:
        print("Takluckan sitter för högt!")
    goto(25000)  # 25050
    print("Du klättrar upp på stegen och öppnar luckan.")  # 25051
    if A[2] != 0:
        print("Där finns inget, så du klättrar ner igen.")
        goto(25000)  # 25053
    print("Det finns en illaluktande gurka här.")  # 25054
    print("Den rasar ned och lägger sej på golvet.")  # 25055
    A[2] = 15
    goto(25025)  # 25056
    if A[2] > 0:
        goto(25070)  # 25060
    if A[17] != 1 and A[17] != Z:
        print("Det behövs en stege för att nå upp.")  # 25062
    if A[17] == 1 or A[17] == Z:
        print("Öppna takluckan!")  # 25064
    S[2] = S[2] - 5  # 25066
    goto(25025)  # 25068
    if A[15] == 5:
        goto(25023)  # 25070
    print("Kistan kan bara öppnas med en kofot.")  # 25072
    goto(25066)  # 25074
    print("Du tittar in i personalköket. Osvald ryter till:")  # 25100
    print("-STICK!!Din eländiga babian!")  # 25102
    print("Du ser en liten faun som quarkar en praktyl. Faunen säjer:")  # 25103
    print("-Vad har du här att göra? Räcker det inte med att folk ränner")  # 25104
    print("omkring som tokar nere hos mej? Ska dom komma hit också?")  # 25105
    print()  # 25110
    print("En liten faun dyker upp.")  # 25115
    if random.random() < 0.8 or S[29] == 1:
        goto(25130)  # 25116
    print("Han kastar en kniv mot dej...                     ")  # 25117
    if random.random() < 0.5:
        goto(25121)
    else:
        print("Den träffar!    !")
    Z = 15  # 25118
    call_method(7500)  # 25119
    goto(9461)  # 25120
    print("Den missar!")
    print("Golvet ger plötsligt vika och du faller.")  # 25121
    goto(15300)  # 25122
    print("Du är i ett mörkt rum.")  # 25130
    Z = 96  # 25135
    call_method_12200()  # 25136
    if X == 1:
        goto(21100)  # 25210
    if X == 6:
        goto(10020)  # 25212
    if X1 == 1:
        goto(25130)  # 25215
    call_method(11000)  # 25220
    goto(25130)  # 25230
    # XXX TELEVERKET - subrutin för jackmontering XXX  # 27050
    D = int(random.random() * S[37]) + 1  # 27060
    A_ = MID_(W_(5), ((D * 3) - 2), 3)  # 27065
    D = VAL(A_)  # 27070
    if J[D] == 1:
        goto(27050)  # 27075
    J[D] = 1  # 27080
    # ? return  # 27085
    print("Just när du ska koppla in telefonen kommer en man med en röd")  # 27100
    print("dräkt som det står TELE på in och slänger en telefonkatalog")  # 27110
    print("på dina fötter.")  # 27120
    if J[Z] != 1:
        goto(27140)
    else:
        J[Z] = 0  # 27122
    print("Med en sur min skruvar han bort telefonjacken ur väggen och går.")  # 27130
    S[2] = S[2] + 5  # 27140
    A[23] = Z
    goto(12210)  # 27150
    # XXXXX RING PERSONALKÖK XXXX  # 27200
    print("Ok.   Ring    , Ring    .")  # 27202
    print()
    print("TUUT ------ TUUT ----- TUUT ------ <klick>")  # 27204
    if W_[6] == "":
        W_[6] = FNI_("Hej, vem där ?")  # 27206
    print("Personalköket rekommenderar:")  # 27212
    print()
    print("Halvruttna tomater med pilaffris.")  # 27214
    print("Vändstekt, långsamt grillad samt hårdkokt " + W_(6))  # 27216
    print("Samt friskt, giftigt grottvatten. (Hi, hi, hi)")  # 27218
    print("<klick> TUUT --- TUUT --- TUUT")  # 27220
    S[29] = 1
    print()
    X1 = 1
    goto(12999)  # 27222
    # XXX Ring Televerket XXXXX  # 27250
    print("Ok.     Ring, Ring.")  # 27252
    print()  # 27254
    print("-Stugas televerk.")  # 27256
    A_ = FNI_("Har ni klagomål på er linje ?")  # 27258
    if FNL_(A_, 1) == "J" or FNL_(A_, 1) == "j":
        goto(27300)  # 27262
    A_ = FNI_("Vilket nummer gäller det ?")  # 27264
    print("Ok. Vänta ett tag så ska jag kolla upp det.")  # 27268
    S = time.sleep(20)
    if S:  # 27270
        A1_ = input("TUU    T")
        goto(27270)
    if INSTR(A_, "481") > 0:
        goto(27280)  # 27272
    if INSTR(A_, "999") > 0:
        goto(27290)  # 27274
    if INSTR(A_, "100") > 0 and J[100] == 0:
        print("Abonnemanget har upphört.<klick>")
    goto(12210)  # 27275
    print("Det är inget fel på den linjen.")  # 27276
    print("<klick>")
    S[28] = 2
    goto(12210)  # 27278
    if S[6] > 0:
        goto(27284)  # 27280
    print("Linjen fungerar utmärkt. (För en gångs skull...)")
    goto(12210)  # 27282
    print("Jaha. Hm, linjen är väl okej, men abonnenten...")  # 27284
    print("Det fixar sej nog om ett tag..")  # 27286
    print("<klick>")  # 27287
    goto(12210)  # 27288
    print("Nummerändring. Nya numret är 900.")
    goto(12210)  # 27290
    print("Jag ska skicka någon för att fixa det.")  # 27300
    print("<klick>")  # 27302
    print("Ur skuggorna kommer plötsligt en man klädd i en röd")  # 27304
    goto(7081)  # 27306
    # XXX Ring Larmcentralen. XXX  # 27400
    print("Ok. Ring, Ring    .")  # 27402
    print("Larmcentralen, var god dröj.")
    time.sleep(20)  # 27404
    if S:  # 27406
        A_ = input("  Var god dröj  ") # _A_
        time.sleep(30)
        goto(27406)
    print("LARMCENTRAlen. Vi fixar allt - snabbt!")  # 27408
    print("Vad vill Du ha hjälp med")  # 27410
    A_ = FNC_(FNI_(" ?"))  # 27412
    print("Det går inte.")  # 27414
    if INSTR(A_, "RÖVARE") > 0:
        goto(27428)  # 27416
    if INSTR(A_, "TRAPPA") > 0:
        goto(27434)  # 27418
    if INSTR(A_, "HISS") > 0:
        goto(27440)  # 27420
    if INSTR(A_, "BÅT") > 0:
        goto(27444)  # 27422
    print("<klick>")  # 27424
    goto(12210)  # 27426
    print("Jo, förresten. Jag får väl snacka med honom. Om jag")  # 27428
    print("får tag på honom. Han är ofta ute på jakt...")  # 27430
    S[3] = -1
    goto(27424)  # 27432
    print("Jo, förresten. Vi får väl ta och se över våra trappor.")  # 27434
    print("Jag ska genast kontakta gatukontoret.")  # 27436
    S[15] = 0
    S[17] = 0
    S[18] = 0
    goto(27424)  # 27438
    print("Vänta, var det hissen du sa ?  Jag får väl se över den då.")  # 27440
    S[40] = 4
    S[41] = 0
    goto(27424)  # 27442
    print("Nu får det vara slut på båtfärderna!!")  # 27444
    S[35] = 0.5
    goto(27424)  # 27446
    if J[100] == 0:
        goto(12826)
    else:
        print(FNS_("ringer", 2))  # 27600
    if Z == 100:
        I = 1
    else:
        I = 5  # 27602
    for I in range(1, 8):  # 27604
        S = time.sleep(I)
        if S:
            A_ = input("?")  # 27606
        print("R    ing!")  # 27608

    print()
    S = time.sleep(I)  # 27612
    if Z == 100:
        print("Det är visst upptaget.")
    else:
        print("Ingen svarar.")  # 27614
    goto(12210)  # 27616
    print("En automatisk telefonsvarare svarar:")  # 27620
    print(" - Han är tyvärr inte inne. Han har alltid så mycket att")  # 27622
    print("   göra att han aldrig hinner svara i telefon.")  # 27624
    print("<klick>")  # 27626
    goto(12210)  # 27628
    goto([27632, 27640, 27650, 27650][S[6] + 1])  # 27630
    if A[29] != 58:
        goto(27652)  # 27632
    if Z == 58:
        print("Du hör en signal. Vakten går bort ett ögonblick.")  # 27633
    print("Ring, Ring    !")  # 27634
    print(" - Stör mej inte! Jag vaktar!")  # 27636
    goto(27626)  # 27638
    if (A[29] == 58 or A[29] == 1) and Z == 58:
        print("Du hör en signal. Vakten kravlar iväg.")  # 27640
    if A[29] != 58:
        goto(27652)  # 27641
    print("Ring, Rin    g!")  # 27642
    print(" - Hick, HELAN GÅÅÅÅÅÅÅÅR... HI    CK!")  # 27644
    goto(27626)  # 27646
    if Z == 58:
        print("Du hör en signal.")  # 27650
    I = 4
    goto(27604)  # 27652
    # XXX VAKT XXXXX  # 28000
    if A[29] == Z or A[29] == 1:
        print("Vakten sover för djupt.")
    goto(12210)  # 28002
    if A[29] != Z and A[29] != 1:
        print("Jag ser ingen VAKT här.")
    goto(12210)  # 28010
    if S[6] == 2:
        print("Vakten är redan död! Ser du inte blodfläckarna!")
    goto(12210)  # 28012
    if A[4] != 1:
        print("Du har inget du kan döda honom med.")
    goto(12210)  # 28014
    if S[6] == 3:
        goto(28030)  # 28016
    if S[6] == 1:
        goto(28026)  # 28018
    print("Du kastar hillebarden mot vakten, men han duckar.")  # 28020
    A[4] = Z
    S[1] = S[1] - 1  # 28022
    goto(12210)  # 28024
    print("Du kastar hillebarden mot den fulle vakten. Han fångar")  # 28026
    print("upp den i luften med en elegant gest.")  # 28027
    A[4] = 2
    S[1] = S[1] - 1  # 28028
    goto(12210)  # 28029
    print("Du kastar hillebarden mot den sovande")  # 28030
    print("vakten, som stönar och bleknar.")  # 28034
    print("Du drar den bloddrypande hillebarden ur liket och torkar av den.")  # 28036
    S[6] = 2
    A[22] = Z
    A[29] = Z
    S[51] = 0  # 28038
    if Z == 63:
        S[52] = S[50]
    S[2] = S[2] + 25  # 28039
    if A[15] == 2:
        A[15] = Z  # 28040
    if A[25] == 2:
        A[25] = Z  # 28042
    if A[26] == 2:
        A[26] = Z  # 28044
    X1 = 1
    goto(12999)  # 28046
    if C_ == "":
        goto(12999)  # 28090
    if C_ == "UPP":
        goto(9950)  # 28092
    for I in range(1, A[0]):  # 28100
        if A_(I, 1) != "":
            if INSTR(C_, A_(I, 2)) > 0 or INSTR(C_, A_(I, 3)) > 0:
                goto(28105)  # 28101
        continue  # 28102
    I = 0  # 28103
    if (A[29] != 1 and A[29] != Z) or S[6] > 1:
        goto(12840)  # 28105
    if INSTR(C_, "GUBBE") > 0 or S[30] == Z:
        goto(12840)  # 28106
    if I > 0:
        goto(28110)  # 28107
    print("Det kan du inte ge till vakten.")
    goto(12210)  # 28108
    if I != 26 and I != 25 and I != 15 and I != 4 and I != 18:
        goto(28108)  # 28110
    if A[I] != 1:
        print("Du bär väl " + FNA_(I) + A_(I, 4) + ".")
    goto(12210)  # 28112
    if I == 18:
        goto(12360)  # 28114
    print("Vakten tar emot " + A_(I, 4) + " med ett snett leende.")  # 28116
    S[1] = S[1] - 1
    A[I] = 2
    goto(12210)  # 28118
    if A[29] != Z and A[29] != 1:
        goto(6418)  # 28130
    if S[6] == 3:
        goto(28150)  # 28132
    if S[6] == 1:
        goto(28140)  # 28134
    print("Vakten hindrar dej.")
    goto(12210)  # 28136
    if S[1] == 9:
        goto(6420)  # 28140
    print("Vakten släpper motvilligt " + A_(I, 4) + ".")  # 28142
    S[1] = S[1] + 1
    A[I] = 1  # 28144
    goto(12210)  # 28146
    print("Har du hjärta att ta någonting från en sovande vakt?!?")  # 28150
    A_ = FNI_("")
    A_ = FNC_(A_)  # 28152
    if A_ != "JA":
        goto(12214)  # 28154
    print("Har Du inget hjärta i kroppen ?!!Jag vägrar!")
    goto(12214)  # 28156
    if A[22] != 63:
        goto(6418)  # 28160
    if S[1] == 9:
        goto(6420)  # 28162
    S[52] = 0
    S[2] = S[2] - 30  # 28164
    goto(6422)  # 28166
    # XXX RÖVARE XXXX  # 29000
    S[4] = S[4] + 1  # 29005
    if S[4] > 8:
        goto(29050)  # 29010
    if random.random() < 0.2:
        S[4] = S[3] = 0
    goto(6069)  # 29015
    if random.random() < 0.7:
        print("Du hör tunga fotsteg i närheten.")  # 29020
    goto(6069)  # 29025
    if Z == 80:
        goto(6069)  # 29050
    B = 0  # 29055
    if random.randint(0, 3) == 3: # 29060
        S[3] = 0
        S[41] = 1
        goto(6069)
    for I in range(1, 14):  # 29065
        if A[I] == 1:
            A[I] = 80
        B = B + 1
        S[1] = S[1] - 1  # 29070
        if A[I] == Z:
            A[I] = 80
        B = B + 1  # 29075
    if B == 0:
        goto(6069)  # 29085
    if S[20] == 1:
        S[20] = 0  # 29090
    print()  # 29095
    print("Plötsligt hoppar en skäggig rövare fram ur mörkret och säjer:")  # 29100
    print(" - Jag snor det här krafset och gömmer det i mitt")  # 29105
    print("   gömställe långt nere!!")  # 29110
    print()
    print("Han försvinner lika fort som han kom!")  # 29115
    S[4] = -7
    S[3] = -1  # 29120
    goto(6069)  # 29125
    # XXX GUBBE XXXX  # 30000
    if S[30] == 96 or S[49] == 1:
        pass  # ? return  # 30001
    S[30] = random.randint(91, 100)  # 30002
    S[49] = 0
    X1 = 2
    if S[30] == Z or S[30] == 51 or S[30] == 60:
        goto(30002)  # 30004
    print("Gubben reser sej, muttrar någonting om att man aldrig")  # 30006
    print("får vara i fred, och försvinner.")
    # ? return  # 30008
    if S[30] != Z:
        print("Jag ser ingen gubbe här.")
    goto(12210)  # 30010
    if A[19] == 0:
        print("Gubben har ju vattenflaskan.")
    goto(12210)  # 30012
    if A[19] != 1 or S[32] > 0:
        print("Du har ju ingen full vattenflaska.")
    goto(12210)  # 30014
    print("Gubben dricker ur vattenflaskan och ser genast gladare ut.")  # 30016
    S[49] = 1
    S[32] = 1
    goto(12210)  # 30018
    if I == 11 and S[30] == Z and S[49] == 2:
        goto(30028)  # 30020
    if I == 19 and A[10] == 0:
        goto(30036)  # 30022
    print("Gubben vägrar att släppa " + A_(I, 4) + ".")  # 30024
    goto(12210)  # 30026
    if S[1] == 9:
        goto(6420)  # 30028
    print("Du tar pärlhalsbandet från den bländade gubben.")  # 30030
    S[49] = 0
    A[11] = 1
    X1 = 1
    S[1] = S[1] + 1  # 30032
    goto(30002)  # 30034
    if S[1] == 9:
        goto(6420)  # 30036
    print("Du tar vattenflaskan från gubben.")  # 30038
    S[1] = S[1] + 1
    X1 = 1
    A[19] = 1  # 30040
    goto(30002)  # 30042
    if S[30] != Z:
        print("Jag ser ingen GUBBE här.")
    goto(12210)  # 30050
    print("Gubben ser din hotande blick och smiter iväg.")  # 30052
    S[30] = random.randint(91, 100)  # 30054
    S[49] = 0
    if S[30] == Z or S[30] == 51 or S[30] == 60:
        goto(30054)  # 30056
    goto(12210)  # 30058
    Z = 100  # XXX TEFELONSTUGAN XXX Z=100 ZZZZZZZZZZ  # 35000
    S[27] = S[27] + 1  # 35005
    if S[27] > 3 and S[27] < 8:
        goto(35030)  # 35010
    print("Du är i en stuga med dörrar bakåt, framåt och åt")  # 35015
    print("höger. Högt upp i taket finns ett fönster.")  # 35020
    goto(35035)  # 35025
    print("Du är i stugan.")  # 35030
    if S[27] == 8:
        S[27] = 4  # 35035
    call_method_6000()  # 35040
    if S[27] == 1 and J[100] == 1 and A[25] == 100:
        print("Telefonen ringer.")  # 35045
    print()
    A_ = FNI_("")  # 35050
    print()
    call_method_12000()  # 35052
    if INSTR(A_, "SVAR") > 0:
        goto(35100)  # 35055
    if X1 == 1:
        goto(35015)  # 35065
    if X > 3 and X < 7:
        goto(35085)  # 35070
    call_method(11000)  # 35075
    goto(35030)  # 35080
    if S[27] == 1:
        S[27] = 0  # 35085
    goto([7556, 9190, 35150][(X - 3)])  # 35090
    if S[27] > 1 or J[100] == 0 or A[25] != 100:
        goto(35075)  # 35100
    S[27] = 2  # 35105
    print("Du svarar i telefon och hör en röst:")  # 35110
    if W_[6] == "":
        W_[6] = FNI_("- Vad heter du ?")  # 35115
    print("Hej, " + W_(6) + " ! Bra att Du också har skaffat en telefon.")  # 35120
    print("<klick>")  # 35122
    goto(35030)  # 35125
    if A[1] == 1:
        print("Dörren är igenbommad av Stugas gatukontor.")
    goto(35000)  # 35150
    goto(2127)  # 35155
    Z = 61  # XXXXX KYRKOGÅRD XXXXX  # 36000
    print("Du är på en kyrkogård. Du står vid en gravsten på kanten")  # 36005
    print("till en grav. En stig leder framåt och bakåt.")  # 36010
    call_method_12200()  # 36015
    if X1 == 1:
        goto(36000)  # 36020
    if X == 0 or X > 6:
        goto(36035)  # 36025
    goto([36035, 36050, 36035, 36035, 21100, 2150][X])  # 36030
    call_method(11000)  # 36035
    print("Du är på kyrkogården.")  # 36040
    goto(36015)  # 36045
    Z = 63  # XXXXX GRAVEN XXXXX  # 36050
    print("Du är i en grav. Det luktar unket här.")  # 36055
    print("Prästen tittar ner. Han ser ut så här:")  # 36060
    call_method(700)  # 36065
    if S[50] - S[52] > 30 and S[52] > 0:
        S[52] = 0
    A[22] = 2
    A[5] = 63  # 36067
    call_method_12200()  # 36070
    if X1 == 1:
        goto(36090)  # 36075
    if X == 1:
        goto(36000)  # 36080
    call_method(11000)  # 36085
    print("Du är i en grav.")  # 36090
    goto(36070)  # 36095
    Z = 17  # XXXXX OSVALDS RUM XXXXX  # 40000
    if S[5] > 4:
        S[5] = 1
    else:
        S[5] = S[5] + 1  # 40015
    if S[5] == 1:
        goto(40030)  # 40017
    print("Du är i Osvalds rum.")
    goto(40100)  # 40020
    print("Du är i Osvalds rum, ett rum med fyra dörrar. På den högra står det")  # 40030
    print("ZZZZ, på den vänstra står det THORVALD och på den rakt fram")  # 40031
    print("står det GARDEROB.")  # 40032
    if S[15] == 0 and S[7] == 1:
        print("En trappa går nedåt.")  # 40060
    if S[15] == 1 and S[7] == 1:
        print("Det finns rester av en trappa här.")  # 40061
    call_method_12200()  # 40100
    if X1 == 1:
        goto(40030)  # 40110
    if X == 0 or X == 7:
        goto(40200)  # 40115
    goto([40200, 40140, 25000, 18000, 41000, 40200][X])  # 40120
    if S[7] == 0:
        goto(40200)  # 40140
    if S[15] != 0:
        print("Trappan är avspärrad av Stugas gatukontor.")
    goto(40015)  # 40145
    if A[1] != 1:
        goto(13235)  # 40147
    print("Trappan rasar ihop.")
    S[15] = 1
    goto(40015)  # 40150
    call_method(11000)  # 40200
    goto(40020)  # 40210
    # XXX GARDEROBEN XXXXX Z=4 XXXX  # 41000
    print("Du är i en mörk garderob.")  # 41005
    print("Bakom dej och till vänster finns det dörrar.")  # 41010
    S[4] = 1
    Z = 4  # 41030
    call_method_12200()  # 41040
    if X1 == 1:
        goto(41005)  # 41080
    if X == 6:
        goto(40000)  # 41090
    if X == 3:
        goto(9020)  # 41100
    call_method(11000)  # 41105
    print("Du är i garderoben.")  # 41110
    goto(41040)  # 41120


def call_method_6000():  #? semi-done
    if _DEBUG:
        time.sleep(0.5)
        print('call_method_6000')
    # ```` RUMSBESKRIVNING ```````````` TA ````````` SLÄPP ````````````  # 06000
    if S[2] == 335 and random.random() > 0.5:  # 06002
        print("Plötsligt kommer Thorvald fram och säjer:")
        call_method_99000(skip_name=True)
    if Z == 70 and A1 == 1:  # 06003
        print("På marken ligger en enorm rubin.")
    if A[1] == Z:  # 06005
        print("Det finns en diamant här.")
    if A[15] == Z:  # 06006
        print("Det ligger en kofot här.")
    if A[16] == Z:  # 06007
        print("Det står en cykelpump här.")
    if A[2] == Z:  # 06008
        print("Det finns en illaluktande gurka här.")
    if A[3] == Z:  # 06009
        print("Det finns en silvertacka här.")
    if A[17] == Z and Z != 11:  # 06010
        print("Det står en stege här.")
    if A[18] == Z:  # 06011
        if S[31] == 0:  # 06012
            print("Det finns en fylld brännvinsflaska här.")
        if S[31] == 1:  # 06013
            print("Det finns en tom brännvinsflaska här.")
    if A[19] == Z:  # 06014
        if S[32] == 0:  # 06015
            print("Det finns en fylld vattenflaska här.")
        if S[32] == 1:  # 06016
            print("Det finns en tom vattenflaska här.")
    if A[20] == Z:  # 06017
        if S[33] == 0:  # 06018
            print("Det finns en pumpad boll här.")
        if S[33] == 1:  # 06019
            print("Det finns en opumpad boll här.")
    if A[4] == Z:  # 06020
        print("Det står en hillebard här.")
    if A[21] == Z:  # 06021
        print("Det står en spade här.")
    if A[5] == Z:  # 06022
        print("Det ligger en dödskalle här.")
    if A[6] == Z:  # 06023
        print("Det finns en väckarklocka här.")
    if A[23] == Z:  # 06024
        print("Det ligger en tunn telefonkatalog här.")
    if A[12] == Z:  # 06025
        print("Det ligger en faunsko här.")
    if A[7] == Z:  # 06026
        print("Det finns en massa guldmynt här.")
    if J[Z] == 1 and A[25] == Z:  # 06027
        print("En telefon är inkopplad i en jack i väggen.")
    if J[Z] == 1 and A[25] != Z and A[30] != Z:  # 06028
        print("Det finns en telefonjack i väggen.")
    if J[Z] != 1 and A[25] == Z and S[44] != Z:  # 06029
        print("Det finns en telefon här.")
    if A[26] == Z:  # 06030
        print("Det finns några nycklar här.")
    if A[27] == Z:  # 06031
        print("Det hänger en sax här.")
    if A[28] == Z:  # 06032
        print("Det hänger en slägga här.")
    if A[22] == Z:  # 06033
        print("Det ligger ett äckligt lik här.")
    if A[11] == Z:  # 06034
        print("Det finns ett glittrande pärlhalsband här.")
    if A[8] == Z:  # 06035
        print("Det ligger en trilogi här.")
    if A[24] == Z:  # 06036
        print("Det står en lampa här.")
    if A[9] == Z:  # 06037
        print("Det ligger ett kontrakt här.")
    if A[10] == Z:  # 06038
        print("Det hänger en lagerkrans här.")
    if S[30] == Z:  # 06039
        goto(6200)
    if J[Z] == 1 and A[30] == Z:  # 06040
        print("En förlängningssladd är inkopplad i en jack i väggen.")
    if J[Z] != 1 and A[30] == Z:  # 06042
        print("Det ligger en förlängningssladd här.")
    if J[Z] != 1 and S[44] == Z and A[25] == Z:  # 06043
        print("En telefon är inkopplad i en förlängningssladd.")
    if S[44] == Z and (A[25] != Z or J[Z] == 1):  # 06044
        print("En förlängningssladd sticker in hit.")
    if S[44] == -1 and Z != A[30]:  # 06048
        S[44] = Z
        print("Förlängningssladden räcker precis hit.")
    if S[3] > 0:  # 06050
        goto(29000)
    if random.randint(0, 19) != 1 or S[50] < 50:  # 06060
        goto(6069)
    for i in range(1, 14):  # 06062
        if A[i] == 1:
            S[3] = S[3] + 1
    if S[3] > 0:  # 06064
        S[4] = random.randint(0, 5) + int(S[3] / 2 + 0.5)
    if random.randint(0, 30) != 1:  # 06069
        goto(6100)
    if S[48] > 0:  # 06070
        print("En glasmästare springer förbi dej.")
        S[48] = 0
    if S[15] != 1 and S[17] != 1 and S[18] != 1:  # 06072
        goto(6076)
    print("En verkmästare från Stugas gatukontor lunkar förbi dej.")  # 06074
    S[15] = S[17] = S[18] = 0
    if S[41] == 1:
        print("En hissreparatör går förbi dej.")  # 06076
        S[41] = 0
        S[40] = random.randint(0, 9) + 1
    if S[50] - S[21] > 25 and S[21] > 0:  # 06098
        goto(6130)
    if A[29] != Z:  # 06100
        goto(6120)
    if S[50] - S[51] > 30 and S[51] > 0:  # 06102
        goto(6124)
    if S[6] == 0:  # 06104
        print("Här står en vakt.")
    if S[6] == 1:  # 06106
        print("En full vakt raglar omkring här.")
    if S[6] == 2:  # 06108
        print("Det finns blodfläckar på golvet.")
        return
    if S[6] == 3:  # 06110
        print("En vakt sover här.")
    if A[15] == 2:  # 06112
        print("Han har din kofot.")
    if A[26] == 2:  # 06114
        print("Han har dina nycklar.")
    if A[25] == 2:  # 06116
        print("Han bär på en telefon.")
    if A[4] == 2:  # 06118
        print("Han bär på en juvelprydd hillebard.")  # 06119
        return
    if A[29] != 1:  # 06120
        return
    if S[50] - S[51] < 31 and S[51] > 0:  # 06122
        print("Du följs av en full vakt.")
        goto(6112)
    S[1] = S[1] - 1  # 06123
    print("Vakten har nyktrat till nu.")  # 06124
    if S[6] == 3:
        print("Han vaknar och sträcker på sej.")  # 06126
    A[29] = Z  # 06128
    S[6] = 0
    S[51] = 0
    return  # 06129
    S[21] = 0  # 06130
    print("Dina fötter är läkta nu.")  # 06131
    goto(6100)  # 06132
    if A[19] > 0 and A[11] > 0:
        print("Här sitter en gubbe.")
        goto(6210)  # 06200


def call_method_12000():
    S[36] = 0  # XXXXX KOMMANDOAVKODARE XXXXX  # 12000
    if A_ == "":  # 12001
        goto(12210)
    X = 0
    X1 = 0
    A_ = FNC_(A_)  # 12003
    if FNL_(A_, 3) == "UPP" or A_ == "U":
        X = 1  # 12010
    if FNL_(A_, 3) == "NER" or FNL_(A_, 3) == "NED" or A_ == "N":
        X = 2  # 12012
    if INSTR(A_, "VÄNSTER") > 0 or A_ == "V":
        X = 3  # 12014
    if INSTR(A_, "HÖGER") > 0 or A_ == "H":
        X = 4  # 12016
    if INSTR(A_, "FRAM") > 0 or A_ == "F":
        X = 5  # 12018
    if INSTR(A_, "BAKÅ") > 0 or A_ == "B":
        X = 6  # 12020
    if INSTR(A_, "HJÄLP") > 0:
        X = 7  # 12025
    if X > 0 and X != 7 and S[21] > 0:
        print(FNS_("haltar", 5))  # 12027
    E = INSTR(A_, " ")
    C_ = FNM_(A_, E)  # 12030
    if C_ == "":
        C_ = ""
    goto(12050)  # 12032
    if FNL_(C_, 1) == " ":
        C_ = FNM_(C_, 2)
    goto(12032)  # 12034
    S[50] = S[50] + 1
    S1 = 0  # 12050
    if FNL_(A_, 5) == "VÄNTA" or FNL_(A_, 5) == "STANN":
        goto(12570)  # 12052
    if INSTR(A_, "HELVETE") > 0:
        print("Åt vilket håll är det?")
    goto(12210)  # 12055
    if FNL_(A_, 5) == "HOPPA":
        goto(12130)  # 12056
    if FNL_(A_, 6) == "VRICKA":
        goto(12584)  # 12057
    if INSTR(A_, "KNACK") > 0:
        print("Ingenting händer.")
    goto(12210)  # 12058
    if FNL_(A_, 4) == "SKIT":
        goto(12590)  # 12059
    if FNL_(A_, 5) == "SKRIK":
        goto(12550)  # 12060
    if (
        FNL_(A_, 3) == "FAN"
        or FNL_(A_, 5) == "JÄVLA"
        or FNL_(A_, 6) == "DJÄVLA"
        or FNL_(A_, 5) == "SATAN"
    ):
        goto(12555)  # 12061
    if A_ == "TITTA" or A_ == "SE":
        X1 = 1
    S[50] = S[50] - 1  # 12062
    if A_ == "ALEA JACTA EST":
        goto(12220)  # 12063
    if A_ == "SLUTA":
        goto(9950)  # 12064
    if FNL_(A_, 2) == "GÅ":
        goto(12255)  # 12065
    if FNL_(A_, 5) == "BLÄND":
        goto(12850)  # 12066
    if FNL_(A_, 3) == "GE ":
        goto(28090)  # 12067
    if A_ == "VEKTOR":
        goto(98000)  # %%%%% Denna rad kan tas bort  # 12068
    if FNL_(A_, 4) == "VÄCK" and S[6] == 3:
        goto(28000)  # 12069
    if FNL_(A_, 5) == "INVEN":
        goto(8613)  # 12070
    if FNL_(A_, 2) == "TA":
        goto(6300)  # 12071
    if FNL_(A_, 5) == "SLÄPP":
        goto(7000)  # 12072
    if FNL_(A_, 4) == "FYLL":
        goto(12340)  # 12073
    if FNL_(A_, 5) == "DRICK":
        goto(12270)  # 12074
    if FNL_(A_, 4) == "RING":
        goto(12800)  # 12075
    if A_ == "POÄNG":
        print("Du har" + S[2] + "poäng.")
    goto(12210)  # 12076
    if FNL_(A_, 4) == "GRÄV":
        goto(12230)  # 12077
    if FNL_(A_, 5) == "SPARK":
        goto(12580)  # 12078
    if FNL_(A_, 4) == "DÖDA":
        goto(12240)  # 12079
    if FNL_(A_, 1) == "?":
        X1 = 1
    S[50] = S[50] - 1
    call_method(91000)  # 12080
    if (
        A_ == "UT"
        or INSTR(A_, " UT ") > 0
        or FNL_(A_, 3) == "UT "
        or FNR_(A_, 3) == " UT"
    ):
        goto(12420)  # 12081
    if FNL_(A_, 5) == "ÖPPNA":
        goto(12440)  # 12082
    if FNL_(A_, 5) == "STÄNG":
        goto(12470)  # 12083
    if FNL_(A_, 3) == "LÄS":
        goto(12650)  # 12084
    if FNL_(A_, 5) == "PUMPA":
        goto(12900)  # 12085
    if FNL_(A_, 5) == "SIMMA" or FNL_(A_, 5) == "DUSCH" or FNL_(A_, 4) == "BADA":
        goto(12890)  # 12086
    if FNL_(A_, 4) == "FÖLJ":
        goto(12910)  # 12087
    if (
        A_ == "IN"
        or INSTR(A_, " IN ") > 0
        or FNL_(A_, 3) == "IN "
        or FNR_(A_, 3) == " IN"
        or INSTR(A_, "IGENOM") > 0
    ):
        goto(12400)  # 12088
    if FNL_(A_, 5) == "KASTA":
        print("Tyvärr har kastarmen gått ur led.")
    goto(12210)  # 12089
    if FNL_(A_, 4) == "INFO":
        goto(12770)  # 12090
    if FNL_(A_, 3) == "ÅT" and C_ != "":
        A_ = C_
    goto(12214)  # 12091
    if FNL_(A_, 5) == "BEGRA":
        goto(12510)  # 12092
    if FNL_(A_, 9) == "KOPPLA IN":
        goto(12140)  # 12093
    if FNL_(A_, 9) == "KOPPLA UT" or FNL_(A_, 9) == "KOPPLA UR":
        goto(12160)  # 12094
    if A_ == "SPARA":
        call_method_80000()  #           &&&&&  # 12095
    if FNL_(A_, 5) == "ÅTERS":
        call_method_80200()  #   &&&&&  # 12096
    if FNL_(A_, 4) == "LOGG":
        goto(12950)  #    &&&&&  # 12097
    for I in range(1, A[0]):  # 12098
        if A_(I, 1) == "":
            goto(12103)  # 12099
        if FNL_(A_, 5) == FNL_(A_(I, 2), 5) or A_ == A_(I, 2):
            goto(12600)  # 12100
        if FNL_(A_, 5) == FNL_(A_(I, 3), 5) or A_ == A_(I, 3):
            goto(12600)  # 12101
    goto(12999)  # 12104
    if S[33] == 1:
        print("Bollen är inte pumpad.")
    goto(12210)  # 12120
    if Z == 39 and S[48] < 1:
        X = 13
    goto(12999)  # 12122
    print("Du sparkar bollen så hårt att den försvinner.")  # 12123
    if A[20] == 1:
        S[1] = S[1] - 1  # 12124
    A[20] = random.randint(0, 2) + 9  # 12125
    goto(12210)  # 12126
    if INSTR(A_, "VATTEN") > 0 or INSTR(A_, "VATTNET") > 0:
        goto(12890)  # 12130
    if S[36] != 0:
        goto(12057)  # 12132
    if C_ == "UPP" or C_ == "UPPÅT":
        X = 1
    else:
        X = 2  # 12134
    goto(12999)  # 12136
    if J[Z] != 1 and S[44] != Z:
        print("Det finns ingen jack här.")
    goto(12210)  # KOPPLA IN   # 12140
    if len(A_) > 10:
        A_ = FNM_(A_, 11)
    else:
        A_ = FNC_(FNI_("Vad vill du koppla in ?"))  # 12142
    if FNL_(A_, 5) == "TELEF":
        I = 25
    else:
        I = 0  # 12144
    if FNL_(A_, 5) == "FÖRLÄ" or FNL_(A_, 5) == "SLADD":
        I = 30  # 12146
    if I == 0:
        print("Det kan man inte koppla in.")
    goto(12210)  # 12148
    goto(7030)  # 12150
    if len(A_) > 10:
        A_ = FNM_(A_, 11)
    else:
        goto(12170)  # KOPPLA UR  # 12160
    if FNL_(A_, 5) == "TELEF":
        I = 25
    else:
        I = 0  # 12162
        if FNL_(A_, 5) == "FÖRLÄ" or FNL_(A_, 5) == "SLADD":
            I = 30  # 12164
        if (I == 30 and S[44] == Z) or (I > 0 and J[Z] == 1):
            goto(6410)  # 12166
    print("Det finns inget inkopplat i jacken.")
    goto(12210)  # 12168
    if S[44] == Z:
        I = 30
    goto(6410)  # 12170
    if J[Z] != 1:
        print("Det finns ingen jack här.")
    goto(12210)  # 12172
    if A[25] == Z:
        I = 25
    goto(6410)  # 12174
    if A[30] == Z:
        I = 30
    goto(6410)  # 12176
    print("Ingenting är inkopplat i jacken.")
    goto(12210)  # 12178


def call_method_91000():
    print("Stuga är ett ADVENTURE-liknande spel på svenska.")  # 91000
    print("Du ska utforska ett hus och dess omgivningar. Datorn är dina")  # 91005
    print("ögon och händer. Ge enkla order till datorn, till exempel:")  # 91010
    print("SLÄPP TAVLAN, GE SAFTFLASKAN, NORR, UPPÅT, VÄNSTER...")  # 91015
    print("Utanför stugan förflyttar du dej med väderstreck som kan för-")  # 91020
    print("kortas till N, S, V, Ö, NV, NÖ, SÖ och SV. Inne i stugan används")  # 91025
    print("riktningarna FRAMÅT (F), BAKÅT (B), VÄNSTER (V), HÖGER (H),")  # 91030
    print("UPPÅT (U) samt NERÅT (N).")  # 91035
    print("I vissa rum kan du få särskild hjälp (det ger poängavdrag) om du")  # 91040
    print("skriver HJÄLP. INVENT listar alla saker du bär på, POÄNG skriver")  # 91045
    print("ut hur många poäng du har och TITTA skriver ut den fullständiga")  # 91050
    print("beskrivningen av rummet. Ge kommandot SLUTA när du är färdig.")  # 91055
    print("Skriv INFO för att få en lista över kommandona.")  # 91060
    print()  # 91065
    print("Du ska försöka att skaffa så många poäng som möjligt. Poäng får")  # 91070
    print("du genom att upptäcka nya ställen och ta vara på värdesaker.")  # 91075
    print()  # 91080


def call_method(n):  # TODO
    pass


# Version: 4O(114)-4     821227/VE  # 00001
S1 = S2 = X1 = 0  # todo
ERROR = ERL = 0  # todo
ERR = 27  # todo
TIME_ = 0  # todo
DATE_ = datetime.today().strftime("%d-%b").upper()
S = [0] * 55  # 00002
W = [""] * 7
W_ = W  # todo
J = [0] * 101
A = [[0] * 4] * 31
X = 0
goto(90000)  # 00003
# ************************  S T U G A  *****************************  # 00005
# ******* STUGA är skrivet av Viggo Eriksson, Kimmo Eriksson *******  # 00010
# ******* och Olle Johansson. Adressen till programmakarna   *******  # 00015
# ******* är Solängsvägen 170, 191 54 SOLlenTUNA.            *******  # 00020
# ******* Denna fil är hemlig och får inte spridas ut utan   *******  # 00025
# ******* författarnas tillstånd.                  810321    *******  # 00030
# ******************************************************************  # 00035
# Rader märkta med _____ är till för kompatibilitet med gamla versioner  # 00050
# Rader märkta med %%%%% får bara finnas med på Oden och Nadja  # 00055
# Rader märkta med &&&&& använder DEC-10-BASIC-filhantering  # 00060
# ********************** THORVALD: ******************************  # 00700


def sub_700():
    if random.random() >= 0.8:  # 00701
        print("               IIIIIIIIIIIIIIII")  # 00702
        print("   _ _ _      II              II      _ _ _")  # 00703
        print("__I I I I_____I                I_____I I I I______")  # 00704
        print("  I I I I     I   I--I  I--I   I     I I I I")  # 00705
        print("  I_I_I_I     I   I  I  I  I   I     I_I_I_I")  # 00706
        print("              I   I  I  I  I   I    ")  # 00707
        print("              I   I *I  I* I   I")  # 00708
        print("              I   I__I  I__I   I")  # 00709
        print("              II              II")  # 00710
        print("               II            II")  # 00711
        print("                II          II")  # 00712
        print("                 I__      __I")  # 00713
        print("                    I    I")  # 00714
        print("                    I    I")  # 00715
        print("                    I    I")  # 00716
        print("                    I    I")  # 00717
        print("                    II  II")  # 00718
        print("                     I__I")  # 00719
        print()  # 00720
        print()  # 00721
    else:
        print("                      I------I")  # 00724
        print("----------------------I *  * I----------------------------")  # 00725
        print("                      I      I")  # 00726
        print("                       --II--")  # 00727
        print("                         II")  # 00728
        print("                         --")


# ******************OLLES SUBRUTIN****************************  # 00730
def sub_730():
    print("Du kommer in i ett rum där det står en massa djur! På en")  # 00731
    print("skylt i luften står det")  # 00732
    print("    RUM UNDER BYGGNAD, SUPREMS BYGGNADS AB")  # 00733
    print("Plötsligt omges du av ett gult moln!")  # 00734


call_method(11000)  # 01499
Z = 53
S[25] = S[25] + 1  # XXXXX VIGGOS ATELJE XXXXX  # 01500
if S[25] > 2 and S[25] < 8:
    print("Du är i Ateljen.")
goto(1511)  # 01503
print("Du är i Ateljen. Här finns det tre dörrar.")  # 01504
print("Dom går åt vänster, åt höger och bakåt.")  # 01505
print("På väggen står det: ALEA JACTA EST")  # 01506
if S[25] > 8:
    S[25] = 4  # 01511
call_method_12200()  # 01512
if X1 == 1:
    goto(1504)  # 01517
if X == 0:
    goto(1499)  # 01518
goto([1499, 1499, 15000, 15050, 1499, 1540, 1530][X])  # 01520
if A[10] == 53:
    goto(1538)  # 01530
print("TIPS!! Prova orden och gå tillbaka hit.")
S[2] = S[2] - 10
goto(1500)  # 01532
print("TIPS!! Ta lagerkransen och skriv HJÄLP igen.")  # 01538
S[2] = S[2] - 10
goto(1500)  # 01539
if A[1] != 1:
    goto(9991)  # 01540
print("Dörren har gått i baklås så du kommer inte ut åt det hållet!")  # 01542
if A[26] == 1 or A[26] == Z:
    print("Dina nycklar passar inte i nyckelhålet.")  # 01544
goto(1500)  # 01548
call_method(11000)  # 01908
print("Du är i en stor svängande labyrint.")  # 01909
Z = 34  # 01910
call_method_12200()  # 01911
if X == 0 or X > 6:
    goto(1908)  # 01913

goto([1970, 1919, 1939, 8095, 1950, 1929][X])  # 01914
call_method(11000)  # 01918
print("Du är i en svängig stor labyrint.")  # 01919
Z = 92
call_method_12200()  # XX KIVIS LABYRintRUM 3 XXXX Z=92 XXX  # 01921
if X == 0 or X > 6:
    goto(1918)  # 01922
goto([1929, 1944, 1960, 1950, 1909, 8300][X])  # 01923
call_method(11000)  # 01928
print("Du är i en svängande stor labyrint.")  # 01929
Z = 89
call_method_12200()  # XX KIVIS LABYRintRUM 2 XXXX Z=89 XXX  # 01931
if X == 0 or X > 6:
    goto(1928)  # 01932
goto([1960, 1950, 1939, 1909, 1970, 1919][X])  # 01933
if random.random() < 0.5:
    goto(16500)
else:
    goto(15432)  # 01939
print("Du är i en återvändsgång. Här står Kimmo och säjer:")  # 01944
print(" - Det här är återvändsgången i denna labyrint.")  # 01945
print("   här gömmer piraten sina skatter. Jag är piraten!")  # 01946
print("               HAR HAR HAR")  # 01947
if G == 1:
    print("Han håller din halvruttna tomat i handen.")  # 01948
print("Du är i en stor svängig labyrint.")  # 01950
Z = 93
call_method_12200()  # XX KIVIS LABYRintRUM 4 XXXX Z=93 XXX  # 01952
if X == 0 or X > 6:
    goto(1956)  # 01953
goto([8000, 1929, 1960, 1970, 1944, 1919][X])  # 01954
call_method(11000)
goto(1950)  # 01956
call_method(11000)  # 01959
print("Du är i en stor labyrint som också är svängig.")  # 01960
Z = 94
call_method_12200()  # XX KIVIS LABYRintRUM 5 XXXX Z=94 XXX  # 01962
if X == 0 or X > 6:
    goto(1959)  # 01963
goto([1919, 8035, 1970, 1980, 1929, 1950][X])  # 01964
call_method(11000)  # 01969
print("Du är i en svängig labyrint som också är stor.")  # 01970
Z = 95
call_method_12200()  # XX KIVIS LABYRintRUM 6 XXXX Z=95 XXX  # 01972
if X == 0 or X > 6:
    goto(1969)  # 01973
goto([1960, 1980, 8071, 1950, 1909, 1929][X])  # 01974
if G == 1:
    goto(1970)
else:
    print("Du har en halvrutten tomat i handen.")  # 01980
print("HAR HAR HAR! ropar en pirat som springer mot dej.")  # 01981
print("Piraten tar din tomat.")  # 01982
G = 1
goto(1970)  # 01983
print("Du är i Högra pannrummet.")  # 02008
S[42] = S[42] + 1  # 02009
if S[42] > 1:
    print("Ett hål finns i väggen.")
    goto(2012)  # 02010
print("En panna sprängs och gör ett hål i väggen.")  # 02011
A_ = FNI_("Vill du gå in i hålet ?")  # 02012
if FNL_(A_, 1) == "J" or FNL_(A_, 1) == "j":
    goto(2019)  # 02014
print("Ok.")  # 02015
goto(14100)  # 02016
call_method(11000)  # 02018
Z = 69  # XXXX GROTTRUM 1 XXXXX Z=69 XXX  # 02019
print("Du är i en grotta som sträcker sej utom synhåll åt vänster och höger.")  # 02020
if S[42] > 0:
    print("Bakom dej finns ett uppsprängt hål.")  # 02021
call_method(20500)  # 02023
if X < 3:
    goto(2018)
else:
    goto([2044, 2032, 2018, 2025, 2018][X - 2])  # 02024
if S[42] > 0:
    goto(14100)
else:
    goto(2018)  # 02025
print("Du gick just genom ett vattenfall.")  # 02032
Z = 91  # XXXXX GROTTRUM 6 XXX Z=91 XXX  # 02033
print("Du är vid ett vattenfall i en skog.")  # 02034
call_method(20500)  # 02035
if X == 0 or X > 6:
    goto(2038)  # 02036
goto([2019, 2066, 2115, 2150, 2066, 2019][X])  # 02037
call_method(11000)  # 02038
goto(2034)  # 02039
call_method(11000)  # 02043
Z = 19  # XXXX GROTTRUM 2 XXX Z=19 XXX  # 02044
if A[12] != 0:
    goto(2051)  # 02045
print("En liten faun springer fram och tänker trampa dej på foten")  # 02046
print("men han tappar en sko och springer ylande därifrån.")  # 02047
A[12] = 19  # 02049
print("Du är i Schweiziska klockrummet.")  # 02051
call_method(20500)  # 02052
if X == 0:
    goto(2043)  # 02054
goto([2043, 2043, 2075, 2150, 2145, 2019, 2043][X])  # 02056
call_method(11000)  # 02065
Z = 33  # XXXXX GROTTRUM 3 XXXXX  # 02066
print("Du är på stranden till en underjordisk sjö.")  # 02067
call_method(20500)  # 02068
if X == 10:
    goto(2107)  # 02071
if X != 0:
    goto([2101, 2104, 2075, 20270, 2107, 2033, 2065][X])
else:
    goto(2065)  # 02073
call_method(11000)  # 02074
Z = 25  # XXX GROTTRUM 5 XXX Z=25 XXX  # 02075
print(
    "Du är på stranden till en underjordisk sjö bredvid en enorm spelautomat."
)  # 02076
print("På den står det:  #DRA I SPAKEN OM DU HAR EN FAUNSKO ATT SATSA #")  # 02077
call_method(20500)  # 02078
if FNL_(A_, 3) != "DRA":
    goto(2089)  # 02079
if A[12] == 1:
    goto(2083)  # 02080
print("FUSKARE! Du har ingen faunsko!")  # 02081
goto(2087)  # 02082
D = random.randint(0, 0) + 1  # 02083
if D > 7:
    goto(2094)  # 02084
print("Grattis    ! Du vann en massa guldmynt.")  # 02085
A[12] = 2
A[7] = 25
S[1] = S[1] - 1  # 02086
print("Du är vid slutet av stranden.")  # 02087
call_method(20500)  # 02088
if X > 0 and X < 7:
    goto([2074, 2074, 20255, 2066, 2107, 2044][X])  # 02089
if X == 10:
    goto(2107)
else:
    goto(2074)  # 02090
print("Tyvärr,du förlorade!")  # 02094
S[1] = S[1] - 1
A[12] = 0  # 02095
goto(2087)  # 02096
print(
    "Du fastnade i en jättesugkopp och kan inte komma loss." + FNS_("sover", 15)
)  # 02101
print("Hoppsan, nu svalt du ihjäl.")  # 02102
goto(9461)  # 02103
print("Du sjunker...S J U N K E R!!")  # 02104
print("Du är")  # 02105
goto(9450)  # 02106
print("Vattnet är lugnt, du simmar fort.")
print(SPACE_(40))  # 02107
goto(2138)  # 02108
print("Järndörrar slår ner omkring dej. Du kan bara gå uppåt.")  # 02109
A_ = FNI_("")
A_ = FNC_(A_)  # 02111
if FNL_(A_, 3) == "UPP" or A_ == "U":
    goto(2135)  # 02112
print("Så kan du väl inte gå!")  # 02113
goto(2111)  # 02114
Z = 20  # XXX GROTTRUM 4 XXX Z=20 XXX  # 02115
print("Du är fortfarande i skogen men åt ett håll skymtar")  # 02116
print("man en stuga.")  # 02117
call_method(20500)  # 02118
if X != 0:
    goto([2120, 2120, 20155, 2120, 2127, 2033, 2120][X])  # 02119
call_method(11000)  # 02120
goto(2115)  # 02121
print("Du hoppar ner i brunnen och ramlar tillslut ner på marken.")  # 02123
goto(14000)  # 02124
call_method(11000)  # 02126
Z = 99  # XXXXX GROTTRUM 7 XXXX Z=99 XXXX  # 02127
print("Du står utanför stugan vid en brunn.")  # 02128
call_method(20500)  # 02129
if X == 0 or X > 6:
    goto(2126)  # 02133
goto([2126, 2123, 2126, 2126, 35000, 2115][X])  # 02134
print("Du har kommit upp ur en brunn. Här finns en stuga.")  # 02135
Z = 99
goto(2129)  # 02136
D = random.randint(0, 4) + 1  # 02138
if D == 2:
    goto(2109)  # 02139
if D > 2:
    goto(36000)
else:
    print("Du dras ner. Nu är du")  # 02140
goto(9450)  # 02143
D = random.randint(0, 5) + 1  # 02145
if D < 4:
    goto(2115)  # 02146
print("En hord fauner kommer framrusande. Nnnnnu är du en våt fläck.")  # 02147
goto(9461)  # 02148
call_method(11000)  # 02149
Z = 98  # XXX GROTTRUM 8 XXXX Z=98 XXXXX  # 02150
print("Du har en halvrutten tomat i handen men den försvinner.")  # 02151
call_method(20500)  # 02152
if X == 0 or X > 6:
    goto(2149)  # 02153
goto([2157, 36000, 2180, 2168, 2161, 2044][X])  # 02154
if S[31] != 0 or A[18] != 1:
    goto(2164)  # 02157
S[31] = 1  # 02158
print("Du har blivit nervös och tar fram brännvinsflaskan och dricker ur den.")  # 02159
goto(2150)  # 02160
print("Du har kommit till en sjö där du ser två båtar.")  # 02161
print("Du kliver i en men upptäcker att den bara var en synvilla.")  # 02162
goto(2104)  # 02163
if S[32] != 0:
    goto(2168)  # 02164
D = random.randint(0, 5) + 1  # 02165
if A[19] == 1 and S[32] == 0:
    goto(2173)  # 02166
S[46] = S[46] + 1  # 02167
print("Du står bakom ett draperi.")  # 02168
goto(2150)  # 02169
S[32] = 1  # 02173
print("Du råkar hälla ut vattnet på en faun som springer ylande iväg.")  # 02174
goto(2150)  # 02175
D = random.randint(0, 0) + 1  # 02180
if D > 8:
    goto(2183)  # 02181
goto(14100)  # 02182
print("Plötsligt känner du en trasa framför näsan och du säckar ihop.")  # 02183
print("När Du vaknar märker Du att ")  # 02184
goto(2168)  # 02185
call_method(11000)  # 02199
Z = 50  # XXX SÖDRA STRANDEN XXXXX Z=50 XXXX  # 02200
print("Du är på den södra sidan av sjön. Här finns ett hus.")  # 02201
if S[35] != 0:
    goto(2207)  # 02203
print("Du hittar ett hål som du kryper ner i.")  # 02204
goto(14000)  # 02205
if S[35] == 1:
    print("Det ligger en roddbåt här.")  # 02207
call_method_15200()  # 02208
if X == 0:
    goto(2220)  # 02211
goto([20255, 20300, 2216, 2241, 20180, 2218, 2199, 2218, 20270, 2107][X])  # 02212
goto(2200)  # 02215
print("Kan du gå på vattnet?")  # 02216
goto(2200)  # 02217
print("Ett staket hindrar dej från att gå ditåt.")  # 02218
goto(2200)  # 02219
if INSTR(A_, "NER") > 0 or INSTR(A_, "NED") > 0 or A_ == "N":
    goto(2204)  # 02220
if S[35] == 1 and (INSTR(A_, "BÅT") > 0 or A_ == "RO"):
    goto(9390)  # 02222
goto(2199)  # 02224
Z = 51  # XXX STRANDHUSET XXXXX Z=51 XXXX  # 02241
print("Du är inne i huset. Här finns en automat med")  # 02242
print("en skylt där det står:")  # 02243
print("   SLÄPP SAKER HÄR, så får du poäng enligt prislistan.")  # 02244
print()  # 02245
print("                  PRISLISTA:")  # 02246
print("        Om du släpper:          Så får du:")  # 02247
print()  # 02248
print("        En tavla         5 poäng")  # 02249
if A[1] == 1:
    print("        En diamant        15 poäng")  # 02250
if A[3] == 1:
    print("         En silvertacka        10 poäng")  # 02251
if A[2] == 1:
    print("        En illaluktande gurka     5 poäng")  # 02252
if A[4] == 1:
    print("        En hillebard        20 poäng")  # 02253
if A[5] == 1:
    print("        En dödskalle        20 poäng")  # 02254
if A[6] == 1:
    print("        En väckarklocka        15 poäng")  # 02255
if A[7] == 1:
    print("        Massor av guldmynt    10 poäng")  # 02256
if A[8] == 1:
    print("        En trilogi        10 poäng")  # 02257
if A[9] == 1:
    print("        Ett kontrakt        15 poäng")  # 02258
if A[10] == 1:
    print("        En lagerkrans        15 poäng")  # 02259
if A[11] == 1:
    print("        Ett pärlhalsband    25 poäng")  # 02260
if A[12] == 1:
    print("        En faunsko         5 poäng")  # 02261
call_method_12200()  # 02272
if X == 15:
    goto(2290)  # 02274
if X == 6:
    goto(2201)  # 02275
if X1 == 1:
    goto(2242)
else:
    call_method(11000)  # 02276
print("Du är vid apparaten och kan bara gå bakåt.")  # 02277
goto(2272)  # 02278
A[I] = 5
S[1] = S[1] - 1  # 02290
S[2] = S[2] + 5  # 02292
if I != 2 and I != 12:
    S[2] = S[2] + 5  # 02294
if I == 1 or I == 6 or I == 10 or I == 9 or I == 11:
    S[2] = S[2] + 5  # 02296
if I == 4 or I == 5 or I == 11:
    S[2] = S[2] + 10  # 02298
print("Maskinen slukar " + A_(I, 4) + ".")  # 02300
goto(2277)  # 02302

print("Här sitter en gubbe med ett pärlhalsband runt halsen.")  # 06202
if A[19] == 0:
    print("I armarna har han en vattenflaska.")  # 06204
if A[19] == 0 and A[10] == 0:
    print("På huvudet bär han din lagerkrans.")  # 06206
if A[19] == 0 and A[10] == 1:
    print("Han stirrar på din lagerkrans.")  # 06208
print()
goto(6040)  # 06210
if C_ != "":
    goto(6305)  # 06300
if Z == 37 and S[38] == 0:
    X = 13
goto(12999)  # 06301
C_ = FNI_("Ta vadå ?")
A_ = C_ = FNC_(C_)  # 06302
for I in range(1, A[0]):  # 06305
    if A_(I, 1) != "":
        if INSTR(C_, A_(I, 2)) > 0 or INSTR(C_, A_(I, 3)) > 0:
            goto(6400)  # 06306
if FNL_(C_, 4) == "ALLT":
    goto(6500)  # 06309
if FNL_(C_, 5) == "VATTE":
    goto(6330)  # 06310
if FNL_(C_, 5) == "GRAVS" and Z == 61:
    print("Gravstenen väger alldeles för mycket.")
goto(12210)  # 06311
if FNL_(C_, 5) == "KISTA":
    goto(6350)  # 06312
if (FNL_(C_, 5) == "FAMIL" or FNL_(C_, 5) == "VAPEN") and Z == 81:
    print("Vapnet sitter för hårt fast.")
goto(12210)  # 06313
if FNL_(C_, 5) == "TAVLA" and S[36] == 0:
    goto(6360)  # 06314
if FNL_(C_, 5) == "SAFTF":
    print("Jag ser ingen SAFTFLASKA här.")
goto(12210)  # 06315
if FNL_(C_, 5) == "FLASK":
    goto(6370)  # 06316
if FNL_(C_, 4) == "PORT" and (Z == 81 or Z == 62):
    print("Porten sitter fast i väggen.")
goto(12210)  # 06317
if FNL_(C_, 4) == "JACK" and J[Z] == 1:
    print("Jacken sitter fastskruvad i väggen!")
goto(12210)  # 06318
if FNL_(C_, 5) == "BRUNN" and Z == 99:
    print("Brunnen är gjuten i marken!")
goto(12210)  # 06319
if FNL_(C_, 5) == "KASSA" and Z == 30:
    print("Det är fastgjutet i berget.")
goto(12210)  # 06320
if FNL_(C_, 3) == "BÅT" and (Z == 49 or Z == 78 or Z == 50):
    goto(6380)  # 06321
if FNL_(C_, 5) == "GUBBE" and S[30] == Z:
    goto(30002)  # 06322
if FNL_(C_, 4) == "LÅDA" and A[28] == 2 and Z == 56:
    print("Lådan är för tung!")
goto(12210)  # 06323
if FNL_(C_, 5) == "RUBIN" and A1 == 1 and Z == 70:
    goto(6355)  # 06324
if FNL_(C_, 3) == "ASK" and A[27] == 2 and Z == 57:
    print("Asken sitter fast i väggen.")
goto(12210)  # 06325
if FNL_(C_, 5) == "FÖNST" and Z == 16 and A[15] == 0:
    print("Fönstret är fastkittat i väggen.")
goto(12210)  # 06326
if Z == 37 and S[38] == 0:
    X = 13
goto(12999)  # 06327
print("Jag ser ingen " + C_ + " här.")
goto(12210)  # 06329
if Z == 25 or Z == 33 or Z == 49 or Z == 50 or Z == 66 or Z == 70 or Z == 91:
    goto(6338)  # 06330
if Z == 72 or Z == 74 or Z == 78 or Z == 79 or Z == 83 or Z == 87 or Z == 88:
    goto(6338)  # 06332
print("Jag ser inget VATTEN här.")  # 06334
goto(12210)  # 06336
if A[19] != 1:
    print("Du har inget att ta vattnet i.")
goto(12210)  # 06338
if S[32] == 0:
    print("Din vattenflaska är redan full.")
goto(12210)  # 06340
print("Du fyller på vattenflaskan med vatten från ")  # 06342
if Z == 91:
    print("vattenfallet.")
else:
    print("sjön.")  # 06344
S[32] = 0
goto(12210)  # 06346
if Z == 15:
    print("Kistan väger 300 kilogram!")
else:
    print("Jag ser ingen KISTA här.")  # 06350
goto(12210)  # 06352
print("Just när du ska ta rubinen kommer Thorvald fram och utropar")  # 06355
print(" - April, april! Nu tar jag hand om rubinen själv!")  # 06356
A1 = 0
goto(12210)  # 06357
print("Du kan väl inte sno en av husets tavlor!")  # 06360
S[2] = S[2] - 1
goto(12210)  # 06362
print("Du måste skriva vilket slags flaska du menar, t ex TA SAFTFLASKA.")  # 06370
goto(12210)  # 06372
print("Du orkar inte bära roddbåten.")  # 06380
goto(12210)  # 06382
if (I == 4 or I == 15 or I == 25 or I == 26) and A[I] == 2:
    goto(28130)  # 06400
if (I == 10 or I == 11 or I == 19) and S[30] == Z and A[I] == 0:
    goto(30020)  # 06402
if I == 22 and Z == 63:
    goto(28160)  # 06404
if I == 29 and S[6] != 1:
    print("Det kan du inte.")
goto(12210)  # 06406
if A[I] == Z or (I == 30 and S[44] == Z):
    goto(6420)  # 06410
if A[I] == 1:
    print("Du bär redan " + A_(I, 4) + ".")
goto(12210)  # 06412
if A[I] == 5:
    print("Man kan inte ta tillbaka saker från maskinen.")
    goto(12210)  # 06414
    print("Jag ser " + FNA_(I) + A_(I, 1) + " här.")
goto(12210)  # 06418
if S[1] == 9:
    print("Du kan inte bära fler saker.")
goto(12210)  # 06420
S[1] = S[1] + 1
A[I] = 1  # 06422
if I == 30 and (J[Z] == 1 or S[44] == Z):
    S[44] = 0
print("Du rycker loss sladden.")
goto(12210)  # 06424
if I == 30:
    S[44] = 0  # 06425
if I == 25 and (S[44] == Z or J[Z] == 1):
    print("Du kopplar ur telefonen.")
else:
    print("Ok.")  # 06426
goto(12210)  # 06428
I = 0  # TA ALLT  # 06500
for I1 in range(1, A[0]):  # 06505
    if A(I1) != Z and (I1 != 30 or S[44] != Z):
        goto(6550)  # 06510
    if I1 == 29 and S[6] != 1:
        goto(6550)  # 06512
    if S[1] < 9:
        goto(6535)  # 06515
    if I == 0:
        print("Du kan inte bära fler saker.")  # 06520
    if I > 0:
        print(".")
    print("Du kan inte bära resten.")  # 06525
    goto(12210)  # 06530
    if I == 0:
        print("Du tar ")
    else:
        print(" och ")  # 06535
    print(A_(I1, 4))
    S[1] = S[1] + 1
    A[I1] = 1
    I = I + 1  # 06540
    if I1 == 22 and Z == 63:
        S[2] = S[2] - 30
    S[52] = 0  # 06545
    if I1 == 30:
        S[44] = 0  # 06547

if Z == 70 and A1 == 1:
    print()
goto(6355)  # 06551
if I == 0 and Z == 37 and S[38] == 0:
    print("Jag ser inget du kan ta här.")
goto(6560)  # 06552
if I == 0:
    print("Det finns inget som du kan ta här.")
else:
    print(".")  # 06555
goto(12210)  # 06560
# XXXXX SLÄPP XXXXX  # 07000
if C_ == "":
    C_ = FNI_("Släpp vadå ?")
A_ = C_ = FNC_(C_)  # 07001
for I in range(1, A[0]):  # 07003
    if A_(I, 1) != "":
        if INSTR(C_, A_(I, 2)) > 0 or INSTR(C_, A_(I, 3)) > 0:
            goto(7030)  # 07005
if FNL_(C_, 4) == "ALLT":
    goto(7100)  # 07008
if C_ == "DEJ" or C_ == "DIG":
    goto(7020)  # 07009
print("Du bär väl ingen " + C_ + "!")
goto(12210)  # 07018
print("Fy! Det vill jag inte.")
S[2] = S[2] - 1
goto(12210)  # 07020
if A[I] == 1:
    goto(7040)  # 07030
print("Du bär väl " + FNA_(I) + A_(I, 1) + "!")  # 07034
goto(12210)  # 07036
if (I == 10 or I == 19) and S[30] == Z:
    goto(7090)  # 07040
if I == 25 and (S[44] == Z or J[Z] == 1):
    goto(7075)  # 07041
if Z == 51 and I < 15:
    X = 15
goto(12999)  # 07042
if Z == 4:
    print("En mystisk kraft hindrar dej från att släppa någonting här.")
goto(12210)  # 07043
if I == 22 and Z == 63:
    S[52] = S[50]
S[2] = S[2] + 25  # 07044
if I == 30 and J[Z] == 1:
    S[44] = -1
else:
    if I == 30:
        S[44] = 0  # 07045
A[I] = Z
S[1] = S[1] - 1  # 07050
if I == 22 and Z == 63:
    print("Du lägger försiktigt ner liket.")
else:
    print("Ok.")  # 07052
goto(12210)  # 07054
S[28] = S[28] + 1
S[1] = S[1] - 1
A[25] = Z  # 07075
if S[28] == 2:
    goto(27100)  # 07077
if S[28] / 3 != int(S[28] / 3) or random.random() < 0.5:
    print("Du kopplar in telefonen.")
    goto(12210)  # 07078
print("Just som du ska koppla in telefonen kommer en man klädd i en röd")  # 07080
print("dräkt som det står  #TELE # på, ")  # 07081
if J[Z] == 1:
    print("skruvar bort telefonjacken")
J[Z] = 0  # 07082
if J[Z] != 1:
    print("tar bort förlängningssladden")
S[44] = 0
A[30] = 0  # 07083
print("och sluddrar fram:")  # 07084
print("- Abonnemangsavgiften är inte betald.")  # 07085
X1 = 1
call_method(27050)  # 07087
goto(12999)  # 07088
if I == 19:
    print("Gubben tar snabbt vattenflaskan när du släpper den.")
goto(7094)  # 07090
print("Gubben sätter din lagerkrans på sitt huvud och ser genast gladare ut.")  # 07092
A[I] = 0
S[1] = S[1] - 1  # 07094
goto(12210)  # 07096
I = 0  # SLÄPP ALLT  # 07100
if Z == 4:
    goto(7043)  # 07102
for I1 in range(1, A[0]):  # 07105
    if A(I1) != 1:
        goto(7135)  # 07110
    if I1 == 22 and Z == 63:
        S[52] = S[50]
    S[2] = S[2] + 25  # 07115
    if I1 == 30 and J[Z] == 1:
        S[44] = -1
    else:
        if I1 == 30:
            S[44] = 0  # 07117
    A[I1] = Z
    S[1] = S[1] - 1  # 07120
    if I == 0:
        print("Du släpper ")
    else:
        print(" och ")  # 07125
    print(A_(I1, 4))
    I = I + 1  # 07130
if I == 0:
    print("Du bär inte på någonting!")
else:
    print(".")  # 07140
goto(12210)  # 07145
for i in range(1, A[0]):
    if A[I] == 1:
        A[I] = Z  # Släpper allt man bär i rummet  # 07500
S[1] = 0  # 07502
# ? return  # 07504
Z = 35  # XXXXX HISSENS MASKINRUM XXX Z=35 XXX  # 07556
print("Du är i hissens maskinrum. Det bullrar och låter.")  # 07558
print("Det finns en dörr bakom Dej.")  # 07559
if A[1] != 1:
    print("Det finns en lucka i golvet.")  # 07560
call_method_12200()  # 07562
if X1 == 1:
    goto(7556)  # 07564
if X == 6:
    goto(35000)  # 07566
if X == 2 and A[1] != 1:
    goto(7570)
else:
    call_method(11000)
goto(7556)  # 07568
call_method(11000)  # 07569
print("Du är i ett litet rum utan fönster.")  # 07570
Z = 32
call_method_12200()  # 07573
if X1 == 1:
    goto(7588)  # 07579
if X == 1:
    goto(7556)  # 07585
if X == 0 or X == 7:
    goto(7569)  # 07586
if X == 5:
    goto(13000)  # 07587
print("Du kan gå framåt och uppåt.")
goto(7570)  # 07588
call_method(8290)  # 07999
Z = 43  # XXXXX LABYRintRUM 8 XXX Z=43 XXX  # 08000
print("Du är i en gångande vindel.")  # 08001
call_method_12200()  # 08002
if X == 0 or X > 7:
    goto(7999)  # 08003
if S[45] == 1:
    goto([1929, 8330, 1944, 8300, 8420, 8300, 8011][X])  # 08007
print("Det hänger en tavla här.")  # 08008
call_method(700)  # 08009
goto([8330, 7999, 8400, 17000, 8020, 16000, 8011][X])  # 08010
goto(8017)  # 08011
S[2] = S[2] - 2  # 08017
print("Gå inte åt höger eller neråt!")
goto(8000)  # 08018
call_method(8290)  # 08019
Z = 44  # XXXXX LEBYRintRUM 9 XXX Z=44 XXX  # 08020
print("Du är i en gång med vindlar överallt.")  # 08021
call_method_12200()  # 08022
if X == 4:
    S[45] = 2  # 08025
if X == 0 or X > 6:
    goto(8019)  # 08026
goto([8250, 8263, 8430][S[45]])  # 08027
call_method(8290)  # 08034
Z = 45  # XXXXX LABYRintRUM 10 XXXXX Z=45 XXX  # 08035
print("Du är i en vindlande gång med hål överallt.")  # 08036
call_method_12200()  # 08037
if X == 0 or X > 6:
    goto(8034)  # 08038
if S[45] == 1:
    S[45] = 3  # 08040
if S[45] == 3:
    goto([8000, 1919, 8300, 8020, 17000, 8365][X])  # 08041
goto([1919, 8071, 8020, 8365, 8300, 8330][X])  # 08042
print("Den här hjälpen kostar inget.")  # 08054
S[3] = 1
S[41] = 1  # 08056
goto(8035)  # 08057
goto([8252, 8258, 8256][S[45]])  # 08067
call_method(8290)  # 08070
Z = 38  # XXXXX LABYRintRUM 3 XXXX Z=38 XXX  # 08071
print("Du är i ett rum som vindlar.")  # 08072
call_method_12200()  # 08073
if X == 0 or X > 6:
    goto(8070)  # 08074
if S[45] == 3:
    goto([8095, 8071, 1919, 8365, 8330, 8020][X])  # 08075
goto([8261, 8253][S[45]])  # 08076
call_method(11000)  # 08093
Z = 39  # XXXXX LABYRintRUM 4 XXXXX  # 08095
print("Du är i ett rum med hål överallt.")  # 08096
if S[48] > 0:
    print("Det finns ett krossat fönster här.")
goto(8102)  # 08097
print("Högt uppe i taket finns ett fönster.")  # 08100
print("Någon knackar på det!!!")  # 08101
call_method_12200()  # 08102
if X1 == 1:
    goto(8095)  # 08103
if X == 13:
    goto(8131)
else:
    if X == 0:
        goto(8093)  # 08104
if X != 7:
    goto(8112)  # 08105
if A[20] == 1 and S[33] == 0:
    print("Sparka din pumpade boll!")
    S[2] = S[2] - 5
    goto(8095)  # 08106
print("Inget du bär kan hjälpa dej att komma upp till fönstret.")
S[2] = S[2] - 2  # 08108
goto(8095)  # 08110
goto([8250, 8254, 8253][S[45]])  # 08112
print("Du sparkar din boll mot fönstret.")  # 08131
print("   PANG!")  # 08132
print("Fönsterrutan gick sönder.")
if S[48] == -1:
    S[2] = S[2] + 10
S[48] = 0  # 08133
S[48] = S[48] + 1  # 08134
print("Ett rep ramlar ner genom fönstret och nån viskar: -Kom fort!")  # 08135
A_ = FNI_("Klättrar du upp på repet ?")  # 08137
if FNL_(A_, 1) == "N" or FNL_(A_, 1) == "n":
    goto(8142)  # 08138
if FNL_(A_, 1) == "J" or FNL_(A_, 1) == "j":
    goto(8144)  # 08139
print("Bestäm dej!")  # 08140
goto(8137)  # 08141
print("TYST!! Han hörde dej och drog upp repet!!!")  # 08142
goto(8095)  # 08143
print("Du klättrar upp i en mörk gång efter en mörk skugga.")  # 08144
print("Långt borta hörs en röst:")  # 08145
print(" - HÖ, HÖ! En boll! In med den!!!")  # 08146
A[20] = 4
S[1] = S[1] - 1  # 08147
if S[48] != -1:
    print("Du är i en mörk gång.")
else:
    call_method(730)
goto(17000)  # 08148
Z = 97  # XXXXX MÖRK GÅNG ÖVER LAB.4 XXXX  # 08149
call_method_12200()  # 08150
if X > 0:
    goto([17000, 25000, 18000, 10020, 8300, 8155, 8153][X])  # 08152
call_method(11000)  # 08153
goto(8149)  # 08154
if S[47] == 1:
    goto(9510)
else:
    goto(2168)  # 08155
goto([8365, 8300, 8000, 8330, 8020, 8095, 8011][X])  # 08250
goto([8420, 8000, 8365, 8300, 17000, 8095, 8054][X])  # 08252
goto([8330, 8020, 8330, 8330, 8300, 8420, 8054][X])  # 08253
goto([8381, 8000, 1500, 1919, 8330, 8300, 8054][X])  # 08254
goto([8095, 8000, 8420, 8071, 8300, 8330, 8054][X])  # 08256
goto([8300, 8920, 8095, 8071, 8330, 14100, 8054][X])  # 08258
goto([8381, 8365, 8300, 8000, 17000, 8071, 8054][X])  # 08261
goto([8095, 8095, 8300, 8365, 8067, 1919, 8054][X])  # 08263
print("Du kan gå åt vänster,höger,framåt,bakåt,uppåt och neråt!")  # 08290
# ? return  # 08291
Z = 36  # XXXXX LABYRintRUM 1 XXXXX  # 08300
print("Du är i en vindlande liten gång med hål.")  # 08302
call_method_12200()  # 08304
if X == 1:
    goto(8095)
elif X == 0:
    goto(8310)  # 08306
if S[45] == 1:
    goto([8320, 17000, 8000, 8322, 8365, 8330, 8700][X])  # 08307
if S[45] == 2:
    goto([8327, 8320, 8365, 8300, 8330, 8381, 8700][X])  # 08308
if S[45] == 3:
    goto([1500, 8330, 8320, 8365, 8322, 8381, 8323][X])  # 08309
call_method(8290)  # 08310
goto(8304)  # 08311
print("Återvändsgränd!")  # 08320
goto(8300)  # 08321
S[45] = 2
goto(8420)  # 08322
print("TIPS!! Skriv framåt!")  # 08323
S[2] = S[2] - 4  # 08324
goto(8300)  # 08325
print("Du är")  # 08327
goto(9450)  # 08328
call_method(8290)  # 08329
Z = 37  # XXXXX LABYRintRUM 2 XXX Z=37 XXXX  # 08330
if S[38] == 0:  # 08331
    print("Du är i en kolsvart gång.")
    goto(8335)
print("Du är i en gång där det på väggen står:")  # 08332
print("Lampan försvinner om det tas ur gången. Stanna kvar!")  # 08333
call_method_6000()  # 08334
A_ = FNI_("")  # 08335
call_method_12000()
if FNL_(A_, 5) == "VÄNTA" or FNL_(A_, 5) == "STANN":
    goto(8345)  # 08336
if X == 13:
    goto(8350)  # 08338
if X == 7 and S[38] == 0:
    goto(8343)  # 08339
if X == 0 or X > 6:
    goto(8329)  # 08340
if S[38] == 1:
    A[24] = 31
S[38] = 2
S[1] = S[1] - 1
print("Lampan försvinner!")  # 08341
goto([8300, 8327, 8320, 8365, 8420, 1919][X])  # 08342
print("HJÄLP: Det finns en sak här i mörkret.")  # 08343
S[2] = S[2] - 5
goto(8330)  # 08344
if A[24] != 1 or S[38] != 1:
    goto(8349)  # 08345
print("Lampan och ")  # 08347
S[38] = 2  # 08348
print("Du lyfts uppåt.")
goto(8148)  # 08349
if S[1] == 9:
    print("Du kan inte bära fler saker.")
goto(8330)  # 08350
print("När du rör saken blir det ljust i gången. Saken är")  # 08351
print("en lampa. På väggen ser du att det står:")  # 08352
S[1] = S[1] + 1
A[24] = 1
S[38] = 1  # 08353
goto(8333)  # 08354
call_method(8290)  # 08363
Z = 40  # XXXXX LABYRintRUM 5 XXXXX  # 08365
print("Du är i en gång med hål.")  # 08366
call_method_12200()  # 08367
if X == 0:
    goto(8363)  # 08368
if S[45] == 1:
    goto([8420, 8328, 8381, 14100, 8330, 8376, 8373][X])  # 08369
if S[45] == 2:
    goto([8376, 8300, 8400, 8320, 8381, 8420, 8700][X])  # 08370
if S[45] == 3:
    goto([8381, 8327, 8320, 8330, 8376, 8420, 8700][X])  # 08371
print("TIPS! Gå åt höger.")  # 08373
S[2] = S[2] - 4  # 08374
goto(8365)  # 08375
if A[8] != 1:
    goto(8330)  # 08376
print("Din trilogi (Sagorna om Härskarringen) försvinner plötsligt.")  # 08377
A[8] = 31
S[1] = S[1] - 1  # 08378
goto(8365)  # 08379
call_method(8290)  # 08380
Z = 41  # XXXXX LABYRintRUM 6 XXXXX  # 08381
print("Du vindlar i en liten gång.")  # 08382
call_method_12200()  # 08384
if X == 0:
    goto(8380)  # 08386
if S[45] == 1:
    goto([8365, 8000, 8300, 8400, 8420, 8320, 8391][X])  # 08387
if S[45] == 2:
    goto([8000, 8300, 8400, 8365, 8420, 8330, 8392][X])  # 08388
if S[45] == 3:
    goto([8420, 8365, 8000, 8400, 8300, 8330, 8392][X])  # 08389
S[45] = 3  # 08391
print("TIPS!!  Gå uppåt eller bakåt!")
S[45] = 3  # 08392
S[2] = S[2] - 4  # 08393
goto(8380)  # 08394
Z = 42  # XXXXX LABYRintRUM 7 XXXXX  # 08400
print("Du står på kanten till en djup brunn.")  # 08401
print("Om du hoppar ner kommer du inte upp igen!")  # 08402
call_method_12200()  # 08403
if X == 0:
    goto(8400)  # 08406
if S[45] == 1:
    goto([8420, 8327, 8381, 8420, 8300, 8330, 8414][X])  # 08407
S[45] = 3  # 08408
goto([8420, 8327, 8330, 8420, 8381, 8300, 8414][X])  # 08409
print("TIPS!! Chansa på uppåt eller neråt!")  # 08414
S[2] = S[2] - 4  # 08415
goto(8403)  # 08416
call_method(8290)  # 08419
Z = 52  # XXXXX LABYRintRUM 11 XXXXX  # 08420
print("Lilla du vindlar.")  # 08421
if S[43] == 0:
    goto(8800)  # 08422
call_method_12200()  # 08423
if X == 0 or X > 6:
    goto(8419)  # 08425
if S[45] == 1:
    goto([8071, 1929, 8381, 8000, 8300, 1500][X])  # 08426
if S[45] == 2:
    goto([8000, 8365, 1950, 8381, 1500, 8300][X])  # 08428
if S[45] == 3:
    goto([8300, 8000, 8365, 1970, 8381, 1500][X])  # 08430
# XXXX FOZZIS BERÄTTELSE XXXXX  # 08440
print("Fozzi tar dej med in i hans loge och säjer :")  # 08442
print(" - Om du säjer ett niosiffrigt tal där ingen siffra är över fem")  # 08443
print("så ska jag, Fozzi den rolige, hjälpa Dej med en berättelse.")  # 08444
A_ = FNI_("Svara SPRINGA eller ett niosiffrigt tal :")  # 08445
if FNC_(FNL_(A_, 5)) == "SPRIN":  # 08446
    goto(8842)
if len(A_) != 9:  # 08447
    goto(8445)

if not all(ch.isdigit() for ch in A_):  # 08448
    goto(8445)
for i in range(0, 9):  # 08450
    X[i] = ord(A_[i])
print()  # 08460
print("Fozzi skriver upp en berättelse på en lapp som han ger dej.")  # 08463
print("Du går tillbaka till scenen och berättar.")  # 08465
print()  # 08470
print(" - Ett meddelande når " + FNF_(1) + " att " + FNF_(2))  # 08472
print("  har släppts ut ur " + FNF_(3) + " och kommer för att lägga")  # 08475
print("  beslag på " + FNF_(4) + ". Staden befinner sej snart i klorna på")  # 08480
print("  " + FNF_(5) + " och folket sätter sej ner och väntar på ")  # 08485
print("  " + FNF_(6) + ".")  # 08487
print("  Oroliga för att skurkarna tänker " + FNF_(7) + " börjar")  # 08490
print("  saloonflickorna bli " + FNF_(8) + ". Skurkarna kommer")  # 08495
print("  men faran avvärjs " + FNF_(9) + ".")  # 08500
print()
print("Publiken jublar men gubbarna på balkongen är bara spydiga.")  # 08532
goto(8907)  # 08533
S[36] = 1  # XXX VÄDERSTRECKSSUBRUTIN XXXXX  # 08600
if A_ == "":
    goto(12210)  # 08602
X = 0
X1 = 0
A_ = FNC_(A_)  # 08603
if FNL_(A_, 6) == "SYDOST" or FNL_(A_, 6) == "SYDÖST" or A_ == "SO" or A_ == "SÖ":
    X = 8  # 08604
if FNL_(A_, 4) == "VÄST" or A_ == "V":
    X = 1  # 08605
if FNL_(A_, 3) == "ÖST" or FNL_(A_, 3) == "OST" or A_ == "Ö" or A_ == "O":
    X = 2  # 08606
if FNL_(A_, 4) == "NORR" or FNL_(A_, 4) == "NORD" or A_ == "N":
    X = 3  # 08607
if FNL_(A_, 3) == "SYD" or FNL_(A_, 5) == "SÖDER" or A_ == "S":
    X = 4  # 08608
if FNL_(A_, 5) == "NORDV" or A_ == "NV":
    X = 5  # 08609
if FNL_(A_, 4) == "SYDV" or A_ == "SV":
    X = 6  # 08610
if FNL_(A_, 5) == "NORDO" or FNL_(A_, 5) == "NORDÖ" or A_ == "NO" or A_ == "NÖ":
    X = 9  # 08611
goto(12025)  # 08612
# XXXX INVENTERING XXX  # 08613
if S[1] == 0:
    print("Du bär ingenting.")
goto(12210)  # 08614
print("Du bär på")  # 08615
if A[1] == 1:
    print("en gnistrande diamant")  # 08617
if A[15] == 1:
    print("en stor kofot")  # 08618
if A[16] == 1:
    print("en ny cykelpump")  # 08619
if A[2] == 1:
    print("en illaluktande gurka")  # uääääääääääääääää  )# 08620
if A[3] == 1:
    print("en snygg silvertacka")  # 08621
if A[17] == 1:
    print("en lång stege")  # 08622
if A[18] != 1:
    goto(8626)  # 08623
if S[31] == 0:
    print("en full brännvinsflaska")  # 08624
if S[31] == 1:
    print("en tom brännvinsflaska")  # 08625
if A[19] != 1:
    goto(8629)  # 08626
if S[32] == 0:
    print("en full vattenflaska")  # 08627
if S[32] == 1:
    print("en tom vattenflaska")  # 08628
if A[20] != 1:
    goto(8632)  # 08629
if S[33] == 0:
    print("en pumpad boll")  # 08630
if S[33] == 1:
    print("en opumpad boll")  # 08631
if A[4] == 1:
    print("en sylvass hillebard")  # 08632
if A[21] == 1:
    print("en jordig spade")  # 08633
if A[5] == 1:
    print("en urgammal dödskalle")  # 08634
if A[6] == 1:
    print("en tickande väckarklocka")  # 08635
if A[11] == 1:
    print("ett glittrande pärlhalsband")  # 08637
if A[22] == 1:
    print("ett äckligt lik")  # 08638
if A[12] == 1:
    print("en ful faunsko")  # 08640
if A[7] == 1:
    print("en massa guldmynt")  # 08641
if A[25] == 1:
    print("en modern telefon")  # 08642
if A[26] == 1:
    print("några gamla nycklar")  # 08645
if A[27] == 1:
    print("en vass sax")  # 08646
if A[28] == 1:
    print("en tung slägga")  # 08647
if A[8] == 1:
    print("en läsvärd trilogi (Sagorna om Härskarringen)")  # 08650
if A[24] == 1:
    print("en lampa")  # 08651
if A[9] == 1:
    print("ett skärt kontrakt")  # 08652
if A[10] == 1:
    print("en grön lagerkrans")  # 08653
if A[23] == 1:
    print("en tunn telefonkatalog")  # 08654
if A[30] == 1:
    print("en förlängningssladd till telefonen")  # 08656
goto(12210)  # 08663
print("Du kan inte få nå #n hjälp så som du ser ut!")
D = random.randint(0, 5) + 1  # 08700
goto([8000, 8300, 8095, 8035, 8420][D])  # 08701
S[43] = 1  # XXX MUPPET SHOW XXX  # 08800
if W_(6) != "":
    goto(8808)  # 08802
print("Här sitter björnen Fozzi och frågar:")  # 08804
W_[6] = FNI_("Vad heter du ?")
goto(8810)  # 08806
print("Björnen Fozzi skyndar förbi dej.")  # 08808
# PLATS FÖR SIGNATUR  # 08810
print("Någon säjer: Här är THE MUPPET SHOW med kvällens gäst-")  # 08830
print("artist: " + W_(6))  # 08831
print("Ridån går upp och du är på en scen tillsammans med")  # 08833
print("grodan Kermit. Dockpubliken applåderar.")  # 08834
A_ = FNI_("Svara SPRING eller UPPTRÄD :")
A_ = FNC_(A_)
print()  # 08836
if FNL_(A_, 5) == "SPRIN":
    goto(8842)  # 08838
if FNL_(A_, 5) == "UPPTR":
    goto(8873)  # 08839
goto(8836)  # 08840
print("Du springer rätt in i ett monster som slukar dej i en enda")  # 08842
print("munsbit! Du känner en sprängladdning här!")  # 08843
A_ = FNI_("Svara ROPA eller SPRÄNG :")
A_ = FNC_(A_)
print()  # 08845
if FNL_(A_, 4) == "ROPA":
    goto(8850)  # 08846
if FNL_(A_, 5) == "SPRÄN":
    goto(8857)  # 08847
goto(8845)  # 08848
print("Du ropar och Kermit hämtar hjälp. Det tar tid.")  # 08850
A_ = FNI_("Svara VÄNTA eller SPRÄNG :")
A_ = FNC_(A_)
print()  # 08852
if FNL_(A_, 5) == "VÄNTA":
    goto(8860)  # 08853
if FNL_(A_, 5) == "SPRÄN":
    goto(8857)  # 08854
goto(8852)  # 08855
print("Du och monstret sprängs i bitar!    ")  # 08857
goto(9461)  # 08859
print("Du väntar i 30 sekunder!")  # 08860
S = ECHO(1)  # 08861
for I in range(1, 6):  # 08862
    D = time.sleep(5)  # 08863
    if D:
        A_ = input()  # 08864
S = ECHO(0)  # 08868
print("Någon skär upp magen. Du märker att")  # 08870
goto(8833)  # 08871
print("Kermit frågar dej om du vill sjunga eller berätta en historia.")  # 08873
A_ = FNI_("Svara SJUNG eller BERÄTTA :")
A_ = FNC_(A_)
print()  # 08875
if FNL_(A_, 5) == "SJUNG":
    goto(8890)  # 08876
if FNL_(A_, 5) == "BERÄT":
    goto(8880)  # 08877
goto(8875)  # 08878
print("Du börjar att berätta men efter första meningen")  # 08880
print("avbryts du av kraftiga bu-rop. Bara två gubbar pä")  # 08881
print("läktaren skrattar (åt ditt utseende). Fozzi erbjuder dej hjälp.")  # 08882
A_ = FNI_("Svara HJÄLP eller SPRING :")
A_ = FNC_(A_)
print()  # 08884
if FNL_(A_, 5) == "SPRIN":
    goto(8842)  # 08885
if FNL_(A_, 5) == "HJÄLP":
    goto(8440)  # 08886
goto(8884)  # 08887
print("Du börjar sjunga: I #m a poor lonesome cowboy and a")  # 08890
print("long way from home...")  # 08891
print("Publiken jublar men sångarna Wayne & Wanda är arga")  # 08894
print("på dej för att du tagit deras plats. Dom vill döda dej!")  # 08895
A_ = FNI_("Svara FRED (med Wayne & Wanda) eller FÖLJ (Kermit) :")  # 08897
A_ = FNC_(A_)
print()  # 08898
if FNL_(A_, 4) == "FRED":
    goto(8920)  # 08899
if FNL_(A_, 4) != "FÖLJ":
    goto(8897)  # 08900
D = random.randint(1, 7)  # 08902
if D > 4:
    goto(8907)  # 08903
print("Wayne & Wanda kommer bakifrån och kastar upp dej i luften!")  # 08904
S[43] = 0
goto(8963)  # 08905
print("Du följer efter Kermit för att få ett kontrakt.")  # 08907
W_[2] = FNI_("Fozzi säjer: Skriv ett intresse som du har :")  # 08910
print("Fozzi tackar för sej och går.")
if S[1] == 9:
    goto(9528)  # 08912
print("Du får ett skärt kontrakt av Kermit.")
print("Det finns en dörr till höger.")  # 08913
A[9] = 1
S[1] = S[1] + 1  # 08914
A_ = FNI_("Svara FÖLJ (Fozzi) eller HÖGER :")
A_ = FNC_(A_)
print()  # 08915
if FNL_(A_, 4) == "FÖLJ":
    goto(8943)  # 08916
if FNL_(A_, 5) == "HÖGER":
    goto(8950)  # 08917
goto(8915)  # 08918
print("Du går fram mot Wayne & Wanda för att sluta fred.")  # 08920
D = random.randint(0, 0) + 1  # 08921
if D == 1:
    goto(8904)  # 08922
print("Du bestämmer att du inte ska sjunga mer så W&W")  # 08923
print("ska kunna behålla jobbet. Fozzi kommer fram och säjer:")  # 08924
W_[2] = FNI_("Skriv ett intresse du har!")  # 08925
print("Fozzi tackar för sej och går. Det finns en dörr till vänster.")  # 08928
A_ = FNI_("Svara FÖLJ (Fozzi) eller VÄNSTER :")
A_ = FNC_(A_)
print()  # 08929
if FNL_(A_, 5) == "VÄNST":
    goto(8950)  # 08930
if FNL_(A_, 4) == "FÖLJ":
    goto(8943)  # 08931
goto(8929)  # 08932
print("Nu går Fozzi in genom en dörr. Det finns också en dörr framåt.")  # 08943
A_ = FNI_("Svara FÖLJ (Fozzi) eller FRAMÅT :")
A_ = FNC_(A_)
print()  # 08944
if FNL_(A_, 5) == "FRAMÅ":
    goto(8950)  # 08945
if FNL_(A_, 4) == "FÖLJ":
    goto(8970)  # 08946
goto(8944)  # 08947
print("Du är innanför dörren. Kermit kommer fram och säjer")  # 08950
print("att du ska vara med i en diskussion om " + W_(2))  # 08951
A_ = FNI_("Svara DISKUTERA eller SPRING :")
A_ = FNC_(A_)
print()  # 08953
if FNL_(A_, 5) == "DISKU":
    goto(8980)  # 08954
if FNL_(A_, 5) == "SPRIN":
    goto(8960)  # 08955
goto(8953)  # 08957
print("Du springer rätt in i ett monster som slukar grönsaker!")  # 08960
print("Han tar upp dej och kastar dej högt upp i luften.")  # 08961
D = random.randint(0, 5) + 1  # 08963
goto([8327, 1500, 14100, 9145, 16000][D])
goto([8327, 1500, 14100, 9145, 16000][D])  # 08964
print("Du är inne i en tortyrkammare. Dörren gick i lås bakom dej!")  # 08970
print("Väggarna närmar sej. Enda vägen ut spärras av ett monster!")  # 08971
A_ = FNI_("Svara SPRING (ut) eller STANNA :")
A_ = FNC_(A_)
print()  # 08973
if FNL_(A_, 5) == "SPRIN":
    goto(8960)  # 08974
if FNL_(A_, 5) == "STANN":
    goto(8977)  # 08975
goto(8973)  # 08976
print("Väggarna klämmer ut inälvorna på dej!")  # 08977
goto(9461)  # 08978
S[2] = S[2] + 30  # 08980
print("Kermit inleder: Nu ska vi återigen höja programmets")  # 08983
print("intellektuella nivå. Vi ska idag prata kring ämnet " + W_(2) + ".")  # 08984
print(W_(6) + " får inleda med en replik. Vad tycker du om " + W_(2) + "?")  # 08985
A_ = FNI_("")  # 08987
print("Kermit: Jag håller fullständigt med dej!")  # 08988
print("Fozzi: Nej helt fel, tvärt om!")  # 08989
print("Gubbarna: Ut med björnen!")  # 08990
print("Fozzi: Det var det värsta!!!!")  # 08991
print("Gubbarna: Nej dina skämt är värre! HA     HA     HA    ...")  # 08992
print("Fozzi: Jag ska minsann...")  # 08993
print("Kermit: Öh...Vi får visst avrunda här. Nästa veckas ämne:")  # 08994
print("-Varför retas folk?")  # 08995
print("Vi ses då i: *****THE MUPPET SHOW*****")  # 08996
goto(1500)  # 08997
call_method(11000)  # 08999
Z = 21
R_ = "första"  # XXXX HISSRUM 1 XXX Z=21 XXX  # 09000
call_method(9250)  # 09002
call_method_12200()  # 09004
if X == 4:
    goto(16000)  # 09008
if X != 3:
    goto(8999)  # 09010
call_method(9260)  # 09012
goto([9008, 9300, 9000][X])  # 09014
call_method(11000)  # 09019
Z = 28
R_ = "åttonde"  # XXXX HISSRUM 8 XXX Z=28 XXX  # 09020
call_method(9250)  # 09022
call_method_12200()  # 09024
if X == 4:
    goto(41000)  # 09026
if X != 3:
    goto(9019)  # 09028
call_method(9260)  # 09030
goto([9026, 9300, 9020][X])  # 09032
Z = 22  # XXXX HISSRUM 2 XXX Z=22 XXX  # 09035
print("Du befinner dej i andra våningens hissrum. Till höger ser man")  # 09037
if S[40] == 2:
    print("en öppen")
else:
    print("en stängd")  # 09039
print(" hissdörr. I den vänstra väggen finns")  # 09041
print("ett hål till ett trapprum.")  # 09043
call_method_12200()  # 09045
if X == 3:
    goto(15370)  # 09047
if X1 == 1:
    goto(9035)  # 09048
if X != 4:
    goto(9056)  # 09051
call_method(9260)  # 09053
goto([9047, 9300, 9035][X])  # 09055
call_method(11000)  # 09056
print("Du är i andra våningens hissrum.")  # 09058
goto(9045)  # 09060
Z = 23  # XXXX HISSRUM 3 XXX Z=23 XXX  # 09065
print("3:e våningens hissrum var visst toaletten.")  # 09066
print("Du spolas ut på golvet. Till vänster finns")  # 09067
print("en dörr men du kan också spola ner dej.")  # 09068
call_method_12200()  # 09069
if FNL_(A_, 3) == "SPO":
    goto(9075)  # 09070
if X1 == 1:
    print("Som sagt, ")
    goto(9065)  # 09071
if X == 3:
    goto(8300)  # 09072
call_method(11000)  # 09073
print("Du är i toaletten.")
goto(9069)  # 09074
print("Du befinner dej")  # 09075
goto(9450)  # 09076
call_method(11000)  # 09099
Z = 27
R_ = "sjunde"  # XXXX HISSRUM 7 XXX Z=27 XXX  # 09100
call_method(9250)  # 09102
call_method_12200()  # 09103
if X == 4:
    goto(1919)  # 09104
if X != 3:
    goto(9099)  # 09105
call_method(9260)  # 09106
goto([9104, 9300, 9100][X])  # 09107
call_method(11000)  # 09144
Z = 24
R_ = "fjärde"  # XXXX HISSRUM 4 XXX Z=24 XXX  # 09145
call_method(9250)  # 09146
print("Bakom dej anar man en öppning.")  # 09147
call_method_12200()  # 09148
if X == 4:
    goto(15432)  # 09150
if X == 6:
    goto(15300)  # 09152
if X != 3:
    goto(9144)  # 09154
call_method(9260)  # 09156
goto([9150, 9300, 9145][X])  # 09158
call_method(11000)  # 09174
Z = 26
R_ = "sjätte"  # XXXX HISSRUM 6 XXX Z=26 XXX  # 09175
call_method(9250)  # 09177
call_method_12200()  # 09179
if X == 4:
    goto(8381)  # 09181
if X != 3:
    goto(9174)  # 09183
call_method(9260)  # 09185
goto([9181, 9300, 9175][X])  # 09187
call_method(11000)  # 09189
Z = 29
R_ = "nionde"  # XXXX HISSRUM 9 XXX Z=29 XXX  # 09190
call_method(9250)  # 09192
call_method_12200()  # 09194
if X == 4:
    goto(35000)  # 09196
if X != 3:
    goto(9189)  # 09198
call_method(9260)  # 09200
goto([9196, 9300, 9190][X])  # 09202
A = A * -1  # 09210
print(S[39])  # 09211
X = S[39]  # 09212
for I in range(1, A):  # 09213
    S = time.sleep(2)  # 09214
    if S:
        goto(9222)  # 09215
    X = X - 1  # 09216
    print("   " + X)  # 09217
print(CHR_(7))  # 09220
goto(9359)  # 09221
C_ = input("")  # 09222
if FNL_(C_, 1) != "N" and FNL_(C_, 1) != "n":
    goto(9216)  # 09223
S[40] = X  # 09224
print("Hissen stannar och du kastas ur!")  # 09225
goto(9360)  # 09226
X = S[39]  # 09228
print(S[39])  # 09229
for I in range(1, A):  # 09230
    S = time.sleep(2)  # 09231
    if S:
        goto(9238)  # 09232
    X = X + 1  # 09233
    print("   " + X)  # 09234
goto(9220)  # 09237
C_ = input("")  # 09238
if FNL_(C_, 1) != "N" and FNL_(C_, 1) != "n":
    goto(9233)  # 09239
goto(9224)  # 09240
print("Du är i " + R_ + " våningens hissrum. Till vänster finns en")  # 09250
if S[40] == Z - 20:
    print("öppen")
else:
    print("stängd")  # 09252
print(" hissdörr och till höger en annan dörr.")  # 09254
# ? return  # 09256
X %= 2
S[39] = Z - 20  # 09260
if S[40] == S[39]:
    S[40] = 0
goto(9280)  # 09261
print("Du står framför en stängd hissdörr. På en knapp bredvid")  # 09262
print("dörren står det HIT.")  # 09263
call_method_12200()  # 09264
if X1 == 1:
    goto(9262)  # 09265
if FNL_(A_, 3) != "TRY" and A_ != "HIT":
    X %= 1
goto(9280)  # 09266
if S[40] == 10:
    print("Hissen kommer inte. Den måste vara trasig!")
X %= 3
goto(9280)  # 09268
I1 = 1  # 09269
I = INSTR(I1, A_, " ")  # 09270
if I < 1 or I >= len(A_):
    goto(9276)  # 09271
D = ASCII(MID_(A_, I + 1, 1))  # 09272
if D > 47 and D < 58:
    S[40] = D - 48
goto(9278)  # 09273
I1 = I + 1  # 09274
if I1 < len(A_):
    goto(9270)  # 09275
S[40] = -1  # 09276
W_ = "TRYCK 0"  # 09277
print("Hissen kommer och du stiger in.")  # 09278
# ? return  # 09280
Z = 18
S[22] = S[22] + 1  # XXX HISSEN XXX  # 09300
if S[40] > 0:
    goto(9335)
else:
    S = time.sleep(2)  # 09301
if S[22] / 2 == int(S[22] / 2):
    print("Du är i hissen.")
goto(9307)  # 09304
print("Du är i hissen. Här finns tio knappar. Dom nio första är numrerade")  # 09305
print("1-9. På den sista står det NÖDSTOPP.")  # 09306
call_method_6000()  # 09307
print("Vilken knapp trycker du på ? ")  # 09308
E = random.randint(0, 9) + 1
E1 = random.randint(0, 5) + 5  # 09309
if S[40] == 0:  # ? or M3%==1%:
    goto(9315)
else:
    if time.sleep(8 + E1):
        goto(9315)  # 09310
print("Dörrarna går igen och hissen startar.")  # 09311
# ? if M2%==1%:
# ?     print()#2,W_
W_ = STR_(E)  # &&&&&  # 09312
S[40] = E
print("Hissen går till" + S[40] + "an.")  # 09313
goto(9356)  # 09314
A_ = FNI_("")
print()  # 09315
if ASCII(A_) > 48 and ASCII(A_) < 58:
    S[40] = VAL(FNL_(A_, 1))
goto(9335)  # 09316
if FNL_(A_, 1) != "N" and FNL_(A_, 1) != "n":
    call_method_12000()
goto(9330)  # 09318
print("Skrik inte på hjälp innan det hemska börjar!")  # 09322
goto(9308)  # 09323
if ASCII(A_) > 48 and ASCII(A_) < 58:
    goto(9316)  # 09330
if X1 == 1:
    goto(9300)  # 09331
call_method(11000)
goto(9305)  # 09332
if S[41] != 1:
    goto(9355)  # 09335
print(FNS_("åker hiss", 5))  # 09337
print("Hissen faller    !!")  # 09338
print("Hissen krossas mot hisschaktets botten.")  # 09339
S[40] = 10
goto(9461)  # 09340
print("Hissen startar.")
S = time.sleep(4)  # 09355
A = S[40] - S[39]  # 09356
if A == 0:
    goto(9360)  # 09357
if A < 0:
    goto(9210)
else:
    goto(9228)  # 09358
print("Hissen är framme. Du går ur...")
if random.random() < 0.1:
    S[41] = 1  # 09359
goto([9000, 9035, 9065, 9145, 9075, 9175, 9100, 9020, 9190][S[40]])  # 09360
Z = 49  # XXX ÖSTRA STRANDEN XXX Z=49 XXXXX  # 09361
print("Du är på östra stranden. Åt norr är det skog.")  # 09362
if S[35] == 0:
    print("Här ligger en roddbåt.")  # 09364
call_method_15200()  # 09366
if S[35] == 0 and (INSTR(A_, "BÅT") > 0 or A_ == "RO"):
    goto(9390)  # 09368
if X != 0:
    goto([20000, 9424, 20070, 9374, 20200, 9374, 9372, 9374, 20085, 2107][X])  # 09370
call_method(11000)
goto(9361)  # 09372
print("Du kan väl inte gå på vattnet?")
goto(9361)  # 09374
Z = 78  # XXXX I BÅTEN XXXXX Z=78 XXXXX  # 09390
print("Du sitter i båten, mitt i sjön.")  # 09391
call_method_15200()
S[35] = random.randint(0, 2)  # 09392
if X == 1:
    goto(9410)  # 09393
if X == 2:
    goto(9416)  # 09394
if X == 3:
    S[35] = 0
goto(9361)  # 09395
if X == 4:
    S[35] = 1
goto(2200)  # 09396
if X == 10:
    goto(2107)  # 09397
call_method(11000)  # 09399
print("Skriv söder, norr, öster eller väster.")  # 09400
goto(9392)  # 09401
print("Oj, en motorbåt åkte för nära dej.")  # 09410
print("Din båt går runt och Du svimmar!")  # 09411
print()  # 09412
print("När Du vaknar är Du")  # 09414
goto(9450)  # 09415
print("Du ror och ror...")  # 09416
print("Plötsligt åker Du in i en vattenvirvel som suger ner ")  # 09417
print("både Dej och båten.")  # 09418
D = time.sleep(3)
if D:
    A_ = input("")  # 09419
print()  # 09420
print("Du flyter upp och ser att")  # 09421
Z = 4
call_method(7500)  # 09422
goto(2066)  # 09423
print("Du är på en stenig sjöstrand.")  # 09424
print("Det finns en liten badhytt här.")
Z = 88  # 09425
print("Ett staket hindrar dej att gå åt NORDOST,ÖSTER eller SYDOST.")  # 09426
call_method_15200()  # 09428
if X1 == 1:
    goto(9424)  # 09429
if X == 0:
    goto(9436)  # 09430
goto([9361, 9426, 20085, 20330, 20070, 9432, 9437, 9426, 9426, 2107][X])  # 09431
print("Kan du gå på vattnet?")  # 09432
goto(9424)  # 09433
if INSTR(A_, "BADHYTT") > 0 or FNL_(A_, 5) == "ÖPPNA" or A_ == "IN":
    goto(9439)  # 09436
call_method(11000)  # 09437
goto(9424)  # 09438
print("Du går in i badhytten men golvet ger vika och du faller...")  # 09439
goto(25000)  # 09440
print(" under bryggan.")  # 09450
print("Du ser ett hål rakt fram, men kan inte komma dit.")  # 09451
if A[1] != 1:
    goto(9455)  # 09452
A[1] = 0
S[1] = S[1] - 1  # 09453
print("OJ! Du tappar diamanten. Den ligger på botten.")  # 09454
if S[2] < 10:
    goto(9459)  # 09455
A_ = FNI_("Vill du vara kvar här ?")  # 09456
if FNL_(A_, 1) == "N" or FNL_(A_, 1) == "n":
    goto(20005)  # 09457
print()  # 09459
print("Din luft är slut och du kvävs. Ditt lik flyter upp.")  # 09460
A_ = FNI_("Vill du att jag ska återuppliva dej ?")  # 09461
S[46] = S[46] + 1  # 09462
if FNL_(A_, 1) == "N" or FNL_(A_, 1) == "n":
    goto(9484)  # 09464
if FNL_(A_, 1) == "J" or FNL_(A_, 1) == "j":
    goto(9470)  # 09467
print("JA eller NEJ! Min chans att lyckas minskar...    ")  # 09468
S[46] = S[46] + 1
goto(9461)  # 09469
print("OK, men skyll inte på mej om något går fe...")  # 09470
if S[46] == 1:
    goto(9479)  # 09471
if S[46] == 6:
    goto(9483)  # 09472
D = random.randint(0, 0) + 1  # 09473
if D > 3:
    goto(9479)  # 09474
print("POFF!!! Ett grönt gasmoln omger dej!")  # 09475
print("OJOJOJ, det gick inte. Du är fortfarande stendöd! Jag")  # 09476
print("lovar att du ska få en värdig begravning!!")  # 09477
goto(99000)  # 09478
print("POFF!!!     Ett grönt gasmoln omger dej!!")  # 09479
print("Du lever!      När gasen skingrats ser Du att ")  # 09480
S[2] = S[2] - 5  # 09482
goto(36050)  # 09483
print("VA? Litar du inte på mig? Senast igår återuppväckte jag")  # 09484
print("en DEC-2020 och den fungerade i flera minuter...")  # 09485
print()  # 09486
print("Men jag ska inte bråka. Du får som du vill.")  # 09487
goto(99000)  # 09488
Z = 54  # XXXXX VIGGOS HEMLIGA RUM 1 XXXXX  # 09490
print("Du är i ett dunkelt, dammtäckt rum.")  # 09491
print("Dörrar går bakåt, åt höger och framåt.")  # 09492
if S[47] > 0:
    print("Det finns ett hål till vänster.")
goto(9496)  # 09493
print("Bakom ett draperi till vänster kan man ana ett hål.")  # 09494
call_method_12200()  # 09496
if X1 == 1:
    goto(9490)  # 09497
if X > 0:
    goto([9501, 9501, 9510, 9558, 9545, 14000, 9501][X])  # 09500
call_method(11000)  # 09501
print("Du är i ett dunkelt, dammtäckt rum.")
goto(9496)  # 09502
Z = 55  # XXXXX VIGGOS HEMLIGA RUM 2 XXXXX  # 09510
if S[47] > 0:
    print("Det finns ett hål i väggen.")
else:
    print("Du är vid draperiet.")  # 09511
call_method_12200()  # 09512
if X == 5:
    goto(9525)  # 09515
if X == 6:
    goto(9492)  # 09516
if FNL_(A_, 5) == "KLIPP" and S[47] == 0:
    goto(9520)  # 09517
if (FNL_(A_, 5) == "ÖPPNA" or FNL_(A_, 3) == "DRA") and S[47] == 0:
    goto(9523)  # 09518
call_method(11000)
goto(9510)  # 09519
if A[27] == 1:
    goto(9535)  # 09520
print("Du har inget att klippa med!")  # 09521
goto(9510)  # 09522
print("Du är för svag för att kunna rubba draperiet.")  # 09523
goto(9510)  # 09524
if S[47] == 1:
    goto(8148)  # 09525
print("Draperiet är i vägen.")  # 09526
goto(9510)  # 09527
Z = 60  # XXXXX MUPPET SHOW DEL 2 XXXXX  # 09528
print("Kermit vill ge dej ett kontrakt, men då måste du släppa")  # 09529
print("något först. (Tänk på att du inte kommer hit igen!!)")  # 09530
A_ = FNI_("Svara SLÄPP <det du vill släppa> eller DÅLIGT:")  # 09531
if FNC_(FNL_(A_, 5)) == "SLÄPP":
    call_method_12000()  # 09532
if S < 9:
    goto(8913)  # 09533
print("Ok.")
print("Du går genom en dörröppning.")
goto(8950)  # 09534
S[47] = 1
S[2] = S[2] + 20  # 09535
print("Du klipper sönder draperiet. Draperiet försvinner.")  # 09536
goto(9510)  # 09537
Z = 56  # XXXXX VIGGOS HEMLIGA RUM 3 XXXXX  # 09545
print("Du är i en återvändsgränd.")  # 09546
if A[28] == 2:
    print("Det ligger en låst låda här som du inte orkar bära.")  # 09547
call_method_12200()  # 09548
if X == 6:
    goto(9490)  # 09550
if FNL_(A_, 3) == "LÅS":
    goto(9553)  # 09551
call_method(11000)
goto(9545)  # 09552
if A[26] != 1 or A[28] != 2:
    print("Det kan du inte.")
goto(9545)  # 09553
print("Du låser upp lådan och hittar en slägga. Lådan försvinner.")  # 09554
A[28] = 56
goto(9545)  # 09555
call_method(11000)  # 09556
print("Du är i höger kammare.")
goto(9562)  # 09557
Z = 57  # XXXXX VIGGOS HEMLIGA RUM 4 XXXXX  # 09558
print("Du är i höger kammare. En väg går framåt, men på ett")  # 09559
print("anslag står det: DU SOM VÅGAR DEJ IN HÄR FÅR ")  # 09560
print("ANTINGEN EN BELÖNING ELLER OCKSÅ ... DÖDEN")  # 09561
if A[27] == 2:
    print("Fastskruvad i väggen sitter en glasask med en sax i.")  # 09562
call_method_12200()  # 09563
if FNL_(A_, 3) == "SLÅ" or FNL_(A_, 5) == "KROSS":
    goto(9568)  # 09564
if X == 0 or X > 6:
    goto(9556)  # 09565
goto([9556, 9556, 9556, 9556, 9575, 9490][X])  # 09566
if A[27] != 2:
    goto(9556)  # 09568
if A[28] != 1:
    print("Du har inget att slå med.")
    goto(9558)  # 09569
print("Du krossar glaset. Saxen ramlar ur och asken försvinner i ett moln.")  # 09570
A[27] = 57
goto(9557)  # 09571
D = random.randint(0, 0)  # 09575
if D < 4:
    print("Gången mynnar ut i ett hus.")
goto(2241)  # 09576
print("Du trampar på en sprängladdning och sprängs i luften!")  # 09577
goto(9461)  # 09578
# ?if M2%==1%:
# ?     CLOSE 2
# ?M2%=0% #&&&&& Stäng ev. loggfil  # 09950
print("Är du säker på att du vill sluta nu?")  # 09951
A_ = FNI_("")
A_ = FNC_(A_)  # 09952
if FNL_(A_, 1) == "J":
    goto(99000)  # 09953
print("Ok. Du har" + S[2] + "poäng!")  # 09957
goto(12210)  # 09958
Z = 8
S[8] = S[8] + 1  # XXXXX HALlen XXXXX  # 09991
if S[8] == 1:
    S[2] = S[2] + 5  # 09993
if S[8] < 3 or S[8] > 7:
    goto(10009)
else:
    goto(10000)  # 09995
call_method(11000)  # 09997
print("Du är i hallen.")  # 10000
call_method_12200()  # 10001
if S1 > 0:
    goto(10001)  # 10002
if X1 == 1:
    goto(10009)  # 10003
if X == 19:
    call_method(12202)
goto(10003)  # 10004
if X > 2 and X < 7:
    goto([15350, 1500, 15425, 10015][X - 2])  # 10006
goto(9997)  # 10008
print("Du är i en hall med tre dörrar. På den vänstra finns en nedåtriktad")  # 10009
print("pil, på dörren rakt fram finns en pil som pekar uppåt och på dörren")  # 10010
print("till höger står det atelje. Bakom dej ligger porten ut ur huset.")  # 10011
if S[19] == 1:
    print("Ytterporten är öppen.")  # 10012
if S[8] > 7:
    S[8] = 3  # 10013
goto(10001)  # 10014
if S[19] == 1:
    print("Porten stängs bakom dej.")
S[19] = 0
goto(20200)  # 10015
print("Porten är stängd!")  # 10016
goto(10000)  # 10017
Z = 16  # XXXXX SKUMGUMMIRUMMET XXXXX  # 10020
print("Du är i Skumgummirummet.")  # 10022
if A[15] == 0:
    print("Det finns ett mystiskt, mörkt fönster i väggen.")  # 10024
if A[15] == 0:
    print("Bakom fönstret anar man ett föremål.")  # 10025
print("Det finns dörrar framåt och åt vänster.")  # 10026
print("En gång går neråt.")  # 10028
call_method_12200()  # 10030
if X1 == 1:
    goto(10020)  # 10032
if X == 0:
    goto(10040)  # 10034
goto([10050, 25130, 25100, 10050, 21100, 25000, 10090][X])  # 10036
if A[15] > 0:
    goto(10050)  # 10040
if FNL_(A_, 5) == "KROSS" or FNL_(A_, 3) == "SLÅ":
    goto(10084)  # 10042
if FNL_(A_, 4) == "SKÄR":
    goto(10060)  # 10044
if FNL_(A_, 5) == "ÖPPNA":
    print("Du kan inte öppna fönstret.")
goto(10052)  # 10046
call_method(11000)  # 10050
print("Du är i Skumgummirummet.")  # 10052
goto(10030)  # 10054
if INSTR(A_, "DIAMA") > 0:
    goto(10072)  # 10060
if INSTR(A_, "TUNGA") > 0:
    goto(9075)  # 10062
A_ = FNI_("Vad ska du skära med? Din vassa tunga ?")  # 10064
A_ = FNC_(A_)  # 10065
if A_ == "JA" or FNL_(A_, 5) == "TUNGA":
    goto(9075)  # 10066
if A_ == "NEJ":
    print("Det var ju skönt!")
goto(10052)  # 10068
if FNL_(A_, 5) != "DIAMA":
    print("Det går inte!")
goto(10052)  # 10070
if A[1] != 1:
    print("Du bär väl ingen DIAMANT!")
goto(10052)  # 10072
print("Du skär upp fönstret med diamanten.")  # 10074
print("En kofot ramlar ut och slår dej hårt i huvudet.")  # 10076
print("Du rasar ihop av slaget." + FNS_("sover", 10))  # 10078
S[2] = S[2] + 10
print("När du vaknar är du fortfarande i Skumgummirummet.")  # 10079
A[15] = 16
goto(10030)  # 10080
if A[28] != 1:
    print("Du har inget att slå med.")
goto(10052)  # 10084
print("Du krossar fönstret med släggan. Därbakom finns en kofot.")  # 10086
print("Thorvald springer fram och säjer: - Jag hörde braket! Nu tar jag")  # 10087
print("kofoten som betalning för det förstörda fönstret.")  # 10088
print("Han tar kofoten och försvinner.")
A[15] = 5
goto(10020)  # 10089
if A[15] > 0:
    goto(10050)  # 10090
if A[1] != 1:
    print("Försök att hitta något du kan skära upp fönstret med.")  # 10092
if A[1] == 1:
    print("Skär upp fönstret med din diamant!")  # 10094
S[2] = S[2] - 5
goto(10052)  # 10096
# VIOLS SUBFELMEDDELANDERUTIN 3  # 11000
if X1 > 0 or S1 > 0:  # 11001
    goto(11100)
else:
    S[50] = S[50] - 1
if INSTR(A_, "HJÄLP") > 0:  # 11002
    print("Du kan inte få någon hjälp här.")
    goto(11100)
if A_ == "N" or A_ == "V":  # 11003
    print("Du kan inte gå ditåt.")
    goto(11100)
if INSTR("*NORR*SÖDER*VÄSTER*ÖSTER*NV*NÖ*NO*SV*SÖ*SO", "*" + A_) > 0:
    goto(11200)  # 11004
if INSTR("*NORDVÄST*NORDÖST*NORDOST*SYDVÄST*SYDÖST*SYDOST", "*" + A_) > 0:
    goto(11200)  # 11005
if INSTR("*UPPÅT*NEDÅT*NERÅT*VÄNSTER*HÖGER*FRAMÅT*BAKÅT", "*" + A_) > 0:
    goto(11220)  # 11006
if INSTR(A_, "SESAM") == 0 and INSTR(A_, "KORKSKRUV") == 0:
    goto(11011)  # 11007
print("Ingenting händer.")  # 11008
goto(11100)  # 11009
if INSTR(A_, "STÄNG") > 0:
    print("Det finns inget du kan stänga här!")
goto(11100)  # 11011
if INSTR(A_, "KROSS") > 0:
    print("Det finns inget du kan krossa här!")
goto(11100)  # 11013
if INSTR(A_, "SKÄR") > 0:
    print("Det finns inget du kan skära här!")
    goto(11100)  # 11014
if A_ == "SE" or INSTR(A_, "TITTA") > 0:
    pass  # ? return  # 11015
if FNL_(A_, 5) == "HOPPA" and X == 1:
    print("Du kommer ingenstans uppåt.")
goto(11100)  # 11017
if FNL_(A_, 5) == "HOPPA":
    print("Det finns inget hål att hoppa ner genom.")
goto(11100)  # 11018
D = random.randint(0, 5) + 1  # 11080
if D == 1:
    print("Va ??")  # 11081
if D == 2:
    print("Jag förstår inte.")  # 11082
if D == 3:
    print("Det förstår jag inte alls.")  # 11083
if D == 4:
    print("Det vet jag inte vad det betyder.")  # 11084
if D == 5:
    print("Uttryck Dej klarare.")  # 11085
print()  # 11099
# ? return  # 11100
if S[36] == 0:
    print("Inomhus ska du ange riktningar, inte väderstreck.")  # 11200
if S[36] != 0:
    print("Du kan inte gå ditåt.")  # 11202
goto(11100)  # 11205
if S[36] == 1:
    print("Utomhus ska du ange väderstreck, inte riktningar.")  # 11220
if S[36] != 1:
    print("Du kan inte gå ditåt.")  # 11225
goto(11100)  # 11230


if ERROR:  # 90000
    goto(97000)  # XXXXX NU BÖRJAR VI XXXXX
W_[3] = TIME_
W_[4] = DATE_  # 90002
S[30] = 96  # 90003
S[32] = 1
S[33] = 1
S[40] = 1  # 90004
# ?MARGIN 80  # 90005
J[100] = 1
J[17] = 1
J[31] = 1  # 90050
J[43] = 1
J[58] = 1
J[78] = 1
J[97] = 1  # 90052
W_[1] = (
    "Stugrådet: Thorvald, Kimmo Eriksson, Olle Johansson, Viggo Eriksson, DEC-op, Thord Andersson"  # 90054
)
call_method(702)  # 90056
W_[5] = "004008009010011012013014015016017021022023024025031034035036038040"  # 90057
W_[5] = W_[5] + "043044046048052054056058059062069078080089093095096097100"  # 90058
S[37] = len(W_[5]) / 3  # 90059
S[45] = 1  # 90060
S[48] = -1
S[20] = -1  # 90062
# X=CRT(1)  # 90064
S[2] = 50  # 90066
if FNL_(DATE_, 6) == "01-APR":
    A1 = 1
else:
    A1 = 0  # 90068
print("Välkommen till VIOLs stuga!!!!!")  # 90070
print()  # 90072
A_ = input("Har du vågat dej in här förut? ")  # 90090
A_ = FNC_(A_)
print()  # 90091
if FNL_(A_, 1) == "J":
    goto(90200)  # 90094
if FNL_(A_, 1) == "N":
    goto(90100)  # 90096
print("JA eller NEJ!")
goto(90090)  # 90098
print("Då behövs lite hjälp och instruktioner!")  # 90100
call_method_91000()  # 90110
print("LYCKA TILL!")  # 90150
print()  # 90153
A[0] = 30  # 90200
S[0] = 53
S[24] = 6
J[0] = 100
for I in range(1, 12):  # 90202
    pass  # ? READ A_(I,1),A_(I,2),A_(I,3),A_(I,4),A[I]  # 90204
#? for I in range(15, A[0]):  # 90208
#?     pass  # ? READ A_(I,1),A_(I,2),A_(I,3),A_(I,4),A[I]  # 90210
goto(20000)  # 90214

if ERR != 27:
    goto(97004)  # 97000
if S2 == 0:
    S1 = 1
    goto(12999)  # 97001
X = 0
X1 = 0
if S1 < 2:
    S1 = 2
else:
    S1 = 1
S2 = 0  # 97002
goto(12999)  # 97003
print("? Fel på rad", ERL, ". Felkod:", ERR)  # 97004

# ? RESUME  # 97006
# %%%%% Raderna 97010 - 98034 behövs bara på Oden och Nadja  # 97010
#! 97010 - 98034 borttagna

def call_method_99000(skip_name=False):
    # XXX SLUT XXXX  # 99000
    #! 99001 - 99003 borttagna
    if skip_name:
        if W_[6] == "":  # 99004
            W_[6] = FNI_("Vad heter du ?")  # %%%%% Kan tas bort
        print(f"Du fick {S[2]} poäng!")  # 99090
    if S[2] < 50:
        I = 50
        print("Du kan klassas som en klantig nybörjare.")
    elif S[2] < 55:
        I = 55
        print("Du är en ren amatör inom stugforskningen.")
    elif S[2] < 65:
        I = 65
        print("Du är en duktig nybörjare inom stugforskningen.")
    elif S[2] < 90:
        I = 90
        print("Du är en erfaren stugforskare.")
    elif S[2] < 120:
        I = 120
        print("Du kan kalla dej en stugfogde.")
    elif S[2] < 150:
        I = 150
        print("Du är en erfaren stugfogde.")
    elif S[2] < 200:
        I = 200
        print("Du är en väldigt erfaren stugfogde.")
    elif S[2] < 250:
        I = 250
        print("Du är biträdande expert på hus i Småland.")
    elif S[2] < 300:
        I = 300
        print("Du är expert på hus i Småland.")
        #! här fanns en bugg
    elif S[2] < 335:
        I = 335
        print("Du är föreslagen som medlem i stugrådet.")
    else:
        I = S[2]  #! eget påhitt
        print("    GRATTIS !!")  # 99160
        print("Du är nu invald i stugrådet.")  # 99170

    if I - S[2] > 0:
        print(f"För att komma upp i nästa klass behöver Du {I - S[2]} poäng till.")  # 99200

    # Eventuell loggning av resultat, 99302 - 99500 kan tas bort  # 99300
    #! 99300 - 99500 borttagna
    print("\nThorvald hälsar:   - Välkommen tillbaka!\n")  # 99990 # 99996
    #            NU ÄR PROGRAMMET NÄSTAN SLUT            KKKKKOLOLOLOLLKHH  # 99998
    # END  # 99999
