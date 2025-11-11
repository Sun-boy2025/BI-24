# Завершение описания аналитических инструментов 22-25
# Инструкция для разработчика Python

instruments_data_22_25 = {

# Инструмент 22
"22_analiz_rentabelnosti": {
    "instrument_number": 22,
    "title": "Анализ рентабельности",
    "category": "profitability_analysis",
    "description": "Комплексный анализ рентабельности деятельности компании по различным направлениям",
    
    "tasks": [
        "Расчет показателей рентабельности продаж, активов и капитала",
        "Факторный анализ изменения рентабельности",
        "Сравнительный анализ рентабельности по сегментам бизнеса",
        "Прогнозирование динамики показателей рентабельности"
    ],
    
    "calculation_algorithm": [
        "Рассчитать основные показатели рентабельности (ROS, ROA, ROE)",
        "Провести факторный анализ изменения рентабельности",
        "Сравнить показатели рентабельности по продуктам и сегментам",
        "Проанализировать влияние операционного рычага на рентабельность",
        "Спрогнозировать будущую динамику рентабельности"
    ],
    
    "auto_calculated_fields": [
        "return_on_sales",              # Рентабельность продаж
        "return_on_assets",             # Рентабельность активов
        "return_on_equity",             # Рентабельность собственного капитала
        "gross_profit_margin",          # Валовая рентабельность
        "operating_margin",             # Операционная рентабельность
        "profitability_trends"          # Тренды рентабельности
    ],
    
    "manual_input_fields": [
        "revenue_data",                 # Данные о выручке (dict)
        "cost_data",                    # Данные о затратах (dict)
        "profit_data",                  # Данные о прибыли (dict)
        "assets_data",                  # Данные об активах (dict)
        "equity_data",                  # Данные о капитале (dict)
        "segment_performance",          # Результаты по сегментам (dict)
        "product_profitability",        # Рентабельность продуктов (dict)
        "market_conditions",            # Рыночные условия (dict)
        "competitive_benchmarks"        # Конкурентные бенчмарки (dict)
    ],
    
    "editable_calculation_fields": [
        "target_ros_rate",              # Целевая рентабельность продаж (float, default: 15.0)
        "target_roa_rate",              # Целевая рентабельность активов (float, default: 12.0)
        "target_roe_rate",              # Целевая рентабельность капитала (float, default: 18.0)
        "industry_average_margins",     # Средние отраслевые маржи (dict)
        "cost_optimization_potential",  # Потенциал оптимизации затрат (float, default: 5.0)
        "revenue_growth_assumption"     # Предположение о росте выручки (float, default: 8.0)
    ],
    
    "main_formulas": [
        "ros = net_profit / net_sales * 100",
        "roa = net_profit / average_total_assets * 100",
        "roe = net_profit / average_shareholders_equity * 100",
        "gross_margin = (revenue - cogs) / revenue * 100",
        "operating_margin = operating_profit / revenue * 100",
        "dupont_roe = (net_profit / sales) * (sales / assets) * (assets / equity)"
    ],
    
    "key_metrics": [
        "profitability_stability_index",
        "margin_improvement_potential",
        "competitive_profitability_position",
        "profitability_risk_score",
        "sustainable_growth_rate",
        "value_creation_efficiency"
    ],
    
    "data_visualization": [
        "Динамика основных показателей рентабельности",
        "Факторный анализ изменения ROE (модель Дюпона)",
        "Сравнение рентабельности по сегментам бизнеса",
        "Бенчмаркинг с конкурентами по марже",
        "Корреляционный анализ рентабельности и ключевых драйверов",
        "Прогнозная модель рентабельности"
    ],
    
    "ai_analysis_prompts": [
        "Проанализируй динамику и факторы изменения рентабельности компании",
        "Определи сегменты бизнеса с наилучшей и наихудшей рентабельностью",
        "Оцени конкурентоспособность уровня рентабельности компании",
        "Предложи стратегию повышения рентабельности бизнеса"
    ],
    
    "python_implementation_notes": [
        "Создать класс ProfitabilityAnalyzer для комплексного анализа рентабельности",
        "Реализовать модель Дюпона для факторного анализа ROE",
        "Использовать регрессионный анализ для выявления драйверов рентабельности",
        "Добавить модули бенчмаркинга с отраслевыми показателями",
        "Интегрировать с системами управленческого учета"
    ]
},

# Инструмент 23
"23_analiz_likvidnosti": {
    "instrument_number": 23,
    "title": "Анализ ликвидности",
    "category": "liquidity_analysis",
    "description": "Анализ платежеспособности и ликвидности компании",
    
    "tasks": [
        "Расчет коэффициентов ликвидности и платежеспособности",
        "Анализ структуры оборотных активов по степени ликвидности",
        "Оценка качества управления денежными потоками",
        "Прогнозирование потребности в ликвидности"
    ],
    
    "calculation_algorithm": [
        "Рассчитать основные коэффициенты ликвидности",
        "Провести анализ структуры активов по степени ликвидности",
        "Оценить качество дебиторской задолженности",
        "Проанализировать денежные потоки от операционной деятельности",
        "Спрогнозировать будущие потребности в ликвидности"
    ],
    
    "auto_calculated_fields": [
        "current_ratio",                # Коэффициент текущей ликвидности
        "quick_ratio",                  # Коэффициент быстрой ликвидности
        "cash_ratio",                   # Коэффициент абсолютной ликвидности
        "working_capital",              # Оборотный капитал
        "cash_conversion_cycle",        # Цикл оборота денежных средств
        "liquidity_risk_assessment"     # Оценка риска ликвидности
    ],
    
    "manual_input_fields": [
        "current_assets",               # Оборотные активы (dict)
        "current_liabilities",          # Краткосрочные обязательства (dict)
        "cash_and_equivalents",         # Денежные средства и эквиваленты (float)
        "accounts_receivable",          # Дебиторская задолженность (float)
        "inventory",                    # Запасы (float)
        "accounts_payable",             # Кредиторская задолженность (float)
        "operating_cash_flows",         # Операционные денежные потоки (dict)
        "credit_facilities",            # Кредитные линии (dict)
        "seasonal_patterns"             # Сезонные особенности (dict)
    ],
    
    "editable_calculation_fields": [
        "minimum_current_ratio",        # Минимальный коэффициент текущей ликвидности (float, default: 1.5)
        "target_quick_ratio",           # Целевой коэффициент быстрой ликвидности (float, default: 1.0)
        "minimum_cash_ratio",           # Минимальный коэффициент абсолютной ликвидности (float, default: 0.2)
        "liquidity_buffer_days",        # Буфер ликвидности в днях (int, default: 30)
        "collection_efficiency_target", # Целевая эффективность сбора ДЗ (float, default: 95.0)
        "inventory_liquidity_factor"    # Фактор ликвидности запасов (float, default: 0.7)
    ],
    
    "main_formulas": [
        "current_ratio = current_assets / current_liabilities",
        "quick_ratio = (current_assets - inventory) / current_liabilities",
        "cash_ratio = cash_and_equivalents / current_liabilities",
        "working_capital = current_assets - current_liabilities",
        "cash_conversion_cycle = dso + dio - dpo",
        "operating_cash_flow_ratio = operating_cash_flow / current_liabilities"
    ],
    
    "key_metrics": [
        "liquidity_adequacy_score",
        "cash_flow_predictability",
        "liquidity_efficiency_index",
        "short_term_solvency_rating",
        "liquidity_management_quality",
        "financial_flexibility_measure"
    ],
    
    "data_visualization": [
        "График динамики коэффициентов ликвидности",
        "Структура оборотных активов по степени ликвидности",
        "Анализ цикла оборота денежных средств",
        "Прогнозный график потребности в ликвидности",
        "Стресс-тестирование ликвидности при различных сценариях",
        "Сравнение показателей ликвидности с отраслевыми нормами"
    ],
    
    "ai_analysis_prompts": [
        "Проанализируй уровень ликвидности и платежеспособности компании",
        "Оцени адекватность текущего уровня ликвидности потребностям бизнеса",
        "Определи риски ликвидности и предложи меры их минимизации",
        "Спрогнозируй будущие потребности в ликвидности с учетом планов развития"
    ],
    
    "python_implementation_notes": [
        "Создать класс LiquidityAnalyzer для анализа ликвидности",
        "Реализовать модели прогнозирования денежных потоков",
        "Добавить стресс-тестирование ликвидности",
        "Использовать временные ряды для анализа сезонности потоков",
        "Интегрировать с банковскими системами для мониторинга остатков"
    ]
},

# Инструмент 24
"24_finansovoe_planirovanie": {
    "instrument_number": 24,
    "title": "Финансовое планирование",
    "category": "financial_planning",
    "description": "Стратегическое и операционное финансовое планирование деятельности компании",
    
    "tasks": [
        "Разработка стратегических финансовых планов",
        "Составление операционных финансовых планов",
        "Планирование инвестиций и источников финансирования",
        "Сценарное моделирование финансовых результатов"
    ],
    
    "calculation_algorithm": [
        "Разработать долгосрочные финансовые прогнозы",
        "Составить операционные планы движения денежных средств",
        "Определить потребности в финансировании и источники средств",
        "Провести сценарный анализ различных вариантов развития",
        "Интегрировать финансовые планы с бизнес-стратегией"
    ],
    
    "auto_calculated_fields": [
        "financial_forecast_model",     # Модель финансового прогнозирования
        "funding_requirements",         # Потребности в финансировании
        "optimal_capital_structure",    # Оптимальная структура капитала
        "scenario_analysis_results",    # Результаты сценарного анализа
        "strategic_financial_metrics",  # Стратегические финансовые метрики
        "plan_sensitivity_analysis"     # Анализ чувствительности плана
    ],
    
    "manual_input_fields": [
        "strategic_objectives",         # Стратегические цели (dict)
        "market_assumptions",           # Рыночные предположения (dict)
        "growth_projections",           # Прогнозы роста (dict)
        "investment_plans",             # Планы инвестиций (dict)
        "financing_options",            # Варианты финансирования (dict)
        "cost_structure_assumptions",   # Предположения о структуре затрат (dict)
        "regulatory_constraints",       # Регулятивные ограничения (dict)
        "macroeconomic_factors",        # Макроэкономические факторы (dict)
        "competitive_landscape"         # Конкурентная среда (dict)
    ],
    
    "editable_calculation_fields": [
        "planning_horizon_years",       # Горизонт планирования в годах (int, default: 5)
        "revenue_growth_assumption",    # Предположение о росте выручки (float, default: 12.0)
        "margin_improvement_target",    # Цель улучшения маржи (float, default: 2.0)
        "capex_to_revenue_ratio",      # Отношение капвложений к выручке (float, default: 5.0)
        "target_debt_to_equity",       # Целевое отношение долга к капиталу (float, default: 0.5)
        "dividend_payout_policy"       # Политика выплаты дивидендов (float, default: 30.0)
    ],
    
    "main_formulas": [
        "projected_revenue = base_revenue * (1 + growth_rate)^years",
        "financing_need = capex + working_capital_increase - operating_cash_flow",
        "sustainable_growth_rate = roe * (1 - dividend_payout_ratio)",
        "wacc = (debt_ratio * cost_of_debt * (1 - tax_rate)) + (equity_ratio * cost_of_equity)",
        "enterprise_value = sum(fcf_t / (1 + wacc)^t) + terminal_value",
        "debt_service_coverage = operating_cash_flow / debt_service"
    ],
    
    "key_metrics": [
        "plan_achievability_score",
        "financial_strategy_alignment",
        "funding_sustainability_rating",
        "value_creation_potential",
        "financial_flexibility_preservation",
        "stakeholder_value_optimization"
    ],
    
    "data_visualization": [
        "Долгосрочный прогноз ключевых финансовых показателей",
        "Сценарный анализ (базовый/оптимистичный/пессимистичный)",
        "План движения денежных средств с разбивкой по видам деятельности",
        "Структура финансирования по годам планового периода",
        "Анализ чувствительности к изменению ключевых драйверов",
        "Дорожная карта достижения финансовых целей"
    ],
    
    "ai_analysis_prompts": [
        "Проанализируй реалистичность и достижимость финансовых планов",
        "Оцени сбалансированность планов роста и финансовой устойчивости",
        "Определи ключевые риски реализации финансовой стратегии",
        "Предложи альтернативные сценарии развития с учетом неопределенности"
    ],
    
    "python_implementation_notes": [
        "Создать класс FinancialPlanner для стратегического планирования",
        "Реализовать Monte Carlo симуляцию для стохастического моделирования",
        "Использовать оптимизационные алгоритмы для выбора структуры капитала",
        "Добавить модули интеграции с внешними экономическими прогнозами",
        "Создать систему автоматического обновления планов при изменении предпосылок"
    ]
},

# Инструмент 25
"25_konsolidirovannyy_otchet": {
    "instrument_number": 25,
    "title": "Консолидированный отчет",
    "category": "consolidated_reporting",
    "description": "Формирование консолидированной отчетности и управленческих отчетов",
    
    "tasks": [
        "Консолидация финансовой отчетности дочерних компаний",
        "Элиминирование внутригрупповых операций",
        "Формирование управленческой отчетности по сегментам",
        "Подготовка аналитических отчетов для принятия решений"
    ],
    
    "calculation_algorithm": [
        "Собрать данные финансовой отчетности всех дочерних компаний",
        "Провести унификацию учетных политик и валют",
        "Исключить внутригрупповые операции и остатки",
        "Рассчитать доли неконтролирующих акционеров",
        "Сформировать консолидированные финансовые отчеты"
    ],
    
    "auto_calculated_fields": [
        "consolidated_revenue",          # Консолидированная выручка
        "consolidated_profit",           # Консолидированная прибыль
        "consolidated_assets",           # Консолидированные активы
        "minority_interest",             # Доля меньшинства
        "intercompany_eliminations",     # Внутригрупповые исключения
        "segment_performance_metrics"    # Показатели по сегментам
    ],
    
    "manual_input_fields": [
        "subsidiary_financials",         # Финансовые данные дочерних компаний (dict)
        "ownership_percentages",         # Доли участия (dict)
        "intercompany_transactions",     # Внутригрупповые операции (dict)
        "currency_exchange_rates",       # Валютные курсы (dict)
        "accounting_policy_differences", # Различия в учетной политике (dict)
        "segment_allocation_rules",      # Правила распределения по сегментам (dict)
        "consolidation_adjustments",     # Консолидационные корректировки (dict)
        "goodwill_and_intangibles",     # Гудвилл и нематериальные активы (dict)
        "joint_ventures_data"           # Данные совместных предприятий (dict)
    ],
    
    "editable_calculation_fields": [
        "consolidation_threshold",      # Порог консолидации в процентах (float, default: 50.0)
        "functional_currency",          # Функциональная валюта (str, default: "RUB")
        "translation_method",           # Метод пересчета валют (str, default: "current_rate")
        "goodwill_impairment_test",     # Тестирование гудвилла на обесценение (bool, default: True)
        "segment_reporting_threshold",   # Порог существенности сегмента (float, default: 10.0)
        "materiality_threshold"         # Порог существенности (float, default: 5.0)
    ],
    
    "main_formulas": [
        "consolidated_revenue = sum(subsidiary_revenues) - intercompany_sales",
        "minority_interest = (subsidiary_equity * minority_percentage)",
        "goodwill = purchase_price - fair_value_net_assets",
        "currency_translation_adjustment = sum((assets - liabilities) * exchange_rate_change)",
        "segment_profit_margin = segment_profit / segment_revenue * 100",
        "return_on_invested_capital = nopat / invested_capital"
    ],
    
    "key_metrics": [
        "consolidation_quality_index",
        "reporting_timeliness_score",
        "segment_performance_variance",
        "intercompany_elimination_accuracy",
        "currency_impact_magnitude",
        "stakeholder_information_value"
    ],
    
    "data_visualization": [
        "Структура консолидированной выручки по сегментам и географии",
        "Мост рентабельности от дочерних компаний к группе",
        "Анализ влияния валютных курсов на результаты",
        "Сравнительная эффективность дочерних компаний",
        "Динамика ключевых консолидированных показателей",
        "Матрица рисков и возможностей по бизнес-сегментам"
    ],
    
    "ai_analysis_prompts": [
        "Проанализируй качество и полноту консолидированной отчетности",
        "Оцени эффективность работы различных дочерних компаний и сегментов",
        "Определи влияние внутригрупповых операций на результаты группы",
        "Предложи улучшения процесса консолидации и управленческой отчетности"
    ],
    
    "python_implementation_notes": [
        "Создать класс ConsolidationEngine для автоматизации консолидации",
        "Реализовать алгоритмы исключения внутригрупповых операций",
        "Использовать pandas для обработки больших объемов финансовых данных",
        "Добавить модули валютного пересчета и hedging-анализа",
        "Интегрировать с ERP-системами дочерних компаний для автоматического сбора данных"
    ]
}

}

print("Завершено создание структуры для всех 25 аналитических инструментов!")
print("Полный набор инструментов готов для разработки аналитического комплекса.")

# Итоговая сводка всех 25 инструментов
all_instruments_summary = {
    "basic_financial_analysis": [1, 2, 3, 4, 5],      # Базовый финансовый анализ
    "sales_marketing_analytics": [6, 7, 8],            # Продажи и маркетинг
    "marketplace_economics": [9, 10],                   # Экономика маркетплейсов
    "budget_cost_management": [11, 12, 13, 14, 15],   # Бюджетирование и затраты
    "working_capital_analysis": [16, 17, 18],          # Управление оборотным капиталом
    "performance_investment": [19, 20, 21],            # Производительность и инвестиции
    "strategic_reporting": [22, 23, 24, 25]           # Стратегическая отчетность
}

print("\nКлассификация инструментов по направлениям:")
for category, tools in all_instruments_summary.items():
    print(f"{category}: инструменты {tools}")