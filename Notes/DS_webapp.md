# Web general
- Что такое SSR, CSR, ISR и SSG, и что из этого выбрать
	- SSR -- Server-Side Rendering
	- CSR -- Client-Side Rendering
	- ISR -- Incremental Static Regeneration
	- SSG -- Static Site Generation
	- SPA -- Single Page Application
- [SSR или SPA веб-сайты: что выбрать для вас и вашего бизнеса](https://tproger.ru/articles/ssr-ili-spa-veb-sajty-chto-vybrat-dlya-vas-i-vawego-biznesa)

# React
- [Create React App](https://create-react-app.dev)
	- [Sunsetting Create React App](https://react.dev/blog/2025/02/14/sunsetting-create-react-app). February 14, 2025 by Matt Carroll and Ricky Hanlon
Today, we’re deprecating Create React App for new apps, and encouraging existing apps to migrate to a framework. We’re also providing docs for when a framework isn’t a good fit for your project, or you prefer to start by building a framework.
- [NVM for Windows](https://github.com/coreybutler/nvm-windows)
The Microsoft/npm/Google recommended Node.js version manager for Windows.
This is not the same thing as nvm! (expand for details)

# Создание первого приложения


## Замена create-react-app
Вы получили уведомление о том, что create-react-app устарел. Вместо него рекомендуется использовать более современные инструменты для создания React-приложений. Вот несколько популярных альтернатив:

Vite: Vite — это быстрый и современный инструмент для создания веб-приложений. Он поддерживает React и предлагает более быструю разработку по сравнению с create-react-app. Вы можете создать новый проект React с помощью Vite, выполнив команду:
`npm create vite@latest my-react-app -- --template react`
Next.js: Next.js — это мощный фреймворк для React, который предоставляет серверный рендеринг, статическую генерацию и множество других функций. Он отлично подходит для создания полноценных веб-приложений. Чтобы создать новый проект с Next.js, выполните:
`npx create-next-app@latest my-next-app`
Remix: Remix — это ещё один современный фреймворк для React, который фокусируется на производительности и удобстве разработки. Он предоставляет мощные возможности для маршрутизации и управления данными. Для создания нового проекта с Remix выполните:
`npx create-remix@latest`
Эти инструменты предлагают более современные и эффективные способы разработки React-приложений, чем create-react-app. Выбор зависит от ваших потребностей и предпочтений.

# CSS
- [What does flex: 1 mean?](https://stackoverflow.com/questions/37386244/what-does-flex-1-mean). In some browsers:
`flex:1`; does not equal `flex:1 1 0`; 
In Chrome Ver 84, `flex: 1` is equivalent to `flex: 1 1 0%`