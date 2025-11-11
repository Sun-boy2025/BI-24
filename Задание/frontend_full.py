# frontend_full.py

"""
Полное техническое задание для Frontend (JavaScript) системы бизнес-аналитики.
С нуля: поддержка 24 инструментов, налоговый учет, ежедневные данные, импорт из 1С.

Технологии:
- HTML5, CSS3
- JavaScript ES6+
- Chart.js
- localStorage
- fetch

Структура проекта:
frontend/
├── index.html
├── styles/main.css
├── styles/components.css
├── scripts/
│   ├── app.js
│   ├── api.js
│   ├── dataGenerator.js
│   ├── ui.js
│   ├── recommendations.js
│   └── analytics/
│       ├── platezhnyy_kalendar.js
│       ├── dds_klassicheskiy.js
│       ├── finansovaya_model.js
│       ├── vliyanie_skidki.js
│       ├── byudget.js
│       ├── otdel_prodazh.js
│       ├── faktory_prodazh.js
│       ├── marketing_otchet.js
│       ├── unit_ekonomika.js
│       ├── finmodel_mp.js
│       ├── plan_dohodov_rashodov.js
│       ├── kalkulator_finkochagi.js
│       └── ... до balans.js (24 файлов)
└── assets/
    ├── icons/
    └── images/

===============================================================================
ЭТАПЫ РАЗРАБОТКИ
===============================================================================

1) Инициализация (1 день)
- Настроить index.html, подключить main.css, app.js, Chart.js CDN.
- Создать контейнеры: #home-view, #org-view, #tools-view, #tool-detail.

2) Управление организациями (1-2 дня)
- Реализовать формы создания/редактирования org: name, description, legal_form, tax_regime, region, okved, employee_count, registration_date.
- Сохранение в localStorage под ключом "orgs".
- Отображение списка orgs на #home-view.
- selectOrganization(id) → loadOrgData(id).

3) Ежедневный учет и генерация тестовых данных (1-2 дня)
- dataGenerator.js:
  function generateTestData(org) {
    const data = { '2025': { 'Q1': {months:{}}, 'Q2':..., 'Q3':... } };
    // loop date from 2025-01-01 to today
    // random income (10k-100k), expenses (5k-50k)
    // calculate tax via calculateTax(in, exp, org.tax_regime)
    // accumulate running_balance
    // assign into data structure by year→quarter→month→day.
    // aggregate monthly summary and quarterly.
    return data;
  }
- ui.js: renderDailyForm(), handleDailySubmit(), loadDailyDataUI().

4) Интерфейс Импорта из 1С (0.5 дня)
- index.html (#import-1c-form): file input + button "Импорт из 1С".
- api.js: upload1CData() POST /api/organizations/{id}/import/1c
- ui.js: showImportStatus(text)

5) Налоговый календарь (1 день)
- ui.js: renderTaxCalendar(org), calculateTaxCalendar(org).
- display next due dates in table or list.

6) Сетка аналитических инструментов (1 день)
- analyticsTools_list in app.js
- renderToolsGrid(): forEach tool → createCard(tool)
- Card: title, category badge, description, button Analyze

7) Детальная страница инструмента (2-3 дня)
- ui.js: showToolDetail(toolId)
- renderKpi(toolId), renderPeriods(toolId), renderCharts(toolId), renderRecommendations(toolId)
- HTML контейнер #tool-detail with subcontainers: .kpi-cards, .quarter-block, .charts-container, .ai-recommendations.

8) Графики и визуализация (1-2 дня)
- charts.js: buildLineChart(ctx, labels, data), buildBarChart(ctx, labels, datasets)
- extractBalanceData(data), extractMonthlyData(data)

9) ИИ-рекомендации (1 день)
- recommendations.js: criteria JSON, generateAIRecommendations(toolId, metrics), displayRecommendations()

10) Скрипты аналитических инструментов (3-4 дня)
- scripts/analytics/ tool_id.js each exports analyze(data) → { summary, periods, charts, recommendations }
- Import in app.js

11) Интерфейс и UX (1-2 дня)
- Responsive design: Flex/Grid
- ARIA attributes, keyboard navigation
- CSS animations for toggle, loading spinners

12) Тестирование и оптимизация (1-2 дня)
- Manual QA
- Verify across Chrome/Firefox/Edge
- Optimize DOM updates (batch renders)
- Performance profiling

===============================================================================
Интеграция с Backend
===============================================================================
- api.js: wrap fetch to backend API for CRUD org, tx, analytics, import
- switch localStorage data → fetch calls when backend готов
- handle errors and loading states

===============================================================================
КРИТЕРИИ ПРИЕМКИ
===============================================================================
- Полный функционал на localhost:3000 без ошибок
- Импорт из 1С работает
- 24 Analyze buttons + detail pages
- Daily data + daily charts
- Tax calendar + reminders
- ИИ-рекомендации отображаются

Рекомендуемые ресурсы:
- Chart.js docs
- MDN JS
- WCAG для accessibility

"""
