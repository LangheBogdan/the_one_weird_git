# Repository-uri potrivite sarcinii

Un catalog pentru alegerea tehnologiilor și a surselor de referință folosite de un coding agent. **Pornim cu zero repository-uri descărcate. Adăugăm unul numai când rezolvă o întrebare concretă din sarcina curentă.**

React, React Native, Svelte și Angular sunt incluse, alături de opțiuni pentru mobile, jocuri, backend, baze de date, API-uri și desktop. Catalogul este extensibil: nu poate enumera întregul ecosistem open source și nu reprezintă o listă de instalare.

## Alege după ce construiești

Acestea sunt recomandări de selecție, nu cerințe ale framework-urilor. Într-un proiect existent, tehnologiile deja folosite au prioritate.

| Sarcină | Punct de plecare | Sursă locală doar dacă apare o întrebare nerezolvată |
| --- | --- | --- |
| Pagină simplă, landing page | HTML + CSS; JavaScript doar pentru interacțiuni | De regulă, niciun repository |
| Blog sau site cu multe pagini de conținut | Astro; WordPress dacă este necesar un CMS | Astro pentru rendering/integrări; WordPress pentru hooks |
| Aplicație web interactivă în React | React; Vite pentru un client simplu | Biblioteca implicată; React intern doar pentru comportament dificil |
| Aplicație React cu routing și server rendering | Next.js | Next.js pentru routing, caching, server/client boundaries |
| Aplicație Svelte | SvelteKit pentru routing și structură de aplicație | SvelteKit pentru framework; Svelte pentru reactivitate/compiler |
| Aplicație Angular | Angular | Angular pentru API-ul sau integrarea folosită |
| Aplicație Vue | Vue; Nuxt dacă sunt necesare funcțiile sale de aplicație | Vue sau Nuxt, conform problemei |
| Aplicație Android/iOS în JavaScript/TypeScript | React Native + Expo | Expo pentru modulele sale; React Native pentru integrarea nativă |
| Aplicație multiplatformă în Dart | Flutter | Pachetul relevant; Flutter intern numai la nevoie |
| Aplicație mobilă pornind de la un UI web | Capacitor + UI-ul existent | Capacitor sau pluginul nativ implicat |
| Joc 2D pentru browser | Phaser | Phaser pentru scene, input, fizică sau lifecycle |
| Joc mobil 2D/3D | Godot; Flame dacă proiectul este deja Flutter și jocul este 2D | Engine-ul ales, numai pentru problema întâlnită |
| Experiență 3D în browser | Three.js sau Babylon.js | O singură bibliotecă de rendering/engine, după cerințe |
| Aplicație desktop cu UI web | Tauri sau Electron | Framework-ul ales pentru IPC și integrarea cu sistemul |
| Citește un API și afișează rezultatul | `fetch` și documentația API-ului | Niciun repository pentru un apel simplu |
| Date de server cu cache, paginare și invalidare | TanStack Query, dacă stack-ul și cerințele îl justifică | TanStack Query; SDK-ul serviciului doar dacă este folosit |
| API backend mic în TypeScript | Hono sau Fastify, după runtime | Framework-ul ales |
| API în Python | FastAPI | FastAPI când documentația și exemplele nu sunt suficiente |
| Aplicație CRUD cu backend complet | Django în Python sau Laravel în PHP | Framework-ul ales; nu ambele |
| Bază de date locală simplă | SQLite + driverul potrivit runtime-ului | Driverul folosit, rareori motorul SQLite |
| Bază de date relațională pentru server | PostgreSQL + driver; ORM doar dacă este util | Driverul sau Drizzle/Prisma; nu motorul PostgreSQL implicit |
| Backend Supabase | SDK-ul limbajului; în JS, `supabase-js` | SDK-ul; platforma întreagă doar pentru self-hosting/debugging intern |
| Magazin WordPress | WooCommerce în WordPress | WooCommerce și componenta WordPress implicată |

Pentru un joc Phaser distribuit ca aplicație mobilă, Capacitor poate fi o opțiune de ambalare, dar performanța și pluginurile trebuie verificate pe dispozitiv. React Native este pentru UI de aplicație; alegerea unui engine de joc se face separat. Detaliile și sursele sunt în [catalogul mobile și jocuri](docs/mobile-game-sources.md).

## Cum folosești catalogul

1. Definește rezultatul: platformă, funcții, tehnologiile existente și cum verifici că funcționează.
2. Alege o singură variantă principală din tabel. Adaugă baze de date, autentificare sau alte biblioteci doar pentru funcții cerute.
3. Consultă documentația versiunii utilizate, exemplele și tipurile deja disponibile.
4. Dacă rămâne o incertitudine, descarcă doar sursa relevantă, fixată la versiunea potrivită. Notează motivul și commit-ul.
5. Oprește extinderea selecției când întrebarea este rezolvată și comportamentul aplicației este verificat.

**Instalarea unei dependențe și descărcarea repository-ului ei sunt acțiuni diferite.** Pachetul instalat rulează în aplicație. Copia din `references/` sau `repos/` este material de studiu și nu se importă în aplicație.

## Fișierele acestui catalog

- [Catalog web, API, backend, date și instrumente](docs/repository-catalog.md)
- [Catalog mobile, jocuri și desktop](docs/mobile-game-sources.md)
- [Descărcare la nevoie și alternativa `git subtree`](docs/on-demand-references.md)
- [Instrucțiuni pentru agent](AGENTS.md)
- [Registrul selecției curente](docs/reference-selection.md)
- [Ideile de bază, plan interactiv](docs/core-ideas.packed.html)
- [Progresul lucrării](TASKS.md)

## Relația cu articolul Effect

[Articolul Effect](https://effect.website/blog/the-one-weird-git-trick-that-makes-coding-agents-more-effect-ive) propune păstrarea surselor dependențelor în proiect folosind `git subtree`, pentru a putea fi explorate de agent. Aici adaptăm ideea la selecția cerută: catalog larg, surse locale puține, alese pentru sarcina concretă. Beneficiul nu presupune clonarea tuturor tehnologiilor și nici adoptarea Effect în fiecare aplicație.

Sursele au fost consultate la **1 octombrie 2026**. Nu este fixată o listă universală de versiuni: fiecare proiect își alege referințele după dependențele sale reale.
