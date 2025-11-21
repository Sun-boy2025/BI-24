# Продолжение описания аналитических инструментов 16-21
# Инструкция для разработчика Python

instruments_data_16_21 = {

# Инструмент 16
"16_analiz_debitorskoy_zadolzhennosti": {
    "instrument_number": 16,
    "title": "Анализ дебиторской задолженности",
    "category": "receivables_management",
    "description": "Управление и анализ дебиторской задолженности, оценка кредитных рисков",
    
    "tasks": [
        "Анализ структуры и динамики дебиторской задолженности",
        "Оценка оборачиваемости и качества дебиторской задолженности",
        "Управление кредитными рисками и просроченной задолженностью",
        "Оптимизация политики предоставления коммерческого кредита"
    ],
    
    "calculation_algorithm": [
        "Классифицировать дебиторскую задолженность по срокам погашения",
        "Рассчитать показатели оборачиваемости дебиторской задолженности",
        "Провести анализ качества и структуры задолженности",
        "Оценить кредитные риски по каждому дебитору",
        "Определить резервы по сомнительным долгам"
    ],
    
    "auto_calculated_fields": [
        "total_receivables",             # Общая дебиторская задолженность
        "receivables_turnover_ratio",    # Коэффициент оборачиваемости ДЗ
        "average_collection_period",     # Средний период инкассации
        "overdue_receivables_amount",    # Сумма просроченной задолженности
        "bad_debt_provision",            # Резерв по сомнительным долгам
        "receivables_aging_analysis"     # Анализ старения задолженности
    ],
    
    "manual_input_fields": [
        "receivables_data",              # Данные по дебиторам (dict)
        "payment_terms",                 # Условия платежа (dict)
        "customer_credit_ratings",       # Кредитные рейтинги клиентов (dict)
        "historical_bad_debts",          # Исторические данные о безнадежных долгах (dict)
        "collection_costs",              # Затраты на взыскание (dict)
        "industry_payment_patterns",     # Отраслевые модели платежей (dict)
        "economic_indicators",           # Экономические показатели (dict)
        "customer_financial_data",       # Финансовые данные клиентов (dict)
        "collateral_information"         # Информация о залогах (dict)
    ],
    
    "editable_calculation_fields": [
        "credit_policy_strictness",      # Строгость кредитной политики (float, default: 0.8)
        "bad_debt_rate_assumption",      # Предполагаемая доля безнадежных долгов (float, default: 2.0)
        "target_collection_period",      # Целевый период инкассации в днях (int, default: 30)
        "credit_limit_multiplier",       # Множитель кредитного лимита (float, default: 1.5)
        "early_payment_discount_rate",   # Ставка скидки за досрочную оплату (float, default: 2.0)
        "collection_efficiency_target"   # Целевая эффективность взыскания (float, default: 95.0)
    ],
    
    "main_formulas": [
        "receivables_turnover = net_credit_sales / average_receivables",
        "collection_period = 365 / receivables_turnover_ratio",
        "bad_debt_ratio = bad_debts_written_off / total_credit_sales * 100",
        "receivables_to_sales = total_receivables / annual_sales * 100",
        "overdue_percentage = overdue_receivables / total_receivables * 100",
        "provision_coverage = bad_debt_provision / total_receivables * 100"
    ],
    
    "key_metrics": [
        "collection_effectiveness_index",
        "credit_risk_score",
        "receivables_quality_rating",
        "cash_conversion_efficiency",
        "customer_payment_behavior",
        "credit_policy_performance"
    ],
    
    "data_visualization": [
        "Анализ старения дебиторской задолженности (гистограмма)",
        "Топ должников по размеру задолженности",
        "Динамика оборачиваемости дебиторской задолженности",
        "Структура задолженности по срокам погашения",
        "Карта рисков по клиентам",
        "Эффективность взыскательных мероприятий"
    ],
    
    "ai_analysis_prompts": [
        "Проанализируй качество дебиторской задолженности и выяви проблемных должников",
        "Оцени эффективность текущей кредитной политики компании",
        "Определи оптимальные условия коммерческого кредитования",
        "Предложи меры по ускорению инкассации дебиторской задолженности"
    ],
    
    "python_implementation_notes": [
        "Создать класс ReceivablesAnalyzer для анализа дебиторской задолженности",
        "Реализовать алгоритмы кредитного скоринга клиентов",
        "Использовать pandas для анализа временных рядов платежей",
        "Добавить модули прогнозирования просроченной задолженности",
        "Интегрировать с внешними бюро кредитных историй"
    ]
},

# Инструмент 17
"17_analiz_kreditorstkoy_zadolzhennosti": {
    "instrument_number": 17,
    "title": "Анализ кредиторской задолженности",
    "category": "payables_management",
    "description": "Управление кредиторской задолженностью и оптимизация платежной дисциплины",
    
    "tasks": [
        "Анализ структуры и динамики кредиторской задолженности",
        "Оптимизация сроков и условий расчетов с поставщиками",
        "Управление ликвидностью через планирование платежей",
        "Контроль своевременности исполнения обязательств"
    ],
    
    "calculation_algorithm": [
        "Классифицировать кредиторскую задолженность по видам и срокам",
        "Рассчитать показатели оборачиваемости кредиторской задолженности",
        "Проанализировать условия расчетов с различными поставщиками",
        "Оценить влияние задолженности на денежные потоки",
        "Оптимизировать график погашения обязательств"
    ],
    
    "auto_calculated_fields": [
        "total_payables",                # Общая кредиторская задолженность
        "payables_turnover_ratio",       # Коэффициент оборачиваемости КЗ
        "average_payment_period",        # Средний период оплаты
        "overdue_payables_amount",       # Сумма просроченных обязательств
        "working_capital_impact",        # Влияние на оборотный капитал
        "supplier_payment_analysis"      # Анализ платежей поставщикам
    ],
    
    "manual_input_fields": [
        "payables_data",                 # Данные по кредиторам (dict)
        "supplier_terms",                # Условия поставщиков (dict)
        "payment_discounts_available",   # Доступные скидки за досрочную оплату (dict)
        "cash_flow_projections",         # Прогнозы денежных потоков (dict)
        "supplier_criticality",          # Критичность поставщиков (dict)
        "contract_penalties",            # Штрафы по договорам (dict)
        "seasonal_payment_patterns",     # Сезонные особенности платежей (dict)
        "supplier_financing_options",    # Возможности финансирования от поставщиков (dict)
        "payment_method_costs"           # Стоимость различных способов оплаты (dict)
    ],
    
    "editable_calculation_fields": [
        "target_payment_period",         # Целевый период оплаты в днях (int, default: 45)
        "cash_discount_threshold",       # Порог для использования скидок (float, default: 2.0)
        "supplier_risk_tolerance",       # Толерантность к рискам поставщиков (float, default: 0.7)
        "payment_priority_weights",      # Веса приоритетности платежей (dict)
        "late_payment_penalty_rate",     # Ставка пени за просрочку (float, default: 0.1)
        "optimal_cash_balance_target"    # Целевой остаток денежных средств (float, default: 5.0)
    ],
    
    "main_formulas": [
        "payables_turnover = cost_of_goods_sold / average_payables",
        "payment_period = 365 / payables_turnover_ratio",
        "cash_conversion_cycle = receivables_period + inventory_period - payables_period",
        "early_payment_savings = discount_rate * payable_amount",
        "cost_of_trade_credit = (1 + discount_rate / (1 - discount_rate)) ^ (365 / payment_period) - 1",
        "payables_to_purchases = total_payables / annual_purchases * 100"
    ],
    
    "key_metrics": [
        "payment_discipline_score",
        "supplier_relationship_index",
        "cash_management_efficiency",
        "trade_credit_utilization",
        "payment_optimization_potential",
        "supplier_dependency_risk"
    ],
    
    "data_visualization": [
        "Структура кредиторской задолженности по поставщикам",
        "График сроков погашения обязательств",
        "Анализ использования коммерческого кредита",
        "Динамика оборачиваемости кредиторской задолженности",
        "Карта критичности поставщиков",
        "Эффективность использования скидок за досрочную оплату"
    ],
    
    "ai_analysis_prompts": [
        "Проанализируй эффективность управления кредиторской задолженностью",
        "Оцени возможности оптимизации платежного календаря",
        "Определи наиболее выгодные условия расчетов с поставщиками",
        "Предложи стратегию управления отношениями с ключевыми кредиторами"
    ],
    
    "python_implementation_notes": [
        "Создать класс PayablesManager для управления кредиторской задолженностью",
        "Реализовать алгоритмы оптимизации платежного календаря",
        "Использовать операционные исследования для оптимизации платежей",
        "Добавить модули анализа условий поставщиков",
        "Интегрировать с банковскими системами для автоматизации платежей"
    ]
},

# Инструмент 18
"18_analiz_zapasov": {
    "instrument_number": 18,
    "title": "Анализ запасов",
    "category": "inventory_management",
    "description": "Управление товарными запасами и оптимизация складских операций",
    
    "tasks": [
        "Анализ структуры и оборачиваемости товарных запасов",
        "Оптимизация размера заказа и уровня запасов",
        "ABC и XYZ анализ товарных позиций",
        "Управление рисками затоваривания и дефицита"
    ],
    
    "calculation_algorithm": [
        "Классифицировать запасы по категориям и характеристикам",
        "Рассчитать показатели оборачиваемости по группам товаров",
        "Провести ABC-анализ по стоимости и XYZ-анализ по регулярности",
        "Определить оптимальные размеры заказов и страховые запасы",
        "Выявить неликвидные и медленно оборачивающиеся товары"
    ],
    
    "auto_calculated_fields": [
        "inventory_turnover_ratio",      # Коэффициент оборачиваемости запасов
        "days_in_inventory",            # Количество дней в запасах
        "abc_classification",           # ABC-классификация товаров
        "xyz_classification",           # XYZ-классификация товаров
        "optimal_order_quantity",      # Оптимальный размер заказа
        "inventory_carrying_cost"       # Стоимость содержания запасов
    ],
    
    "manual_input_fields": [
        "inventory_data",               # Данные по запасам (dict)
        "sales_history",               # История продаж (dict)
        "supplier_lead_times",         # Время поставки поставщиков (dict)
        "storage_costs",               # Затраты на хранение (dict)
        "ordering_costs",              # Затраты на заказ (dict)
        "stockout_costs",              # Затраты от дефицита (dict)
        "seasonal_demand_patterns",    # Сезонные паттерны спроса (dict)
        "product_lifecycle_stage",     # Стадия жизненного цикла товара (dict)
        "supplier_reliability_data"    # Данные о надежности поставщиков (dict)
    ],
    
    "editable_calculation_fields": [
        "target_service_level",         # Целевой уровень сервиса (float, default: 95.0)
        "carrying_cost_rate",          # Ставка затрат на содержание (float, default: 25.0)
        "safety_stock_multiplier",     # Множитель страхового запаса (float, default: 1.65)
        "reorder_point_buffer",        # Буферный запас для точки заказа (float, default: 10.0)
        "obsolescence_risk_factor",    # Фактор риска устаревания (float, default: 5.0)
        "demand_variability_factor"    # Фактор изменчивости спроса (float, default: 1.2)
    ],
    
    "main_formulas": [
        "inventory_turnover = cost_of_goods_sold / average_inventory",
        "days_in_inventory = 365 / inventory_turnover",
        "eoq = sqrt(2 * demand * ordering_cost / carrying_cost)",
        "safety_stock = z_score * sqrt(lead_time) * demand_std_dev",
        "reorder_point = lead_time_demand + safety_stock",
        "total_inventory_cost = carrying_cost + ordering_cost + stockout_cost"
    ],
    
    "key_metrics": [
        "inventory_efficiency_index",
        "stockout_frequency",
        "inventory_accuracy_rate",
        "fill_rate_performance",
        "inventory_investment_roi",
        "warehouse_utilization_rate"
    ],
    
    "data_visualization": [
        "ABC-анализ товаров по стоимостной значимости",
        "XYZ-анализ по стабильности спроса",
        "Матрица ABC-XYZ для стратегий управления",
        "Динамика оборачиваемости запасов по категориям",
        "Анализ неликвидных остатков",
        "График уровня запасов и точек заказа"
    ],
    
    "ai_analysis_prompts": [
        "Проанализируй эффективность управления товарными запасами",
        "Определи оптимальную стратегию пополнения для каждой категории товаров",
        "Выяви товары с риском затоваривания или дефицита",
        "Предложи меры по снижению общего уровня запасов без ущерба сервису"
    ],
    
    "python_implementation_notes": [
        "Создать класс InventoryAnalyzer для анализа запасов",
        "Реализовать алгоритмы ABC и XYZ анализа",
        "Использовать scipy для расчета оптимальных размеров заказов",
        "Добавить модули прогнозирования спроса",
        "Интегрировать с WMS системами для получения данных"
    ]
},

# Инструмент 19
"19_analiz_proizvoditelnosti": {
    "instrument_number": 19,
    "title": "Анализ производительности",
    "category": "productivity_analysis",
    "description": "Анализ производительности труда и эффективности использования ресурсов",
    
    "tasks": [
        "Измерение производительности труда по подразделениям",
        "Анализ эффективности использования рабочего времени",
        "Оценка влияния различных факторов на производительность",
        "Бенчмаркинг показателей производительности"
    ],
    
    "calculation_algorithm": [
        "Определить показатели производительности для различных видов деятельности",
        "Рассчитать производительность труда в натуральном и стоимостном выражении",
        "Проанализировать факторы, влияющие на производительность",
        "Провести сравнительный анализ с отраслевыми стандартами",
        "Выявить резервы повышения производительности"
    ],
    
    "auto_calculated_fields": [
        "labor_productivity_index",      # Индекс производительности труда
        "output_per_employee",          # Выработка на сотрудника
        "revenue_per_labor_hour",       # Выручка на час труда
        "efficiency_ratios",            # Коэффициенты эффективности
        "productivity_trends",          # Тренды производительности
        "benchmark_comparison"          # Сравнение с бенчмарками
    ],
    
    "manual_input_fields": [
        "production_output_data",       # Данные объемов производства (dict)
        "labor_hours_data",            # Данные трудозатрат (dict)
        "employee_count_by_period",    # Численность по периодам (dict)
        "revenue_by_department",       # Выручка по подразделениям (dict)
        "equipment_utilization",       # Использование оборудования (dict)
        "quality_metrics",             # Показатели качества (dict)
        "training_investments",        # Инвестиции в обучение (dict)
        "technology_upgrades",         # Модернизация технологий (dict)
        "industry_benchmarks"          # Отраслевые бенчмарки (dict)
    ],
    
    "editable_calculation_fields": [
        "target_productivity_growth",   # Целевой рост производительности (float, default: 5.0)
        "working_hours_per_year",      # Рабочих часов в году (int, default: 1760)
        "quality_weight_factor",       # Весовой коэффициент качества (float, default: 0.3)
        "automation_impact_factor",    # Фактор влияния автоматизации (float, default: 1.15)
        "learning_curve_coefficient",  # Коэффициент кривой обучения (float, default: 0.9)
        "seasonal_productivity_factor" # Сезонный фактор производительности (dict)
    ],
    
    "main_formulas": [
        "labor_productivity = total_output / total_labor_input",
        "productivity_growth = (current_productivity / previous_productivity - 1) * 100",
        "output_per_employee = total_revenue / number_of_employees",
        "efficiency_ratio = actual_output / standard_output",
        "multifactor_productivity = output / (labor_input + capital_input + material_input)",
        "productivity_index = (current_period_productivity / base_period_productivity) * 100"
    ],
    
    "key_metrics": [
        "overall_productivity_score",
        "productivity_improvement_rate",
        "resource_utilization_efficiency",
        "employee_engagement_impact",
        "technology_productivity_gain",
        "competitive_productivity_position"
    ],
    
    "data_visualization": [
        "Динамика производительности труда по подразделениям",
        "Факторный анализ изменения производительности",
        "Сравнение с отраслевыми показателями",
        "Корреляция производительности и инвестиций в развитие",
        "Карта производительности по видам деятельности",
        "Прогноз развития производительности"
    ],
    
    "ai_analysis_prompts": [
        "Проанализируй динамику и факторы изменения производительности труда",
        "Определи подразделения с наибольшим потенциалом роста эффективности",
        "Оцени влияние различных мероприятий на повышение производительности",
        "Предложи комплекс мер по достижению целевых показателей производительности"
    ],
    
    "python_implementation_notes": [
        "Создать класс ProductivityAnalyzer для анализа производительности",
        "Реализовать многофакторные модели производительности",
        "Использовать статистические методы для выявления трендов",
        "Добавить модули сравнительного анализа с конкурентами",
        "Интегрировать с HR-системами для получения данных о персонале"
    ]
},

# Инструмент 20
"20_byudzhetnoe_upravlenie": {
    "instrument_number": 20,
    "title": "Бюджетное управление",
    "category": "budget_management",
    "description": "Комплексная система бюджетного планирования и контроля",
    
    "tasks": [
        "Составление операционных и финансовых бюджетов",
        "Консолидация бюджетов структурных подразделений",
        "Мониторинг исполнения бюджета и анализ отклонений",
        "Корректировка бюджетов и скользящее планирование"
    ],
    
    "calculation_algorithm": [
        "Составить операционные бюджеты по центрам ответственности",
        "Разработать финансовые бюджеты (движения денежных средств, прибылей и убытков)",
        "Консолидировать все бюджеты в единую систему",
        "Установить процедуры мониторинга и контроля исполнения",
        "Внедрить систему скользящего планирования и корректировок"
    ],
    
    "auto_calculated_fields": [
        "consolidated_budget",           # Консолидированный бюджет
        "budget_variance_analysis",      # Анализ отклонений бюджета
        "budget_execution_rate",         # Уровень исполнения бюджета
        "rolling_forecast",              # Скользящий прогноз
        "budget_performance_score",      # Оценка эффективности бюджетирования
        "variance_significance_flags"    # Флаги значимых отклонений
    ],
    
    "manual_input_fields": [
        "departmental_budgets",          # Бюджеты подразделений (dict)
        "revenue_budgets",              # Бюджеты доходов (dict)
        "expense_budgets",              # Бюджеты расходов (dict)
        "capital_expenditure_budget",   # Бюджет капитальных вложений (dict)
        "cash_flow_budget",             # Бюджет движения денежных средств (dict)
        "strategic_initiatives",        # Стратегические инициативы (dict)
        "external_factors",             # Внешние факторы (dict)
        "regulatory_requirements",      # Нормативные требования (dict)
        "historical_performance"        # Историческая эффективность (dict)
    ],
    
    "editable_calculation_fields": [
        "budget_planning_horizon",      # Горизонт бюджетного планирования (int, default: 12)
        "variance_threshold_major",     # Порог существенного отклонения (float, default: 10.0)
        "variance_threshold_critical",  # Порог критического отклонения (float, default: 20.0)
        "rolling_forecast_frequency",   # Частота скользящего прогнозирования (int, default: 3)
        "budget_flexibility_factor",    # Фактор гибкости бюджета (float, default: 0.05)
        "strategic_reserve_percentage"  # Процент стратегического резерва (float, default: 3.0)
    ],
    
    "main_formulas": [
        "budget_variance = actual_amount - budgeted_amount",
        "variance_percentage = (budget_variance / budgeted_amount) * 100",
        "budget_accuracy = (1 - abs(variance_percentage) / 100) * 100",
        "cumulative_variance = sum(monthly_variances)",
        "forecast_accuracy = 1 - abs(actual_result - forecasted_result) / actual_result",
        "budget_efficiency_score = (achieved_results / budget_resources) * 100"
    ],
    
    "key_metrics": [
        "budget_planning_accuracy",
        "execution_discipline_score",
        "forecasting_reliability",
        "resource_allocation_efficiency",
        "strategic_goal_achievement",
        "budget_process_maturity"
    ],
    
    "data_visualization": [
        "Дашборд исполнения консолидированного бюджета",
        "Анализ отклонений по центрам ответственности",
        "График скользящего прогнозирования",
        "Водопадная диаграмма изменений бюджета",
        "Тепловая карта бюджетных рисков",
        "Сценарный анализ бюджетных показателей"
    ],
    
    "ai_analysis_prompts": [
        "Проанализируй качество бюджетного планирования и точность прогнозов",
        "Определи центры ответственности с наибольшими отклонениями от бюджета",
        "Оцени эффективность распределения ресурсов между подразделениями",
        "Предложи улучшения процесса бюджетного управления"
    ],
    
    "python_implementation_notes": [
        "Создать класс BudgetManager для комплексного управления бюджетами",
        "Реализовать алгоритмы консолидации и анализа отклонений",
        "Использовать pandas для работы с многомерными бюджетными данными",
        "Добавить модули скользящего прогнозирования",
        "Интегрировать с ERP-системами для автоматического сбора фактических данных"
    ]
},

# Инструмент 21
"21_analiz_investitsiy": {
    "instrument_number": 21,
    "title": "Анализ инвестиций",
    "category": "investment_analysis",
    "description": "Оценка эффективности инвестиционных проектов и принятие инвестиционных решений",
    
    "tasks": [
        "Финансовая оценка инвестиционных проектов",
        "Расчет показателей эффективности инвестиций (NPV, IRR, PI)",
        "Анализ рисков инвестиционных проектов",
        "Сравнение альтернативных вариантов инвестирования"
    ],
    
    "calculation_algorithm": [
        "Определить денежные потоки по инвестиционному проекту",
        "Рассчитать ставку дисконтирования с учетом рисков проекта",
        "Вычислить основные показатели эффективности (NPV, IRR, PI, DPP)",
        "Провести анализ чувствительности к изменению ключевых параметров",
        "Выполнить сценарный анализ и оценку рисков"
    ],
    
    "auto_calculated_fields": [
        "net_present_value",            # Чистая приведенная стоимость
        "internal_rate_of_return",      # Внутренняя норма доходности
        "profitability_index",          # Индекс прибыльности
        "discounted_payback_period",    # Дисконтированный срок окупаемости
        "risk_adjusted_return",         # Доходность с учетом риска
        "investment_ranking"            # Ранжирование инвестиций
    ],
    
    "manual_input_fields": [
        "investment_projects",          # Инвестиционные проекты (dict)
        "cash_flows_projection",       # Прогноз денежных потоков (dict)
        "initial_investment_amount",   # Размер первоначальных инвестиций (dict)
        "project_lifetime",            # Срок жизни проекта (dict)
        "salvage_value",               # Ликвидационная стоимость (dict)
        "tax_considerations",          # Налоговые аспекты (dict)
        "financing_structure",         # Структура финансирования (dict)
        "market_conditions",           # Рыночные условия (dict)
        "regulatory_environment"       # Регулятивная среда (dict)
    ],
    
    "editable_calculation_fields": [
        "discount_rate_base",           # Базовая ставка дисконтирования (float, default: 10.0)
        "risk_premium",                 # Премия за риск (float, default: 3.0)
        "inflation_rate_assumption",    # Предполагаемая инфляция (float, default: 4.0)
        "tax_rate",                     # Налоговая ставка (float, default: 20.0)
        "sensitivity_range",            # Диапазон анализа чувствительности (float, default: 20.0)
        "minimum_acceptable_irr"        # Минимально приемлемая IRR (float, default: 15.0)
    ],
    
    "main_formulas": [
        "npv = sum(cash_flow_t / (1 + discount_rate)^t) - initial_investment",
        "irr: sum(cash_flow_t / (1 + irr)^t) = initial_investment",
        "pi = npv / initial_investment + 1",
        "dpp: sum(discounted_cash_flows) = initial_investment",
        "wacc = (equity_cost * equity_weight) + (debt_cost * debt_weight * (1 - tax_rate))",
        "risk_adjusted_npv = npv - (risk_factor * initial_investment)"
    ],
    
    "key_metrics": [
        "investment_attractiveness_score",
        "portfolio_diversification_benefit",
        "capital_efficiency_ratio",
        "risk_return_optimization",
        "strategic_value_alignment",
        "implementation_feasibility_rating"
    ],
    
    "data_visualization": [
        "График NPV при различных ставках дисконтирования",
        "Анализ чувствительности ключевых параметров",
        "Сценарный анализ (оптимистичный/базовый/пессимистичный)",
        "Портфель инвестиционных проектов по доходности и риску",
        "График окупаемости инвестиций",
        "Матрица оценки инвестиционных альтернатив"
    ],
    
    "ai_analysis_prompts": [
        "Проанализируй привлекательность представленных инвестиционных проектов",
        "Оцени риски и потенциальную доходность каждого проекта",
        "Определи оптимальный портфель инвестиций с учетом ограничений",
        "Предложи стратегию управления инвестиционными рисками"
    ],
    
    "python_implementation_notes": [
        "Создать класс InvestmentAnalyzer для анализа инвестиций",
        "Реализовать методы расчета NPV, IRR, PI с использованием numpy",
        "Добавить Monte Carlo симуляцию для анализа рисков",
        "Использовать оптимизационные алгоритмы для портфельного анализа",
        "Интегрировать с внешними источниками рыночных данных"
    ]
}

}

print("Создана структура для инструментов 16-21...")
print("Готово к продолжению с инструментами 22-25...")