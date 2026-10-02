# Catalog de repository-uri: web, API, backend și date

Verificat prin documentația și repository-urile oficiale la 1 octombrie 2026. Linkul din fiecare rând este sursa primară pentru rolul tehnologiei. Coloana despre descărcare exprimă recomandarea acestui catalog, nu o obligație impusă de autorii bibliotecii.

Acestea sunt alternative și extensii condiționate de sarcină. Nu le instala și nu le clona împreună. Pentru fiecare sursă descărcată se verifică versiunea, structura și licența acelui commit; disponibilitatea pe GitHub nu înlocuiește licența.

## Web și UI

| Tehnologie și sursă | Rol | Când merită sursa locală |
| --- | --- | --- |
| [React](https://github.com/react/react) | Bibliotecă pentru UI bazat pe componente | Comportament intern, reconciliere sau integrare neclară; nu pentru un formular obișnuit |
| [Next.js](https://github.com/vercel/next.js) | Framework de aplicație pentru React | Routing, rendering, caching sau server/client boundaries |
| [Svelte](https://github.com/sveltejs/svelte) | UI și compiler | Reactivitate, compilare sau interop dificil |
| [SvelteKit](https://github.com/sveltejs/kit) | Framework de aplicație pentru Svelte | Routing, loading, actions și adapters |
| [Angular](https://github.com/angular/angular) | Framework de aplicații web | Forms, dependency injection, router sau rendering |
| [Vue](https://github.com/vuejs/core) | Framework UI progresiv | Reactivitate sau comportament de componente |
| [Nuxt](https://github.com/nuxt/nuxt) | Framework de aplicație pentru Vue | Routing, rendering și integrări specifice |
| [Astro](https://github.com/withastro/astro) | Framework pentru site-uri orientate spre conținut | Islands, rendering sau integrarea cu un framework UI |
| [Tailwind CSS](https://github.com/tailwindlabs/tailwindcss) | Framework CSS cu clase utilitare | Generare de stiluri și extensii; nu pentru a afla o clasă uzuală |
| [shadcn/ui](https://github.com/shadcn-ui/ui) | Componente al căror cod se adaugă proiectului | Componentele și exemplele relevante; codul deja copiat în proiect poate fi suficient |
| [React Hook Form](https://github.com/react-hook-form/react-hook-form) | Gestionarea formularelor React | Validare și integrarea componentelor controlate |
| [Zustand](https://github.com/pmndrs/zustand) | State management | Persistență, subscriptions sau sincronizare; doar dacă starea locală nu ajunge |

Nu adăuga simultan React, Svelte, Vue și Angular la un proiect nou fără o cerință de integrare explicită. O dependență folosită intern de framework nu devine automat o referință necesară agentului.

## API-uri, validare și logică TypeScript

| Tehnologie și sursă | Rol | Când merită sursa locală |
| --- | --- | --- |
| [`fetch`](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch) | API web pentru cereri HTTP; nu este un pachet separat de clonat | Documentația este în mod normal suficientă |
| [Axios](https://github.com/axios/axios) | Client HTTP | Dacă este deja folosit sau sunt necesare interceptors/adapters; nu implicit peste `fetch` |
| [TanStack Query](https://github.com/TanStack/query) | Gestionarea datelor asincrone și a cache-ului | Invalidare, paginare, optimistic updates; alege adapterul potrivit framework-ului |
| [Zod](https://github.com/colinhacks/zod) | Validare runtime cu scheme TypeScript | Transformări, tipuri inferate sau integrarea validatorului |
| [openapi-typescript / openapi-fetch](https://github.com/openapi-ts/openapi-typescript) | Tipuri și client TypeScript pornind de la OpenAPI | Dacă serviciul oferă o schemă OpenAPI și apar probleme de generare/client |
| [Effect](https://github.com/Effect-TS/effect) | Erori tipizate, resurse, concurență și compoziție TypeScript | Când proiectul folosește Effect și are nevoie de pattern-uri specifice |

Un apel simplu necesită URL-ul, autentificarea și contractul API-ului, tratarea erorilor și verificarea răspunsului. Nu necesită automat Axios, Query, Zod și Effect. TanStack Query gestionează starea datelor; folosește o funcție de transport precum `fetch` sau un SDK. Tipurile generate din OpenAPI nu validează singure răspunsurile la runtime.

Pentru un API specific, caută SDK-ul oficial doar după identificarea serviciului. Selectează SDK-ul limbajului folosit; nu descărca toate SDK-urile furnizorului. Dacă API-ul cere un secret, integrarea trebuie proiectată astfel încât secretul să nu ajungă în clientul public.

## Backend

| Tehnologie și sursă | Rol | Când merită sursa locală |
| --- | --- | --- |
| [Hono](https://github.com/honojs/hono) | Framework HTTP bazat pe Web Standards | Middleware, routing și particularități de runtime |
| [Fastify](https://github.com/fastify/fastify) | Framework backend pentru Node.js | Plugins, hooks, validare și lifecycle |
| [FastAPI](https://github.com/fastapi/fastapi) | Framework API pentru Python | Dependencies, validare și OpenAPI |
| [Django](https://github.com/django/django) | Framework web pentru Python | ORM, auth, admin sau comportament de framework |
| [Laravel](https://github.com/laravel/framework) | Framework web pentru PHP | Routing, ORM, queues sau integrări |
| [Better Auth](https://github.com/better-auth/better-auth) | Framework de autentificare TypeScript | Adapter sau plugin folosit; numai dacă aplicația cere autentificare |

Folosește backend-ul existent dacă acoperă cerința. Într-o aplicație full-stack, o rută server disponibilă în framework poate elimina necesitatea unui server suplimentar.

## Baze de date și acces la date

| Tehnologie și sursă | Rol | Când merită sursa locală |
| --- | --- | --- |
| [SQLite](https://www.sqlite.org/src/doc/trunk/README.md) | Motor SQL embedded; repository-ul oficial folosește Fossil | Dezvoltare/debugging al motorului; pentru CRUD obișnuit, documentația și driverul |
| [PostgreSQL](https://github.com/postgres/postgres) | Server de baze de date relațional; linkul este mirror-ul oficial GitHub | Extensii sau internals; nu pentru a crea tabele și query-uri uzuale |
| [Drizzle ORM](https://github.com/drizzle-team/drizzle-orm) | Scheme și acces SQL în TypeScript | Mapping, query generation și migrări relevante versiunii folosite |
| [Prisma ORM](https://github.com/prisma/orm) | ORM și instrumente pentru acces la date | Schema, client și comportament de migrări |
| [Supabase JS](https://github.com/supabase/supabase-js) | SDK JavaScript pentru serviciile Supabase | Query-uri, auth, realtime sau storage în aplicația client |
| [Supabase](https://github.com/supabase/supabase) | Platformă construită în jurul PostgreSQL | Self-hosting sau debugging al platformei, nu implicit pentru folosirea SDK-ului |

Motorul, driverul, ORM-ul și SDK-ul sunt niveluri diferite. Alege întâi motorul și mediul de execuție, apoi driverul compatibil; adaugă un ORM numai dacă este util. Drizzle și Prisma sunt alternative uzuale, nu un set obligatoriu. Driverul exact se adaugă catalogului când există un proiect concret. Nu expune conexiunea administrativă PostgreSQL într-un frontend.

## Tooling, verificare și CMS

| Tehnologie și sursă | Rol | Când merită sursa locală |
| --- | --- | --- |
| [Vite](https://github.com/vitejs/vite) | Server de dezvoltare și build tooling | Plugin-uri sau debugging de build; nu pentru orice UI |
| [TypeScript](https://github.com/microsoft/TypeScript) | Limbaj și compiler | Compiler, language service sau diagnostic dificil |
| [Vitest](https://github.com/vitest-dev/vitest) | Test runner | Configurare sau comportament dificil de mocking |
| [Playwright](https://github.com/microsoft/playwright) | Testare și automatizare în browser | Probleme de browser automation; nu este test runner pentru UI nativ Android/iOS |
| [React Testing Library](https://github.com/testing-library/react-testing-library) | Testarea componentelor React prin comportamentul vizibil | Queries, async rendering sau compatibilitate cu test runner-ul |
| [WordPress](https://github.com/WordPress/wordpress-develop) | CMS; repository de dezvoltare/mirror | Hooks și dezvoltare de teme/plugin-uri |
| [WooCommerce](https://github.com/woocommerce/woocommerce) | Comerț electronic pe WordPress | Checkout, produse, extensii și hooks |

Codul unui motor, compiler sau browser este rareori necesar pentru folosirea sa normală. Testele proiectului se aleg după riscul funcției dezvoltate, fără clonarea implicită a framework-ului de testare.

## Mobile, jocuri și desktop

Vezi [catalogul dedicat](mobile-game-sources.md) pentru React Native, Expo, Flutter, Capacitor, Godot, Phaser, PixiJS, Three.js, Babylon.js, Flame, Tauri și Electron, cu documentație oficială și condiții de selecție.

## Extinderea catalogului

Pentru o tehnologie nouă, adaugă: cerința care o justifică, repository-ul oficial, rolul, alternativele excluse, versiunea din proiect și întrebarea care necesită sursa. Pentru iOS/Android nativ, pornește de la SDK-ul și documentația platformei; nu presupune că UI toolkit-ul are un repository public complet. Nu prezenta produse proprietare ca open source doar pentru că publică exemple.
