# Variabler = Variabla värden

## Datatyper

Variabler är saker vi sparar i datorns minne.  
Datatyper är HUR vi sparar data.

`Syntax = Grammatik`

## Typer av Datatyper

- Vissa Datatyper kan bara innehålla en sak, ofta bara en specifik typ av sak.
  Jag kallar dessa Datatyper för "simpla datatyper".
- Samlingsdatatyper, Datatyper som kan innehålla flera saker.

Varje sak som ligger i en variabel av en samlingsdatatyp kallas för Element.

## Datatyper som bara kan innehålla en sak ("simpla datatyper")

| Internt namn | Betydelse | Exempel |
| --- | --- | --- |
| `str` | String = Text | `"Hej, hallå!"`, `'Hej, hallå!'`, `"""Hej, hallå!"""`, `'''Hej, hallå!'''` |
| `int` | Integer = Heltal | `2` |
| `float` | Float (Floating point number) = Flyttal/Decimaltal | `2.0` |
| `bool` | Boolean = Sant/Falskt | `True` eller `False` |

## Samlingsdatatyper

### list

List = Lista; Kan ses på som en bokhylla, allt står i en viss ordning.

```python
x = [1, 2, 3]
```

### tuple

Tuple = Kan ses på som en bokhylla, allt står i en viss ordning men någon har
superlimmat fast allting.

```python
x = (1, 2, 3)
```

### dict

Dictionary = Ordbok

`nyckel:värde / key:value`

Nycklar får inte kunna ändras på och de måste vara unika.

```python
x = {2: "två", "ålder": 36}
johan = {"namn": "Johan", "ålder": 36, "längd": 180}
emma = {"namn": "Emma", "ålder": 35, "längd": 174, "ålder": 36}
```

### set

Set = Mängd; Kan ses på som en låda, allt hamnar där det får plats. Det får
bara finnas en av varje sak. Det som läggs i lådan får inte kunna gå att ändra
på.

```python
x = {1, 2, 3}
```

## Referens för snabb översikt

- `list` skapas med `[]`
- `tuple` skapas med `()`
- `dict` skapas med `{}` och måste vara i `nyckel:värde`-format
- `set` skapas med `{}`. Se nedan för ett viktigt undantag och förtydligande.

När man skapar samlingsvariabler så kan de vara tomma, t.ex. `a = ()`, men det
finns ett viktigt undantag:

För att skapa ett tomt set så kan man inte skriva `a = {}`, då blir det ett
tomt dictionary. Vad man måste göra är att skriva `a = set()`, då blir det ett
tomt set.

## Konkatenering

Konkatenering är att slå ihop två saker, t.ex. strängar, genom att lägga dem
efter varandra.
