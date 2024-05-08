# Skriv färdigt programmet så att det skriver ut namnet på den månad som
# representeras av den inskrivna siffran.
# Programmet ska också säga åt användaren an skriva in ett giltigt tal
# nästa gång OM användaren skriver in något som är utanför önskat
# spann på 1 till 12.

# TODO: Lägg till något om att man inte behöver skriva alla tolv.

month = int(input("Skriv in en siffra mellan 1 och 12: "))
if month == 1:
    print("Januari")


print("Vänligen skriv in en giltig siffra nästa gång.")