# Parcijalni ispit - Napredni koncepti programiranja u programskom jeziku Python

## Zadaci

1. Refaktorirati postojeće rješenje iz Modula 2 kako bi koristili modularnu arhitekturu.
2. Uvesti SQLite bazu podataka za trajno pohranjivanje podataka umjesto JSON datoteka.
3. Kreirati REST API klijent za dohvaćanje podataka o korisnicima i prikazivanje prijavljenog korisnika.
4. Razdvojiti korisničko sučelje u zaseban modul i proširiti ga prikazom korisnika i tvrtke u zaglavlju.


## Upute za Rješavanje Zadatka

1. **Priprema okruženja:**
   - Kreirajte "fork" repozitorija na GitHubu.
   - Dodijelite repozitoriju naziv u formatu `pydev_parcijalni_ime_prezime` (primjer: `pydev_parcijalni_pero_peric`). 
   - **VAŽNO:** Nemojte kreirati "clone" repozitorija jer nemate pravo mijenjanja.

2. **Postavljanje Projekta:**
   - Nakon što ste kreirali fork, klonirajte repozitorij s vašeg GitHub profila na lokalno računalo koristeći GitHub Desktop ili drugu omiljenu metodu.
   - Uklonite postojeće virtualno okruženje ako je prisutno i kreirajte novo koristeći `venv` (Python virtualno okruženje).
   - Instalirajte sve potrebne module pomoću `requirements.txt` kako biste osigurali da aplikacija ima sve potrebne biblioteke.

3. **Refaktoriranje postojećeg koda:**
   - Kreirajte direktorij `models/` i unutar njega kreirajte module:
     - `customer_model.py` za rad s kupcima.
     - `product_model.py` za rad s proizvodima.
     - `offer_model.py` za rad s ponudama.
   - Svaki modul treba sadržavati klasu koja predstavlja odgovarajuće entitete (npr. `Customer`, `Product`, `Offer`), uključujući metode za interakciju s bazom podataka.

4. **Kreiranje SQLite baze podataka:**
   - Dodajte datoteku `database.py` koja sadrži klasu za upravljanje bazom (koristeći `sqlite3`).
   - Kreirajte tablice za `customers`, `products`, i `offers`.
   - Implementirajte metode za:
     - Dodavanje novih zapisa.
     - Ažuriranje postojećih zapisa.
     - Dohvaćanje zapisa na temelju upita.

5. **REST API integracija:**
   - Kreirajte direktorij `services/` i unutar njega modul `user_service.py`.
   - Koristite biblioteku `requests` za dohvaćanje podataka s endpointa `https://jsonplaceholder.typicode.com/users`.
   - Implementirajte metodu koja dohvaća podatke o korisnicima i omogućuje korisniku odabir jednog korisnika kao trenutno prijavljenog.

6. **Korisničko sučelje:**
   - Kreirajte modul `user_interface.py` koji:
     - Generira tekstualni izbornik i prikazuje opcije.
     - Prikazuje podatke o prijavljenom korisniku i tvrtki u zaglavlju.
   - Proširite sučelje tako da, uz trenutne funkcionalnosti, uvijek prikazuje:
     - Ime i email prijavljenog korisnika.
     - Informacije o tvrtki (npr. naziv, email, VAT ID).

7. **Implementacija logike za prijavljenog korisnika:**
   - U glavnom modulu (`main.py`) inicijalizirajte prijavljenog korisnika koristeći REST API integraciju.
   - Prikazujte podatke o prijavljenom korisniku u svim dijelovima aplikacije.


#### Očekivani rezultat:
- Aplikacija koristi SQLite za trajno pohranjivanje podataka.
- Kod je organiziran u module (`models`, `services`, `user_interface`).
- Korisničko sučelje je unaprijeđeno i modularizirano.
- API integracija omogućuje dinamičko prikazivanje podataka o korisnicima.

#### Primjer strukture direktorija:
```
offers_calculator/
│
├── main.py
├── database.py
├── user_interface.py
├── services/
│   └── user_service.py
├── models/
│   ├── customer_model.py
│   ├── product_model.py
│   └── offer_model.py
└── db.sqlite3
```

#### Napomena:
- Prilikom implementacije vodite računa o modularnosti i slojevima aplikacije. Koristite klase za sve glavne funkcionalnosti i pridržavajte se zadane strukture aplikacije.

### Dodatne Upute

- Nemojte mijenjati druge dijelove aplikacije. Ako Vaša implementacija ne radi, prilagodite svoje rješenje aplikaciji, a ne obrnuto.
- Koristite `TypeHints` za sve metode kako biste osigurali konzistentnost tipova podataka.

## Podnošenje Rješenja

1. Nakon što završite implementaciju:
   - Napravite commit za sve promjene koristeći `git commit`.
   - Pushajte promjene na vaš GitHub repozitorij koristeći `git push`.

2. **Podjela Repozitorija s Predavačem**:
   - Otvorite vaš repozitorij na GitHubu.
   - Kliknite na karticu **Settings** u repozitoriju.
   - Pronađite opciju **Collaborators** i dodajte predavača kao **Contributor**.
   - Unesite GitHub korisničko ime predavača i pošaljite pozivnicu za pristup.
   - Provjerite da su sve promjene commitane i pushane prije dodavanja predavača.

**Sretno!**
