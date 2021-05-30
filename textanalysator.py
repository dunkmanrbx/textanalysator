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

'''petr David, ADAM 10 Martina, ANNIE bela. Pepa'''
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
isOK = option.isdigit() and int(option) in range(1, numOfTexts+1) # range je bez posledniho prvku, takze +1
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
    statistic[len(word)] = 1 if len(word) not in statistic else statistic[len(word)] + 1

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
midColLength = max(statistic.values()) + 3
maxKeyLength = len(str(max(statistic.keys())))
header = f'LEN| OCCURENCE{" "*(midColLength-len("OCCURENCE"))}| NR.'

print(f'\nThere are {len(workingList)} words in the selected text.')
print(f'There are {len(l_title)} titlecase words.')
print(f'There are {len(l_upper)} uppercase words.')
print(f'There are {len(l_lower)} lowercase words.')
print(f'There are {len(l_digit)} numeric strings.')
print(f'The sum of all the numbers {sum([int(i) for i in l_digit])}.\n')
print('-' * len(header))
print(header)
print('-' * len(header))

for foo in sorted(statistic.items()):
    print(
        f'{" "*(maxKeyLength-len(str(foo[0])))}'
        f'{foo[0]} '
        f'| {"*"*foo[1]}'
        f'{" "*(midColLength-foo[1])}'
        f'| {foo[1]}'
    )

print('-' * len(header))

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
# ------------------------------
# LEN| OCCURENCE           | NR.
# ------------------------------
#  2 | *******             | 7
#  3 | *****************   | 17
#  4 | *********           | 9
#  5 | **********          | 10
#  6 | *******             | 7
#  7 | ***                 | 3
#  8 | **                  | 2
#  9 | *****               | 5
# 10 | *                   | 1
# 13 | *                   | 1
# ------------------------------
