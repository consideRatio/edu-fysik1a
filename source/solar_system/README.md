# Kodplanering

lösning:
    fundering om scope:
        - kan de medskickade funktionerna utnyttja en funktion definierad i början? Blir relevant att anropa en "beräkna avståndsfunktion". En workaround är att skapa en setup distance...
    given simulering behövs konfigureras .setup()
        setup tar emot en funktion som uppdaterar parametrar...
        set_r
        set_v
        set_a
    given simulering kan därefter startas .run()

class SSObj:
    1 - set_r()
    2 - set_v()
    3 - set_a()

class SSSim:
    1 - setup()
    2 - run()



## Allt möjligt...
- Jupyterfiler bör ej uppdateras när jag committar, men det är okej att uppdatera filer jupyterfilen hänvisar till.

## Kodtester
- Ett kodtest ska finnas för varje kodkomplettering.
- Vissa kodkompletteringar avslutas med en simulering.

# Instruktioner

# Kodkomplettering 1
update_r(obj1, t) - Uppdatera r utifrån r, v och t.
* Simulering 1: Jorden åker åt vänster

# Kodkomplettering 2
update_v(obj1, t) - Uppdatera v utifrån v, a och t.
* Simulering 2: Jorden åker åt vänster och accelererar neråt.

# Kodkomplettering 3
update_a(obj1) - Uppdatera a utifrån F och m.
* Simulering 3: Jorden åker åt vänster och accelererar neråt.

# Kodkomplettering 4
get_distance(obj1, obj2) - Beräkna |r2-r1| utifrån två objekt (r1 och r2).

# Kodkomplettering 5
get_direction(obj1, obj2) - Beräkna r2 - r1 och normalisera vektorn

# Kodkomplettering 6
get_G() - Ange G

# Kodkomplettering 7
get_F(obj1, obj2) - Beräkna och returnera kraften på obj1 av obj2.
* Simulering 4: Ett föremål påverkas enkeltriktat av ett annat.

# Kodkomplettering 8
add_contributing_F(obj_array) - Lägg till bidragen krafter

# Kodkomplettering 9
update_F(obj_array) - Uppdatera F utifrån F_parts 
* Simulering 5: Flera föremål påverkas av varandra.

# Kodkompletetring 10
set_initial_conditions() - 
* Simulering 6: Simulerar utifrån elevens indata 


