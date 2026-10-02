# Descărcare doar la nevoie

## Alegerea metodei

| Situație | Metodă |
| --- | --- |
| Documentația sau exemplele rezolvă întrebarea | Nicio descărcare |
| Agentul trebuie să citească implementarea pentru sarcina curentă | Checkout local în `references/<name>/`, exclus din Git |
| Echipa trebuie să primească aceeași sursă odată cu proiectul | `git subtree --squash` în `repos/<name>/` |

Recomandarea pentru acest catalog este checkout-ul local la nevoie. `git subtree` rămâne disponibil pentru referințe comune și persistente, după modelul [articolului Effect](https://effect.website/blog/the-one-weird-git-trick-that-makes-coding-agents-more-effect-ive). Folderul de față nu este încă un repository Git valid; nu am inițializat Git și nu am descărcat surse.

## Înainte de descărcare

Identifică pachetul din manifest și versiunea exactă din lockfile sau SDK. Verifică repository-ul oficial și tag-ul care corespunde acelei versiuni. Un monorepo poate avea tag-uri pe pachet, nu un simplu `v<version>`. Dacă nu poți stabili corespondența, consemnează incertitudinea; nu o înlocui tacit cu `main`.

Completează motivul în [registrul selecției](reference-selection.md). Exemplele de mai jos sunt **șabloane Bash**, nu comenzi executate în această lucrare. Înlocuiește toate valorile `REPLACE_...` înainte de folosire. Rulează din rădăcina proiectului în care este autorizată descărcarea, nu într-un proiect diferit.

## Checkout local la un tag verificat

```bash
reference_url='https://github.com/REPLACE_OWNER/REPLACE_REPOSITORY.git'
reference_tag='REPLACE_WITH_VERIFIED_RELEASE_TAG'
reference_path='references/REPLACE_WITH_LIBRARY_NAME'

git clone --depth 1 --single-branch --branch "$reference_tag" \
  "$reference_url" "$reference_path"
```

Continuă numai după ce clonarea reușește:

```bash
git -C "$reference_path" rev-parse HEAD
git -C "$reference_path" describe --tags --exact-match HEAD
```

Înregistrează SHA-ul complet, tag-ul, versiunea, licența și calea în registru. `--depth 1` limitează istoricul; nu limitează numărul fișierelor din versiunea descărcată. `--branch` acceptă un tag, caz în care checkout-ul este detached. Aceste opțiuni sunt documentate în [manualul `git clone`](https://git-scm.com/docs/git-clone).

Nu reutiliza o cale existentă pentru o altă versiune și nu șterge copia veche automat. Pentru un upgrade, folosește o cale nouă, notează schimbarea și verifică din nou exemplele. Dacă checkout-ul nu se reproduce la SHA-ul înregistrat, raportează diferența înainte să-l folosești ca referință.

`references/` este deja în `.gitignore`. Într-un alt proiect, adaugă aceeași regulă înainte de a crea checkout-uri interne. Copiile nu vor apărea în clonele colegilor: registrul este cel care explică ce trebuie refăcut. Nu executa un `git add` forțat asupra acestor checkout-uri.

## `git subtree` pentru surse urmărite în Git

Folosește metoda doar într-un repository valid, cu un commit inițial, identitate Git configurată și working tree curat. Verifică mai întâi starea; nu face automat commit sau stash pentru modificările utilizatorului. Directorul destinație trebuie să fie nou.

```bash
git rev-parse --show-toplevel
git status --short
git subtree -h
```

După verificarea condițiilor și a tag-ului:

```bash
reference_url='https://github.com/REPLACE_OWNER/REPLACE_REPOSITORY.git'
reference_tag='REPLACE_WITH_VERIFIED_RELEASE_TAG'
reference_prefix='repos/REPLACE_WITH_LIBRARY_NAME'

git subtree add --prefix="$reference_prefix" \
  "$reference_url" "$reference_tag" --squash
```

Pentru actualizarea unei referințe deja existente, doar când proiectul are nevoie de versiunea respectivă:

```bash
reference_tag='REPLACE_WITH_VERIFIED_TARGET_TAG'
git subtree pull --prefix="$reference_prefix" \
  "$reference_url" "$reference_tag" --squash
```

`subtree add` creează automat un commit de integrare. `--squash` comprimă istoricul upstream importat, nu conținutul sursei; pot exista atât commit-ul squash, cât și commit-ul de integrare. Sursa devine parte din proiect și crește dimensiunea lui. Vezi [manualul `git subtree`](https://github.com/git/git/blob/master/contrib/subtree/git-subtree.adoc).

Păstrează licențele upstream și înregistrează commit-ul sursei importate, distinct de commit-ul creat în proiect. Confirmă-l din tag-ul upstream și metadatele `git-subtree-split` ale commit-ului squash. Nu adăuga `repos/` în `.gitignore` dacă ai ales să urmărești aceste fișiere în Git. Nu combina cele două metode în aceeași cale și nu publica modificări în repository-ul upstream.

## Cum citește agentul sursa

Pornește de la exemple și teste relevante, apoi urmărește API-ul până în implementare. Pentru un checkout ignorat, caută explicit numai acolo:

```bash
rg --files --hidden --no-ignore -g '!.git/**' references/REPLACE_WITH_LIBRARY_NAME
```

Într-un proiect de aplicație, exclude `references/` și `repos/` din build, lint, descoperirea testelor, watchers și sugestii de auto-import, potrivit instrumentelor sale. Acest catalog nu adaugă configurație pentru un editor sau un build încă neales.

Nu importa aplicația din copia de referință și nu instala automat dependențele acelei copii. O sursă locală ajută cercetarea; rezultatul se confirmă în aplicația reală. Oprește descărcările când întrebarea este rezolvată.

## Limitele verificării acestei lucrări

Sintaxa a fost comparată cu documentația Git și cu help-ul local `git subtree`. Nu am executat clonarea, importul sau actualizarea unui subtree: utilizatorul a cerut catalog și descărcare numai la nevoie. Nu există o versiune de aplicație pentru care să alegem acum tag-uri reale. Comenzile pentru Git nu se aplică direct repository-ului Fossil al SQLite.
