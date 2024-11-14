# Parcijalni ispit - Napredni koncepti programiranja u programskom jeziku Python

## Upute za Rješavanje Zadatka

### Priprema okruženja
1. Kreirajte **fork** repozitorija na GitHubu: [https://github.com/algebra-pydev/parcijalni-ispit-03-napredni-koncepti-programiranja-u-programskom-jeziku-python](https://github.com/algebra-pydev/parcijalni-ispit-03-napredni-koncepti-programiranja-u-programskom-jeziku-python).
2. Imenovanje repozitorija u formatu `pydev_parcijalni_ime_prezime` (primjer: `pydev_parcijalni_pero_peric`).
3. **VAŽNO:** Nemojte kreirati "clone" repozitorija jer nemate pravo mijenjanja.

### Postavljanje Projekta
1. Nakon što ste kreirali fork, klonirajte repozitorij s vašeg GitHub profila na lokalno računalo.
2. Postavite novo virtualno okruženje pomoću `venv`.
3. Instalirajte sve potrebne module koristeći `requirements.txt` kako biste osigurali da aplikacija ima sve potrebne biblioteke.

---

### Struktura Aplikacije i Pristup Bazi Podataka
- Aplikacija koristi **modularnu** i **objektno-orijentiranu** strukturu s podjelom na slojeve:
  - **UI Layer**
  - **Service Layer**
  - **Repository Layer**
- **Folderi po funkcionalnostima** uključuju slojeve i module specifične za funkcionalnosti i pristup SQLite bazi podataka.

---

### Zadaci za Implementaciju (Skraćeni Opseg)

1. **Ponude (Offers)**:
   - **Dohvaćanje svih ponuda** i **dohvaćanje ponude po ID-u** pomoću SQLite baze podataka.
   - **Kreiranje nove ponude** s automatskim izračunom iznosa (sub_total, tax, total).
   - Implementirati potrebne funkcije samo u **sqlite3 repozitoriju**.

2. **Proizvodi (Products)**:
   - **Dohvaćanje svih proizvoda** i **dodavanje novog proizvoda**.
   - Implementirati repozitorij s pristupom bazi koristeći samo SQLAlchemy.

3. **Korisnici (Users)**:
   - **Dohvaćanje podataka o korisnicima** s REST API-ja [JSONPlaceholder Users](https://jsonplaceholder.typicode.com/users).
   - Implementirajte repozitorij koji dohvaća podatke putem API-ja i omogućuje njihovo prikazivanje u aplikaciji.

4. **Kupci (Customers)**:
   - **Dohvaćanje svih kupaca** i **dodavanje novog kupca** pomoću SQLite baze podataka.
   - Implementirati potrebne funkcije samo u **sqlite3 repozitoriju**.

---

### Zadaci po Funkcionalnostima (Detalji)

#### 1. Ponude (Offers)
   - **sqlite3 repozitorij**:
     - `get_all_offers`: dohvaća sve ponude iz baze.
     - `get_offer_by_id`: dohvaća specifičnu ponudu prema ID-u.
     - `create_offer`: kreira novu ponudu u bazi, dodaje podatke o stavkama i računa iznos.

   - Polaznici trebaju dopuniti kod i implementirati funkcije u `repository_sqlite.py`, a zatim testirati funkcionalnost pomoću UI sloja.

#### 2. Proizvodi (Products)
   - **SQLAlchemy repozitorij**:
     - `get_all_products`: dohvaća sve proizvode iz baze.
     - `add_product`: dodaje novi proizvod u bazu.

   - Polaznici trebaju dopuniti SQLAlchemy repozitorij s ovim funkcijama. Servisni sloj koristi ove funkcije za rad s proizvodima.

#### 3. Korisnici (Users)
   - **REST API repozitorij**:
     - `get_all_users`: dohvaća sve korisnike s API-ja JSONPlaceholder.

   - Polaznici trebaju implementirati funkciju za dohvaćanje svih korisnika pomoću API-ja i prikazati ih u UI sloju.

#### 4. Kupci (Customers)
   - **sqlite3 repozitorij**:
     - `get_all_customers`: dohvaća sve kupce iz baze.
     - `add_customer`: dodaje novog kupca u bazu.

   - Polaznici trebaju dopuniti SQLite repozitorij za funkcionalnost `customers` te testirati u UI sloju.

---

### Primjer Rješavanja Zadatka

#### Početni Kod Funkcije
```python
# TODO: Implementirati funkciju za dohvaćanje svih ponuda
def get_all_offers():
    pass
```

#### Implementirani Kod Funkcije
```python
def get_all_offers():
    query = "SELECT * FROM offers"
    cursor = self.connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    return results
```

> **Napomena:** Funkcija `get_all_offers` koristi SQL upit za dohvaćanje svih ponuda iz baze. Prilikom implementacije obratite pažnju na sve komentare označene `#TODO` i slijedite predloženu strukturu koda.

---

### Dodatne Upute

- Nemojte mijenjati druge dijelove aplikacije. Ako vaša implementacija ne radi, prilagodite svoje rješenje aplikaciji, a ne obrnuto.
- Koristite `TypeHints` prema uputama u komentarima kako biste osigurali konzistentnost tipova podataka.

---

### Podnošenje Rješenja

1. Nakon što završite implementaciju:
   - Napravite commit za sve promjene koje ste unijeli koristeći opciju `git commit`.
   - Pushajte promjene na vaš GitHub repozitorij pomoću `git push`.

2. **Podjela Repozitorija s Predavačem**:
   - Otvorite vaš repozitorij na GitHubu.
   - Kliknite na karticu **Settings** u repozitoriju.
   - Pronađite opciju **Collaborators** i dodajte predavača kao **Contributor**.
   - Unesite GitHub korisničko ime predavača i pošaljite pozivnicu za pristup.
   - **VAŽNO**: Uvjerite se da su sve potrebne promjene commitane i pushane prije dodavanja predavača, kako bi predavač mogao vidjeti kompletno rješenje.

**Sretno!**
