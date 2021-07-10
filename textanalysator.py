from prettytable import PrettyTable

# -----------------------------------------------------------------------------
# VSTUPNÍ DATA
# - Pole s texty k analýze
# - Slovník s DB uživatelů
# -----------------------------------------------------------------------------
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.''',

'''Během pandemického období mnozí zaměstnanci amerických 
poboček kávového řetězce Starbucks přiznali, že čelí velkému 
pracovnímu tlaku i agresivním zákazníkům. 
Někteří si stěžují, že na pobočkách chybějí zaměstnanci a oni 
tak často musí pracovat přesčas. Jejich mzda ovšem zůstává
pořád stejná.''',

'''V roce 2020 rozšířil kavárenský řetězec své služby a začal 
spolupracovat s rozvážkovou společností Uber Eats, která doručuje 
sortiment až k zákazníkovi. Procento tržeb společnosti Starbucks 
prostřednictvím mobilních objednávek za posledních několik let 
významně vzrostlo, z deseti procent veškerého prodeje na 
konci roku 2017 na 24 procent na konci roku 2020.''',

'''Delfín obecný je velmi aktivní a společenský, žije 
ve společenství o deseti až několika tisících jedincích. 
Upřednostňuje hluboké vody v pobřežních oblastech, často se 
za účelem lovu kořisti sdružuje mnoho skupin dohromady 
a jindy spolu různé skupiny soupeří. 
Ke spánku využívá jen polovinu mozku, druhou hemisférou 
je bdělý, přičemž obě poloviny může střídat. 
Plave maximální rychlostí přinejmenším 40 km/h 
(a možná až 60 km/h) s maximální hloubkou ponoru 300 metrů. 
Má silnou ocasní ploutev, ta mu umožňuje dlouhé skoky nad 
hladinu i poskakování ve vzpřímeném postoji za pomoci 
rychlých úderů o hladinu. Profil kůže mu ale k plavání nepomáhá. 
Pod vodou je schopen zůstat až 10 minut na jedno nadechnutí, 
ale většinou se vynořuje častěji. Domlouvá se pomocí 
echolokace na frekvencích 1000 Hz–150 kHz. Březost trvá 
10–11,5 měsíce, období rozmnožování je jaro a podzim, 
v tropickém pásmu celoročně. Samice rodí jedno mládě. 
Mláďata se rodí ocasem napřed a dosahují délky 
0.8–1 m a hmotnosti přibližně 10 kg. 
Delfíni se dožívají až 30 let.'''
]

USERS = {
    'bob' : '123',
    'ann' : 'pass123',
    'mike': 'password123',
    'liz' : 'pass123',
    }

# -----------------------------------------------------------------------------
# VÝBĚR UŽIVATELE
# -----------------------------------------------------------------------------
uname = input('Enter your login: ')
passwd = input(f'Enter password for {uname}: ')
if USERS.get(uname) != passwd:
    print(f'Could not authenticate {uname} - wrong username or password. Exiting ...')
    exit()

# -----------------------------------------------------------------------------
# VOLBA TEXTU K ANALÝZE
# -----------------------------------------------------------------------------
DELIMINER = '-' * 45
numOfTexts = len(TEXTS)

print(DELIMINER)
print(f'Welcome to the app, {uname}!')
print(f'We have {numOfTexts} texts to be analyzed.')
print(DELIMINER)

option = input(f'\nEnter a number between 1 and {numOfTexts} to select: ')
isOK = option.isdigit() and int(option) in range(1, numOfTexts+1)
if not isOK:
    print(f'Your option {option} is not allowed. Exiting ...')
    exit()

# -----------------------------------------------------------------------------
# ANALÝZA TEXTU
#
# 1. Pomocí metody replace() se nahradí prázdným znakem znaky '.', ',', ':', ';'
# 2. Pomocí metody split() rozdělen text na pole slov - workingList
# 3. Z tohoto pole slov vytvořeny další nová čtyři pole, která obsahují
#    jen jeden konkrétní typ slov, tedy titlecase, uppercase, lowercase a digit
# 4. Statistika výskytu délek slov je slovník, kde klíč je daný počet znaků ve slově 
#    a hodnota je četnost výskytu takto dlouhých slov v textu.
# 
# Pozn.: Jedno slovo může patřit do více skupin:
# >>> s = '30N'
# >>> print(s.istitle())
# True
# >>> print(s.isupper())
# True
# -----------------------------------------------------------------------------
workingText = TEXTS[int(option)-1]

for c in ['.', ',', ':', ';']:
    workingText = workingText.replace(c, '')

workingList = workingText.split()

l_title = [f for f in workingList if f.istitle()]
l_upper = [f for f in workingList if f.isupper()]
l_lower = [f for f in workingList if f.islower()]
l_digit = [f for f in workingList if f.isdigit()]

statistic = dict()

for word in workingList:
    statistic[len(word)] = statistic.get(len(word), 0) + 1

# -----------------------------------------------------------------------------
# VÝSLEDNÝ REPORT
#
# Pro sestavení reportu statistiky je použita návratová
# hodnota metody items(), což je pole ntic,
# kde každá ntice je dvojice klíč-hodnota.
# Například dict_items([(4, 2), (5, 2), (2, 1), (7, 1)])
#
# Jelikož je slovník neseřazená kolekce, je třeba ještě použit funkci sorted()
# -----------------------------------------------------------------------------
print(f'\nThere are {len(workingList)} words in the selected text.')
print(f'There are {len(l_title)} titlecase words.')
print(f'There are {len(l_upper)} uppercase words.')
print(f'There are {len(l_lower)} lowercase words.')
print(f'There are {len(l_digit)} numeric strings.')
print(f'The sum of all the numbers {sum([int(i) for i in l_digit])}.\n')

table = PrettyTable()
table.field_names = ['LEN', 'OCCURENCE', 'NR.']
table.align = 'r'
table.align['OCCURENCE'] = 'l'

for foo in sorted(statistic.items()):
    table.add_row([foo[0], '*'*foo[1], foo[1]])

print(table)

# -----------------------------------------------------------------------------
# Příklad výstupu
# -----------------------------------------------------------------------------
# Enter your login: ann
# Enter password for ann: pass123
# ---------------------------------------------
# Welcome to the app, ann!
# We have 4 texts to be analyzed.
# ---------------------------------------------
#
# Enter a number between 1 and 4 to select: 2
# 
# There are 62 words in the selected text.
# There are 10 titlecase words.
# There are 0 uppercase words.
# There are 51 lowercase words.
# There are 1 numeric strings.
# The sum of all the numbers 300.
#
# +-----+-------------------+-----+
# | LEN | OCCURENCE         | NR. |
# +-----+-------------------+-----+
# |   2 | *******           |   7 |
# |   3 | ***************** |  17 |
# |   4 | *********         |   9 |
# |   5 | **********        |  10 |
# |   6 | *******           |   7 |
# |   7 | ***               |   3 |
# |   8 | **                |   2 |
# |   9 | *****             |   5 |
# |  10 | *                 |   1 |
# |  13 | *                 |   1 |
# +-----+-------------------+-----+