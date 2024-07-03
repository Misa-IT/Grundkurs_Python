## Klasser & Objekt! 

| Nomenklatur<br>(vad man menar med en specifik fras eller ord) |                                                                                                                                                                                                                 |
|---------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Objektorienterad programmering                            | En typ av programmering där man använder sig av Objekt för att dela upp data och funktionalitet.<br/>Inkapsling är en av de viktigaste bitarna och vi känner till det begreppet sen tidigare med namnet namespace. |
| Objekt                                                        | En grupp data och instruktionerna för datorn om hur man behandlar sagda data.<br/>En Instans av en Klass.<br/>Om Klassen är en pepparkaksform så är Objekt pepparkakorna som vi skapar med hjälp av formen.|
| Klass                                                         | En 'ritning' för en typ av Objekt.<br/>Precis som en pepparkaksform kan användas för att göra flera pepparkakor så kan en Klass användas för att skapa flera objekt.|
| Instans                                                       | En specifik kopia av ett koncept.<br/>T.ex. en specifik bok istället för konceptet böcker.<br/>En term man använder för att vara tydlig med att man pratar om t.ex. en specifik lista (alltså ett list-objekt) och inte list-objekt i allmänhet.|
| Metoder                                                       | Funktioner som ligger i Objekt. \(Eller i en Klass men det är utanför grundkursen.\)<br/>Har alltid argumentet self i de situationer vi går igenom i grundkursen.                                             |
| Attribut                                                      | Egenskaper hos Objekt. Oftast är de data/variabler och metoder.                                                                                                                                                       |
| Konstruktor                                                   | \_\_init\_\_-metoden som körs när man skapar ett Objekt.                                                                                                                                                        |
| Arv                                                           | När man använder sig av en annan 'ritning' \(en annan Klass\) för att påbörja en ny 'ritning' \(en ny Klass\).<br/>En Klass kan ärva från mer än en Klass.                                                                                                         |

Exempelstruktur:

    Klass = Bok
    Klass som ärver från Bok = Pocketbok(Bok)
    Klass som ärver från Pocketbok och en annan Klass = SaganOmRingenSomPocket(Pocketbok, SaganOmRingen)
    Objekt som skapas från klassen SaganOmRingenSomPocket = Ett specifikt exemplar av den boken.