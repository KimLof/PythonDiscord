# Discord Bot -projekti

Tämä on yksinkertainen Discord-botti, joka tarjoaa perustoimintoja, kuten käyttäjien puhekanavilla viettämän ajan seurannan ja satunnaisvastausten antamisen käyttäjien kysymyksiin.

## Käyttöönotto

Seuraavat ohjeet auttavat sinua saamaan botin toimimaan Discord-palvelimellasi.

### Edellytykset

- Python 3.6 tai uudempi
- discord.py-kirjasto
- Pythonin `dotenv`-kirjasto ympäristömuuttujien käsittelyyn (valinnainen)

### Asennus

1. Kloonaa repositorio koneellesi.
    ```bash
    git clone https://github.com/KimLof/PythonDiscord.git
    ```

2. Asenna tarvittavat Python-kirjastot.
    ```bash
    pip install -r requirements.txt
    ```

3. Luo `config.py`-tiedosto projektin juureen ja lisää siihen Discord-bot-tokenisi. Alempana lisää tietoa tästä kohdassa 2.
    ```plaintext
    TOKEN = SinunBotTokenisiTähän
    ```

4. Käynnistä botti.
    ```bash
    python bot.py
    ```

### Botin lisääminen Discord-palvelimelle

1. Mene Discord Developer -portaaliin ja luo uusi sovellus.
2. Luo bot-käyttäjä sovelluksellesi ja kopioi bot-token.
3. Luo OAuth2 URL "OAuth2 URL Generator" -työkalulla. Valitse "bot" skoopiksi ja määritä tarvittavat oikeudet.
4. Avaa generoitu URL selaimessasi ja lisää botti haluamallesi Discord-palvelimelle.

## Komennot

Bot tukee seuraavia komentoja:

- `!hei`: Bot vastaa tervehdyksellä.
- `!kysy`: Bot antaa satunnaisen vastauksen määritellystä tiedostosta.
- `!aika`: Näyttää, kuinka kauan olet ollut nykyisellä puhekanavalla.
- `!kokonaisaika`: Näyttää kokonaisajan, jonka olet viettänyt puhekanavilla.

`!kysy` tarvitsee juuteen kysy.txt tiedoston. Sinne voi lisätä vastauksia erotellen rivinvaihdolla. Botti valitsee satunnaisesti niistä yhden vastauksen kun `!kysy` kutsutaan.

