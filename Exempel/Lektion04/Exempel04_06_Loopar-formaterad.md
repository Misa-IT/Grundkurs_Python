# Flödeskontroll del 2, Loopar

## Nomenklatur

Termer som används och vad de betyder i sammanhanget:

**Element:**

En sak i en samling. T.ex. "Första elementet i en lista."

**Iterera:**

Upprepa

**Itereringsvariabel:**

Den variabel man kollar på vid varje varv av en loop. Kan också kallas
upprepningsvariabel.

## Ett exempel på en dåligt formulerad instruktion

Instruktion: Applicera schampo, skölj ur och upprepa.

```text
Applicera schampo
Skölj ur
Applicera schampo
Skölj ur
[...]
```

I Python finns det while-loopar och for-loopar.

## while-loopar

```text
Så länge som [Något] stämmer så gör detta:
    [Instruktioner]

While [Something] is True do this:
    [Instructions]
```

```python
while [Nånting]:
    [Instruktioner]
```

## for-loopar

```text
För varje element i [Samling] så gör detta:
    [Instruktioner]

For each element in [Collection] do this:
    [Instructions]

For each element in [Collection], call the thing [Name], and do this:
    [Instructions]
```

```python
for [Sak/Itereringsvariabel] in [Samling]:
    [Instruktioner]
```
