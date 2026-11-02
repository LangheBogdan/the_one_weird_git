# Declanșatorul de aprobare

Skill-ul care adaugă repository-uri de referință pornește numai după aprobarea planului și autorizarea tehnologiilor. Ambele se citesc dintr-un singur loc: frontmatter-ul YAML din [`docs/implementation-plan.md`](implementation-plan.md). O aprobare dată doar în chat nu declanșează skill-ul.

## Ce înseamnă „plan aprobat”

Toate condițiile trebuie îndeplinite:

1. `status` are exact valoarea `approved`.
2. `approved_by` conține login-ul GitHub al persoanei care aprobă.
3. `approved_on` conține o dată în formatul `YYYY-MM-DD`.
4. Secțiunile `Rezultat`, `Platformă și stack existent` și `Criteriu de acceptare` sunt completate.
5. `approved_hash` conține amprenta planului aprobat (vezi [Când aprobarea expiră](#când-aprobarea-expiră)).

## Ce înseamnă „tehnologie autorizată”

Fiecare intrare din `technologies` trebuie să aibă:

| Câmp | Regulă |
| --- | --- |
| `name` | Numele scurt, folosit și în calea `references/<name>/` |
| `package` | Numele pachetului din manifest |
| `version` | Versiunea exactă instalată; intervalele precum `^3.0.0`, `~3.1`, `3.x`, `>=3` sau `*` sunt respinse |
| `repository` | URL-ul oficial, fără credențiale |
| `authorized` | `true` |
| `open_question` | Opțional: întrebarea concretă la care răspunde sursa |

Lista nu poate fi goală. Dacă o singură intrare nu este autorizată sau nu are versiune exactă, skill-ul se oprește și raportează intrarea, fără descărcări parțiale.

## Autorizat nu înseamnă descărcat

Autorizarea permite o descărcare; nu o cere. Conform regulilor 3 și 8 din [`AGENTS.md`](../AGENTS.md), skill-ul ia în calcul numai intrările cu `open_question`, una câte una, și se oprește când întrebarea are răspuns. Fiecare descărcare se înregistrează în [registrul selecției](reference-selection.md). Zero descărcări este un rezultat valid.

## Când aprobarea expiră

Orice modificare a listei `technologies` sau a criteriului de acceptare după aprobare readuce `status` la `draft`. Planul trebuie aprobat din nou înainte ca skill-ul să ruleze.

Regula este verificată automat prin `approved_hash`, o amprentă `sha256` calculată din lista `technologies` și din textul secțiunii `Criteriu de acceptare` (fără comentariile HTML). Câmpul `approved_hash` nu intră în calcul. Restul planului, de exemplu `Pași`, se poate modifica fără o nouă aprobare.

La aprobare, după ce ai citit planul:

```bash
python3 scripts/check_repo.py --plan-hash
```

Copiază valoarea afișată în `approved_hash`, împreună cu `status: approved`, `approved_by` și `approved_on`. Dacă după aceea se schimbă o versiune, un URL sau criteriul de acceptare, amprenta nu mai corespunde și CI-ul eșuează până la o nouă aprobare.

## Verificarea automată

CI-ul rulează [`scripts/check_repo.py`](../scripts/check_repo.py) la fiecare push în `main` și la fiecare PR. Pentru un plan cu `status: approved`, scriptul verifică regulile de mai sus și eșuează dacă una nu este îndeplinită. Textul ajutător din secțiunile planului este scris în comentarii HTML, deci o secțiune care conține doar comentariul este considerată goală. Rulează local cu `python3 scripts/check_repo.py`.
