# Funktioner!

## Nomenklatur

Termer som används och vad de betyder i sammanhanget:

**Definiera:**

Att berätta vad något betyder. I Python använder man termen t.ex. när man
skapar eller ändrar på en variabel. Används även när man skapar egna Funktioner
och Klasser. Klasser kommer vi gå igenom i en senare lektion.

**Funktion:**

En samling kod som namngivits för att lätt kunna återanvändas. En instruktion
till datorn.

**Objekt:**

En samling data och instruktioner om hur man interagerar med den. T.ex. via
Metoder som ligger i Objektet eller med operatorer. (`+`, `-`, `*`, etc.)

**Metod:**

En Funktion som ligger i ett Objekt. (Eller en Klass, men det är utanför
grundkursen.)

**Argument:**

Det man skickar till en Funktion.

**Returnera:**

Att skicka tillbaka.

## SYNTAX ÄR JÄTTEVIKTIGT

Python är ett objektorienterat programmeringsspråk. Vi kommer att tala mer om
Objekt i Lektion09.

## Namespaces / Namnrymder

Namespaces / Namnrymder är avskiljningar för att hålla namn unika.

Exempel: Postnummer, epost, telefonnummer

Exempel: info@misa.se

## Olika namn för Funktioner

Funktioner kallas för olika saker i olika programmeringsspråk:

```text
Funktioner = Procedurer = Subrutiner
Functions = Processes = Sub-routines
```

## Argument

Argument = Det man skickar till en Funktion eller Metod.

Man "skickar" Argument genom att skriva in det som ska skickas mellan
parenteserna när man "anropar" en Funktion.

**Positional Arguments / Positionsargument:**

Argument där ordningen man skriver dem i spelar STOR roll.

**Keyword Arguments / Nyckelordsargument:**

Argument där man anger namn på Argumenten för att särskilja dem.

## Matematiska Funktioner och Funktioner i Python

Matematiska Funktioner ser väldigt liknande ut som Funktioner i Python:

Matte:

```text
f(x) = x * 2
eller
y = x * 2
```

Python:

```python
def f(x):
    return x * 2
```

## Typannoteringar för returvärden

Precis som vi i Lektion 2 lärde oss att annotera variabler (`namn: str = "Alex"`),
kan vi annotera vad en funktion förväntas returnera.

Returtypen skrivs med en pil `->` efter parameterparenteserna, före kolonet:

```python
def f(x) -> int:
    return x * 2
```

Om en funktion inte returnerar något värde (utan bara utför en handling,
t.ex. skriver ut text med `print()`), returnerar den i Python i själva verket
värdet `None`. Då annoterar vi returtypen som `-> None`:

```python
def hej() -> None:
    print("Hej!")
```

Precis som för variabler är typannoteringar i Python **beskrivande och
dokumenterande.** De orsakar inte att programmet kraschar om fel typ
returneras vid körning, men hjälper utvecklare och utvecklingsmiljöer (som
PyCharm) att förstå och hitta fel i koden.

## Designprincip i Python

```text
DRY
Don't Repeat Yourself
Upprepa Dig Inte
```

Ska man göra samma sak flera gånger är det alltså bättre att "bryta ut" den
saken till en Funktion, precis som man använder loopar för att inte behöva
skriva samma sak om och om igen.
