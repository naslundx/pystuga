00001	'Version: 4O(114)-4     821227/VE
00002	DIM S(55),W$(7),J(100),A(31),A$(31,4),X(20)
00003	GOTO 90000
00005	'************************  S T U G A  *****************************
00010	'******* STUGA är skrivet av Viggo Eriksson, Kimmo Eriksson *******
00015	'******* och Olle Johansson. Adressen till programmakarna   *******
00020	'******* är Solängsvägen 170, 191 54 SOLLENTUNA.            *******
00025	'******* Denna fil är hemlig och får inte spridas ut utan   *******
00030	'******* författarnas tillstånd.                  810321    *******
00035	'******************************************************************
00050	'Rader märkta med $$$$$ är till för kompatibilitet med gamla versioner
00055	'Rader märkta med %%%%% får bara finnas med på Oden och Nadja
00060	'Rader märkta med &&&&& använder DEC-10-BASIC-filhantering
00700	REM ********************** THORVALD: ******************************
00701	IF RND<0.8 THEN 724
00702	PRINT "               IIIIIIIIIIIIIIII"
00703	PRINT "   _ _ _      II              II      _ _ _"
00704	PRINT "__I I I I_____I                I_____I I I I______"
00705	PRINT "  I I I I     I   I--I  I--I   I     I I I I"
00706	PRINT "  I_I_I_I     I   I  I  I  I   I     I_I_I_I"
00707	PRINT "              I   I  I  I  I   I    "
00708	PRINT "              I   I *I  I* I   I"
00709	PRINT "              I   I__I  I__I   I"
00710	PRINT "              II              II"
00711	PRINT "               II            II"
00712	PRINT "                II          II"
00713	PRINT "                 I__      __I"
00714	PRINT "                    I    I"
00715	PRINT "                    I    I"
00716	PRINT "                    I    I"
00717	PRINT "                    I    I"
00718	PRINT "                    II  II"
00719	PRINT "                     I__I"
00720	PRINT
00721	PRINT
00723	RETURN
00724	PRINT "                      I------I"
00725	PRINT "----------------------I *  * I----------------------------"
00726	PRINT "                      I      I"
00727	PRINT "                       --II--"
00728	PRINT "                         II"
00729	PRINT "                         --" \ RETURN
00730	REM******************OLLES SUBRUTIN****************************
00731	PRINT "Du kommer in i ett rum där det står en massa djur! På en"
00732	PRINT "skylt i luften står det"
00733	PRINT "    RUM UNDER BYGGNAD, SUPREMS BYGGNADS AB"
00734	PRINT "Plötsligt omges du av ett gult moln!"
00735	RETURN
01499	GOSUB 11000
01500	Z=53 \ S(25)=S(25)+1'XXXXX VIGGOS ATELJE XXXXX
01503	IF S(25)>2 AND S(25)<8 THEN PRINT "Du är i Ateljen." \ GOTO 1511
01504	PRINT "Du är i Ateljen. Här finns det tre dörrar."
01505	PRINT "Dom går åt vänster, åt höger och bakåt."
01506	PRINT "På väggen står det: ALEA JACTA EST"
01511	IF S(25)>8 THEN S(25)=4
01512	GOSUB 12200
01517	IF X1=1 THEN 1504
01518	IF X=0 THEN 1499
01520	ON X GOTO 1499,1499,15000,15050,1499,1540,1530
01530	IF A(10)=53 THEN 1538
01532	PRINT "TIPS!! Prova orden och gå tillbaka hit." \ S(2)=S(2)-10 \ GOTO 1500
01538	PRINT "TIPS!! Ta lagerkransen och skriv HJÄLP igen."
01539	S(2)=S(2)-10 \ GOTO 1500
01540	IF A(1)<>1 THEN 9991
01542	PRINT "Dörren har gått i baklås så du kommer inte ut åt det hållet!"
01544	IF A(26)=1 OR A(26)=Z THEN PRINT "Dina nycklar passar inte i nyckelhålet."
01548	GOTO 1500
01908	GOSUB 11000
01909	PRINT "Du är i en stor svängande labyrint."
01910	Z=34
01911	GOSUB 12200
01913	IF X=0 OR X>6 THEN 1908
01914	ON X GOTO 1970,1919,1939,8095,1950,1929
01918	GOSUB 11000
01919	PRINT "Du är i en svängig stor labyrint."
01921	Z=92 \ GOSUB 12200'XX KIVIS LABYRINTRUM 3 XXXX Z=92 XXX
01922	IF X=0 OR X>6 THEN 1918
01923	ON X GOTO 1929,1944,1960,1950,1909,8300
01928	GOSUB 11000
01929	PRINT "Du är i en svängande stor labyrint."
01931	Z=89 \ GOSUB 12200'XX KIVIS LABYRINTRUM 2 XXXX Z=89 XXX
01932	IF X=0 OR X>6 THEN 1928
01933	ON X GOTO 1960,1950,1939,1909,1970,1919
01939	ON (INT(RND*2)+1) GOTO 16500,15432
01944	PRINT "Du är i en återvändsgång. Här står Kimmo och säjer:"
01945	PRINT " - Det här är återvändsgången i denna labyrint."
01946	PRINT "   här gömmer piraten sina skatter. Jag är piraten!"
01947	PRINT "               HAR HAR HAR"
01948	IF G=1 THEN PRINT "Han håller din halvruttna tomat i handen."
01950	PRINT "Du är i en stor svängig labyrint."
01952	Z=93 \ GOSUB 12200'XX KIVIS LABYRINTRUM 4 XXXX Z=93 XXX
01953	IF X=0 OR X>6 THEN 1956
01954	ON X GOTO 8000,1929,1960,1970,1944,1919
01956	GOSUB 11000 \ GOTO 1950
01959	GOSUB 11000
01960	PRINT "Du är i en stor labyrint som också är svängig."
01962	Z=94 \ GOSUB 12200'XX KIVIS LABYRINTRUM 5 XXXX Z=94 XXX
01963	IF X=0 OR X>6 THEN 1959
01964	ON X GOTO 1919,8035,1970,1980,1929,1950
01969	GOSUB 11000
01970	PRINT "Du är i en svängig labyrint som också är stor."
01972	Z=95 \ GOSUB 12200'XX KIVIS LABYRINTRUM 6 XXXX Z=95 XXX
01973	IF X=0 OR X>6 THEN 1969
01974	ON X GOTO 1960,1980,8071,1950,1909,1929
01980	IF G=1 THEN 1970 ELSE PRINT "Du har en halvrutten tomat i handen."
01981	PRINT "HAR HAR HAR! ropar en pirat som springer mot dej."
01982	PRINT "Piraten tar din tomat."
01983	G=1 \ GOTO 1970
02008	PRINT "Du är i Högra pannrummet."
02009	S(42)=S(42)+1
02010	IF S(42)>1 THEN PRINT "Ett hål finns i väggen." \ GOTO 2012
02011	PRINT "En panna sprängs och gör ett hål i väggen."
02012	A$=FNI$("Vill du gå in i hålet ?")
02014	IF FNL$(A$,1)="J" OR FNL$(A$,1)="j" THEN 2019
02015	PRINT "Ok."
02016	GOTO 14100
02018	GOSUB 11000
02019	Z=69 'XXXX GROTTRUM 1 XXXXX Z=69 XXX
02020	PRINT "Du är i en grotta som sträcker sej utom synhåll åt vänster och höger."
02021	IF S(42)>0 THEN PRINT "Bakom dej finns ett uppsprängt hål."
02023	GOSUB 20500
02024	IF X<3 THEN 2018 ELSE ON X-2 GOTO 2044,2032,2018,2025,2018
02025	IF S(42)>0 THEN 14100 ELSE 2018
02032	PRINT "Du gick just genom ett vattenfall."
02033	Z=91'XXXXX GROTTRUM 6 XXX Z=91 XXX
02034	PRINT "Du är vid ett vattenfall i en skog."
02035	GOSUB 20500
02036	IF X=0 OR X>6 THEN 2038
02037	ON X GOTO 2019,2066,2115,2150,2066,2019
02038	GOSUB 11000
02039	GOTO 2034
02043	GOSUB 11000
02044	Z=19'XXXX GROTTRUM 2 XXX Z=19 XXX
02045	IF A(12)<>0 THEN 2051
02046	PRINT "En liten faun springer fram och tänker trampa dej på foten"
02047	PRINT "men han tappar en sko och springer ylande därifrån."
02049	A(12)=19
02051	PRINT "Du är i Schweiziska klockrummet."
02052	GOSUB 20500
02054	IF X=0 THEN 2043
02056	ON X GOTO 2043,2043,2075,2150,2145,2019,2043
02065	GOSUB 11000
02066	Z=33'XXXXX GROTTRUM 3 XXXXX
02067	PRINT "Du är på stranden till en underjordisk sjö."
02068	GOSUB 20500
02071	IF X=10 THEN 2107
02073	IF X<>0 THEN ON X GOTO 2101,2104,2075,20270,2107,2033,2065 ELSE 2065
02074	GOSUB 11000
02075	Z=25 'XXX GROTTRUM 5 XXX Z=25 XXX
02076	PRINT "Du är på stranden till en underjordisk sjö bredvid en enorm spelautomat."
02077	PRINT "På den står det: 'DRA I SPAKEN OM DU HAR EN FAUNSKO ATT SATSA'"
02078	GOSUB 20500
02079	IF FNL$(A$,3)<>"DRA" THEN 2089
02080	IF A(12)=1 THEN 2083
02081	PRINT "FUSKARE! Du har ingen faunsko!"
02082	GOTO 2087
02083	D=INT(RND*10)+1
02084	IF D>7 THEN 2094
02085	PRINT "Grattis	! Du vann en massa guldmynt."
02086	A(12)=2 \ A(7)=25 \ S(1)=S(1)-1
02087	PRINT "Du är vid slutet av stranden."
02088	GOSUB 20500
02089	IF X>0 AND X<7 THEN ON X GOTO 2074,2074,20255,2066,2107,2044
02090	IF X=10 THEN 2107 ELSE 2074
02094	PRINT "Tyvärr,du förlorade!"
02095	S(1)=S(1)-1 \ A(12)=0
02096	GOTO 2087
02101	PRINT "Du fastnade i en jättesugkopp och kan inte komma loss.";FNS$("sover",15)
02102	PRINT "Hoppsan, nu svalt du ihjäl."
02103	GOTO 9461
02104	PRINT "Du sjunker...S J U N K E R!!"
02105	PRINT "Du är";
02106	GOTO 9450
02107	PRINT "Vattnet är lugnt, du simmar fort."\PRINT SPACE$(40)
02108	GOTO 2138
02109	PRINT "Järndörrar slår ner omkring dej. Du kan bara gå uppåt."
02111	A$=FNI$("") \ A$=FNC$(A$)
02112	IF FNL$(A$,3)="UPP" OR A$="U" THEN 2135
02113	PRINT "Så kan du väl inte gå!"
02114	GOTO 2111
02115	Z=20 'XXX GROTTRUM 4 XXX Z=20 XXX
02116	PRINT "Du är fortfarande i skogen men åt ett håll skymtar"
02117	PRINT "man en stuga."
02118	GOSUB 20500
02119	IF X<>0 THEN ON X GOTO 2120,2120,20155,2120,2127,2033,2120
02120	GOSUB 11000
02121	GOTO 2115
02123	PRINT "Du hoppar ner i brunnen och ramlar tillslut ner på marken."
02124	GOTO 14000
02126	GOSUB 11000
02127	Z=99 'XXXXX GROTTRUM 7 XXXX Z=99 XXXX
02128	PRINT "Du står utanför stugan vid en brunn."
02129	GOSUB 20500
02133	IF X=0 OR X>6 THEN 2126
02134	ON X GOTO 2126,2123,2126,2126,35000,2115
02135	PRINT "Du har kommit upp ur en brunn. Här finns en stuga."
02136	Z=99 \ GOTO 2129
02138	D=INT(RND*4)+1
02139	IF D=2 THEN 2109
02140	IF D>2 THEN 36000 ELSE PRINT "Du dras ner. Nu är du";
02143	GOTO 9450
02145	D=INT(RND*5)+1
02146	IF D<4 THEN 2115
02147	PRINT "En hord fauner kommer framrusande. Nnnnnu är du en våt fläck."
02148	GOTO 9461
02149	GOSUB 11000
02150	Z=98'XXX GROTTRUM 8 XXXX Z=98 XXXXX
02151	PRINT "Du har en halvrutten tomat i handen men den försvinner."
02152	GOSUB 20500
02153	IF X=0 OR X>6 THEN 2149
02154	ON X GOTO 2157,36000,2180,2168,2161,2044
02157	IF S(31)<>0 OR A(18)<>1 THEN 2164
02158	S(31)=1
02159	PRINT "Du har blivit nervös och tar fram brännvinsflaskan och dricker ur den."
02160	GOTO 2150
02161	PRINT "Du har kommit till en sjö där du ser två båtar."
02162	PRINT "Du kliver i en men upptäcker att den bara var en synvilla."
02163	GOTO 2104
02164	IF S(32)<>0 THEN 2168
02165	D=INT(RND*5)+1
02166	IF A(19)=1 AND S(32)=0 THEN 2173
02167	S(46)=S(46)+1
02168	PRINT "Du står bakom ett draperi."
02169	GOTO 2150
02173	S(32)=1
02174	PRINT "Du råkar hälla ut vattnet på en faun som springer ylande iväg."
02175	GOTO 2150
02180	D=INT (RND*10)+1
02181	IF D>8 THEN 2183
02182	GOTO 14100
02183	PRINT "Plötsligt känner du en trasa framför näsan och du säckar ihop."
02184	PRINT "När Du vaknar märker Du att ";
02185	GOTO 2168
02199	GOSUB 11000
02200	Z=50'XXX SÖDRA STRANDEN XXXXX Z=50 XXXX
02201	PRINT "Du är på den södra sidan av sjön. Här finns ett hus."
02203	IF S(35)<>0 THEN 2207
02204	PRINT "Du hittar ett hål som du kryper ner i."
02205	GOTO 14000
02207	IF S(35)=1 THEN PRINT "Det ligger en roddbåt här."
02208	GOSUB 15200
02211	IF X=0 THEN 2220
02212	ON X GOTO 20255,20300,2216,2241,20180,2218,2199,2218,20270,2107
02215	GOTO 2200
02216	PRINT "Kan du gå på vattnet?"
02217	GOTO 2200
02218	PRINT "Ett staket hindrar dej från att gå ditåt."
02219	GOTO 2200
02220	IF INSTR(1,A$,"NER")>0 OR INSTR(1,A$,"NED")>0 OR A$="N" THEN 2204
02222	IF S(35)=1 AND (INSTR(1,A$,"BÅT")>0 OR A$="RO") THEN 9390
02224	GOTO 2199
02241	Z=51'XXX STRANDHUSET XXXXX Z=51 XXXX
02242	PRINT "Du är inne i huset. Här finns en automat med"
02243	PRINT "en skylt där det står:"
02244	PRINT "   SLÄPP SAKER HÄR, så får du poäng enligt prislistan."
02245	PRINT
02246	PRINT "          		PRISLISTA:"
02247	PRINT "		Om du släpper:          Så får du:"
02248	PRINT
02249	PRINT "		En tavla		 5 poäng"
02250	IF A(1)=1 THEN PRINT "		En diamant		15 poäng"
02251	IF A(3)=1 THEN PRINT " 		En silvertacka		10 poäng"
02252	IF A(2)=1 THEN PRINT "		En illaluktande gurka	 5 poäng"
02253	IF A(4)=1 THEN PRINT "		En hillebard		20 poäng"
02254	IF A(5)=1 THEN PRINT "		En dödskalle		20 poäng"
02255	IF A(6)=1 THEN PRINT "		En väckarklocka		15 poäng"
02256	IF A(7)=1 THEN PRINT "		Massor av guldmynt	10 poäng"
02257	IF A(8)=1 THEN PRINT "		En trilogi		10 poäng"
02258	IF A(9)=1 THEN PRINT "		Ett kontrakt		15 poäng"
02259	IF A(10)=1 THEN PRINT "		En lagerkrans		15 poäng"
02260	IF A(11)=1 THEN PRINT "		Ett pärlhalsband	25 poäng"
02261	IF A(12)=1 THEN PRINT "		En faunsko		 5 poäng"
02272	GOSUB 12200
02274	IF X=15 THEN 2290
02275	IF X=6 THEN 2201
02276	IF X1=1 THEN 2242 ELSE GOSUB 11000
02277	PRINT "Du är vid apparaten och kan bara gå bakåt."
02278	GOTO 2272
02290	A(I)=5 \ S(1)=S(1)-1
02292	S(2)=S(2)+5
02294	IF I<>2 AND I<>12 THEN S(2)=S(2)+5
02296	IF I=1 OR I=6 OR I=10 OR I=9 OR I=11 THEN S(2)=S(2)+5
02298	IF I=4 OR I=5 OR I=11 THEN S(2)=S(2)+10
02300	PRINT "Maskinen slukar ";A$(I,4);"."
02302	GOTO 2277
06000	REM ```` RUMSBESKRIVNING ```````````` TA ````````` SLÄPP ````````````
06002	IF S(2)=335 AND RND>0.5 THEN PRINT "Plötsligt kommer Thorvald fram och säjer:" \ GOTO 99160
06003	IF Z=70 AND A1=1 THEN PRINT "På marken ligger en enorm rubin."
06005	IF A(1)=Z THEN PRINT "Det finns en diamant här."
06006	IF A(15)=Z THEN PRINT "Det ligger en kofot här."
06007	IF A(16)=Z THEN PRINT "Det står en cykelpump här."
06008	IF A(2)=Z THEN PRINT "Det finns en illaluktande gurka här."
06009	IF A(3)=Z THEN PRINT "Det finns en silvertacka här."
06010	IF A(17)=Z AND Z<>11 THEN PRINT "Det står en stege här."
06011	IF A(18)<>Z THEN 6014
06012	IF S(31)=0 THEN PRINT "Det finns en fylld brännvinsflaska här."
06013	IF S(31)=1 THEN PRINT "Det finns en tom brännvinsflaska här."
06014	IF A(19)<>Z THEN 6017
06015	IF S(32)=0 THEN PRINT "Det finns en fylld vattenflaska här."
06016	IF S(32)=1 THEN PRINT "Det finns en tom vattenflaska här."
06017	IF A(20)<>Z THEN 6020
06018	IF S(33)=0 THEN PRINT "Det finns en pumpad boll här."
06019	IF S(33)=1 THEN PRINT "Det finns en opumpad boll här."
06020	IF A(4)=Z THEN PRINT "Det står en hillebard här."
06021	IF A(21)=Z THEN PRINT "Det står en spade här."
06022	IF A(5)=Z THEN PRINT "Det ligger en dödskalle här."
06023	IF A(6)=Z THEN PRINT "Det finns en väckarklocka här."
06024	IF A(23)=Z THEN PRINT "Det ligger en tunn telefonkatalog här."
06025	IF A(12)=Z THEN PRINT "Det ligger en faunsko här."
06026	IF A(7)=Z THEN PRINT "Det finns en massa guldmynt här."
06027	IF J(Z)=1 AND A(25)=Z THEN PRINT "En telefon är inkopplad i en jack i väggen."
06028	IF J(Z)=1 AND A(25)<>Z AND A(30)<>Z THEN PRINT "Det finns en telefonjack i väggen."
06029	IF J(Z)<>1 AND A(25)=Z AND S(44)<>Z THEN PRINT "Det finns en telefon här."
06030	IF A(26)=Z THEN PRINT "Det finns några nycklar här."
06031	IF A(27)=Z THEN PRINT "Det hänger en sax här."
06032	IF A(28)=Z THEN PRINT "Det hänger en slägga här."
06033	IF A(22)=Z THEN PRINT "Det ligger ett äckligt lik här."
06034	IF A(11)=Z THEN PRINT "Det finns ett glittrande pärlhalsband här."
06035	IF A(8)=Z THEN PRINT "Det ligger en trilogi här."
06036	IF A(24)=Z THEN PRINT "Det står en lampa här."
06037	IF A(9)=Z THEN PRINT "Det ligger ett kontrakt här."
06038	IF A(10)=Z THEN PRINT "Det hänger en lagerkrans här."
06039	IF S(30)=Z THEN 6200
06040	IF J(Z)=1 AND A(30)=Z THEN PRINT "En förlängningssladd är inkopplad i en jack i väggen."
06042	IF J(Z)<>1 AND A(30)=Z THEN PRINT "Det ligger en förlängningssladd här."
06043	IF J(Z)<>1 AND S(44)=Z AND A(25)=Z THEN PRINT "En telefon är inkopplad i en förlängningssladd."
06044	IF S(44)=Z AND (A(25)<>Z OR J(Z)=1) THEN PRINT "En förlängningssladd sticker in hit."
06048	IF S(44)=-1 AND Z<>A(30) THEN S(44)=Z \ PRINT "Förlängningssladden räcker precis hit."
06050	IF S(3)>0 THEN 29000
06060	IF INT(RND*20)<>1 OR S(50)<50 THEN 6069
06062	S(3)=S(3)+1 IF A(I)=1 FOR I=1 TO 14
06064	IF S(3)>0 THEN S(4)=INT(RND*6)+INT(S(3)/2+0.5)
06069	IF INT(RND*30)<>1 THEN 6100
06070	IF S(48)>0 THEN PRINT "En glasmästare springer förbi dej."\S(48)=0
06072	IF S(15)<>1 AND S(17)<>1 AND S(18)<>1 THEN 6076
06074	PRINT "En verkmästare från Stugas gatukontor lunkar förbi dej." \ S(15)=S(17)=S(18)=0
06076	IF S(41)=1 THEN PRINT "En hissreparatör går förbi dej."\S(41)=0\S(40)=INT(RND*9)+1
06098	IF S(50)-S(21)>25 AND S(21)>0 THEN 6130
06100	IF A(29)<>Z THEN 6120
06102	IF S(50)-S(51)>30 AND S(51)>0 THEN 6124
06104	IF S(6)=0 THEN PRINT "Här står en vakt."
06106	IF S(6)=1 THEN PRINT "En full vakt raglar omkring här."
06108	IF S(6)=2 THEN PRINT "Det finns blodfläckar på golvet." \ RETURN
06110	IF S(6)=3 THEN PRINT "En vakt sover här."
06112	IF A(15)=2 THEN PRINT "Han har din kofot."
06114	IF A(26)=2 THEN PRINT "Han har dina nycklar."
06116	IF A(25)=2 THEN PRINT "Han bär på en telefon."
06118	IF A(4)=2 THEN PRINT "Han bär på en juvelprydd hillebard."
06119	RETURN
06120	IF A(29)<>1 THEN RETURN
06122	IF S(50)-S(51)<31 AND S(51)>0 THEN PRINT "Du följs av en full vakt." \ GOTO 6112
06123	S(1)=S(1)-1
06124	PRINT "Vakten har nyktrat till nu."
06126	IF S(6)=3 THEN PRINT "Han vaknar och sträcker på sej."
06128	A(29)=Z \ S(6)=0 \ S(51)=0
06129	RETURN
06130	S(21)=0
06131	PRINT"Dina fötter är läkta nu."
06132	GOTO 6100
06200	IF A(19)>0 AND A(11)>0 THEN PRINT "Här sitter en gubbe." \ GOTO 6210
06202	PRINT "Här sitter en gubbe med ett pärlhalsband runt halsen."
06204	IF A(19)=0 THEN PRINT "I armarna har han en vattenflaska."
06206	IF A(19)=0 AND A(10)=0 THEN PRINT "På huvudet bär han din lagerkrans."
06208	IF A(19)=0 AND A(10)=1 THEN PRINT "Han stirrar på din lagerkrans."
06210	PRINT  \ GOTO 6040
06300	IF C$<>"" THEN 6305
06301	IF Z=37 AND S(38)=0 THEN X=13 \ GOTO 12999
06302	C$=FNI$("Ta vadå ?") \ A$=C$=FNC$(C$)
06305	FOR I=1 TO A(0)
06306	IF A$(I,1)<>"" THEN IF INSTR(1,C$,A$(I,2))>0 OR INSTR(1,C$,A$(I,3))>0 THEN 6400
06308	NEXT I
06309	IF FNL$(C$,4)="ALLT" THEN 6500
06310	IF FNL$(C$,5)="VATTE" THEN 6330
06311	IF FNL$(C$,5)="GRAVS" AND Z=61 THEN PRINT "Gravstenen väger alldeles för mycket."\GOTO 12210
06312	IF FNL$(C$,5)="KISTA" THEN 6350
06313	IF (FNL$(C$,5)="FAMIL" OR FNL$(C$,5)="VAPEN") AND Z=81 THEN PRINT "Vapnet sitter för hårt fast."\GOTO 12210
06314	IF FNL$(C$,5)="TAVLA" AND S(36)=0 THEN 6360
06315	IF FNL$(C$,5)="SAFTF" THEN PRINT "Jag ser ingen SAFTFLASKA här."\GOTO 12210
06316	IF FNL$(C$,5)="FLASK" THEN 6370
06317	IF FNL$(C$,4)="PORT" AND (Z=81 OR Z=62) THEN PRINT "Porten sitter fast i väggen."\GOTO 12210
06318	IF FNL$(C$,4)="JACK" AND J(Z)=1 THEN PRINT "Jacken sitter fastskruvad i väggen!"\GOTO 12210
06319	IF FNL$(C$,5)="BRUNN" AND Z=99 THEN PRINT "Brunnen är gjuten i marken!"\GOTO 12210
06320	IF FNL$(C$,5)="KASSA" AND Z=30 THEN PRINT "Det är fastgjutet i berget."\GOTO 12210
06321	IF FNL$(C$,3)="BÅT" AND (Z=49 OR Z=78 OR Z=50) THEN 6380
06322	IF FNL$(C$,5)="GUBBE" AND S(30)=Z THEN 30002
06323	IF FNL$(C$,4)="LÅDA" AND A(28)=2 AND Z=56 THEN PRINT "Lådan är för tung!"\GOTO 12210
06324	IF FNL$(C$,5)="RUBIN" AND A1=1 AND Z=70 THEN 6355
06325	IF FNL$(C$,3)="ASK" AND A(27)=2 AND Z=57 THEN PRINT "Asken sitter fast i väggen."\GOTO 12210
06326	IF FNL$(C$,5)="FÖNST" AND Z=16 AND A(15)=0 THEN PRINT "Fönstret är fastkittat i väggen."\GOTO 12210
06327	IF Z=37 AND S(38)=0 THEN X=13 \ GOTO 12999
06329	PRINT "Jag ser ingen ";C$;" här." \ GOTO 12210
06330	IF Z=25 OR Z=33 OR Z=49 OR Z=50 OR Z=66 OR Z=70 OR Z=91 THEN 6338
06332	IF Z=72 OR Z=74 OR Z=78 OR Z=79 OR Z=83 OR Z=87 OR Z=88 THEN 6338
06334	PRINT "Jag ser inget VATTEN här."
06336	GOTO 12210
06338	IF A(19)<>1 THEN PRINT "Du har inget att ta vattnet i." \ GOTO 12210
06340	IF S(32)=0 THEN PRINT "Din vattenflaska är redan full." \ GOTO 12210
06342	PRINT "Du fyller på vattenflaskan med vatten från ";
06344	IF Z=91 THEN PRINT "vattenfallet." ELSE PRINT "sjön."
06346	S(32)=0 \ GOTO 12210
06350	IF Z=15 THEN PRINT "Kistan väger 300 kilogram!" ELSE PRINT "Jag ser ingen KISTA här."
06352	GOTO 12210
06355	PRINT "Just när du ska ta rubinen kommer Thorvald fram och utropar"
06356	PRINT " - April, april! Nu tar jag hand om rubinen själv!"
06357	A1=0 \ GOTO 12210
06360	PRINT "Du kan väl inte sno en av husets tavlor!"
06362	S(2)=S(2)-1 \ GOTO 12210
06370	PRINT "Du måste skriva vilket slags flaska du menar, t ex TA SAFTFLASKA."
06372	GOTO 12210
06380	PRINT "Du orkar inte bära roddbåten."
06382	GOTO 12210
06400	IF (I=4 OR I=15 OR I=25 OR I=26) AND A(I)=2 THEN 28130
06402	IF (I=10 OR I=11 OR I=19) AND S(30)=Z AND A(I)=0 THEN 30020
06404	IF I=22 AND Z=63 THEN 28160
06406	IF I=29 AND S(6)<>1 THEN PRINT "Det kan du inte." \ GOTO 12210
06410	IF A(I)=Z OR (I=30 AND S(44)=Z) THEN 6420
06412	IF A(I)=1 THEN PRINT "Du bär redan ";A$(I,4);"." \ GOTO 12210
06414	IF A(I)=5 THEN PRINT "Man kan inte ta tillbaka saker från maskinen."\GOTO 12210
06418	PRINT "Jag ser ";FNA$(I);A$(I,1);" här." \ GOTO 12210
06420	IF S(1)=9 THEN PRINT "Du kan inte bära fler saker." \ GOTO 12210
06422	S(1)=S(1)+1 \ A(I)=1
06424	IF I=30 AND (J(Z)=1 OR S(44)=Z) THEN S(44)=0 \ PRINT "Du rycker loss sladden." \ GOTO 12210
06425	IF I=30 THEN S(44)=0
06426	IF I=25 AND (S(44)=Z OR J(Z)=1) THEN PRINT "Du kopplar ur telefonen." ELSE PRINT "Ok."
06428	GOTO 12210
06500	I=0'TA ALLT
06505	FOR I1=1 TO A(0)
06510	IF A(I1)<>Z AND (I1<>30 OR S(44)<>Z) THEN 6550
06512	IF I1=29 AND S(6)<>1 THEN 6550
06515	IF S(1)<9 THEN 6535
06520	IF I=0 THEN PRINT "Du kan inte bära fler saker."
06525	IF I>0 THEN PRINT "." \ PRINT "Du kan inte bära resten."
06530	GOTO 12210
06535	IF I=0 THEN PRINT "Du tar "; ELSE PRINT " och ";
06540	PRINT A$(I1,4); \ S(1)=S(1)+1 \ A(I1)=1 \ I=I+1
06545	IF I1=22 AND Z=63 THEN S(2)=S(2)-30 \ S(52)=0
06547	IF I1=30 THEN S(44)=0
06550	NEXT I1
06551	IF Z=70 AND A1=1 THEN PRINT \ GOTO 6355
06552	IF I=0 AND Z=37 AND S(38)=0 THEN PRINT "Jag ser inget du kan ta här." \ GOTO 6560
06555	IF I=0 THEN PRINT "Det finns inget som du kan ta här." ELSE PRINT "."
06560	GOTO 12210
07000	REM XXXXX SLÄPP XXXXX
07001	IF C$="" THEN C$=FNI$("Släpp vadå ?") \ A$=C$=FNC$(C$)
07003	FOR I=1 TO A(0)
07005	IF A$(I,1)<>"" THEN IF INSTR(1,C$,A$(I,2))>0 OR INSTR(1,C$,A$(I,3))>0 THEN 7030
07007	NEXT I
07008	IF FNL$(C$,4)="ALLT" THEN 7100
07009	IF C$="DEJ" OR C$="DIG" THEN 7020
07018	PRINT "Du bär väl ingen ";C$;"!" \ GOTO 12210
07020	PRINT "Fy! Det vill jag inte." \ S(2)=S(2)-1 \ GOTO 12210
07030	IF A(I)=1 THEN 7040
07034	PRINT "Du bär väl ";FNA$(I);A$(I,1);"!"
07036	GOTO 12210
07040	IF (I=10 OR I=19) AND S(30)=Z THEN 7090
07041	IF I=25 AND (S(44)=Z OR J(Z)=1) THEN 7075
07042	IF Z=51 AND I<15 THEN X=15 \ GOTO 12999
07043	IF Z=4 THEN PRINT "En mystisk kraft hindrar dej från att släppa någonting här." \ GOTO 12210
07044	IF I=22 AND Z=63 THEN S(52)=S(50) \ S(2)=S(2)+25
07045	IF I=30 AND J(Z)=1 THEN S(44)=-1 ELSE IF I=30 THEN S(44)=0
07050	A(I)=Z \ S(1)=S(1)-1
07052	IF I=22 AND Z=63 THEN PRINT "Du lägger försiktigt ner liket." ELSE PRINT "Ok."
07054	GOTO 12210
07075	S(28)=S(28)+1 \ S(1)=S(1)-1 \ A(25)=Z
07077	IF S(28)=2 THEN 27100
07078	IF S(28)/3<>INT(S(28)/3) OR RND<0.5 THEN PRINT "Du kopplar in telefonen."\GOTO 12210
07080	PRINT "Just som du ska koppla in telefonen kommer en man klädd i en röd"
07081	PRINT "dräkt som det står 'TELE' på, ";
07082	IF J(Z)=1 THEN PRINT "skruvar bort telefonjacken" \ J(Z)=0
07083	IF J(Z)<>1 THEN PRINT "tar bort förlängningssladden" \ S(44)=0 \ A(30)=0
07084	PRINT "och sluddrar fram:"
07085	PRINT "- Abonnemangsavgiften är inte betald." \ PRINT
07087	X1=1 \ GOSUB 27050
07088	GOTO 12999
07090	IF I=19 THEN PRINT "Gubben tar snabbt vattenflaskan när du släpper den." \ GOTO 7094
07092	PRINT "Gubben sätter din lagerkrans på sitt huvud och ser genast gladare ut."
07094	A(I)=0 \ S(1)=S(1)-1
07096	GOTO 12210
07100	I=0'SLÄPP ALLT
07102	IF Z=4 THEN 7043
07105	FOR I1=1 TO A(0)
07110	IF A(I1)<>1 THEN 7135
07115	IF I1=22 AND Z=63 THEN S(52)=S(50) \ S(2)=S(2)+25
07117	IF I1=30 AND J(Z)=1 THEN S(44)=-1 ELSE IF I1=30 THEN S(44)=0
07120	A(I1)=Z \ S(1)=S(1)-1
07125	IF I=0 THEN PRINT "Du släpper "; ELSE PRINT " och ";
07130	PRINT A$(I1,4); \ I=I+1
07135	NEXT I1
07140	IF I=0 THEN PRINT "Du bär inte på någonting!" ELSE PRINT "."
07145	GOTO 12210
07500	A(I)=Z IF A(I)=1 FOR I=1 TO A(0)'Släpper allt man bär i rummet
07502	S(1)=0
07504	RETURN
07556	Z=35'XXXXX HISSENS MASKINRUM XXX Z=35 XXX
07558	PRINT "Du är i hissens maskinrum. Det bullrar och låter."
07559	PRINT "Det finns en dörr bakom Dej."
07560	IF A(1)<>1 THEN PRINT "Det finns en lucka i golvet."
07562	GOSUB 12200
07564	IF X1=1 THEN 7556
07566	IF X=6 THEN 35000
07568	IF X=2 AND A(1)<>1 THEN 7570 ELSE GOSUB 11000 \ GOTO 7556
07569	GOSUB 11000
07570	PRINT "Du är i ett litet rum utan fönster."
07573	Z=32 \ GOSUB 12200
07579	IF X1=1 THEN 7588
07585	IF X=1 THEN 7556
07586	IF X=0 OR X=7 THEN 7569
07587	IF X=5 THEN 13000
07588	PRINT "Du kan gå framåt och uppåt."\GOTO 7570
07999	GOSUB 8290
08000	Z=43'XXXXX LABYRINTRUM 8 XXX Z=43 XXX
08001	PRINT "Du är i en gångande vindel."
08002	GOSUB 12200
08003	IF X=0 OR X>7 THEN 7999
08007	IF S(45)=1 THEN ON X GOTO 1929,8330,1944,8300,8420,8300,8011
08008	PRINT "Det hänger en tavla här."
08009	GOSUB 700
08010	ON X GOTO 8330,7999,8400,17000,8020,16000,8011
08011	GOTO 8017
08017	S(2)=S(2)-2
08018	PRINT "Gå inte åt höger eller neråt!" \ GOTO 8000
08019	GOSUB 8290
08020	Z=44'XXXXX LEBYRINTRUM 9 XXX Z=44 XXX
08021	PRINT "Du är i en gång med vindlar överallt."
08022	GOSUB 12200
08025	IF X=4 THEN S(45)=2
08026	IF X=0 OR X>6 THEN 8019
08027	ON S(45) GOTO 8250,8263,8430
08034	GOSUB 8290
08035	Z=45'XXXXX LABYRINTRUM 10 XXXXX Z=45 XXX
08036	PRINT "Du är i en vindlande gång med hål överallt."
08037	GOSUB 12200
08038	IF X=0 OR X>6 THEN 8034
08040	IF S(45)=1 THEN S(45)=3
08041	IF S(45)=3 THEN ON X GOTO 8000,1919,8300,8020,17000,8365
08042	ON X GOTO 1919,8071,8020,8365,8300,8330
08054	PRINT "Den här hjälpen kostar inget."
08056	S(3)=1 \ S(41)=1
08057	GOTO 8035
08067	ON S(45) GOTO 8252,8258,8256
08070	GOSUB 8290
08071	Z=38'XXXXX LABYRINTRUM 3 XXXX Z=38 XXX
08072	PRINT "Du är i ett rum som vindlar."
08073	GOSUB 12200
08074	IF X=0 OR X>6 THEN 8070
08075	IF S(45)=3 THEN ON X GOTO 8095,8071,1919,8365,8330,8020
08076	ON S(45) GOTO 8261,8253
08093	GOSUB 11000
08095	Z=39'XXXXX LABYRINTRUM 4 XXXXX
08096	PRINT "Du är i ett rum med hål överallt."
08097	IF S(48)>0 THEN PRINT "Det finns ett krossat fönster här." \ GOTO 8102
08100	PRINT "Högt uppe i taket finns ett fönster."
08101	PRINT "Någon knackar på det!!!"
08102	GOSUB 12200
08103	IF X1=1 THEN 8095
08104	IF X=13 THEN 8131 ELSE IF X=0 THEN 8093
08105	IF X<>7 THEN 8112
08106	IF A(20)=1 AND S(33)=0 THEN PRINT "Sparka din pumpade boll!"\S(2)=S(2)-5\GOTO 8095
08108	PRINT "Inget du bär kan hjälpa dej att komma upp till fönstret." \ S(2)=S(2)-2
08110	GOTO 8095
08112	ON S(45) GOTO 8250,8254,8253
08131	PRINT "Du sparkar din boll mot fönstret."
08132	PRINT "   PANG!"
08133	PRINT "Fönsterrutan gick sönder." \ IF S(48)=-1 THEN S(2)=S(2)+10\S(48)=0
08134	S(48)=S(48)+1
08135	PRINT "Ett rep ramlar ner genom fönstret och nån viskar: -Kom fort!"
08137	A$=FNI$("Klättrar du upp på repet ?")
08138	IF FNL$(A$,1)="N" OR FNL$(A$,1)="n" THEN 8142
08139	IF FNL$(A$,1)="J" OR FNL$(A$,1)="j" THEN 8144
08140	PRINT "Bestäm dej!"
08141	GOTO 8137
08142	PRINT "TYST!! Han hörde dej och drog upp repet!!!"
08143	GOTO 8095
08144	PRINT "Du klättrar upp i en mörk gång efter en mörk skugga."
08145	PRINT "Långt borta hörs en röst:"
08146	PRINT " - HÖ, HÖ! En boll! In med den!!!"
08147	A(20)=4\S(1)=S(1)-1
08148	IF S(48)<>-1 THEN PRINT "Du är i en mörk gång." ELSE GOSUB 730 \ GOTO 17000
08149	Z=97 'XXXXX MÖRK GÅNG ÖVER LAB.4 XXXX
08150	GOSUB 12200
08152	IF X>0 THEN ON X GOTO 17000,25000,18000,10020,8300,8155,8153
08153	GOSUB 11000
08154	GOTO 8149
08155	IF S(47)=1 THEN 9510 ELSE 2168
08250	ON X GOTO 8365,8300,8000,8330,8020,8095,8011
08252	ON X GOTO 8420,8000,8365,8300,17000,8095,8054
08253	ON X GOTO 8330,8020,8330,8330,8300,8420,8054
08254	ON X GOTO 8381,8000,1500,1919,8330,8300,8054
08256	ON X GOTO 8095,8000,8420,8071,8300,8330,8054
08258	ON X GOTO 8300,8920,8095,8071,8330,14100,8054
08261	ON X GOTO 8381,8365,8300,8000,17000,8071,8054
08263	ON X GOTO 8095,8095,8300,8365,8067,1919,8054
08290	PRINT "Du kan gå åt vänster,höger,framåt,bakåt,uppåt och neråt!"
08291	RETURN
08300	Z=36'XXXXX LABYRINTRUM 1 XXXXX
08302	PRINT "Du är i en vindlande liten gång med hål."
08304	GOSUB 12200
08306	IF X=1 THEN 8095 ELSE IF X=0 THEN 8310
08307	IF S(45)=1 THEN ON X GOTO 8320,17000,8000,8322,8365,8330,8700
08308	IF S(45)=2 THEN ON X GOTO 8327,8320,8365,8300,8330,8381,8700
08309	IF S(45)=3 THEN ON X GOTO 1500,8330,8320,8365,8322,8381,8323
08310	GOSUB 8290
08311	GOTO 8304
08320	PRINT "Återvändsgränd!"
08321	GOTO 8300
08322	S(45)=2 \ GOTO 8420
08323	PRINT "TIPS!! Skriv framåt!"
08324	S(2)=S(2)-4
08325	GOTO 8300
08327	PRINT "Du är";
08328	GOTO 9450
08329	GOSUB 8290
08330	Z=37'XXXXX LABYRINTRUM 2 XXX Z=37 XXXX
08331	IF S(38)=0 THEN PRINT "Du är i en kolsvart gång." \ GOTO 8335
08332	PRINT "Du är i en gång där det på väggen står:"
08333	PRINT "Lampan försvinner om det tas ur gången. Stanna kvar!"
08334	GOSUB 6000
08335	A$=FNI$("") \ GOSUB 12000
08336	IF FNL$(A$,5)="VÄNTA" OR FNL$(A$,5)="STANN" THEN 8345
08338	IF X=13 THEN 8350
08339	IF X=7 AND S(38)=0 THEN 8343
08340	IF X=0 OR X>6 THEN 8329
08341	IF S(38)=1 THEN A(24)=31 \ S(38)=2 \ S(1)=S(1)-1 \ PRINT "Lampan försvinner!"
08342	ON X GOTO 8300,8327,8320,8365,8420,1919
08343	PRINT "HJÄLP: Det finns en sak här i mörkret."
08344	S(2)=S(2)-5 \ GOTO 8330
08345	IF A(24)<>1 OR S(38)<>1 THEN 8349
08347	PRINT "Lampan och ";
08348	S(38)=2
08349	PRINT "Du lyfts uppåt." \ GOTO 8148
08350	IF S(1)=9 THEN PRINT "Du kan inte bära fler saker." \ GOTO 8330
08351	PRINT "När du rör saken blir det ljust i gången. Saken är"
08352	PRINT "en lampa. På väggen ser du att det står:"
08353	S(1)=S(1)+1 \ A(24)=1 \ S(38)=1
08354	GOTO 8333
08363	GOSUB 8290
08365	Z=40'XXXXX LABYRINTRUM 5 XXXXX
08366	PRINT "Du är i en gång med hål."
08367	GOSUB 12200
08368	IF X=0 THEN 8363
08369	IF S(45)=1 THEN ON X GOTO 8420,8328,8381,14100,8330,8376,8373
08370	IF S(45)=2 THEN ON X GOTO 8376,8300,8400,8320,8381,8420,8700
08371	IF S(45)=3 THEN ON X GOTO 8381,8327,8320,8330,8376,8420,8700
08373	PRINT "TIPS! Gå åt höger."
08374	S(2)=S(2)-4
08375	GOTO 8365
08376	IF A(8)<>1 THEN 8330
08377	PRINT "Din trilogi (Sagorna om Härskarringen) försvinner plötsligt."
08378	A(8)=31 \ S(1)=S(1)-1
08379	GOTO 8365
08380	GOSUB 8290
08381	Z=41'XXXXX LABYRINTRUM 6 XXXXX
08382	PRINT "Du vindlar i en liten gång."
08384	GOSUB 12200
08386	IF X=0 THEN 8380
08387	IF S(45)=1 THEN ON X GOTO 8365,8000,8300,8400,8420,8320,8391
08388	IF S(45)=2 THEN ON X GOTO 8000,8300,8400,8365,8420,8330,8392
08389	IF S(45)=3 THEN ON X GOTO 8420,8365,8000,8400,8300,8330,8392
08391	S(45)=3
08392	PRINT "TIPS!!  Gå uppåt eller bakåt!" \ S(45)=3
08393	S(2)=S(2)-4
08394	GOTO 8380
08400	Z=42'XXXXX LABYRINTRUM 7 XXXXX
08401	PRINT "Du står på kanten till en djup brunn."
08402	PRINT "Om du hoppar ner kommer du inte upp igen!"
08403	GOSUB 12200
08406	IF X=0 THEN 8400
08407	IF S(45)=1 THEN ON X GOTO 8420,8327,8381,8420,8300,8330,8414
08408	S(45)=3
08409	ON X GOTO 8420,8327,8330,8420,8381,8300,8414
08414	PRINT "TIPS!! Chansa på uppåt eller neråt!"
08415	S(2)=S(2)-4
08416	GOTO 8403
08419	GOSUB 8290
08420	Z=52'XXXXX LABYRINTRUM 11 XXXXX
08421	PRINT "Lilla du vindlar."
08422	IF S(43)=0 THEN 8800
08423	GOSUB 12200
08425	IF X=0 OR X>6 THEN 8419
08426	IF S(45)=1 THEN ON X GOTO 8071,1929,8381,8000,8300,1500
08428	IF S(45)=2 THEN ON X GOTO 8000,8365,1950,8381,1500,8300
08430	IF S(45)=3 THEN ON X GOTO 8300,8000,8365,1970,8381,1500
08440	REM XXXX FOZZIS BERÄTTELSE XXXXX
08442	PRINT "Fozzi tar dej med in i hans loge och säjer :"
08443	PRINT " - Om du säjer ett niosiffrigt tal där ingen siffra är över fem"
08444	PRINT "så ska jag, Fozzi den rolige, hjälpa Dej med en berättelse."
08445	A$=FNI$("Svara SPRINGA eller ett niosiffrigt tal :")
08446	IF FNC$(FNL$(A$,5))="SPRIN" THEN 8842
08447	IF LEN(A$)<>9 THEN 8445
08448	GOTO 8445 IF ASCII(FNM$(A$,I))<48 OR ASCII(FNM$(A$,I))>54 FOR I=1 TO 9
08450	X(I)=VAL(MID$(A$,I,1)) FOR I=1 TO 9
08460	PRINT
08463	PRINT "Fozzi skriver upp en berättelse på en lapp som han ger dej."
08465	PRINT "Du går tillbaka till scenen och berättar."
08470	PRINT
08472	PRINT " - Ett meddelande når ";FNF$(1);" att ";FNF$(2)
08475	PRINT "  har släppts ut ur ";FNF$(3);" och kommer för att lägga"
08480	PRINT "  beslag på ";FNF$(4);". Staden befinner sej snart i klorna på"
08485	PRINT "  ";FNF$(5);" och folket sätter sej ner och väntar på "
08487	PRINT "  ";FNF$(6);"."
08490	PRINT "  Oroliga för att skurkarna tänker ";FNF$(7);" börjar"
08495	PRINT "  saloonflickorna bli ";FNF$(8);". Skurkarna kommer"
08500	PRINT "  men faran avvärjs ";FNF$(9);"."
08532	PRINT\PRINT "Publiken jublar men gubbarna på balkongen är bara spydiga."
08533	GOTO 8907
08600	S(36)=1 'XXX VÄDERSTRECKSSUBRUTIN XXXXX
08602	IF A$="" THEN 12210
08603	X=0 \ X1=0 \ A$=FNC$(A$)
08604	IF FNL$(A$,6)="SYDOST" OR FNL$(A$,6)="SYDÖST" OR A$="SO" OR A$="SÖ" THEN X=8
08605	IF FNL$(A$,4)="VÄST" OR A$="V" THEN X=1
08606	IF FNL$(A$,3)="ÖST" OR FNL$(A$,3)="OST" OR A$="Ö" OR A$="O" THEN X=2
08607	IF FNL$(A$,4)="NORR" OR FNL$(A$,4)="NORD" OR A$="N" THEN X=3
08608	IF FNL$(A$,3)="SYD" OR FNL$(A$,5)="SÖDER" OR A$="S" THEN X=4
08609	IF FNL$(A$,5)="NORDV" OR A$="NV" THEN X=5
08610	IF FNL$(A$,4)="SYDV" OR A$="SV" THEN X=6
08611	IF FNL$(A$,5)="NORDO" OR FNL$(A$,5)="NORDÖ" OR A$="NO" OR A$="NÖ" THEN X=9
08612	GOTO 12025
08613	'XXXX INVENTERING XXX
08614	IF S(1)=0 THEN PRINT "Du bär ingenting." \ GOTO 12210
08615	PRINT "Du bär på"
08617	IF A(1)=1 THEN PRINT "en gnistrande diamant"
08618	IF A(15)=1 THEN PRINT "en stor kofot"
08619	IF A(16)=1 THEN PRINT "en ny cykelpump"
08620	IF A(2)=1 THEN PRINT "en illaluktande gurka"' uääääääääääääääää
08621	IF A(3)=1 THEN PRINT "en snygg silvertacka"
08622	IF A(17)=1 THEN PRINT "en lång stege"
08623	IF A(18)<>1 THEN 8626
08624	IF S(31)=0 THEN PRINT "en full brännvinsflaska"
08625	IF S(31)=1 THEN PRINT "en tom brännvinsflaska"
08626	IF A(19)<>1 THEN 8629
08627	IF S(32)=0 THEN PRINT "en full vattenflaska"
08628	IF S(32)=1 THEN PRINT "en tom vattenflaska"
08629	IF A(20)<>1 THEN 8632
08630	IF S(33)=0 THEN PRINT "en pumpad boll"
08631	IF S(33)=1 THEN PRINT "en opumpad boll"
08632	IF A(4)=1 THEN PRINT "en sylvass hillebard"
08633	IF A(21)=1 THEN PRINT "en jordig spade"
08634	IF A(5)=1 THEN PRINT "en urgammal dödskalle"
08635	IF A(6)=1 THEN PRINT "en tickande väckarklocka"
08637	IF A(11)=1 THEN PRINT "ett glittrande pärlhalsband"
08638	IF A(22)=1 THEN PRINT "ett äckligt lik"
08640	IF A(12)=1 THEN PRINT "en ful faunsko"
08641	IF A(7)=1 THEN PRINT "en massa guldmynt"
08642	IF A(25)=1 THEN PRINT "en modern telefon"
08645	IF A(26)=1 THEN PRINT "några gamla nycklar"
08646	IF A(27)=1 THEN PRINT "en vass sax"
08647	IF A(28)=1 THEN PRINT "en tung slägga"
08650	IF A(8)=1 THEN PRINT "en läsvärd trilogi (Sagorna om Härskarringen)"
08651	IF A(24)=1 THEN PRINT "en lampa"
08652	IF A(9)=1 THEN PRINT "ett skärt kontrakt"
08653	IF A(10)=1 THEN PRINT "en grön lagerkrans"
08654	IF A(23)=1 THEN PRINT "en tunn telefonkatalog"
08656	IF A(30)=1 THEN PRINT "en förlängningssladd till telefonen"
08663	GOTO 12210
08700	PRINT "Du kan inte få nå'n hjälp så som du ser ut!"\ D=INT(RND*5)+1
08701	ON D GOTO 8000,8300,8095,8035,8420
08800	S(43)=1'XXX MUPPET SHOW XXX
08802	IF W$(6)<>"" THEN 8808
08804	PRINT "Här sitter björnen Fozzi och frågar:"
08806	W$(6)=FNI$("Vad heter du ?") \ GOTO 8810
08808	PRINT "Björnen Fozzi skyndar förbi dej."
08810	REM PLATS FÖR SIGNATUR
08830	PRINT "Någon säjer: Här är THE MUPPET SHOW med kvällens gäst-"
08831	PRINT "artist: ";W$(6)
08833	PRINT "Ridån går upp och du är på en scen tillsammans med"
08834	PRINT "grodan Kermit. Dockpubliken applåderar."
08836	A$=FNI$("Svara SPRING eller UPPTRÄD :") \ A$=FNC$(A$) \ PRINT
08838	IF FNL$(A$,5)="SPRIN" THEN 8842
08839	IF FNL$(A$,5)="UPPTR" THEN 8873
08840	GOTO 8836
08842	PRINT "Du springer rätt in i ett monster som slukar dej i en enda"
08843	PRINT "munsbit! Du känner en sprängladdning här!"
08845	A$=FNI$("Svara ROPA eller SPRÄNG :") \ A$=FNC$(A$) \ PRINT
08846	IF FNL$(A$,4)="ROPA" THEN 8850
08847	IF FNL$(A$,5)="SPRÄN" THEN 8857
08848	GOTO 8845
08850	PRINT "Du ropar och Kermit hämtar hjälp. Det tar tid."
08852	A$=FNI$("Svara VÄNTA eller SPRÄNG :") \ A$=FNC$(A$) \ PRINT
08853	IF FNL$(A$,5)="VÄNTA" THEN 8860
08854	IF FNL$(A$,5)="SPRÄN" THEN 8857
08855	GOTO 8852
08857	PRINT "Du och monstret sprängs i bitar!	"
08859	GOTO 9461
08860	PRINT "Du väntar i 30 sekunder!"
08861	S=ECHO(1)
08862	FOR I=1 TO 6
08863	D=SLEEP(5)
08864	IF D THEN INPUT ""_A$
08867	NEXT I
08868	S=ECHO(0)
08870	PRINT "Någon skär upp magen. Du märker att"
08871	GOTO 8833
08873	PRINT "Kermit frågar dej om du vill sjunga eller berätta en historia."
08875	A$=FNI$("Svara SJUNG eller BERÄTTA :") \ A$=FNC$(A$) \ PRINT
08876	IF FNL$(A$,5)="SJUNG" THEN 8890
08877	IF FNL$(A$,5)="BERÄT" THEN 8880
08878	GOTO 8875
08880	PRINT "Du börjar att berätta men efter första meningen"
08881	PRINT "avbryts du av kraftiga bu-rop. Bara två gubbar pä"
08882	PRINT "läktaren skrattar (åt ditt utseende). Fozzi erbjuder dej hjälp."
08884	A$=FNI$("Svara HJÄLP eller SPRING :") \ A$=FNC$(A$) \ PRINT
08885	IF FNL$(A$,5)="SPRIN" THEN 8842
08886	IF FNL$(A$,5)="HJÄLP" THEN 8440
08887	GOTO 8884
08890	PRINT "Du börjar sjunga: I'm a poor lonesome cowboy and a"
08891	PRINT "long way from home..."
08894	PRINT "Publiken jublar men sångarna Wayne & Wanda är arga"
08895	PRINT "på dej för att du tagit deras plats. Dom vill döda dej!"
08897	A$=FNI$("Svara FRED (med Wayne & Wanda) eller FÖLJ (Kermit) :")
08898	A$=FNC$(A$) \ PRINT
08899	IF FNL$(A$,4)="FRED" THEN 8920
08900	IF FNL$(A$,4)<>"FÖLJ" THEN 8897
08902	D=INT(RND*7)+1
08903	IF D>4 THEN 8907
08904	PRINT "Wayne & Wanda kommer bakifrån och kastar upp dej i luften!"
08905	S(43)=0 \ GOTO 8963
08907	PRINT "Du följer efter Kermit för att få ett kontrakt."
08910	W$(2)=FNI$("Fozzi säjer: Skriv ett intresse som du har :")
08912	PRINT "Fozzi tackar för sej och går." \ IF S(1)=9 THEN 9528
08913	PRINT "Du får ett skärt kontrakt av Kermit."\PRINT "Det finns en dörr till höger."
08914	A(9)=1 \ S(1)=S(1)+1
08915	A$=FNI$("Svara FÖLJ (Fozzi) eller HÖGER :") \ A$=FNC$(A$) \PRINT
08916	IF FNL$(A$,4)="FÖLJ" THEN 8943
08917	IF FNL$(A$,5)="HÖGER" THEN 8950
08918	GOTO 8915
08920	PRINT "Du går fram mot Wayne & Wanda för att sluta fred."
08921	D=INT(RND*20)+1
08922	IF D=1 THEN 8904
08923	PRINT "Du bestämmer att du inte ska sjunga mer så W&W"
08924	PRINT "ska kunna behålla jobbet. Fozzi kommer fram och säjer:"
08925	W$(2)=FNI$("Skriv ett intresse du har!")
08928	PRINT "Fozzi tackar för sej och går. Det finns en dörr till vänster."
08929	A$=FNI$("Svara FÖLJ (Fozzi) eller VÄNSTER :") \ A$=FNC$(A$) \ PRINT
08930	IF FNL$(A$,5)="VÄNST" THEN 8950
08931	IF FNL$(A$,4)="FÖLJ" THEN 8943
08932	GOTO 8929
08943	PRINT "Nu går Fozzi in genom en dörr. Det finns också en dörr framåt."
08944	A$=FNI$("Svara FÖLJ (Fozzi) eller FRAMÅT :") \ A$=FNC$(A$) \ PRINT
08945	IF FNL$(A$,5)="FRAMÅ" THEN 8950
08946	IF FNL$(A$,4)="FÖLJ" THEN 8970
08947	GOTO 8944
08950	PRINT "Du är innanför dörren. Kermit kommer fram och säjer"
08951	PRINT "att du ska vara med i en diskussion om ";W$(2)
08953	A$=FNI$("Svara DISKUTERA eller SPRING :") \ A$=FNC$(A$) \ PRINT
08954	IF FNL$(A$,5)="DISKU" THEN 8980
08955	IF FNL$(A$,5)="SPRIN" THEN 8960
08957	GOTO 8953
08960	PRINT "Du springer rätt in i ett monster som slukar grönsaker!"
08961	PRINT "Han tar upp dej och kastar dej högt upp i luften."
08963	D=INT(RND*5)+1
08964	ON D GOTO 8327,1500,14100,9145,16000
08970	PRINT "Du är inne i en tortyrkammare. Dörren gick i lås bakom dej!"
08971	PRINT "Väggarna närmar sej. Enda vägen ut spärras av ett monster!"
08973	A$=FNI$("Svara SPRING (ut) eller STANNA :") \ A$=FNC$(A$) \ PRINT
08974	IF FNL$(A$,5)="SPRIN" THEN 8960
08975	IF FNL$(A$,5)="STANN" THEN 8977
08976	GOTO 8973
08977	PRINT "Väggarna klämmer ut inälvorna på dej!"
08978	GOTO 9461
08980	S(2)=S(2)+30
08983	PRINT "Kermit inleder: Nu ska vi återigen höja programmets"
08984	PRINT "intellektuella nivå. Vi ska idag prata kring ämnet ";W$(2);"."
08985	PRINT W$(6);" får inleda med en replik. Vad tycker du om ";W$(2);"?"
08987	A$=FNI$("")
08988	PRINT "Kermit: Jag håller fullständigt med dej!"
08989	PRINT "Fozzi: Nej helt fel, tvärt om!"
08990	PRINT "Gubbarna: Ut med björnen!"
08991	PRINT "Fozzi: Det var det värsta!!!!"
08992	PRINT "Gubbarna: Nej dina skämt är värre! HA	 HA	 HA	..."
08993	PRINT "Fozzi: Jag ska minsann..."
08994	PRINT "Kermit: Öh...Vi får visst avrunda här. Nästa veckas ämne:"
08995	PRINT "-Varför retas folk?"
08996	PRINT "Vi ses då i: *****THE MUPPET SHOW*****"
08997	GOTO 1500
08999	GOSUB 11000
09000	Z=21 \ R$="första"'XXXX HISSRUM 1 XXX Z=21 XXX
09002	GOSUB 9250
09004	GOSUB 12200
09008	IF X=4 THEN 16000
09010	IF X<>3 THEN 8999
09012	GOSUB 9260
09014	ON X% GOTO 9008,9300,9000
09019	GOSUB 11000
09020	Z=28 \ R$="åttonde"'XXXX HISSRUM 8 XXX Z=28 XXX
09022	GOSUB 9250
09024	GOSUB 12200
09026	IF X=4 THEN 41000
09028	IF X<>3 THEN 9019
09030	GOSUB 9260
09032	ON X% GOTO 9026,9300,9020
09035	Z=22'XXXX HISSRUM 2 XXX Z=22 XXX
09037	PRINT "Du befinner dej i andra våningens hissrum. Till höger ser man"
09039	IF S(40)=2 THEN PRINT "en öppen"; ELSE PRINT "en stängd";
09041	PRINT " hissdörr. I den vänstra väggen finns"
09043	PRINT "ett hål till ett trapprum."
09045	GOSUB 12200
09047	IF X=3 THEN 15370
09048	IF X1=1 THEN 9035
09051	IF X<>4 THEN 9056
09053	GOSUB 9260
09055	ON X% GOTO 9047,9300,9035
09056	GOSUB 11000
09058	PRINT "Du är i andra våningens hissrum."
09060	GOTO 9045
09065	Z=23'XXXX HISSRUM 3 XXX Z=23 XXX
09066	PRINT "3:e våningens hissrum var visst toaletten."
09067	PRINT "Du spolas ut på golvet. Till vänster finns"
09068	PRINT "en dörr men du kan också spola ner dej."
09069	GOSUB 12200
09070	IF FNL$(A$,3)="SPO" THEN 9075
09071	IF X1=1 THEN PRINT "Som sagt, "; \ GOTO 9065
09072	IF X=3 THEN 8300
09073	GOSUB 11000
09074	PRINT "Du är i toaletten." \ GOTO 9069
09075	PRINT "Du befinner dej";
09076	GOTO 9450
09099	GOSUB 11000
09100	Z=27 \ R$="sjunde"'XXXX HISSRUM 7 XXX Z=27 XXX
09102	GOSUB 9250
09103	GOSUB 12200
09104	IF X=4 THEN 1919
09105	IF X<>3 THEN 9099
09106	GOSUB 9260
09107	ON X% GOTO 9104,9300,9100
09144	GOSUB 11000
09145	Z=24 \ R$="fjärde"'XXXX HISSRUM 4 XXX Z=24 XXX
09146	GOSUB 9250
09147	PRINT "Bakom dej anar man en öppning."
09148	GOSUB 12200
09150	IF X=4 THEN 15432
09152	IF X=6 THEN 15300
09154	IF X<>3 THEN 9144
09156	GOSUB 9260
09158	ON X% GOTO 9150,9300,9145
09174	GOSUB 11000
09175	Z=26 \ R$="sjätte"'XXXX HISSRUM 6 XXX Z=26 XXX
09177	GOSUB 9250
09179	GOSUB 12200
09181	IF X=4 THEN 8381
09183	IF X<>3 THEN 9174
09185	GOSUB 9260
09187	ON X% GOTO 9181,9300,9175
09189	GOSUB 11000
09190	Z=29 \ R$="nionde"'XXXX HISSRUM 9 XXX Z=29 XXX
09192	GOSUB 9250
09194	GOSUB 12200
09196	IF X=4 THEN 35000
09198	IF X<>3 THEN 9189
09200	GOSUB 9260
09202	ON X% GOTO 9196,9300,9190
09210	A=A*-1
09211	PRINT S(39);
09212	X=S(39)
09213	FOR I=1 TO A
09214	S=SLEEP(2)
09215	IF S THEN 9222
09216	X=X-1
09217	PRINT "   ";X;
09219	NEXT I
09220	PRINT CHR$(7)
09221	GOTO 9359
09222	INPUT ""_C$
09223	IF FNL$(C$,1)<>"N" AND FNL$(C$,1)<>"n" THEN 9216
09224	S(40)=X
09225	PRINT "Hissen stannar och du kastas ur!"
09226	GOTO 9360
09228	X=S(39)
09229	PRINT S(39);
09230	FOR I=1 TO A
09231	S=SLEEP(2)
09232	IF S THEN 9238
09233	X=X+1
09234	PRINT "   ";X;
09236	NEXT I
09237	GOTO 9220
09238	INPUT ""_C$
09239	IF FNL$(C$,1)<>"N" AND FNL$(C$,1)<>"n" THEN 9233
09240	GOTO 9224
09250	PRINT "Du är i ";R$;" våningens hissrum. Till vänster finns en"
09252	IF S(40)=Z-20 THEN PRINT "öppen"; ELSE PRINT "stängd";
09254	PRINT " hissdörr och till höger en annan dörr."
09256	RETURN
09260	X%=2 \ S(39)=Z-20
09261	IF S(40)=S(39) THEN S(40)=0 \ GOTO 9280
09262	PRINT "Du står framför en stängd hissdörr. På en knapp bredvid"
09263	PRINT "dörren står det HIT."
09264	GOSUB 12200
09265	IF X1=1 THEN 9262
09266	IF FNL$(A$,3)<>"TRY" AND A$<>"HIT" THEN X%=1 \ GOTO 9280
09268	IF S(40)=10 THEN PRINT "Hissen kommer inte. Den måste vara trasig!" \ X%=3 \ GOTO 9280
09269	I1=1
09270	I=INSTR(I1,A$," ")
09271	IF I<1 OR I>=LEN(A$) THEN 9276
09272	D=ASCII(MID$(A$,I+1,1))
09273	IF D>47 AND D<58 THEN S(40)=D-48 \ GOTO 9278
09274	I1=I+1
09275	IF I1<LEN(A$) THEN 9270
09276	S(40)=-1
09277	W$="TRYCK 0"
09278	PRINT "Hissen kommer och du stiger in."
09280	RETURN
09300	Z=18 \ S(22)=S(22)+1 'XXX HISSEN XXX
09301	IF S(40)>0 THEN 9335 ELSE S=SLEEP(2)
09304	IF S(22)/2=INT(S(22)/2) THEN PRINT "Du är i hissen." \ GOTO 9307
09305	PRINT "Du är i hissen. Här finns tio knappar. Dom nio första är numrerade"
09306	PRINT "1-9. På den sista står det NÖDSTOPP."
09307	GOSUB 6000
09308	PRINT "Vilken knapp trycker du på ? ";
09309	E=INT(RND*9)+1 \ E1=INT(RND*15)+5
09310	IF S(40)=0 OR M3%=1% THEN 9315 ELSE IF SLEEP(8+E1) THEN 9315
09311	PRINT \ PRINT "Dörrarna går igen och hissen startar."
09312	IF M2%=1% THEN PRINT #2,W$ \ W$=STR$(E)'&&&&&
09313	S(40)=E \ PRINT "Hissen går till";S(40);"an."
09314	GOTO 9356
09315	A$=FNI$("") \ PRINT
09316	IF ASCII(A$)>48 AND ASCII(A$)<58 THEN S(40)=VAL(FNL$(A$,1)) \ GOTO 9335
09318	IF FNL$(A$,1)<>"N" AND FNL$(A$,1)<>"n" THEN GOSUB 12000\GOTO 9330
09322	PRINT "Skrik inte på hjälp innan det hemska börjar!"
09323	GOTO 9308
09330	IF ASCII(A$)>48 AND ASCII(A$)<58 THEN 9316
09331	IF X1=1 THEN 9300
09332	GOSUB 11000 \ GOTO 9305
09335	IF S(41)<>1 THEN 9355
09337	PRINT FNS$("åker hiss",5)
09338	PRINT "Hissen faller	!!"
09339	PRINT "Hissen krossas mot hisschaktets botten."
09340	S(40)=10 \ GOTO 9461
09355	PRINT "Hissen startar." \ S=SLEEP(4)
09356	A=S(40)-S(39)
09357	IF A=0 THEN 9360
09358	IF A<0 THEN 9210 ELSE 9228
09359	PRINT "Hissen är framme. Du går ur..."\ IF RND<0.1 THEN S(41)=1
09360	ON S(40) GOTO 9000,9035,9065,9145,9075,9175,9100,9020,9190
09361	Z=49'XXX ÖSTRA STRANDEN XXX Z=49 XXXXX
09362	PRINT "Du är på östra stranden. Åt norr är det skog."
09364	IF S(35)=0 THEN PRINT "Här ligger en roddbåt."
09366	GOSUB 15200
09368	IF S(35)=0 AND (INSTR(1,A$,"BÅT")>0 OR A$="RO") THEN 9390
09370	IF X<>0 THEN ON X GOTO 20000,9424,20070,9374,20200,9374,9372,9374,20085,2107
09372	GOSUB 11000 \ GOTO 9361
09374	PRINT "Du kan väl inte gå på vattnet?" \ GOTO 9361
09390	Z=78'XXXX I BÅTEN XXXXX Z=78 XXXXX
09391	PRINT "Du sitter i båten, mitt i sjön."
09392	GOSUB 15200 \ S(35)=INT(RND*2)
09393	IF X=1 THEN 9410
09394	IF X=2 THEN 9416
09395	IF X=3 THEN S(35)=0 \ GOTO 9361
09396	IF X=4 THEN S(35)=1 \ GOTO 2200
09397	IF X=10 THEN 2107
09399	GOSUB 11000
09400	PRINT "Skriv söder, norr, öster eller väster."
09401	GOTO 9392
09410	PRINT "Oj, en motorbåt åkte för nära dej."
09411	PRINT "Din båt går runt och Du svimmar!"
09412	PRINT
09414	PRINT "När Du vaknar är Du";
09415	GOTO 9450
09416	PRINT "Du ror och ror..."
09417	PRINT "Plötsligt åker Du in i en vattenvirvel som suger ner "
09418	PRINT "både Dej och båten."
09419	D=SLEEP(3) \ IF D THEN INPUT ""_A$
09420	PRINT
09421	PRINT "Du flyter upp och ser att"
09422	Z=4\GOSUB 7500
09423	GOTO 2066
09424	PRINT "Du är på en stenig sjöstrand."
09425	PRINT "Det finns en liten badhytt här."\Z=88
09426	PRINT "Ett staket hindrar dej att gå åt NORDOST,ÖSTER eller SYDOST."
09428	GOSUB 15200
09429	IF X1=1 THEN 9424
09430	IF X=0 THEN 9436
09431	ON X GOTO 9361,9426,20085,20330,20070,9432,9437,9426,9426,2107
09432	PRINT "Kan du gå på vattnet?"
09433	GOTO 9424
09436	IF INSTR(1,A$,"BADHYTT")>0 OR FNL$(A$,5)="ÖPPNA" OR A$="IN" THEN 9439
09437	GOSUB 11000
09438	GOTO 9424
09439	PRINT "Du går in i badhytten men golvet ger vika och du faller..."
09440	GOTO 25000
09450	PRINT " under bryggan."
09451	PRINT "Du ser ett hål rakt fram, men kan inte komma dit."
09452	IF A(1)<>1 THEN GOTO 9455
09453	A(1)=0 \ S(1)=S(1)-1
09454	PRINT "OJ! Du tappar diamanten. Den ligger på botten."
09455	IF S(2)<10 THEN 9459
09456	A$=FNI$("Vill du vara kvar här ?")
09457	IF FNL$(A$,1)="N" OR FNL$(A$,1)="n" THEN 20005
09459	PRINT
09460	PRINT "Din luft är slut och du kvävs. Ditt lik flyter upp."
09461	A$=FNI$("Vill du att jag ska återuppliva dej ?")
09462	S(46)=S(46)+1
09464	IF FNL$(A$,1)="N" OR FNL$(A$,1)="n" THEN 9484
09467	IF FNL$(A$,1)="J" OR FNL$(A$,1)="j" THEN 9470
09468	PRINT "JA eller NEJ! Min chans att lyckas minskar...	"
09469	S(46)=S(46)+1 \ GOTO 9461
09470	PRINT "OK, men skyll inte på mej om något går fe..."
09471	IF S(46)=1 THEN 9479
09472	IF S(46)=6 THEN 9483
09473	D=INT(RND*10)+1
09474	IF D>3 THEN 9479
09475	PRINT "POFF!!! Ett grönt gasmoln omger dej!"
09476	PRINT "OJOJOJ, det gick inte. Du är fortfarande stendöd! Jag"
09477	PRINT "lovar att du ska få en värdig begravning!!"
09478	GOTO 99000
09479	PRINT "POFF!!!	 Ett grönt gasmoln omger dej!!"
09480	PRINT "Du lever! 	 När gasen skingrats ser Du att "
09482	S(2)=S(2)-5
09483	GOTO 36050
09484	PRINT "VA? Litar du inte på mig? Senast igår återuppväckte jag"
09485	PRINT "en DEC-2020 och den fungerade i flera minuter..."
09486	PRINT
09487	PRINT "Men jag ska inte bråka. Du får som du vill."
09488	GOTO 99000
09490	Z=54'XXXXX VIGGOS HEMLIGA RUM 1 XXXXX
09491	PRINT "Du är i ett dunkelt, dammtäckt rum."
09492	PRINT "Dörrar går bakåt, åt höger och framåt."
09493	IF S(47)>0 THEN PRINT "Det finns ett hål till vänster." \ GOTO 9496
09494	PRINT "Bakom ett draperi till vänster kan man ana ett hål."
09496	GOSUB 12200
09497	IF X1=1 THEN 9490
09500	IF X>0 THEN ON X GOTO 9501,9501,9510,9558,9545,14000,9501
09501	GOSUB 11000
09502	PRINT "Du är i ett dunkelt, dammtäckt rum."\GOTO 9496
09510	Z=55'XXXXX VIGGOS HEMLIGA RUM 2 XXXXX
09511	IF S(47)>0 THEN PRINT "Det finns ett hål i väggen." ELSE PRINT "Du är vid draperiet."
09512	GOSUB 12200
09515	IF X=5 THEN 9525
09516	IF X=6 THEN 9492
09517	IF FNL$(A$,5)="KLIPP" AND S(47)=0 THEN 9520
09518	IF (FNL$(A$,5)="ÖPPNA" OR FNL$(A$,3)="DRA") AND S(47)=0 THEN 9523
09519	GOSUB 11000 \ GOTO 9510
09520	IF A(27)=1 THEN 9535
09521	PRINT "Du har inget att klippa med!"
09522	GOTO 9510
09523	PRINT "Du är för svag för att kunna rubba draperiet."
09524	GOTO 9510
09525	IF S(47)=1 THEN 8148
09526	PRINT "Draperiet är i vägen."
09527	GOTO 9510
09528	Z=60'XXXXX MUPPET SHOW DEL 2 XXXXX
09529	PRINT "Kermit vill ge dej ett kontrakt, men då måste du släppa"
09530	PRINT "något först. (Tänk på att du inte kommer hit igen!!)"
09531	A$=FNI$("Svara SLÄPP <det du vill släppa> eller DÅLIGT:")
09532	IF FNC$(FNL$(A$,5))="SLÄPP" THEN GOSUB 12000
09533	IF S<9 THEN 8913
09534	PRINT "Ok." \ PRINT "Du går genom en dörröppning." \ GOTO 8950
09535	S(47)=1 \ S(2)=S(2)+20
09536	PRINT "Du klipper sönder draperiet. Draperiet försvinner."
09537	GOTO 9510
09545	Z=56'XXXXX VIGGOS HEMLIGA RUM 3 XXXXX
09546	PRINT "Du är i en återvändsgränd."
09547	IF A(28)=2 THEN PRINT "Det ligger en låst låda här som du inte orkar bära."
09548	GOSUB 12200
09550	IF X=6 THEN 9490
09551	IF FNL$(A$,3)="LÅS" THEN 9553
09552	GOSUB 11000 \ GOTO 9545
09553	IF A(26)<>1 OR A(28)<>2 THEN PRINT "Det kan du inte." \ GOTO 9545
09554	PRINT "Du låser upp lådan och hittar en slägga. Lådan försvinner."
09555	A(28)=56 \ GOTO 9545
09556	GOSUB 11000
09557	PRINT "Du är i höger kammare." \ GOTO 9562
09558	Z=57'XXXXX VIGGOS HEMLIGA RUM 4 XXXXX
09559	PRINT "Du är i höger kammare. En väg går framåt, men på ett"
09560	PRINT "anslag står det: DU SOM VÅGAR DEJ IN HÄR FÅR "
09561	PRINT "ANTINGEN EN BELÖNING ELLER OCKSÅ ... DÖDEN"
09562	IF A(27)=2 THEN PRINT "Fastskruvad i väggen sitter en glasask med en sax i."
09563	GOSUB 12200
09564	IF FNL$(A$,3)="SLÅ" OR FNL$(A$,5)="KROSS" THEN 9568
09565	IF X=0 OR X>6 THEN 9556
09566	ON X GOTO 9556,9556,9556,9556,9575,9490
09568	IF A(27)<>2 THEN 9556
09569	IF A(28)<>1 THEN PRINT "Du har inget att slå med."\ GOTO 9558
09570	PRINT "Du krossar glaset. Saxen ramlar ur och asken försvinner i ett moln."
09571	A(27)=57 \ GOTO 9557
09575	D=INT(RND*10)
09576	IF D<4 THEN PRINT "Gången mynnar ut i ett hus." \ GOTO 2241
09577	PRINT "Du trampar på en sprängladdning och sprängs i luften!"
09578	GOTO 9461
09950	IF M2%=1% THEN CLOSE 2 \ M2%=0%'&&&&& Stäng ev. loggfil
09951	PRINT \ PRINT "Är du säker på att du vill sluta nu?";
09952	A$=FNI$("") \ A$=FNC$(A$)
09953	IF FNL$(A$,1)="J" THEN 99000
09957	PRINT "Ok. Du har";S(2);"poäng!"
09958	GOTO 12210
09991	Z=8 \ S(8)=S(8)+1'XXXXX HALLEN XXXXX
09993	IF S(8)=1 THEN S(2)=S(2)+5
09995	IF S(8)<3 OR S(8)>7 THEN 10009 ELSE 10000
09997	GOSUB 11000
10000	PRINT "Du är i hallen."
10001	GOSUB 12200
10002	IF S1>0 THEN 10001
10003	IF X1=1 THEN 10009
10004	IF X=19 THEN GOSUB 12202 \ GOTO 10003
10006	IF X>2 AND X<7 THEN ON X-2 GOTO 15350,1500,15425,10015
10008	GOTO 9997
10009	PRINT "Du är i en hall med tre dörrar. På den vänstra finns en nedåtriktad"
10010	PRINT "pil, på dörren rakt fram finns en pil som pekar uppåt och på dörren"
10011	PRINT "till höger står det atelje. Bakom dej ligger porten ut ur huset."
10012	IF S(19)=1 THEN PRINT "Ytterporten är öppen."
10013	IF S(8)>7 THEN S(8)=3
10014	GOTO 10001
10015	IF S(19)=1 THEN PRINT "Porten stängs bakom dej."\S(19)=0\GOTO 20200
10016	PRINT "Porten är stängd!"
10017	GOTO 10000
10020	Z=16'XXXXX SKUMGUMMIRUMMET XXXXX
10022	PRINT "Du är i Skumgummirummet."
10024	IF A(15)=0 THEN PRINT "Det finns ett mystiskt, mörkt fönster i väggen."
10025	IF A(15)=0 THEN PRINT "Bakom fönstret anar man ett föremål."
10026	PRINT "Det finns dörrar framåt och åt vänster."
10028	PRINT "En gång går neråt."
10030	GOSUB 12200
10032	IF X1=1 THEN 10020
10034	IF X=0 THEN 10040
10036	ON X GOTO 10050,25130,25100,10050,21100,25000,10090
10040	IF A(15)>0 THEN 10050
10042	IF FNL$(A$,5)="KROSS" OR FNL$(A$,3)="SLÅ" THEN 10084
10044	IF FNL$(A$,4)="SKÄR" THEN 10060
10046	IF FNL$(A$,5)="ÖPPNA" THEN PRINT "Du kan inte öppna fönstret." \ GOTO 10052
10050	GOSUB 11000
10052	PRINT "Du är i Skumgummirummet."
10054	GOTO 10030
10060	IF INSTR(1,A$,"DIAMA")>0 THEN 10072
10062	IF INSTR(1,A$,"TUNGA")>0 THEN 9075
10064	A$=FNI$("Vad ska du skära med? Din vassa tunga ?")
10065	A$=FNC$(A$)
10066	IF A$="JA" OR FNL$(A$,5)="TUNGA" THEN 9075
10068	IF A$="NEJ" THEN PRINT "Det var ju skönt!" \ GOTO 10052
10070	IF FNL$(A$,5)<>"DIAMA" THEN PRINT "Det går inte!" \ GOTO 10052
10072	IF A(1)<>1 THEN PRINT "Du bär väl ingen DIAMANT!"\GOTO 10052
10074	PRINT "Du skär upp fönstret med diamanten."
10076	PRINT "En kofot ramlar ut och slår dej hårt i huvudet."
10078	PRINT "Du rasar ihop av slaget.";FNS$("sover",10)
10079	S(2)=S(2)+10\PRINT "När du vaknar är du fortfarande i Skumgummirummet."
10080	A(15)=16 \ GOTO 10030
10084	IF A(28)<>1 THEN PRINT "Du har inget att slå med." \ GOTO 10052
10086	PRINT "Du krossar fönstret med släggan. Därbakom finns en kofot."
10087	PRINT "Thorvald springer fram och säjer: - Jag hörde braket! Nu tar jag"
10088	PRINT "kofoten som betalning för det förstörda fönstret."
10089	PRINT "Han tar kofoten och försvinner." \ A(15)=5 \ GOTO 10020
10090	IF A(15)>0 THEN 10050
10092	IF A(1)<>1 THEN PRINT "Försök att hitta något du kan skära upp fönstret med."
10094	IF A(1)=1 THEN PRINT "Skär upp fönstret med din diamant!"
10096	S(2)=S(2)-5 \ GOTO 10052
11000	REM VIOLS SUBFELMEDDELANDERUTIN 3
11001	IF X1>0 OR S1>0 THEN 11100 ELSE S(50)=S(50)-1
11002	IF INSTR(1,A$,"HJÄLP")>0 THEN PRINT "Du kan inte få någon hjälp här." \ GOTO 11100
11003	IF A$="N" OR A$="V" THEN PRINT "Du kan inte gå ditåt." \ GOTO 11100
11004	IF INSTR(1,"*NORR*SÖDER*VÄSTER*ÖSTER*NV*NÖ*NO*SV*SÖ*SO","*"+A$)>0 THEN 11200
11005	IF INSTR(1,"*NORDVÄST*NORDÖST*NORDOST*SYDVÄST*SYDÖST*SYDOST","*"+A$)>0 THEN 11200
11006	IF INSTR(1,"*UPPÅT*NEDÅT*NERÅT*VÄNSTER*HÖGER*FRAMÅT*BAKÅT","*"+A$)>0 THEN 11220
11007	IF INSTR(1,A$,"SESAM")=0 AND INSTR(1,A$,"KORKSKRUV")=0 THEN 11011
11008	PRINT "Ingenting händer."
11009	GOTO 11100
11011	IF INSTR(1,A$,"STÄNG")>0 THEN PRINT "Det finns inget du kan stänga här!"\GOTO  11100
11013	IF INSTR(1,A$,"KROSS")>0 THEN PRINT "Det finns inget du kan krossa här!"\GOTO 11100
11014	IF INSTR(1,A$,"SKÄR")>0 THEN PRINT "Det finns inget du kan skära här!"\  GOTO 11100
11015	IF A$="SE" OR INSTR(1,A$,"TITTA")>0 THEN RETURN
11017	IF FNL$(A$,5)="HOPPA" AND X=1 THEN PRINT "Du kommer ingenstans uppåt." \ GOTO 11100
11018	IF FNL$(A$,5)="HOPPA" THEN PRINT "Det finns inget hål att hoppa ner genom." \ GOTO 11100
11080	D=INT(RND*5)+1
11081	IF D=1 THEN PRINT "Va ??"
11082	IF D=2 THEN PRINT "Jag förstår inte."
11083	IF D=3 THEN PRINT "Det förstår jag inte alls."
11084	IF D=4 THEN PRINT "Det vet jag inte vad det betyder."
11085	IF D=5 THEN PRINT "Uttryck Dej klarare."
11099	PRINT
11100	RETURN
11200	IF S(36)=0 THEN PRINT "Inomhus ska du ange riktningar, inte väderstreck."
11202	IF S(36)<>0 THEN PRINT "Du kan inte gå ditåt."
11205	GOTO 11100
11220	IF S(36)=1 THEN PRINT "Utomhus ska du ange väderstreck, inte riktningar."
11225	IF S(36)<>1 THEN PRINT "Du kan inte gå ditåt."
11230	GOTO 11100
12000	S(36)=0'XXXXX KOMMANDOAVKODARE XXXXX
12001	IF A$="" THEN 12210
12003	X=0 \ X1=0 \ A$=FNC$(A$)
12010	IF FNL$(A$,3)="UPP" OR A$="U" THEN X=1
12012	IF FNL$(A$,3)="NER" OR FNL$(A$,3)="NED" OR A$="N" THEN X=2
12014	IF INSTR(1,A$,"VÄNSTER")>0 OR A$="V" THEN X=3
12016	IF INSTR(1,A$,"HÖGER")>0 OR A$="H" THEN X=4
12018	IF INSTR(1,A$,"FRAM")>0 OR A$="F" THEN X=5
12020	IF INSTR(1,A$,"BAKÅ")>0 OR A$="B" THEN X=6
12025	IF INSTR(1,A$,"HJÄLP")>0 THEN X=7
12027	IF X>0 AND X<>7 AND S(21)>0 THEN PRINT FNS$("haltar",5);
12030	E=INSTR(1,A$," ") \ C$=FNM$(A$,E)
12032	IF C$="" THEN C$="" \ GOTO 12050
12034	IF FNL$(C$,1)=" " THEN C$=FNM$(C$,2) \ GOTO 12032
12050	S(50)=S(50)+1 \ S1=0
12052	IF FNL$(A$,5)="VÄNTA" OR FNL$(A$,5)="STANN" THEN 12570
12055	IF INSTR(A$,"HELVETE")>0 THEN PRINT "Åt vilket håll är det?" \ GOTO 12210
12056	IF FNL$(A$,5)="HOPPA" THEN 12130
12057	IF FNL$(A$,6)="VRICKA" THEN 12584
12058	IF INSTR(A$,"KNACK")>0 THEN PRINT "Ingenting händer." \ GOTO 12210
12059	IF FNL$(A$,4)="SKIT" THEN 12590
12060	IF FNL$(A$,5)="SKRIK" THEN 12550
12061	IF FNL$(A$,3)="FAN" OR FNL$(A$,5)="JÄVLA" OR FNL$(A$,6)="DJÄVLA" OR FNL$(A$,5)="SATAN" THEN 12555
12062	IF A$="TITTA" OR A$="SE" THEN X1=1 \ S(50)=S(50)-1
12063	IF A$="ALEA JACTA EST" THEN 12220
12064	IF A$="SLUTA" THEN 9950
12065	IF FNL$(A$,2)="GÅ" THEN 12255
12066	IF FNL$(A$,5)="BLÄND" THEN 12850
12067	IF FNL$(A$,3)="GE " THEN 28090
12068	IF A$="VEKTOR" THEN 98000'%%%%% Denna rad kan tas bort
12069	IF FNL$(A$,4)="VÄCK" AND S(6)=3 THEN 28000
12070	IF FNL$(A$,5)="INVEN" THEN 8613
12071	IF FNL$(A$,2)="TA" THEN 6300
12072	IF FNL$(A$,5)="SLÄPP" THEN 7000
12073	IF FNL$(A$,4)="FYLL" THEN 12340
12074	IF FNL$(A$,5)="DRICK" THEN 12270
12075	IF FNL$(A$,4)="RING" THEN 12800
12076	IF A$="POÄNG" THEN PRINT "Du har";S(2);"poäng." \ GOTO 12210
12077	IF FNL$(A$,4)="GRÄV" THEN 12230
12078	IF FNL$(A$,5)="SPARK" THEN 12580
12079	IF FNL$(A$,4)="DÖDA" THEN 12240
12080	IF FNL$(A$,1)="?" THEN X1=1 \ S(50)=S(50)-1 \ GOSUB 91000
12081	IF A$="UT" OR INSTR(1,A$," UT ")>0 OR FNL$(A$,3)="UT " OR FNR$(A$,3)=" UT" THEN 12420
12082	IF FNL$(A$,5)="ÖPPNA" THEN 12440
12083	IF FNL$(A$,5)="STÄNG" THEN 12470
12084	IF FNL$(A$,3)="LÄS" THEN 12650
12085	IF FNL$(A$,5)="PUMPA" THEN 12900
12086	IF FNL$(A$,5)="SIMMA" OR FNL$(A$,5)="DUSCH" OR FNL$(A$,4)="BADA" THEN 12890
12087	IF FNL$(A$,4)="FÖLJ" THEN 12910
12088	IF A$="IN" OR INSTR(1,A$," IN ")>0 OR FNL$(A$,3)="IN " OR FNR$(A$,3)=" IN" OR INSTR(1,A$,"IGENOM")>0 THEN 12400
12089	IF FNL$(A$,5)="KASTA" THEN PRINT "Tyvärr har kastarmen gått ur led."\GOTO 12210
12090	IF FNL$(A$,4)="INFO" THEN 12770
12091	IF FNL$(A$,3)="ÅT" AND C$<>"" THEN A$=C$ \ GOTO 12214
12092	IF FNL$(A$,5)="BEGRA" THEN 12510
12093	IF FNL$(A$,9)="KOPPLA IN" THEN 12140
12094	IF FNL$(A$,9)="KOPPLA UT" OR FNL$(A$,9)="KOPPLA UR" THEN 12160
12095	IF A$="SPARA" THEN 80000'           &&&&&
12096	IF FNL$(A$,5)="ÅTERS" THEN 80200'   &&&&&
12097	IF FNL$(A$,4)="LOGG" THEN 12950'    &&&&&
12098	FOR I=1 TO A(0)
12099	IF A$(I,1)="" THEN 12103
12100	IF FNL$(A$,5)=FNL$(A$(I,2),5) OR A$=A$(I,2) THEN 12600
12101	IF FNL$(A$,5)=FNL$(A$(I,3),5) OR A$=A$(I,3) THEN 12600
12103	NEXT I
12104	GOTO 12999
12120	IF S(33)=1 THEN PRINT"Bollen är inte pumpad."\GOTO 12210
12122	IF Z=39 AND S(48)<1 THEN X=13 \ GOTO 12999
12123	PRINT "Du sparkar bollen så hårt att den försvinner."
12124	IF A(20)=1 THEN S(1)=S(1)-1
12125	A(20)=INT(RND*92)+9
12126	GOTO 12210
12130	IF INSTR(A$,"VATTEN")>0 OR INSTR(A$,"VATTNET")>0 THEN 12890
12132	IF S(36)<>0 THEN 12057
12134	IF C$="UPP" OR C$="UPPÅT" THEN X=1 ELSE X=2
12136	GOTO 12999
12140	IF J(Z)<>1 AND S(44)<>Z THEN PRINT "Det finns ingen jack här." \ GOTO 12210'KOPPLA IN
12142	IF LEN(A$)>10 THEN A$=FNM$(A$,11) ELSE A$=FNC$(FNI$("Vad vill du koppla in ?"))
12144	IF FNL$(A$,5)="TELEF" THEN I=25 ELSE I=0
12146	IF FNL$(A$,5)="FÖRLÄ" OR FNL$(A$,5)="SLADD" THEN I=30
12148	IF I=0 THEN PRINT "Det kan man inte koppla in." \ GOTO 12210
12150	GOTO 7030
12160	IF LEN(A$)>10 THEN A$=FNM$(A$,11) ELSE 12170'KOPPLA UR
12162	IF FNL$(A$,5)="TELEF" THEN I=25 ELSE I=0
12164	IF FNL$(A$,5)="FÖRLÄ" OR FNL$(A$,5)="SLADD" THEN I=30
12166	IF (I=30 AND S(44)=Z) OR (I>0 AND J(Z)=1) THEN 6410
12168	PRINT "Det finns inget inkopplat i jacken." \ GOTO 12210
12170	IF S(44)=Z THEN I=30 \ GOTO 6410
12172	IF J(Z)<>1 THEN PRINT "Det finns ingen jack här." \ GOTO 12210
12174	IF A(25)=Z THEN I=25 \ GOTO 6410
12176	IF A(30)=Z THEN I=30 \ GOTO 6410
12178	PRINT "Ingenting är inkopplat i jacken." \ GOTO 12210
12200	REM'XXXXX ALLMÄN GOSUBRUTIN XXXXXX
12201	GOSUB 6000
12202	PRINT
12203	IF S1<2 THEN A$=FNI$("") \ PRINT
12204	GOSUB 12000
12208	RETURN
12210	PRINT'XXXX INMATNINGSRUTIN XXXX
12211	IF S(49)=0 AND S(30)=Z AND Z<>96 THEN X1=1 \ GOTO 30000
12212	IF S<9 AND Z=60 THEN 12999
12213	A$=FNI$("")
12214	PRINT
12215	IF S(36)=1 THEN 8600 ELSE 12000
12220	IF A(10)=5 OR A(10)=53 THEN PRINT "Ingenting händer." \ GOTO 12210
12223	IF A(10)=1 THEN 12226
12224	IF Z=53 THEN PRINT "Nu hänger lagerkransen på väggen." ELSE PRINT "Ok."
12225	A(10)=53 \ GOTO 12210
12226	S(1)=S(1)-1 \ A(10)=53
12227	IF Z=53 THEN 12224
12228	PRINT "Lagerkransen försvinner." \ GOTO 12210
12230	IF A(21)<>1 THEN PRINT "Du har ingenting du kan gräva med." \ GOTO 12210
12232	IF Z<>77 THEN PRINT "Marken är för hård." \ GOTO 12210
12234	IF S(20)=1 THEN PRINT "Platsen är redan helt utgrävd." \ GOTO 12210
12236	X=13 \ GOTO 12999
12240	IF FNL$(C$,5)="GUBBE" OR (C$="" AND S(30)=Z) THEN 30050
12242	IF FNL$(C$,4)="VAKT" OR (C$="" AND (A(29)=Z OR A(29)=1)) THEN 28010
12248	PRINT "Det finns inget du kan döda här." \ GOTO 12210
12255	IF C$<>"" THEN A$=C$ \ GOTO 12214
12260	PRINT "Åt vilket håll?"
12261	A$=FNI$("")
12262	GOTO 12214
12270	IF FNL$(C$,5)="BRÄNN" THEN 12280
12272	IF FNL$(C$,5)="VATTE" THEN 12282
12274	IF C$<>"" THEN GOSUB 11000 \ GOTO 12210
12276	C$=FNI$("Drick vad ?")
12278	C$=FNC$(C$) \ GOTO 12270
12280	IF A(18)=1 AND S(31)=0 THEN 12310 ELSE 12306
12282	IF A(19)=1 AND S(32)=0 THEN 12292
12284	IF Z=25 OR Z=33 OR Z=49 OR Z=50 OR Z=66 OR Z=70 THEN 12296
12286	IF Z=72 OR Z=74 OR Z=78 OR Z=79 OR Z=83 OR Z=87 OR Z=88 THEN 12296
12288	IF Z=91 THEN PRINT "Du dricker ur vattenfallet." \ GOTO 12300
12290	PRINT "Jag ser inget VATTEN här." \ GOTO 12210
12292	PRINT "Du dricker ur vattenflaskan."
12294	S(32)=1 \ GOTO 12300
12296	PRINT "Du dricker ur sjön."
12300	PRINT "Klunk...klunk...klunk......AHHHH!"
12302	GOTO 12210
12306	PRINT "Jag ser inget BRÄNNVIN här." \ GOTO 12210
12310	PRINT "Du dricker ur brännvinsflaskan."
12312	PRINT "Klunk...klunk...klunk......HICK	!"
12314	FOR I=1 TO 9
12316	S=SLEEP(3)
12318	PRINT TAB(INT(RND*66)+1);"HICK	!"
12320	NEXT I
12322	PRINT \ S(31)=1
12324	PRINT "Nu hoppas jag att vi har nyktrat till så pass att vi kan fortsätta!"
12326	PRINT \ GOTO 12210
12340	IF FNL$(C$,5)="GUBBE" OR (C$="" AND S(30)=Z) THEN 30010
12341	IF FNL$(C$,4)="VAKT" OR (C$="" AND (A(29)=Z OR A(29)=1)) THEN 12360
12342	IF INSTR(1,C$,"BRÄNN")>0 THEN 12306
12344	IF INSTR(1,C$,"VATTE")>0 THEN 12380
12346	IF C$="FYLL" OR INSTR(1,C$,"FLASKA")>0 THEN 12350
12348	GOSUB 11000 \ GOTO 12210
12350	IF A(18)=1 OR A(19)=1 THEN C$=FNI$("Fyll med vad ?")\C$=FNC$(C$)\GOTO 12340
12354	PRINT "Du har ju ingen flaska!" \ GOTO 12210
12360	IF A(29)<>Z AND A(29)<>1 THEN PRINT "Jag ser ingen VAKT här."\GOTO 12210
12361	IF S(6)=2 THEN PRINT "Vakten är ju död." \ GOTO 12210
12362	IF S(6)=3 THEN PRINT "Han sover för djupt." \ GOTO 12210
12364	IF A(18)<>1 THEN PRINT "Du har inget att fylla honom med." \ GOTO 12210
12366	IF S(31)=1 THEN PRINT "Din brännvinsflaska är tom." \ GOTO 12210
12368	S(31)=1 \ S(51)=S(50)
12370	PRINT "Vakten dricker upp ditt brännvin i en enda klunk."
12372	IF S(6)=0 THEN S(6)=1 \ GOTO 12210
12374	PRINT "Den nu redlöst fulle vakten ramlar ihop i en hög på golvet och somnar."
12376	S(6)=3 \ A(29)=Z
12378	GOTO 12210
12380	IF A(19)<>1 THEN PRINT "Du bär ingen vattenflaska som du kan fylla."\GOTO 12210
12382	IF S(32)=0 THEN PRINT "Din vattenflaska är så full den kan bli." \ GOTO 12210
12384	IF Z=25 OR Z=33 OR Z=49 OR Z=50 OR Z=66 OR Z=70 OR Z=72 THEN 12390
12386	IF Z=74 OR Z=78 OR Z=79 OR Z=83 OR Z=87 OR Z=88 OR Z=91 THEN 12390
12388	GOTO 12290
12390	PRINT "Du fyller vattenflaskan med vatten från ";
12392	IF Z=91 THEN PRINT "vattenfallet." ELSE PRINT "sjön."
12394	S(32)=0 \ GOTO 12210
12400	IF Z=81 THEN X=3
12402	IF Z=50 THEN X=4
12404	IF Z=99 OR Z=55 THEN X=5
12406	IF Z=30 THEN S(23)=1 \ PRINT "I garderoben hittar du ett kassaskåp." \ GOTO 12210
12408	IF X>0 THEN 12999 ELSE 12089
12420	IF Z=8 OR Z=51 OR Z=100 THEN X=6
12428	IF X>0 THEN 12999 ELSE 12082
12440	IF Z=81 OR Z=8 THEN 12450
12442	IF Z=30 THEN 12456
12444	IF Z=62 AND S(7)=0 THEN PRINT "Porten är låst." \ GOTO 12210
12448	GOTO 12083
12450	IF S(19)=1 THEN PRINT "Dörren är ju redan öppen!"
12452	IF S(19)<>1 THEN PRINT "Dörren öppnas med ett gnäll	."
12454	S(19)=1 \ X=19 \ GOTO 12999
12456	IF INSTR(1,A$,"GARDE")>0 OR (C$="" AND S(23)=0) THEN 12466
12458	IF INSTR(1,A$,"KASSA")=0 AND C$<>"" THEN 12083
12460	IF Z=31 THEN PRINT "Kassaskåpet är redan öppet." \ GOTO 12210
12464	PRINT "Dörren är utan handtag och lås." \ GOTO 12210
12466	IF S(23)=1 THEN PRINT "Garderoben är redan öppen." \ GOTO 12210
12468	PRINT "Du öppnar garderoben och hittar ett litet kassaskåp där."
12469	S(23)=1 \ GOTO 12210
12470	IF Z=30 THEN 12480
12472	IF Z=31 THEN 12486
12478	GOTO 12084
12480	IF S(23)=0 THEN PRINT "Garderoben är redan stängd." \ GOTO 12210
12482	PRINT "Ok." \ S(23)=0 \ GOTO 12210
12486	IF INSTR(1,A$,"GARDE")>0 OR (C$="" AND S(23)=1) THEN 12494
12488	IF INSTR(1,A$,"KASSA")=0 AND C$<>"" THEN 12084
12490	PRINT "Kassaskåpet stängs sakta."
12492	Z=30 \ GOTO 12999
12494	PRINT "Kassaskåpet och garderoben stängs."
12496	S(23)=0 \ GOTO 12492
12510	IF Z<>63 AND Z<>61 THEN PRINT "Marken är för hård!" \ GOTO 12210
12512	IF FNL$(C$,3)<>"LIK" AND FNL$(C$,4)<>"VAKT" AND (C$="" AND A(22)<>1) THEN 12526
12514	IF A(29)=1 OR A(29)=Z THEN PRINT "Du kan inte begrava en levande!" \ GOTO 12210
12516	IF A(22)<>1 AND A(22)<>Z THEN PRINT "Du har inget sånt att begrava!" \ GOTO 12210
12518	IF A(22)=63 THEN PRINT "Liket är redan begravt!" \ GOTO 12210
12520	IF A(22)=1 THEN S(1)=S(1)-1
12522	A(22)=63 \ S(2)=S(2)+25 \ S(52)=S(50)
12524	PRINT "Ok." \ GOTO 12210
12526	PRINT "Man kan bara begrava lik!" \ GOTO 12210
12550	I=INSTR(A$," ")'================== SKRIK
12551	IF I=0 OR I=LEN(A$) THEN PRINT "AAAAAAARRRRRRRRRR	GHHHHH	H!" ELSE PRINT "Ok. ";FNM$(A$,I+1)
12553	GOTO 12210
12555	'====================================================SVÄRORD============
12557	PRINT "Vilket språk!"
12559	GOTO 12210
12570	'==========================================VÄNTA===========STANNA=======
12572	PRINT"Ok.";FNS$("väntar",10)
12574	IF Z=37 THEN 12999 ELSE PRINT "Så där ja!"
12576	GOTO 12210
12580	IF S(21)>0 THEN PRINT"Du kan inte sparka något med vrickade fötter!"\GOTO 12210
12582	IF (FNL$(C$,4)="BOLL" OR C$="") AND (A(20)=Z OR A(20)=1) THEN 12120
12584	PRINT"AJ! Du vrickar dina fötter."
12586	S(21)=S(50)
12588	GOTO 12210
12590	IF Z<>23 THEN PRINT "Ok." \ GOTO 12210
12592	PRINT "Oj! Du ramlar själv ner i toaletten." \ A$="SPOLA"
12594	GOTO 12999
12600	PRINT "Vad vill du göra med ";A$(I,4);"?"
12601	A1$=FNI$("") \ A$=A1$+" "+A$(I,1)
12610	GOTO 12214
12650	IF INSTR(1,A$,"KATAL")>0 THEN 12670
12652	IF INSTR(1,A$,"KONTR")>0 THEN 12700
12654	IF INSTR(1,A$,"TRILO")>0 THEN 12710
12655	IF INSTR(1,A$,"LOGGF")>0 THEN 12975'&&&&&
12656	IF INSTR(1,A$,"KLOCK")>0 THEN 12740
12657	IF INSTR(1,A$,"GRAV")>0 OR INSTR(1,A$,"STEN")>0 THEN 12750
12658	IF A$<>"LÄS" THEN GOSUB 11000 \ GOTO 12210
12660	A$=FNI$("Vad vill du läsa ?") \ A$=FNC$(A$) \ GOTO 12650
12670	IF A(23)<>1 AND A(23)<>Z THEN PRINT "Jag ser ingen KATALOG här." \ GOTO 12210
12672	PRINT
12674	PRINT "    TELEFONKATALOG ÖVER STUGAN"
12676	PRINT "Telefonnr:    Abonnent:"
12678	PRINT "   000        Stugas televerk"
12680	PRINT "   100        Stugan"
12682	PRINT "   307        Hissreparatören"
12684	PRINT "   323        Glasmästaren"
12686	PRINT "   405        Personalköket"
12688	PRINT "   481        Vakten"
12690	PRINT "   999        Larmcentralen"
12698	GOTO 12210
12700	IF A(9)<>1 AND A(9)<>Z THEN PRINT "Jag ser inget KONTRAKT här."\GOTO 12210
12702	PRINT "Tyvärr är kontraktet skrivet med Kermits oläsliga handstil."
12704	PRINT \ GOTO 12210
12710	IF A(8)<>1 AND A(8)<>Z THEN PRINT "Jag ser ingen TRILOGI här." \ GOTO 12210
12712	PRINT \ PRINT
12714	PRINT "Tre ringar för älvkungarnas makt högt i det blå,"
12716	PRINT "sju för dvärgarnas furstar i salarna av sten,"
12718	PRINT "nio för de dödliga, som köttets väg skall gå,"
12720	PRINT "en för Mörkrets herre i ondskans dunkla sken"
12722	PRINT "i Mordorslandets hisnande gruva."
12724	PRINT \ PRINT "En ring att sämja dem,"
12726	PRINT "en ring att främja dem,"
12728	PRINT "en ring att djupt i mörkrets"
12730	PRINT "vida riken tämja dem -"
12732	PRINT "i Mordors land, där skuggorna ruva..."
12734	PRINT \ PRINT
12736	GOTO 12210
12740	IF A(6)<>1 AND A(6)<>Z THEN PRINT "Jag ser ingen KLOCKA här."\GOTO 12210
12742	PRINT TIME$
12744	GOTO 12210
12750	IF Z<>61 THEN PRINT "Jag ser ingen GRAVSTEN här." \ GOTO 12210
12752	IF LEN(W$(6))=0 THEN PRINT "Gravstenen är tom." \ GOTO 12210
12754	PRINT "Här vilar sej ";W$(6);"." \ PRINT
12756	PRINT W$(6);" försvann in i ett okänt hus klockan ";W$(3);
12757	IF W$(4)=DATE$ THEN PRINT ELSE PRINT " ";W$(4)
12758	PRINT "och sågs aldrig mer."
12760	PRINT \ GOTO 12210
12770	PRINT "INFORMATION OM VISSA KOMMANDON:"
12772	PRINT "Förflyttning inomhus:"
12774	PRINT "UPPÅT, NERÅT, FRAMÅT, BAKÅT, VÄNSTER, HÖGER (U, N, F, B, V, H)"
12776	PRINT "Förflyttning utanför huset:"
12778	PRINT "NORR, SÖDER, VÄSTER, ÖSTER (N, S, V, Ö) NV, NÖ, SV, SÖ"
12780	PRINT \ PRINT "INVENT skriver allt man bär på"
12781	PRINT "HJÄLP  ger ibland hjälp"
12782	PRINT "POÄNG  visar hur många poäng man har fått"
12783	PRINT "TITTA  ger hela rumsbeskrivningen"
12784	PRINT "SPARA  sparar spelat på fil"'                         &&&&&
12785	PRINT "ÅTERSKAPA  hämtar tillbaka spelet"'                   &&&&&
12787	PRINT "LOGGA  skriver en loggfil med alla kommandon man ger"'&&&&&
12788	PRINT "LÄS LOGGFIL  utför kommandona i en loggfil"'          &&&&&
12789	PRINT "SLUTA  slutar" \ PRINT \ GOTO 12210
12800	IF A(25)=1 AND (J(Z)=1 OR S(44)=Z) THEN PRINT "Du HÅLLER ju i telefonsladden."
12802	IF A(25)<>1 AND A(25)<>Z THEN PRINT "Jag ser ingen TELEFON här."
12804	IF J(Z)<>1 AND S(44)<>Z THEN PRINT "Jag ser ingen TELEFONJACK här."
12806	IF (J(Z)<>1 AND S(44)<>Z) OR A(25)<>Z THEN 12210
12808	IF C$="" THEN C$=FNI$("Ring vart:")
12810	IF INSTR(1,C$,"000")>0 THEN 27250
12812	IF INSTR(1,C$,"100")>0 THEN 27600
12814	IF INSTR(1,C$,"307")>0 OR INSTR(1,C$,"323")>0 THEN 27620
12816	IF INSTR(1,C$,"405")>0 THEN 27200
12818	IF INSTR(1,C$,"481")>0 THEN 27630
12821	IF INSTR(1,C$,"900")>0 THEN 27400
12822	IF FNC$(C$)="HEM" THEN 12835
12826	PRINT "Du hör en röst säja:"
12828	PRINT "- Ingen abonnent på det numret."
12830	GOTO 12210
12835	IF W$(6)="" THEN PRINT "Du hör din egen röst:  - Jag är inte hemma än!" \ GOTO 12210
12836	PRINT "Du hör en röst säja:"
12837	PRINT "- Detta är "W$(6)"s telefonsvarare. "W$(6)" är inte hemma."
12838	GOTO 12210
12840	IF S(30)<>Z THEN PRINT "Du kan inte ge något till någon här."\ GOTO 12210
12842	IF I=10 OR I=19 THEN 7030
12844	IF INSTR(1,C$,"VATTE")>0 THEN 30010
12846	PRINT "Gubben tar inte emot det." \ GOTO 12210
12850	IF A(24)<>1 THEN PRINT "Du har inget att blända med." \ GOTO 12210
12851	IF FNL$(C$,5)="GUBBE" OR (C$="" AND S(30)=Z) THEN 12860
12852	IF FNL$(C$,4)="VAKT" OR (C$="" AND (A(29)=Z OR A(29)=1)) THEN 12880
12854	PRINT "Du kan inte blända någon här." \ GOTO 12210
12860	IF S(30)<>Z THEN PRINT "Jag ser ingen GUBBE här." \ GOTO 12210
12864	IF A(19)=0 THEN PRINT "Du försöker blända gubben men han häller"
12866	IF A(19)=0 THEN PRINT "vattenflaskan som skydd." \ GOTO 12210
12868	IF S(49)=0 OR S(49)=2 OR S(30)=96 THEN 30002
12870	S(49)=2 \ PRINT "Du bländar den stackars gubben med lampan." \ GOTO 12210
12880	IF (A(29)=Z OR A(29)=1) AND S(6)<>2 THEN PRINT "Du klarar inte av att blända vakten."\GOTO 12210
12881	IF S(6)=2 THEN PRINT "Vakten är död." ELSE PRINT "Jag ser ingen VAKT här."
12882	GOTO 12210
12890	IF Z=25 OR Z=33 OR Z=49 OR Z=50 OR Z=66 OR Z=70 THEN X=10 \ GOTO 12999
12892	IF Z=72 OR Z=74 OR Z=78 OR Z=79 OR Z=83 OR Z=87 OR Z=88 THEN X=10\GOTO 12999
12893	IF Z=91 THEN PRINT "Vattenfallets vatten är alldeles för kallt."\GOTO 12210
12894	PRINT "Här finns det inget vatten." \ GOTO 12210
12900	IF A(20)<>1 THEN PRINT "Du har inget att pumpa."
12902	IF A(16)<>1 THEN PRINT "Du har inget att pumpa med."
12904	IF A(20)=1 AND S(33)=0 THEN PRINT "Din boll är redan pumpad."
12906	IF A(16)=1 AND A(20)=1 AND S(33)=1 THEN PRINT "Ok." \ S(33)=0
12908	GOTO 12210
12910	IF INSTR(1,A$,"RÖVAR")>0 THEN PRINT "Jag ser ingen RÖVARE här." \ GOTO 12210
12912	IF INSTR(1,A$,"GUBBE")>0 THEN 12920
12914	IF INSTR(1,A$,"EFTER")>0 THEN PRINT "Jag ser ingen du kan följa efter."\GOTO 12210
12916	IF (INSTR(1,A$,"RÅD")>0 OR INSTR(1,A$,"THORVALD")>0) AND Z=59 THEN 12924
12918	GOTO 12088
12920	IF S(30)=Z THEN PRINT "Gubben sitter ju här!" \ GOTO 12210
12922	PRINT "Jag ser ingen GUBBE här." \ GOTO 12210
12924	PRINT "Du ska inte ha någon fördel bara för att Stugrådet råkar ha samman-"
12926	PRINT "träde när du ramlar in. Du får försöka hitta skattkammaren själv."
12928	PRINT "(Förresten har dom redan försvunnit!)" \ GOTO 12210
12950	IF M2%=1% THEN GOTO 12970'&&&&&
12951	PRINT "Vad heter loggfilen"; \ INPUT LINE M2$'&&&&&
12952	ON ERROR GOTO 12962'&&&&&
12954	OPEN M2$ FOR OUTPUT AS FILE #2'&&&&&
12956	ON ERROR GOTO 97000'&&&&&
12958	PRINT "Nu loggas alla kommandon på filen ";M2$'&&&&&
12960	M2%=1% \ W$=CHR$(3) \ GOTO 12210'&&&&&
12962	RESUME 12964'&&&&&
12964	ON ERROR GOTO 97000'&&&&&
12966	PRINT "? Jag kan inte öppna ";M2$'&&&&&
12968	GOTO 12210'&&&&&
12970	M2%=0% \ CLOSE 2'&&&&&
12972	PRINT "Loggningen på ";M2$;" avslutad."'&&&&&
12974	GOTO 12210'&&&&&
12975	PRINT "Vad heter loggfilen"; \ INPUT LINE M3$'&&&&&
12976	IF M3$="" THEN 12210 ELSE IF M3%=1% THEN CLOSE 3 \ M3%=0%'&&&&&
12977	ON ERROR GOTO 12985'&&&&&
12979	OPEN M3$ FOR INPUT AS FILE #3'&&&&&
12981	ON ERROR GOTO 97000'&&&&&
12983	M3%=1% \ GOTO 12210'&&&&&
12985	RESUME 12987'&&&&&
12987	PRINT "? Jag kan inte öppna ";M3$'&&&&&
12988	ON ERROR GOTO 97000'&&&&&
12989	GOTO 12210'&&&&&
12999	IF S(30)=Z THEN 30000 ELSE RETURN
13000	Z=58'XXX FARSTUN XXXXX
13002	PRINT "Du är i farstun, ett litet rum med en dörr bakom dej"
13003	PRINT "och en stor portal rakt fram."
13004	GOSUB 12200
13005	IF X1=1 THEN 13000
13006	IF X>4 THEN ON X-4 GOTO 13173,7570,13010
13008	GOSUB 11000
13009	GOTO 13000
13010	IF S(6)>0 OR A(29)<>Z THEN 13008
13012	PRINT "Det finns en sak som kan påverka vakten."
13014	S(2)=S(2)-10
13016	GOTO 13000
13172	GOSUB 11000
13173	Z=62'XXX PORTEN XXX
13175	PRINT "Du står vid en jättelik, utsmyckad port."
13176	GOSUB 12200
13177	IF X>5 THEN ON X-5 GOTO 13000,13195
13178	IF X=5 AND S(7)=1 THEN 13220
13179	IF X=5 THEN PRINT "Porten är låst." \ GOTO 13173
13180	IF X1=1 THEN 13173
13184	IF FNL$(A$,3)<>"LÅS" THEN 13172
13186	IF INSTR(1,A$,"UPP")>0 THEN 13200
13188	IF S(7)=0 THEN PRINT "Porten är redan låst." \ GOTO 13173
13190	PRINT "Det går inte utan nycklar." \ GOTO 13173
13195	IF S(7)<>0 OR S(26)=1 THEN 13172
13196	IF A(26)<>2 THEN PRINT "Vakten orkar låsa upp porten, men han har inga nycklar."
13197	IF A(26)=2 THEN PRINT "Ta hit vakten och lås upp porten."
13198	S(2)=S(2)-15 \ GOTO 13173
13200	IF S(7)=1 THEN PRINT "Porten är redan upplåst." \ GOTO 13173
13202	IF A(26)=1 THEN PRINT "Du orkar inte vrida om nyckeln själv." \ GOTO 13173
13204	IF A(29)<>1 OR A(26)<>2 THEN PRINT "Det går inte." \ GOTO 13173
13206	PRINT "Vakten låser upp porten."
13208	PRINT "Han tittar på nycklarna ett slag, innan han äter upp dom."
13218	S(7)=1 \ A(26)=0 \ S(2)=S(2)+10 \ GOTO 13173
13220	IF S(26)=1 THEN 13235 ELSE S(26)=1
13222	PRINT "Du har kommit in i matrummet. Här har Stugrådet sammanträde."
13223	PRINT "Just nu pratar ordföranden, Thorvald:"
13224	GOSUB 700
13225	PRINT " - Vi har samlats till detta krismöte för att diskutera den"
13226	PRINT "   allvarliga frågan om stugforskarnas kvalitet. Jag, och många"
13227	PRINT "   med mej, anser att stugforskarnas kvalitet genomgående har"
13228	PRINT "   försämrats."
13229	PRINT "Kimmo:"
13230	PRINT " - Jag håller med dej. Titta bara på den som kom in nu! Jag"
13231	PRINT "   föreslår att vi fortsätter vårt sammanträde i skattkammaren."
13232	PRINT \ PRINT "Hela församlingen reser sej och ger sej iväg."
13233	PRINT \ PRINT
13235	Z=59 \ PRINT "Du är i husets matrum. Väggarna är målade i rött och guld."
13237	IF S(15)=0 THEN PRINT "En trappa leder uppåt."
13238	IF S(15)=1 THEN PRINT "En trappa har gått uppåt, men är nu obrukbar."
13241	GOSUB 12200
13244	IF X<>0 THEN ON X GOTO 13247,13245,13245,13245,13245,13173,13245
13245	GOSUB 11000
13246	GOTO 13235
13247	IF S(15)=0 AND NOT A(1)=1 THEN 40000
13248	IF S(15)=1 THEN 13252
13249	PRINT "Trappan rasar ihop."
13250	S(15)=1
13251	GOTO 13235
13252	PRINT "Trappan är avspärrad av stugas gatukontor."
13253	GOTO 13235
14000	Z=64'XXXXX MÖRKA GÅNGEN XXXXX
14004	PRINT "Du är i en mörk gång. Framåt är en öppning."
14008	PRINT "Till vänster skymtar man en grind och till höger en panna."
14010	PRINT "Det finns ett hål i golvet och en gång går snett bakåt-uppåt."
14012	GOSUB 12200
14018	IF X1=1 THEN 14000
14020	IF X<>0 THEN ON X GOTO 9490,1909,14030,14100,8000,9490,14022
14022	GOSUB 11000
14024	PRINT "Du är i en mörk gång." \ GOTO 14012
14030	PRINT "Du går genom en grind som går i lås bakom dej."
14032	GOTO 20040
14034	PRINT "Grinden öppnar sej och du går in."
14036	PRINT "BA	NG!!  Grinden stängs bakom dej!"
14038	GOTO 14000
14099	GOSUB 11000
14100	Z=65'XXXXX PANNRUMMET XXXXX
14106	PRINT "Du är i Pannrummet, en trång gång går snett uppåt-framåt"
14107	PRINT "och en går åt vänster. Till höger fortsätter Pannrummet."
14112	GOSUB 12200
14121	IF X=0 THEN 14099
14124	ON X GOTO 14139,14099,15050,2008,14139,14099,14099
14139	IF A(1)<>1 THEN 14000
14142	PRINT "Nå'nting du bär på tar emot. Skriv INVENT och släpp det."
14145	GOTO 14100
14998	GOSUB 11000
15000	Z=10 \ S(10)=S(10)+1'XXXXX KÄLLAREN XXXXX
15004	IF S(10)<3 OR S(10)>7 THEN 15018
15006	PRINT "Du är i källaren."
15008	GOSUB 12200
15012	IF X1=1 THEN 15018
15013	IF X=0 THEN 14998
15014	ON X GOTO 16000,14998,15300,16500,1500,14998,14998
15018	PRINT "Du är i källaren. Ett kallt och rått rum med tre dörrar"
15020	PRINT "(vänster,höger och framåt) och en gång uppåt."
15024	IF S(10)>8 THEN S(10)=4
15026	GOTO 15008
15050	Z=9 \ S(9)=S(9)+1 \ S(45)=2'XXXXX ÅP-RUMMET XXXXX
15056	IF S(9)<3 OR S(9)>7 THEN 15066
15058	PRINT "Du är i ÅP-rummet."
15060	GOSUB 12200
15062	IF X<>0 THEN ON X GOTO 15076,15064,15386,14100,1500,15078,15064
15064	GOSUB 11000
15066	IF S(9)>8 THEN S(9)=4
15068	PRINT "Du är i ett stort rum som heter ÅP-rummet."
15070	PRINT "Dörrar leder till vänster och höger men"
15072	PRINT "man kan också gå framåt."
15074	GOTO 15060
15076	PRINT "Tror du att du kan flyga?" \ GOTO 15058
15078	PRINT "Du kan inte gå bakåt!" \ GOTO 15058
15200	GOSUB 6000'XXXXX ALLMÄN GOSUBRUTIT XXXXX
15202	PRINT
15203	IF S1<2 THEN A$=FNI$("") \ PRINT
15204	GOSUB 8600
15205	RETURN
15299	GOSUB 11000
15300	Z=11'XXX Hilbertrummet XXX
15302	PRINT "Du är i Hilbertrummet, ett rum med fyra dörrar och hål i taket och golvet."
15304	IF A(17)=11 THEN PRINT "En stege är uppställd mot hålet i taket."
15306	GOSUB 12200
15308	IF X=0 OR X>6 THEN 15299
15310	ON X GOTO 15312,17000,16000,15000,9145,16500
15312	IF A(17)=11 THEN 25000
15314	PRINT "Du når inte upp till hålet." \ GOTO 15300
15349	GOSUB 11000
15350	Z=46 'XXX TRAPPRUM 1 XXXXXZ=46 XXX
15351	PRINT "Du är i ett rum med två rulltrappor."
15352	PRINT "Det finns en dörr bakom dej."
15354	IF S(17)=1 THEN PRINT "Den nedåtgående rulltrappan är avspärrad av Stugas gatukontor."
15355	IF S(18)=1 THEN PRINT "Den uppåtgående rulltrappan är avspärrad av Stugas satukontor."
15356	GOSUB 12200
15357	IF X=6 THEN 9991
15358	IF X=1 AND S(18)=0 THEN 15370
15359	IF X=2 AND S(17)=0 THEN 15386 ELSE 15349
15369	GOSUB 11000
15370	Z=47'XXX TRAPPRUM 2 XXX
15372	PRINT "Du är i ett rum med en nedåtgående rulltrappa och en dörr åt höger."
15373	IF S(18)=1 THEN PRINT "Rulltrappan är avspärrad av Stugas gatukontor."
15374	GOSUB 12200
15375	IF X=4 THEN 9035
15376	IF A(1)=1 AND X=2 AND S(18)=0 THEN 15382
15377	IF X=2 AND S(18)=0 THEN 15350 ELSE 15369
15382	PRINT "Just när du går fram mot rulltrappan, stannar den och en"
15383	PRINT "gubbe springer fram och spärrar av den."
15384	S(18)=1 \ GOTO 15370
15385	GOSUB 11000
15386	Z=48'XXX TRAPPRUM 3 XXXXX
15388	PRINT "Du är i ett rum med en uppåtgående rulltrappa och en dörr framåt."
15390	IF S(17)=1 THEN PRINT "Rulltrappan är avspärrad av Stugas gatukontor."
15392	GOSUB 12200
15394	IF X=5 THEN 15050
15396	IF X<>1 OR S(17)<>0 THEN 15385 ELSE IF A(1)<>1 THEN 15350
15398	PRINT "Just när du går fram mot rulltrappan, stannar den och en"
15399	PRINT "gubbe springer fram och spärrar av den."
15400	S(17)=1 \ GOTO 15386
15425	Z=90'XXXXX TRAPPRUM 4 XXXXX
15427	PRINT "Dörren öppnar sej och du går in i ett rum"
15428	PRINT "med två trappor och en dörr bakåt."
15429	GOSUB 12200
15430	IF X>0 THEN ON X GOTO 16000,9145,15431,15431,15431,15434,15438
15431	GOSUB 11000
15432	PRINT "Du är i trapprummet." \ Z=90
15433	GOTO 15429
15434	IF A(1)<>1 THEN 9991
15435	PRINT "Dörren har gått i baklås."
15436	IF A(26)=1 OR A(26)=90 THEN PRINT "Din nyckel passar inte i låset!"
15437	GOTO 15432
15438	IF A(1)=1 THEN PRINT "TIPS!! Något du bär hindrar dej att gå bakåt!" \ GOTO 15432
15439	GOTO 15431
16000	Z=12 \ S(12)=S(12)+1'XXXXX VINDEN XXXXX
16012	IF S(12)>2 AND S(12)<8 THEN PRINT "Du är på vinden." \ GOTO 16055
16020	PRINT "Du är på vinden, ett litet skrymsle högst ner i huset."
16030	PRINT "Härifrån kan man gå överallt."
16032	PRINT "På väggen står det: SESAM"
16040	IF RND<0.5 THEN PRINT "Någon säjer:  - Du kom hit klockan ";W$(3);" ";W$(4)
16045	IF S(12)>8 THEN S(12)=4
16055	GOSUB 12200
16057	IF X1=1 THEN 16020
16058	IF X>0 THEN ON X GOTO 15000,15432,9000,15300,17000,16500,16060
16060	GOSUB 11000
16065	PRINT "Du är på vinden." \ GOTO 16055
16500	Z=13 \ S(13)=S(13)+1'XXXXX TOMMA RUMMET XXXXX
16512	IF S(13)>2 AND S(13)<8 THEN PRINT "Du är i Tomma rummet." \ GOTO 16530
16515	PRINT "Du är i ett tomt rum. Det finns ett hål i taket och en ribbstol"
16517	PRINT "som leder dit. Dörrar leder åt höger och åt vänster."
16525	IF S(13)>8 THEN S(13)=4
16530	GOSUB 12200
16535	IF X1=1 THEN 16515
16540	IF X>0 THEN ON X GOTO 16000,16545,15000,15300,16545,16545,16545
16545	GOSUB 11000
16550	PRINT "Du är i Tomma rummet." \ GOTO 16530
17000	Z=14 \ S(14)=S(14)+1'XXXXX UNDERLIGA RUMMET XXXXX
17005	IF S(14)<3 OR S(14)>8 THEN 17100
17010	PRINT "Du är i Underliga rummet."
17020	GOSUB 12200
17025	IF X<7 AND X>0 THEN ON X GOTO 17150,17180,17185,17195,17220,17240
17031	IF X1=1 THEN 17100
17032	GOSUB 11000
17033	GOTO 17010
17100	PRINT "Du är i ett underligt rum. Dimslöjor sveper kring dina fötter"
17101	PRINT "och du ser gångar i alla riktningar."
17110	IF S(14)>8 THEN S(14)=4
17120	GOTO 17020
17150	PRINT "Jag är ledsen, men det tar lång tid att komma fram här."
17155	PRINT FNS$("tar mej fram",15)
17160	D=INT(RND*6)+1
17165	IF D=1 THEN 20040
17172	IF D=3 THEN 15050
17175	GOTO 17182
17180	D=INT(RND*4)+1
17181	IF D=4 THEN 40000
17182	PRINT "Du har vindlat runt i en trång gång och kommer tillbaka."
17183	GOTO 17010
17185	D=INT(RND*6)+1
17186	IF D<3 THEN PRINT "Du har en rutten tomat i handen, men den försvinner."
17190	IF D=5 THEN IF A(1)<>1 THEN 9991 ELSE 14100
17191	IF D=6 THEN 14100
17192	GOTO 17182
17195	D=INT(RND*10)+1
17197	IF D>5 AND S(2)>50 THEN 18000
17205	IF D=2 THEN 14100
17210	IF D=3 THEN 8000
17215	GOTO 17182
17220	IF S(3)>0 AND S(41)=1 THEN 9035
17230	IF S(40)=4 THEN 1500
17235	GOTO 9190
17240	D=INT(RND*10)
17245	IF D=2 THEN 15370
17250	GOTO 17182
18000	PRINT "Du är i ZZZZ-rummet. Ett stort schackbräde är ritat på golvet."
18020	IF RND<0.3 OR A(18)<>1 OR S(31)<>1 THEN 18120
18030	PRINT "Fozzi kommer fram ur dunklet, utklädd till kung."
18080	PRINT "Han ser din brännvinsflaska och säjer:"
18081	PRINT "- Det är väl synd att gå omkring här med en tom brännvinsflaska."
18090	PRINT \ PRINT "Han tar fram en fickplunta ur kostymen och fyller på"
18095	S(31)=0
18100	PRINT "din brännvinsflaska."
18105	PRINT "Fozzi mumlar något om en faun och knuffar ut dej ur rummet."
18110	ON INT(RND*3)+1 GOTO 40000,1960,1960
18120	PRINT "Du trampas på tårna av en faun, så du springer ut igen."
18125	GOTO 18110
20000	IF S(2)>50 THEN 20005'XXX BRYGGAN XXXXX
20001	PRINT "Du står på en brygga någonstans i Småland. Bakom din solvärmda rygg"
20002	PRINT "åker man vattenskidor. En kyrkklocka (som du inte ser) slår tolv."
20003	PRINT "Du ser ett hus rakt fram."
20004	GOTO 20006
20005	PRINT "Du är på bryggan och ser ett hus rakt fram."
20006	Z=70
20007	GOSUB 15200
20008	IF S1>0 THEN 20007
20009	IF X1=1 THEN 20000
20010	IF X<>0 THEN ON X GOTO 20030,9361,20200,20013,20020,20013,20011,20013,20070,2107
20011	GOSUB 11000
20012	GOTO 20005
20013	PRINT "Du kan väl inte gå på vattnet?"
20014	GOTO 20005
20020	Z=71'XXXXX SKOG 1 XXXXX
20021	PRINT "Du är i skogen."
20024	GOSUB 15200
20025	IF X<>0 THEN ON X GOTO 20040,20200,20028,20030,20028,20055,20026,20005,20028
20026	GOSUB 11000
20027	GOTO 20020
20028	PRINT "Ett staket hindrar dej att gå ditåt."
20029	GOTO 20020
20030	Z=72'XXXX STRAND 1 XXX Z=72 XXXXX
20031	PRINT "Du är på stranden väster om bryggan."
20032	IF S(53)=1 THEN 20350 ELSE S(53)=S(53)+1
20033	GOSUB 15200
20034	IF X<>0 THEN ON X GOTO 20055,20000,20020,20037,20040,20037,20035,20037,20200,2107
20035	GOSUB 11000
20036	GOTO 20030
20037	PRINT "Du kan väl inte gå på vattnet?"
20038	GOTO 20030
20040	Z=73'XXXXX SKOG MED GRIND XXXXX
20041	PRINT "Du är i skogen, framför en låst grind."
20042	if A(26)=1 THEN PRINT "Dina nycklar passar inte i grinden."
20043	GOSUB 15200
20044	IF A$="IN" THEN PRINT "Grinden är ju låst!"\GOTO 20040
20045	IF FNL$(A$,3)="LÅS" THEN IF A(26)=1 THEN 20042 ELSE PRINT "Det går inte!"\GOTO 20040
20046	IF A$="SESAM" THEN 14034
20047	IF X<>0 THEN ON X GOTO 20050,20020,20050,20055,20050,20050,20048,20030,20050
20048	GOSUB 11000
20049	GOTO 20040
20050	PRINT "Ett staket hindrar dej att gå ditåt!"
20051	GOTO 20040
20054	GOSUB 11000
20055	Z=74'XXX STRAND 2 XXXX Z=74 XXXXX
20056	PRINT "Du är på stranden nordväst om sjön."
20057	GOSUB 15200
20058	IF X1=1 THEN 20061
20059	IF X=0 THEN 20054
20060	ON X GOTO 20063,20030,20040,20155,20063,20063,20054,20065,20020,2107
20061	PRINT "Du är på en strand som fortsätter åt öster. Långt bort i öster"
20062	PRINT "skymtar man en brygga. Åt norr och söder är det skog."
20063	PRINT "Ett staket hindrar dej att gå åt väster, nordväst eller sydväst."
20064	GOTO 20055
20065	PRINT "Du kan väl inte gå på vattnet?" \ GOTO 20055
20070	Z=75'XXXXX SKOG 2 XXXXX
20071	PRINT "Du är i skogen. Åt väster ser du ett hus."
20073	GOSUB 15200
20074	IF X<>0 THEN ON X GOTO 20200,20085,20077,9361,20077,20000,20075,9424,20077
20075	GOSUB 11000
20076	GOTO 20070
20077	PRINT "Ett staket hindrar dej att gå ditåt."
20078	GOTO 20070
20085	Z=76'XXXXX SKOG 3 XXXXX
20086	PRINT "Du är i skogen."
20088	GOSUB 15200
20089	IF X<>0 THEN ON X GOTO 20070,20092,20094,9424,20092,9361,20090,20105,20092
20090	GOSUB 11000
20091	GOTO 20085
20092	PRINT "Ett elektriskt stängsel hindrar dej att gå ditåt."
20093	GOTO 20085
20094	PRINT "Du går runt, runt. Efter ett tag märker du att du gått vilse."
20095	PRINT "Du går över en äng och ett högt berg."
20096	PRINT \ PRINT
20097	PRINT "Plötsligt hittar du ";
20098	D=INT(RND*5)
20099	IF D<4 THEN 20102
20100	PRINT "en stig som du följer tillbaka."
20101	GOTO 20085
20102	PRINT "ett hål som du hoppar ner genom."
20103	PRINT \ GOTO 8000
20105	PRINT "Du kryper igenom ett hål i staketet."
20107	Z=77'XXX OVANFÖR RÖVARGÖMSTÄLLET XXX
20108	PRINT "Du är i skogen."
20110	IF S(20)<1 THEN PRINT "Det ser ut som något har grävt här tidigare."
20112	IF S(20)=1 THEN PRINT "Det finns en grop här."
20114	GOSUB 20500
20116	IF X=2 AND S(20)=1 THEN 20143
20117	IF X1=1 THEN 20107
20118	IF X<13 THEN 20085
20120	IF S(20)<0 THEN S(2)=S(2)+10
20122	S(20)=1
20124	PRINT "Du gräver och gräver...";FNS$("gräver",10)
20143	Z=80'XXXX RÖVARGÖMSTÄLLET XXXX
20145	PRINT "Du är längst ner i en grop och kan bara gå uppåt."
20147	GOSUB 12200
20149	IF X=1 THEN S(3)=1 \ GOTO 20107
20151	GOSUB 11000 \ GOTO 20143
20155	Z=79 'XXXXX SKOG 4 XXXXX Z=79 XXX
20156	PRINT "Du är i skogen, väster om sjön."
20158	GOSUB 15200
20161	IF X<>0 THEN ON X GOTO 20197,2115,20055,20165,20197,20197,20162,20180,20195,2107
20162	GOSUB 11000
20163	GOTO 20155
20165	Z=82 'XXXXX SKOG 5 XXXXX Z=82 XXX
20166	PRINT "Du är i skogen, sydväst om sjön."
20168	GOSUB 15200
20172	IF X<>0 THEN ON X GOTO 20178,20180,20155,20240,20178,20178,20173,20255,20176
20173	GOSUB 11000
20174	GOTO 20165
20176	PRINT "Kan du gå på vattnet?"
20177	GOTO 20165
20178	PRINT "Ett staket hindrar dej att gå ditåt."
20179	GOTO 20165
20180	Z=66 'XXXXX SKOG 6 XXXXX Z=66 XXX
20181	PRINT "Du är söder om sjön. En grotta leder åt ÖSTER."
20183	GOSUB 15200
20187	IF X<>0 THEN ON X GOTO 20165,2075,20191,20255,20155,20240,20188,2200,20191,2107
20188	GOSUB 11000
20189	GOTO 20180
20191	PRINT "Kan du gå på vattnet?"
20192	GOTO 20180
20195	PRINT "Kan du gå på vattnet?"
20196	GOTO 20155
20197	PRINT "Ett staket hindrar dej att gå ditåt."
20198	GOTO 20155
20199	GOSUB 11000
20200	Z=81'XXXXX FRAMFÖR HUSET XXXX Z=81 XXX
20202	PRINT "Du står framför husets väldiga port."
20204	GOSUB 15200
20206	IF X1=1 THEN 20232
20208	IF X=19 THEN GOSUB 15202 \ GOTO 20206
20210	IF X=0 THEN 20199
20212	ON X GOTO 20020,20070,20225,20230,20214,20030,20199,9361,20214
20214	PRINT "Huset är i vägen." \ GOTO 20200
20225	IF S(19)=1 THEN PRINT "Porten stängs bakom dej." \ S(19)=0 \ GOTO 9991
20226	PRINT "Porten är stängd!"
20227	GOTO 20200
20230	PRINT "En avskyvärd stank driver dej tillbaka!"
20231	GOTO 20200
20232	PRINT "Du står på en trappa framför ett stort hus. En stor port"
20233	PRINT "prydd med ett familjevapen i guld och silver finns bredvid"
20234	PRINT "dej. I söder ser du en brygga. Åt väster och öster står"
20235	PRINT "skogen tät."
20239	GOTO 20204
20240	Z=67 'XXXXX SKOG 7 XXXXX Z=67 XXX
20241	PRINT "Du är i skogen."
20243	GOSUB 15200
20247	IF X<>0 THEN ON X GOTO 20251,20255,20165,20251,20251,20251,20248,20251,20180
20248	GOSUB 11000
20249	GOTO 20240
20251	PRINT "Ett staket hindrar dej att gå ditåt."
20252	GOTO 20240
20255	Z=68 'XXXXX SKOG 8 XXXXX Z=68 XXX
20256	PRINT "Du är i skogen. En grotta leder åt NORDOST."
20258	GOSUB 15200
20262	IF X<>0 THEN ON X GOTO 20240,2200,20180,20266,20165,20266,20263,20266,2075
20263	GOSUB 11000
20264	GOTO 20255
20266	PRINT "Ett staket hindrar dej att gå ditåt."
20267	GOTO 20256
20270	Z=83 'XXXXX SKOG 9 XXXXX Z=83 XXX
20271	PRINT "Du är söder om sjön. En grotta leder åt VÄSTER."
20273	GOSUB 15200
20277	IF X<>0 THEN ON X GOTO 2066,20285,20281,20300,20281,2200,20278,20315,20330,2107
20278	GOSUB 11000
20279	GOTO 20270
20281	PRINT "Kan du gå på vattnet?"
20282	GOTO 20270
20285	Z=84 'XXXXX SKOG 10 XXXX Z=84 XXX
20286	PRINT "Du är i skogen, sydost om sjön."
20288	GOSUB 15200
20292	IF X<>0 THEN ON X GOTO 20270,20297,20330,20315,20295,20300,20293,20297,20297
20293	GOSUB 11000
20294	GOTO 20285
20295	PRINT "Kan du gå på vattnet?"
20296	GOTO 20285
20297	PRINT "Ett staket hindrar dej att gå ditåt."
20298	GOTO 20285
20300	Z=85 'XXXXX SKOG 11 XXXX Z=85 XXX
20301	PRINT "Du är i skogen. En grotta leder åt NORDVÄST."
20303	GOSUB 15200
20307	IF X<>0 THEN ON X GOTO 2200,20315,20270,20312,2066,20312,20309,20312,20285
20309	GOSUB 11000
20310	GOTO 20300
20312	PRINT "Ett staket hindrar dej att gå ditåt."
20313	GOTO 20300
20315	Z=86 'XXXXX SKOG 12 XXXX Z=86 XXX
20316	PRINT "Du är i skogen."
20318	GOSUB 15200
20322	IF X<>0 THEN ON X GOTO 20300,20327,20285,20327,20270,20327,20324,20327,20327
20324	GOSUB 11000
20325	GOTO 20315
20327	PRINT "Ett staket hindrar dej att gå ditåt."
20328	GOTO 20315
20330	Z=87 'XXXXX SKOG 13 XXXX Z=87 XXX
20331	PRINT "Du är i skogen, öster om sjön."
20333	GOSUB 15200
20336	IF X<>0 THEN ON X GOTO 20340,20342,9424,20285,20340,20270,20338,20342,20342,2107
20338	GOSUB 11000
20339	GOTO 20330
20340	PRINT "Kan du gå på vattnet?"
20341	GOTO 20330
20342	PRINT "Ett staket hindrar dej att gå ditåt."
20343	GOTO 20330
20350	S(53)=2
20352	PRINT "Plötsligt hoppar ett konstigt, blått litet djur fram"
20354	PRINT "ur skogen och ropar:"
20356	PRINT " - Hjälp	! Jag vet inte om jag är en bug eller en feature!"
20358	PRINT "Det springer rätt ut i sjön och simmar bort."
20360	PRINT \ GOTO 20033
20500	GOSUB 6000'SABBAR 6000, INPUTTAR, KOLLAR BÅDE 8600 OCH 12000
20502	PRINT
20504	IF S1<2 THEN A$=FNI$("") \ PRINT
20506	X=0
20508	GOSUB 8600
20510	IF X1=1 THEN 20520
20512	IF X>0 AND X<5 THEN X=X+2 ELSE GOSUB 12000
20520	S(36)=2 \ RETURN
21100	Z=30'XXXXX DIMMIGT BERGSRUM XXXXX
21120	PRINT "Du är i ett dimmigt bergsrum. Kall rå luft blåser dej i"
21122	PRINT "ansiktet. Här finns";
21130	IF S(23)=0 THEN PRINT " en garderob."
21140	IF S(23)=1 THEN PRINT " ett kassaskåp i en garderob."
21155	PRINT "En gång leder uppåt och nedåt."
21160	GOSUB 12200
21180	IF X1=1 THEN 21120
21190	IF X=0 OR X>6 THEN 21220
21200	ON X GOTO 25000,25130,36000,21230,21230,10020
21220	IF INSTR(1,A$,"KORKSKRUV")>0 THEN 21300
21230	GOSUB 11000
21240	PRINT "Du är i ett dimmigt bergsrum."
21250	GOTO 21160
21300	IF S(23)=1 THEN 21330
21310	GOTO 21230
21330	PRINT "Kassaskåpet öppnas."
21340	Z=31
21350	GOSUB 12200
21380	IF X>0 AND X<7 THEN 21500
21390	IF S(23)=0 OR Z=30 THEN 21240
21410	GOSUB 11000
21415	PRINT "Kassaskåpet är öppet."
21420	GOTO 21350
21500	PRINT "Kassaskåpet stängs."
21510	Z=30 \ GOTO 21180
25000	Z=15'XXX THORVALDS RUM X
25001	PRINT "Du är i Thorvalds rum. Vid väggen står en stor förseglad"
25004	IF A(1)=0 THEN A(1)=15
25005	PRINT "kista. I taket finns en taklucka och i golvet finns ett hål."
25008	IF A(3)=31 THEN PRINT "På väggen står det: KORKSKRUV HJÄLPER TILL MED KASS..."
25010	GOSUB 12200
25012	IF X>0 THEN ON X GOTO 25050,15300,25100,10020,40000,21100,25060
25014	IF X1=1 THEN 25000
25016	IF INSTR(1,A$,"ÖPPNA")>0 THEN 25045
25019	IF INSTR(1,A$,"KISTA")>0 THEN 25035
25020	IF INSTR(1,A$,"LÅS UPP KIST")>0 THEN PRINT "Det finns inget lås."\GOTO 25025
25023	GOSUB 11000
25025	PRINT "Du är i Thorvalds rum." \ GOTO 25010
25035	IF A(15)<>1 THEN PRINT "Du kan inte öppna kistan."\GOTO 25025
25036	PRINT "Du bänder upp kistan med din kofot och ser att det ligger en"
25037	PRINT "cykelpump där!"
25038	PRINT "Slarvig som du är lyckas du tappa kofoten i kistan när du tar"
25039	PRINT "pumpen. Kistlocket smäller igen."
25040	A(16)=1 \ A(15)=5 \ GOTO 25000
25045	IF A$="ÖPPNA" THEN A$=FNI$("Öppna vad") \ A$=FNC$(A$)
25046	IF INSTR(1,A$,"KIST")>0 THEN 25035
25047	IF INSTR(1,A$,"TAKLU")=0 AND INSTR(1,A$,"LUCK")=0 THEN 25023
25050	IF A(17)<>1 AND A(17)<>Z THEN PRINT "Takluckan sitter för högt!"\GOTO 25000
25051	PRINT "Du klättrar upp på stegen och öppnar luckan."
25053	IF A(2)<>0 THEN PRINT "Där finns inget, så du klättrar ner igen."\ GOTO 25000
25054	PRINT "Det finns en illaluktande gurka här."
25055	PRINT "Den rasar ned och lägger sej på golvet."
25056	A(2)=15 \ GOTO 25025
25060	IF A(2)>0 THEN 25070
25062	IF A(17)<>1 AND A(17)<>Z THEN PRINT "Det behövs en stege för att nå upp."
25064	IF A(17)=1 OR A(17)=Z THEN PRINT "Öppna takluckan!"
25066	S(2)=S(2)-5
25068	GOTO 25025
25070	IF A(15)=5 THEN 25023
25072	PRINT "Kistan kan bara öppnas med en kofot."
25074	GOTO 25066
25100	PRINT "Du tittar in i personalköket. Osvald ryter till:"
25102	PRINT "-STICK!!Din eländiga babian!"
25103	PRINT "Du ser en liten faun som quarkar en praktyl. Faunen säjer:"
25104	PRINT "-Vad har du här att göra? Räcker det inte med att folk ränner"
25105	PRINT "omkring som tokar nere hos mej? Ska dom komma hit också?"
25110	PRINT
25115	PRINT "En liten faun dyker upp."
25116	IF RND<0.8 OR S(29)=1 THEN 25130
25117	PRINT "Han kastar en kniv mot dej...                     ";
25118	IF RND<0.5 THEN 25121 ELSE PRINT "Den träffar!	!" \ Z=15
25119	GOSUB 7500
25120	GOTO 9461
25121	PRINT "Den missar!" \ PRINT "Golvet ger plötsligt vika och du faller."
25122	GOTO 15300
25130	PRINT "Du är i ett mörkt rum."
25135	Z=96
25136	GOSUB 12200
25210	IF X=1 THEN 21100
25212	IF X=6 THEN 10020
25215	IF X1=1 THEN 25130
25220	GOSUB 11000
25230	GOTO 25130
27050	REM XXX TELEVERKET - subrutin för jackmontering XXX
27060	D=INT(RND*S(37))+1
27065	A$=MID$(W$(5),((D*3)-2),3)
27070	D=VAL(A$)
27075	IF J(D)=1 THEN 27050
27080	J(D)=1
27085	RETURN
27100	PRINT "Just när du ska koppla in telefonen kommer en man med en röd"
27110	PRINT "dräkt som det står TELE på in och slänger en telefonkatalog"
27120	PRINT "på dina fötter."
27122	IF J(Z)<>1 THEN 27140 ELSE J(Z)=0
27130	PRINT "Med en sur min skruvar han bort telefonjacken ur väggen och går."
27140	S(2)=S(2)+5
27150	A(23)=Z \ GOTO 12210
27200	REM XXXXX RING PERSONALKÖK XXXX
27202	PRINT "Ok.   Ring	, Ring	."
27204	PRINT\PRINT "TUUT ------ TUUT ----- TUUT ------ <klick>"
27206	IF W$(6)="" THEN W$(6)=FNI$("Hej, vem där ?")
27212	PRINT "Personalköket rekommenderar:"
27214	PRINT\PRINT "Halvruttna tomater med pilaffris."
27216	PRINT "Vändstekt, långsamt grillad samt hårdkokt ";W$(6)
27218	PRINT "Samt friskt, giftigt grottvatten. (Hi, hi, hi)"
27220	PRINT "<klick> TUUT --- TUUT --- TUUT"
27222	S(29)=1 \ PRINT \ X1=1 \ GOTO 12999
27250	REM XXX Ring Televerket XXXXX
27252	PRINT "Ok. 	Ring, Ring."
27254	PRINT
27256	PRINT "-Stugas televerk."
27258	A$=FNI$("Har ni klagomål på er linje ?")
27262	IF FNL$(A$,1)="J" OR FNL$(A$,1)="j" THEN 27300
27264	A$=FNI$("Vilket nummer gäller det ?")
27268	PRINT "Ok. Vänta ett tag så ska jag kolla upp det."
27270	S=SLEEP(20%) \ IF S THEN INPUT "TUU	T"_A1$ \ GOTO 27270
27272	IF INSTR(1,A$,"481")>0 THEN 27280
27274	IF INSTR(1,A$,"999")>0 THEN 27290
27275	IF INSTR(1,A$,"100")>0 AND J(100)=0 THEN PRINT "Abonnemanget har upphört.<klick>"\GOTO 12210
27276	PRINT "Det är inget fel på den linjen."
27278	PRINT "<klick>" \ S(28)=2 \ GOTO 12210
27280	IF S(6)>0 THEN 27284
27282	PRINT "Linjen fungerar utmärkt. (För en gångs skull...)"\ GOTO 12210
27284	PRINT "Jaha. Hm, linjen är väl okej, men abonnenten..."
27286	PRINT "Det fixar sej nog om ett tag.."
27287	PRINT "<klick>"
27288	GOTO 12210
27290	PRINT "Nummerändring. Nya numret är 900." \ GOTO 12210
27300	PRINT "Jag ska skicka någon för att fixa det."
27302	PRINT "<klick>" \ PRINT
27304	PRINT "Ur skuggorna kommer plötsligt en man klädd i en röd"
27306	GOTO 7081
27400	REM XXX Ring Larmcentralen. XXX
27402	PRINT "Ok. Ring, Ring	."
27404	PRINT \ PRINT "Larmcentralen, var god dröj." \ S=SLEEP(20)
27406	IF S THEN INPUT "  Var god dröj  "_A$ \S=SLEEP(30) \ GOTO 27406
27408	PRINT "LARMCENTRALEN. Vi fixar allt - snabbt!"
27410	PRINT "Vad vill Du ha hjälp med";
27412	A$=FNC$(FNI$(" ?"))
27414	PRINT "Det går inte."
27416	IF INSTR(1,A$,"RÖVARE")>0 THEN 27428
27418	IF INSTR(1,A$,"TRAPPA")>0 THEN 27434
27420	IF INSTR(1,A$,"HISS")>0 THEN 27440
27422	IF INSTR(1,A$,"BÅT")>0 THEN 27444
27424	PRINT "<klick>"
27426	GOTO 12210
27428	PRINT "Jo, förresten. Jag får väl snacka med honom. Om jag"
27430	PRINT "får tag på honom. Han är ofta ute på jakt..."
27432	S(3)=-1 \ GOTO 27424
27434	PRINT "Jo, förresten. Vi får väl ta och se över våra trappor."
27436	PRINT "Jag ska genast kontakta gatukontoret."
27438	S(15)=0 \ S(17)=0 \ S(18)=0 \ GOTO 27424
27440	PRINT "Vänta, var det hissen du sa ?  Jag får väl se över den då."
27442	S(40)=4 \ S(41)=0 \ GOTO 27424
27444	PRINT "Nu får det vara slut på båtfärderna!!"
27446	S(35)=0.5 \ GOTO 27424
27600	IF J(100)=0 THEN 12826 ELSE PRINT FNS$("ringer",2)
27602	IF Z=100 THEN I=1 ELSE I=5
27604	FOR I%=1 TO 8
27606	S=SLEEP(I) \ IF S THEN INPUT ""_A$
27608	PRINT "R	ing!";
27610	NEXT I%
27612	PRINT \ S=SLEEP(I)
27614	IF Z=100 THEN PRINT "Det är visst upptaget." ELSE PRINT "Ingen svarar."
27616	GOTO 12210
27620	PRINT "En automatisk telefonsvarare svarar:"
27622	PRINT " - Han är tyvärr inte inne. Han har alltid så mycket att"
27624	PRINT "   göra att han aldrig hinner svara i telefon."
27626	PRINT "<klick>"
27628	GOTO 12210
27630	ON S(6)+1 GOTO 27632,27640,27650,27650
27632	IF A(29)<>58 THEN 27652
27633	IF Z=58 THEN PRINT "Du hör en signal. Vakten går bort ett ögonblick."
27634	PRINT "Ring, Ring	!"
27636	PRINT " - Stör mej inte! Jag vaktar!"
27638	GOTO 27626
27640	IF (A(29)=58 OR A(29)=1) AND Z=58 THEN PRINT "Du hör en signal. Vakten kravlar iväg."
27641	IF A(29)<>58 THEN 27652
27642	PRINT "Ring, Rin	g!"
27644	PRINT " - Hick, HELAN GÅÅÅÅÅÅÅÅR... HI	CK!"
27646	GOTO 27626
27650	IF Z=58 THEN PRINT "Du hör en signal."
27652	I=4 \ GOTO 27604
28000	REM XXX VAKT XXXXX
28002	IF A(29)=Z OR A(29)=1 THEN PRINT "Vakten sover för djupt." \ GOTO 12210
28010	IF A(29)<>Z AND A(29)<>1 THEN PRINT "Jag ser ingen VAKT här."\GOTO 12210
28012	IF S(6)=2 THEN PRINT "Vakten är redan död! Ser du inte blodfläckarna!"\GOTO 12210
28014	IF A(4)<>1 THEN PRINT "Du har inget du kan döda honom med."\GOTO 12210
28016	IF S(6)=3 THEN 28030
28018	IF S(6)=1 THEN 28026
28020	PRINT "Du kastar hillebarden mot vakten, men han duckar."
28022	A(4)=Z \ S(1)=S(1)-1
28024	GOTO 12210
28026	PRINT "Du kastar hillebarden mot den fulle vakten. Han fångar"
28027	PRINT "upp den i luften med en elegant gest."
28028	A(4)=2 \ S(1)=S(1)-1
28029	GOTO 12210
28030	PRINT "Du kastar hillebarden mot den sovande"
28034	PRINT "vakten, som stönar och bleknar."
28036	PRINT "Du drar den bloddrypande hillebarden ur liket och torkar av den."
28038	S(6)=2 \ A(22)=Z \ A(29)=Z \ S(51)=0
28039	IF Z=63 THEN S(52)=S(50) \ S(2)=S(2)+25
28040	IF A(15)=2 THEN A(15)=Z
28042	IF A(25)=2 THEN A(25)=Z
28044	IF A(26)=2 THEN A(26)=Z
28046	X1=1 \ GOTO 12999
28090	IF C$="" THEN 12999
28092	IF C$="UPP" THEN 9950
28100	FOR I=1 TO A(0)
28101	IF A$(I,1)<>"" THEN IF INSTR(1,C$,A$(I,2))>0 OR INSTR(1,C$,A$(I,3))>0 THEN 28105
28102	NEXT I
28103	I=0
28105	IF (A(29)<>1 AND A(29)<>Z) OR S(6)>1 THEN 12840
28106	IF INSTR(1,C$,"GUBBE")>0 OR S(30)=Z THEN 12840
28107	IF I>0 THEN 28110
28108	PRINT "Det kan du inte ge till vakten." \ GOTO 12210
28110	IF I<>26 AND I<>25 AND I<>15 AND I<>4 AND I<>18 THEN 28108
28112	IF A(I)<>1 THEN PRINT "Du bär väl ";FNA$(I);A$(I,4);"." \ GOTO 12210
28114	IF I=18 THEN 12360
28116	PRINT "Vakten tar emot ";A$(I,4);" med ett snett leende."
28118	S(1)=S(1)-1 \ A(I)=2 \ GOTO 12210
28130	IF A(29)<>Z AND A(29)<>1 THEN 6418
28132	IF S(6)=3 THEN 28150
28134	IF S(6)=1 THEN 28140
28136	PRINT "Vakten hindrar dej." \ GOTO 12210
28140	IF S(1)=9 THEN 6420
28142	PRINT "Vakten släpper motvilligt ";A$(I,4);"."
28144	S(1)=S(1)+1 \ A(I)=1
28146	GOTO 12210
28150	PRINT "Har du hjärta att ta någonting från en sovande vakt?!?"
28152	A$=FNI$("") \ A$=FNC$(A$)
28154	IF A$<>"JA" THEN 12214
28156	PRINT "Har Du inget hjärta i kroppen ?!!Jag vägrar!"\GOTO 12214
28160	IF A(22)<>63 THEN 6418
28162	IF S(1)=9 THEN 6420
28164	S(52)=0 \ S(2)=S(2)-30
28166	GOTO 6422
29000	REM XXX RÖVARE XXXX
29005	S(4)=S(4)+1
29010	IF S(4)>8 THEN 29050
29015	IF RND<0.2 THEN S(4)=S(3)=0 \ GOTO 6069
29020	IF RND<0.7 THEN PRINT "Du hör tunga fotsteg i närheten."
29025	GOTO 6069
29050	IF Z=80 THEN 6069
29055	B=0
29060	IF INT(RND*4)=3 THEN S(3)=0 \ S(41)=1 \ GOTO 6069
29065	FOR I=1 TO 14
29070	IF A(I)=1 THEN A(I)=80 \ B=B+1 \ S(1)=S(1)-1
29075	IF A(I)=Z THEN A(I)=80 \ B=B+1
29080	NEXT I
29085	IF B=0 THEN 6069
29090	IF S(20)=1 THEN S(20)=0
29095	PRINT
29100	PRINT "Plötsligt hoppar en skäggig rövare fram ur mörkret och säjer:"
29105	PRINT " - Jag snor det här krafset och gömmer det i mitt"
29110	PRINT "   gömställe långt nere!!"
29115	PRINT \ PRINT "Han försvinner lika fort som han kom!"
29120	S(4)=-7 \ S(3)=-1
29125	GOTO 6069
30000	REM XXX GUBBE XXXX
30001	IF S(30)=96 OR S(49)=1 THEN RETURN
30002	S(30)=INT(RND*92)+9 \ S(49)=0 \ X1=2
30004	IF S(30)=Z OR S(30)=51 OR S(30)=60 THEN 30002
30006	PRINT "Gubben reser sej, muttrar någonting om att man aldrig"
30008	PRINT "får vara i fred, och försvinner." \ RETURN
30010	IF S(30)<>Z THEN PRINT "Jag ser ingen gubbe här." \ GOTO 12210
30012	IF A(19)=0 THEN PRINT "Gubben har ju vattenflaskan." \ GOTO 12210
30014	IF A(19)<>1 OR S(32)>0 THEN PRINT "Du har ju ingen full vattenflaska."\GOTO 12210
30016	PRINT "Gubben dricker ur vattenflaskan och ser genast gladare ut."
30018	S(49)=1 \ S(32)=1 \ GOTO 12210
30020	IF I=11 AND S(30)=Z AND S(49)=2 THEN 30028
30022	IF I=19 AND A(10)=0 THEN 30036
30024	PRINT "Gubben vägrar att släppa ";A$(I,4);"."
30026	GOTO 12210
30028	IF S(1)=9 THEN 6420
30030	PRINT "Du tar pärlhalsbandet från den bländade gubben."
30032	S(49)=0 \ A(11)=1 \ X1=1 \ S(1)=S(1)+1
30034	GOTO 30002
30036	IF S(1)=9 THEN 6420
30038	PRINT "Du tar vattenflaskan från gubben."
30040	S(1)=S(1)+1 \ X1=1 \ A(19)=1
30042	GOTO 30002
30050	IF S(30)<>Z THEN PRINT "Jag ser ingen GUBBE här." \ GOTO 12210
30052	PRINT "Gubben ser din hotande blick och smiter iväg."
30054	S(30)=INT(RND*92)+9 \ S(49)=0
30056	IF S(30)=Z OR S(30)=51 OR S(30)=60 THEN 30054
30058	GOTO 12210
35000	Z=100'XXX TEFELONSTUGAN XXX Z=100 ZZZZZZZZZZ
35005	S(27)=S(27)+1
35010	IF S(27)>3 AND S(27)<8 THEN 35030
35015	PRINT "Du är i en stuga med dörrar bakåt, framåt och åt"
35020	PRINT "höger. Högt upp i taket finns ett fönster."
35025	GOTO 35035
35030	PRINT "Du är i stugan."
35035	IF S(27)=8 THEN S(27)=4
35040	GOSUB 6000
35045	IF S(27)=1 AND J(100)=1 AND A(25)=100 THEN PRINT "Telefonen ringer."
35050	PRINT \ A$=FNI$("")
35052	PRINT \ GOSUB 12000
35055	IF INSTR(1,A$,"SVAR")>0 THEN 35100
35065	IF X1=1 THEN 35015
35070	IF X>3 AND X<7 THEN 35085
35075	GOSUB 11000
35080	GOTO 35030
35085	IF S(27)=1 THEN S(27)=0
35090	ON (X-3) GOTO 7556,9190,35150
35100	IF S(27)>1 OR J(100)=0 OR A(25)<>100 THEN 35075
35105	S(27)=2
35110	PRINT "Du svarar i telefon och hör en röst:"
35115	IF W$(6)="" THEN W$(6)=FNI$("- Vad heter du ?")
35120	PRINT "Hej, ";W$(6);" ! Bra att Du också har skaffat en telefon."
35122	PRINT "<klick>"
35125	GOTO 35030
35150	IF A(1)=1 THEN PRINT "Dörren är igenbommad av Stugas gatukontor." \ GOTO 35000
35155	GOTO 2127
36000	Z=61'XXXXX KYRKOGÅRD XXXXX
36005	PRINT "Du är på en kyrkogård. Du står vid en gravsten på kanten"
36010	PRINT "till en grav. En stig leder framåt och bakåt."
36015	GOSUB 12200
36020	IF X1=1 THEN 36000
36025	IF X=0 OR X>6 THEN 36035
36030	ON X GOTO 36035,36050,36035,36035,21100,2150
36035	GOSUB 11000
36040	PRINT "Du är på kyrkogården."
36045	GOTO 36015
36050	Z=63'XXXXX GRAVEN XXXXX
36055	PRINT "Du är i en grav. Det luktar unket här."
36060	PRINT "Prästen tittar ner. Han ser ut så här:"
36065	GOSUB 700
36067	IF S(50)-S(52)>30 AND S(52)>0 THEN S(52)=0 \ A(22)=2 \ A(5)=63
36070	GOSUB 12200
36075	IF X1=1 THEN 36090
36080	IF X=1 THEN 36000
36085	GOSUB 11000
36090	PRINT "Du är i en grav."
36095	GOTO 36070
40000	Z=17'XXXXX OSVALDS RUM XXXXX
40015	IF S(5)>4 THEN S(5)=1 ELSE S(5)=S(5)+1
40017	IF S(5)=1 THEN 40030
40020	PRINT "Du är i Osvalds rum." \ GOTO 40100
40030	PRINT "Du är i Osvalds rum, ett rum med fyra dörrar. På den högra står det"
40031	PRINT "ZZZZ, på den vänstra står det THORVALD och på den rakt fram"
40032	PRINT "står det GARDEROB."
40060	IF S(15)=0 AND S(7)=1 THEN PRINT "En trappa går nedåt."
40061	IF S(15)=1 AND S(7)=1 THEN PRINT "Det finns rester av en trappa här."
40100	GOSUB 12200
40110	IF X1=1 THEN 40030
40115	IF X=0 OR X=7 THEN 40200
40120	ON X GOTO 40200,40140,25000,18000,41000,40200
40140	IF S(7)=0 THEN 40200
40145	IF S(15)<>0 THEN PRINT "Trappan är avspärrad av Stugas gatukontor."\GOTO 40015
40147	IF A(1)<>1 THEN 13235
40150	PRINT "Trappan rasar ihop." \ S(15)=1 \ GOTO 40015
40200	GOSUB 11000
40210	GOTO 40020
41000	REM XXX GARDEROBEN XXXXX Z=4 XXXX
41005	PRINT "Du är i en mörk garderob."
41010	PRINT "Bakom dej och till vänster finns det dörrar."
41030	S(4)=1 \ Z=4
41040	GOSUB 12200
41080	IF X1=1 THEN 41005
41090	IF X=6 THEN 40000
41100	IF X=3 THEN 9020
41105	GOSUB 11000
41110	PRINT "Du är i garderoben."
41120	GOTO 41040
80000	REM *** SPARA *** &&&&& DEC-10 SPECIELL KOD PÅ 80000-80565
80005	ON ERROR GOTO 80500'&&&&&
80100	OPEN "STUGA.SPA" FOR OUTPUT AS FILE #1'&&&&&
80102	ON ERROR GOTO 97000'&&&&&
80105	MARGIN #1,132 \ QUOTE #1 \ X=0'&&&&&
80110	PRINT #1,A(I); FOR I=0 TO A(0)'&&&&&
80115	X=X+A(I)/(PI) FOR I=0 TO A(0)'&&&&&
80120	PRINT #1'&&&&&
80125	PRINT #1,S(I); FOR I=0 TO S(0)'&&&&&
80127	X=X+S(I)/(PI-1) FOR I=0 TO S(0)'&&&&&
80130	PRINT #1'&&&&&
80131	PRINT #1,G/2,Z*7,X+G+Z'&&&&&
80132	FOR I=0 TO S(24)'&&&&&
80135	IF W$(I)="" THEN PRINT #1,"-----" ELSE PRINT #1,W$(I)'&&&&&
80138	NEXT I'&&&&&
80140	PRINT #1,J(I); FOR I=0 TO J(0)'&&&&&
80150	CLOSE 1'&&&&&
80155	PRINT "Det nuvarande läget är sparat på filen STUGA.SPA."'&&&&&
80160	GOTO 12210'&&&&&
80200	REM *** ÅTERSKAPA ***'&&&&&
80202	ON ERROR GOTO 80500'&&&&&
80205	OPEN "STUGA.SPA" FOR INPUT AS FILE #1'&&&&&
80210	ON ERROR GOTO 80520'&&&&&
80300	MARGIN #1,132 \ X=0'&&&&&
80305	INPUT #1,A(0)'&&&&&
80310	INPUT #1,A(I) FOR I=1 TO A(0)'&&&&&
80315	X=X+A(I)/(PI) FOR I=0 TO A(0)'&&&&&
80318	INPUT #1,S(0)'&&&&&
80319	IF S(0)=0 THEN S(0)=53'$$$$$ Standardvärde. Raden bör tas bort småningom'&&&&&
80320	INPUT #1,S(I) FOR I=1 TO S(0)'&&&&&
80325	X=X+S(I)/(PI-1) FOR I=0 TO S(0)'&&&&&
80326	IF S(24)=0 THEN S(24)=6'$$$$$'&&&&&
80327	ON ERROR GOTO 80540'$$$$$ Koll om gammal fil. Raden bör tas bort.'&&&&&
80329	INPUT #1,G,Z,I1'&&&&&
80330	INPUT #1,W$(I) FOR I=0 TO S(24)'&&&&&
80332	W$(I)="" IF FNL$(W$(I),5)="-----" FOR I=0 TO S(24)'&&&&&
80336	'IF END#1 THEN 80340'$$$$$'&&&&&
80337	INPUT #1,J(0)
80338	INPUT #1,J(I) FOR I=1 TO 100
80340	G=G*2 \ Z=Z/7'&&&&&
80341	X=X+G+Z'&&&&&
80342	CLOSE 1'&&&&&
80343	ON ERROR GOTO 97000'&&&&&
80345	IF ABS(X-I1)>0.03 THEN PRINT "Fel på STUGA.SPA!" \ STOP'&&&&&
80347	S2=1'Återskapaflagga'&&&&&
80350	IF Z=4 THEN 41000'&&&&&
80355	IF Z<8 OR Z>100 THEN PRINT "Fel i STUGA.SPA!" \ STOP'&&&&&
80360	IF Z<20 THEN ON Z-7 GOTO 9991,15050,15000,15300,16000,16500,17000,25000,10020,40000,9300,2044'&&&&&
80365	IF Z<31 THEN ON Z-19 GOTO 2115,9000,9035,9065,9145,2075,9175,9100,9020,9190,21100'&&&&&
80370	IF Z<41 THEN ON Z-30 GOTO 21340,7570,2066,1909,7556,8300,8330,8071,8095,8365'&&&&&
80375	IF Z<51 THEN ON Z-40 GOTO 8381,8400,8000,8020,8035,15350,15370,15386,9361,2200'&&&&&
80380	IF Z<61 THEN ON Z-50 GOTO 2241,8420,1500,9490,9510,9545,9558,13000,13235,9528'&&&&&
80385	IF Z<71 THEN ON Z-60 GOTO 36000,13173,36050,14000,14100,20180,20240,20255,2019,20000'&&&&&
80390	IF Z<81 THEN ON Z-70 GOTO 20020,20030,20040,20055,20070,20085,20107,9390,20155,20143'&&&&&
80395	IF Z<91 THEN ON Z-80 GOTO 20200,20165,20270,20285,20300,20315,20330,9424,1929,15432'&&&&&
80400	ON Z-90 GOTO 2033,1919,1950,1960,1970,25130,8148,2150,2127,35000'&&&&&
80500	PRINT "? Kan inte öppna STUGA.SPA."'&&&&&
80505	RESUME 80510'&&&&&
80510	ON ERROR GOTO 97000'&&&&&
80515	GOTO 12210'&&&&&
80520	PRINT "Fel inuti STUGA.SPA!"'&&&&&
80525	CLOSE 1'&&&&&
80530	RESUME 99999'&&&&&
80540	RESUME 80545'$$$$$ Raderna 80540-80565 bör tas bort småningom.'&&&&&
80545	ON ERROR GOTO 80520'&&&&&
80550	INPUT #1,W$(I) FOR I=0 TO 6'&&&&&
80552	INPUT #1,W$(3)'Starttid'&&&&&
80555	INPUT #1,A1$ FOR I=8 TO 14'&&&&&
80560	INPUT #1,G,Z,I1'&&&&&
80565	GOTO 80332'$$$$$'&&&&&
90000	ON ERROR GOTO 97000'XXXXX NU BÖRJAR VI XXXXX
90002	W$(3)=TIME$ \ W$(4)=DATE$
90003	S(30)=96
90004	S(32)=1 \ S(33)=1 \ S(40)=1
90005	MARGIN 80
90050	J(100)=1 \ J(17)=1 \ J(31)=1
90052	J(43)=1 \ J(58)=1 \ J(78)=1 \ J(97)=1
90054	W$(1)="Stugrådet: Thorvald, Kimmo Eriksson, Olle Johansson, Viggo Eriksson, DEC-op, Thord Andersson"
90056	GOSUB 702
90057	W$(5)="004008009010011012013014015016017021022023024025031034035036038040"
90058	W$(5)=W$(5)+"043044046048052054056058059062069078080089093095096097100"
90059	S(37)=LEN(W$(5))/3
90060	S(45)=1
90062	S(48)=-1 \ S(20)=-1
90064	'X=CRT(1)
90066	S(2)=50
90068	IF FNL$(DATE$,6)="01-APR" THEN A1=1 ELSE A1=0
90070	PRINT "Välkommen till VIOLs stuga!!!!!"
90072	PRINT
90090	INPUT "Har du vågat dej in här förut";A$
90091	A$=FNC$(A$) \ PRINT \ PRINT
90094	IF FNL$(A$,1)="J" THEN 90200
90096	IF FNL$(A$,1)="N" THEN 90100
90098	PRINT "JA eller NEJ!" \ GOTO 90090
90100	PRINT "Då behövs lite hjälp och instruktioner!" \ PRINT
90110	GOSUB 91000
90150	PRINT "LYCKA TILL!"
90153	PRINT
90200	A(0)=30 \ S(0)=53 \ S(24)=6 \ J(0)=100
90202	FOR I=1 TO 12
90204	READ A$(I,1),A$(I,2),A$(I,3),A$(I,4),A(I)
90206	NEXT I
90208	FOR I=15 TO A(0)
90210	READ A$(I,1),A$(I,2),A$(I,3),A$(I,4),A(I)
90212	NEXT I
90214	GOTO 20000
90300	DATA "DIAMANT","DIAMA","DIAMA","diamanten",15
90302	DATA "GURKA","GURKA","ILLAL","gurkan",0
90304	DATA "SILVERTACKA","SILVE","TACKA","silvertackan",31
90306	DATA "HILLEBARD","HILLE","JUVEL","hillebarden",2
90308	DATA "DÖDSKALLE","DÖDSK","SKALL","dödskallen",0
90310	DATA "KLOCKA","VÄCKA","KLOCK","klockan",59
90312	DATA "GULDMYNT","GULD","MYNT","guldmynten",0
90314	DATA "TRILOGI","TRILO","SAGAN","trilogin",36
90316	DATA "KONTRAKT","KONTR","SKÄRT","kontraktet",0
90318	DATA "LAGERKRANS","LAGER","KRANS","lagerkransen",53
90320	DATA "PÄRLHALSBAND","PÄRL","HALSB","pärlhalsbandet",0
90322	DATA "FAUNSKO","FAUN","SKO","faunskon",0
90330	DATA "KOFOT","KOFOT","KOFOT","kofoten",0
90332	DATA "CYKELPUMP","CYKEL","PUMP","cykelpumpen",0
90334	DATA "STEGE","STEGE","STEGE","stegen",4
90336	DATA "BRÄNNVINSFLASKA","BRÄNN","BRÄNN","brännvinsflaskan",97
90338	DATA "VATTENFLASKA","VATTENF","VATTENF","vattenflaskan",0
90340	DATA "BOLL","BOLL","BOLL","bollen",8
90342	DATA "SPADE","SPADE","SPADE","spaden",61
90344	DATA "LIK","LIK","LIK","liket",0
90346	DATA "KATALOG","KATAL","TELEFONK","katalogen",0
90348	DATA "LAMPA","LAMPA","LAMPA","lampan",0
90350	DATA "TELEFON","TELEF","TELEF","telefonen",100
90352	DATA "NYCKLAR","NYCKL","NYCKE","nycklarna",54
90354	DATA "SAX","SAX","SAX","saxen",2
90356	DATA "SLÄGGA","SLÄGG","SLÄGG","släggan",2
90357	DATA "VAKT","VAKT","VAKT","vakten",58
90358	DATA "FÖRLÄNGNINGSSLADD","FÖRLÄ","SLADD","förlängningssladden",26
90400	REM Data för Fozzis berättelse
90402	DATA "Dodge City","Boot Hill","en by i Montana","fantomengrottan"
90404	DATA "fängelsechefen i Råå","Trondheim"
90406	DATA "bröderna Dalton","Sven Olssons kvintett","bröderna Brothers"
90408	DATA "Kimmo, den gamle fyllbulten,","Curt Nicolin","Jesse James"
90410	DATA "fängelset","San Franciscos hem för tankspridda","sin limosin"
90412	DATA "burarna i Bronx Zoo","en labyrint i Småland","riksdagshuset"
90414	DATA "fritidsorganet GLAD OCH NAKEN","sheriffen","guldlasten"
90416	DATA "några glada flickor","en aktie i Kuben","en illaluktande gurka"
90418	DATA "fruktans demoner","ett bankrån","Butch Cassidys hustru"
90420	DATA "jultomten","en hjärnskakningsepidemi","kvarterspolisen"
90422	DATA "ett bakhåll","ett fel på Malmös TV 2-sändare","en taxi"
90424	DATA "att toaletten ska bli ledig","att sheriffen ska göra något","Lucky Luke"
90426	DATA "skjuta sönder stan","störa indianerna","varsla om lockout"
90428	DATA "väcka guvernören","ta gisslan på Norges ambassad","dra sej tillbaka"
90430	DATA "rädda","lätt berusade","måna om sitt utseende","allt färre"
90432	DATA "svårflörtade","sömniga"
90434	DATA "på ett helt annat ställe","för sent","i grevens tid"
90436	DATA "en liten aning för tidigt","samtidigt","inte"
90600	DEF FNA$(I1)
90602	IF I1=7 OR I1=26 THEN FNA$="inga " ELSE IF I1=9 OR I1=11 OR I1=22 THEN FNA$="inget " ELSE FNA$="ingen "
90604	FNEND
90650	DEF FNS$(X1$,X)
90655	D=ECHO(1)
90660	D=SLEEP(X)
90665	IF D THEN PRINT"Tyst, jag ";X1$;\INPUT "!"_A$ \ GOTO 90660
90670	D=ECHO(0) \ FNS$="" \ PRINT
90675	FNEND
90700	DEF FNC$(A$)
90705	X1$=FNL$(A$,130) \ X2$="" \ FNC$=""
90710	IF LEN(X1$)>20 THEN X2$=FNM$(X1$,21) \ X1$=FNL$(X1$,20)
90715	CHANGE X1$ TO X
90720	X(X2)=X(X2)-32 IF X(X2)>96 AND X(X2)<126 FOR X2=1 TO X(0)
90750	CHANGE X TO X1$
90755	FNC$=FNC$+X1$
90760	IF X2$<>"" THEN X1$=X2$ \ X2$="" \ GOTO 90710
90765	FNEND
90800	DEF FNL$(X1$,X)
90805	IF X<=0 THEN FNL$="" \ GOTO 90815
90810	IF X>LEN(X1$) THEN FNL$=X1$ ELSE FNL$=LEFT$(X1$,X)
90815	FNEND
90820	DEF FNR$(X1$,X)
90825	IF X<=0 THEN FNR$="" \ GOTO 90835
90830	IF X>LEN(X1$) THEN FNR$=X1$ ELSE FNR$=RIGHT$(X1$,X)
90835	FNEND
90840	DEF FNM$(X1$,X)
90845	IF X>LEN(X1$) OR X<=0 THEN FNM$="" \ GOTO 90855
90850	FNM$=MID$(X1$,X,LEN(X1$)-X+1)
90855	FNEND
90900	DEF FNF$(X)
90910	READ X1$ FOR I1=0 TO X(X)
90920	FNF$=X1$
90930	READ X1$ FOR I1=X(X)+1 TO 5
90940	FNEND
90950	DEF FNI$(X1$)
90960	IF M2%=1% AND W$<>CHR$(3) THEN PRINT #2,W$'&&&&&
90970	PRINT X1$;
90980	IF M3%=0% THEN INPUT ""_W$ \ GOTO 90990
90982	' IF END#3 THEN M3%=0% \ GOTO 90980'&&&&&
90984	INPUT LINE #3,W$ \ PRINT W$'&&&&&
90990	FNI$=W$
90995	FNEND
91000	PRINT "Stuga är ett ADVENTURE-liknande spel på svenska."
91005	PRINT "Du ska utforska ett hus och dess omgivningar. Datorn är dina"
91010	PRINT "ögon och händer. Ge enkla order till datorn, till exempel:"
91015	PRINT "SLÄPP TAVLAN, GE SAFTFLASKAN, NORR, UPPÅT, VÄNSTER..."
91020	PRINT "Utanför stugan förflyttar du dej med väderstreck som kan för-"
91025	PRINT "kortas till N, S, V, Ö, NV, NÖ, SÖ och SV. Inne i stugan används"
91030	PRINT "riktningarna FRAMÅT (F), BAKÅT (B), VÄNSTER (V), HÖGER (H),"
91035	PRINT "UPPÅT (U) samt NERÅT (N)."
91040	PRINT "I vissa rum kan du få särskild hjälp (det ger poängavdrag) om du"
91045	PRINT "skriver HJÄLP. INVENT listar alla saker du bär på, POÄNG skriver"
91050	PRINT "ut hur många poäng du har och TITTA skriver ut den fullständiga"
91055	PRINT "beskrivningen av rummet. Ge kommandot SLUTA när du är färdig."
91060	PRINT "Skriv INFO för att få en lista över kommandona."
91065	PRINT
91070	PRINT "Du ska försöka att skaffa så många poäng som möjligt. Poäng får"
91075	PRINT "du genom att upptäcka nya ställen och ta vara på värdesaker."
91080	PRINT
91090	RETURN
97000	IF ERR<>27 THEN 97004
97001	IF S2=0 THEN S1=1 \ RESUME 12999
97002	X=0 \ X1=0 \ IF S1<2 THEN S1=2 ELSE S1=1 \ S2=0
97003	RESUME 12999
97004	PRINT "? Fel på rad"ERL". Felkod:"ERR
97006	RESUME
97010	'%%%%% Raderna 97010 - 98034 behövs bara på Oden och Nadja
97011	PRINT "? Kan inte öppna STUGA.TXT<11,155>. Ge kommandot"'%%%%%
97012	PRINT "  PATH/ADD:DSKD: innan du kör STUGA nästa gång"'%%%%%
97014	PRINT "  så slipper du förhoppningsvis denna utskrift."'%%%%%
97016	RESUME 99996'%%%%%
98000	INPUT "S, A, A$, W$ eller Z; index; S eller L:"_A1$,A1%,A2$'%%%%%
98001	ON ERROR GOTO 98020'%%%%%
98002	IF A2$="S" THEN INPUT "Nytt värde:"_A3$'%%%%%
98003	IF A1$="S" THEN PRINT S(A1%) \ IF A2$="S" THEN S(A1%)=VAL(A3$)'%%%%%
98004	IF A1$="A" THEN PRINT A(A1%) \ IF A2$="S" THEN A(A1%)=VAL(A3$)'%%%%%
98006	IF A1$="W$" THEN PRINT W$(A1%) \ IF A2$="S" THEN W$(A1%)=A3$'%%%%%
98007	IF A1$="Z" THEN PRINT Z \ IF A2$="S" THEN Z=VAL(A3$) \ GOTO 80360'%%%%%
98008	IF A1$="A$" THEN 98030'%%%%%
98009	ON ERROR GOTO 97000'%%%%%
98010	A$=FNI$("") \ GOTO 12214'%%%%%
98020	PRINT "Felaktigt index!"'%%%%%
98022	RESUME 98009'%%%%%
98030	INPUT "1, 2, 3 eller 4:"_A2%'%%%%%
98032	PRINT A$(A1%,A2%) \ IF A2$="S" THEN A$(A1%,A2%)=A3$'%%%%%
98034	GOTO 98009'%%%%%
99000	REM XXX SLUT XXXX
99002	IF M2%=1% THEN PRINT #2,W$ \ CLOSE 2 \ M2%=0%'&&&&& LOGGA
99003	IF M3%=1% THEN CLOSE 3 \ M3%=0%'&&&&&
99004	IF W$(6)="" THEN W$(6)=FNI$("Vad heter du ?")'%%%%% Kan tas bort
99090	PRINT "Du fick";S(2);"poäng!"
99100	IF S(2)<50 THEN I=50 \PRINT "Du kan klassas som en klantig nybörjare."\GOTO 99200
99104	IF S(2)<55 THEN I=55 \PRINT "Du är en ren amatör inom stugforskningen."\GOTO 99200
99110	IF S(2)<65 THEN I=65\PRINT "Du är en duktig nybörjare inom stugforskningen."\GOTO 99200
99112	IF S(2)<90 THEN I=90\PRINT "Du är en erfaren stugforskare."\GOTO 99200
99114	IF S(2)<120 THEN I=120\PRINT "Du kan kalla dej en stugfogde."\GOTO 99200
99120	IF S(2)<150 THEN I=150\PRINT "Du är en erfaren stugfogde."\ GOTO 99200
99130	IF S(2)<200 THEN I=200 \ PRINT "Du är en väldigt erfaren stugfogde."\GOTO 99200
99140	IF S(2)<250 THEN I=250 \ PRINT "Du är biträdande expert på hus i Småland." \ GOTO 99200
99145	IF S(2)<300 THEN I=300\PRINT "Du är expert på hus i Småland."\GOTO 99300
99150	IF S(2)<335 THEN I=335 \PRINT "Du är föreslagen som medlem i stugrådet."\GOTO 99200
99160	PRINT "	GRATTIS !!"
99170	PRINT "Du är nu invald i stugrådet."
99174	GOTO 99300
99200	PRINT "För att komma upp i nästa klass behöver Du";
99210	PRINT I-S(2);"poäng till."
99300	REM Eventuell loggning av resultat, 99302 - 99500 kan tas bort
99302	INPUT "Vill du ge några synpunkter på STUGA";A$ \ A$=FNC$(A$)'%%%%%
99305	IF FNL$(A$,1)="J" THEN 99350'%%%%%
99310	IF FNL$(A$,1)="N" THEN I=0 \ GOTO 99400'%%%%%
99315	PRINT "Svara JA eller NEJ!"'%%%%%
99320	GOTO 99300'%%%%%
99350	PRINT "Skriv nu! Avsluta med en extra radframmatning."'%%%%%
99355	FOR I=1 TO 50'%%%%%
99360	INPUT LINE W$(I)'%%%%%
99365	IF W$(I)="" THEN I=I-1 \ GOTO 99395'%%%%%
99370	IF LEN(W$(I))>80 THEN W$(I)=FNL$(W$(I),80)'%%%%%
99375	NEXT I'%%%%%
99395	PRINT "Tack!"'%%%%%
99400	ON ERROR GOTO 97010'%%%%%
99402	' OPEN "STUGA.TXT[11,155]$80" AS FILE :1'%%%%%
99405	' SET :1,LOF(:1)+1'%%%%%
99410	A$=DATE$+" "+TIME$+"  "+STR$(S(2))+"  "+W$(6)'%%%%%
99415	' RITE :1,A$'%%%%%
99420	' WRITE :1,W$(J) FOR J=1 TO I'%%%%%
99500	CLOSE 1'%%%%%
99990	PRINT \ PRINT "Thorvald hälsar:   - Välkommen tillbaka!"
99996	PRINT
99998	REM            NU ÄR PROGRAMMET NÄSTAN SLUT            KKKKKOLOLOLOLLKHH
99999	END
