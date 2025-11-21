# Продолжение описания аналитических инструментов 11-25
# Инструкция для разработчика Python

instruments_data_11_25 = {

# Инструмент 11
"11_plan_dokhodov_rashodov": {
    "instrument_number": 11,
    "title": "План доходов и расходов",
    "category": "budget_planning",
    "description": "Комплексное планирование доходов и расходов компании с детализацией по статьям",
    
    "tasks": [
        "Составление подробного плана доходов по источникам",
        "Планирование операционных и внеоперационных расходов",
        "Прогнозирование финансового результата",
        "Контроль исполнения плана доходов и расходов"
    ],
    
    "calculation_algorithm": [
        "Определить источники доходов и их прогнозируемые объемы",
        "Классифицировать расходы на постоянные и переменные",
        "Рассчитать плановые показатели по месяцам",
        "Определить точки безубыточности по периодам",
        "Провести сценарный анализ при различных условиях"
    ],
    
    "auto_calculated_fields": [
        "total_planned_revenue",         # Общие плановые доходы
        "total_planned_expenses",        # Общие плановые расходы
        "planned_profit_loss",           # Плановая прибыль/убыток
        "break_even_analysis",           # Анализ безубыточности
        "variance_analysis",             # Анализ отклонений
        "profitability_forecast"         # Прогноз рентабельности
    ],
    
    "manual_input_fields": [
        "revenue_sources",               # Источники доходов (dict)
        "planned_revenue_monthly",       # Плановые доходы по месяцам (dict)
        "fixed_expenses",                # Постоянные расходы (dict)
        "variable_expenses",             # Переменные расходы (dict)
        "one_time_expenses",             # Единовременные расходы (dict)
        "seasonal_factors",              # Сезонные факторы (dict)
        "inflation_assumptions",         # Предположения по инфляции (dict)
        "growth_assumptions",            # Предположения по росту (dict)
        "contingency_reserves"           # Резервы на непредвиденные расходы (float)
    ],
    
    "editable_calculation_fields": [
        "planning_period_months",        # Период планирования (int, default: 12)
        "revenue_growth_rate",           # Темп роста доходов (float, default: 10.0)
        "cost_inflation_rate",           # Уровень инфляции затрат (float, default: 5.0)
        "contingency_percentage",        # Процент резерва (float, default: 5.0)
        "seasonality_adjustment",        # Сезонные корректировки (dict)
        "scenario_pessimistic_factor",   # Пессимистичный сценарий (float, default: 0.8)
        "scenario_optimistic_factor"     # Оптимистичный сценарий (float, default: 1.2)
    ],
    
    "main_formulas": [
        "planned_profit = planned_revenue - planned_expenses",
        "margin_percentage = (planned_revenue - variable_costs) / planned_revenue * 100",
        "break_even_point = fixed_costs / (1 - variable_cost_ratio)",
        "roi_planned = planned_profit / invested_capital * 100",
        "expense_ratio = planned_expenses / planned_revenue * 100",
        "growth_rate = (current_period - previous_period) / previous_period * 100"
    ],
    
    "key_metrics": [
        "revenue_diversification_index",
        "expense_structure_efficiency",
        "seasonal_stability_score",
        "plan_accuracy_rating",
        "cash_flow_predictability",
        "profitability_sustainability"
    ],
    
    "data_visualization": [
        "График планируемых доходов и расходов по месяцам",
        "Структура доходов по источникам (круговая диаграмма)",
        "Структура расходов по статьям (водопадная диаграмма)",
        "Сценарный анализ (пессимистичный/базовый/оптимистичный)",
        "График точки безубыточности",
        "Тепловая карта сезонности доходов и расходов"
    ],
    
    "ai_analysis_prompts": [
        "Проанализируй сбалансированность планируемых доходов и расходов",
        "Оцени реалистичность заложенных предположений роста",
        "Определи наиболее рискованные статьи планирования",
        "Предложи меры по оптимизации структуры расходов"
    ],
    
    "python_implementation_notes": [
        "Создать класс BudgetPlanner для планирования доходов и расходов",
        "Реализовать методы сценарного моделирования",
        "Использовать pandas для работы с временными рядами",
        "Добавить алгоритмы детекции аномалий в планах",
        "Создать систему уведомлений о существенных отклонениях"
    ]
},

# Инструмент 12
"12_kalkulyator_finansovogo_rychaga": {
    "instrument_number": 12,
    "title": "Калькулятор финансового рычага",
    "category": "leverage_analysis",
    "description": "Анализ эффективности использования заемного капитала и расчет финансового рычага",
    
    "tasks": [
        "Расчет коэффициента финансового рычага",
        "Анализ структуры капитала компании",
        "Оценка влияния заемных средств на рентабельность",
        "Определение оптимального уровня долговой нагрузки"
    ],
    
    "calculation_algorithm": [
        "Определить размер собственного и заемного капитала",
        "Рассчитать коэффициенты финансового рычага",
        "Проанализировать влияние на рентабельность собственного капитала",
        "Оценить финансовые риски различных уровней долговой нагрузки",
        "Смоделировать оптимальную структуру капитала"
    ],
    
    "auto_calculated_fields": [
        "financial_leverage_ratio",      # Коэффициент финансового рычага
        "debt_to_equity_ratio",          # Отношение долга к собственному капиталу
        "interest_coverage_ratio",       # Коэффициент покрытия процентов
        "debt_service_coverage",         # Коэффициент покрытия долговых обязательств
        "leverage_effect",               # Эффект финансового рычага
        "optimal_capital_structure"      # Оптимальная структура капитала
    ],
    
    "manual_input_fields": [
        "total_assets",                  # Общие активы (float)
        "equity_capital",                # Собственный капитал (float)
        "debt_capital",                  # Заемный капитал (float)
        "interest_expenses",             # Процентные расходы (float)
        "ebit",                         # Прибыль до уплаты процентов и налогов (float)
        "tax_rate",                     # Налоговая ставка (float)
        "cost_of_debt",                 # Стоимость долга (float)
        "cost_of_equity",               # Стоимость собственного капитала (float)
        "industry_benchmarks"           # Отраслевые бенчмарки (dict)
    ],
    
    "editable_calculation_fields": [
        "target_debt_ratio",            # Целевое соотношение долга (float, default: 0.4)
        "maximum_leverage_ratio",       # Максимальный коэффициент рычага (float, default: 3.0)
        "minimum_interest_coverage",    # Минимальное покрытие процентов (float, default: 2.5)
        "risk_premium_adjustment",      # Поправка на риск (float, default: 0.02)
        "growth_financing_needs",       # Потребность в финансировании роста (float, default: 0.15)
        "liquidity_buffer_percentage"   # Буфер ликвидности (float, default: 10.0)
    ],
    
    "main_formulas": [
        "financial_leverage = total_assets / equity_capital",
        "debt_to_equity = debt_capital / equity_capital", 
        "interest_coverage = ebit / interest_expenses",
        "roe_leveraged = roe_unleveraged + (roe_unleveraged - cost_of_debt) * (debt / equity) * (1 - tax_rate)",
        "degree_of_financial_leverage = ebit / (ebit - interest_expenses)",
        "wacc = (equity / total_capital) * cost_of_equity + (debt / total_capital) * cost_of_debt * (1 - tax_rate)"
    ],
    
    "key_metrics": [
        "leverage_efficiency_score",
        "financial_risk_rating",
        "capital_structure_optimality",
        "debt_capacity_utilization",
        "leverage_impact_on_roe",
        "financial_flexibility_index"
    ],
    
    "data_visualization": [
        "График зависимости ROE от уровня долговой нагрузки",
        "Структура капитала (круговая диаграмма)",
        "Сравнение с отраслевыми показателями",
        "График изменения WACC при различных уровнях долга",
        "Анализ чувствительности к изменению процентных ставок",
        "Матрица риск-доходность для различных структур капитала"
    ],
    
    "ai_analysis_prompts": [
        "Проанализируй эффективность текущей структуры капитала",
        "Оцени финансовые риски существующего уровня долговой нагрузки",
        "Определи оптимальное соотношение собственного и заемного капитала",
        "Предложи стратегию управления долговой нагрузкой"
    ],
    
    "python_implementation_notes": [
        "Создать класс LeverageCalculator для расчета финансового рычага",
        "Реализовать алгоритмы оптимизации структуры капитала",
        "Использовать scipy для оптимизационных расчетов",
        "Добавить модули сравнения с отраслевыми бенчмарками",
        "Создать симуляцию различных сценариев финансирования"
    ]
},

# Инструмент 13
"13_kalkulyator_sebestoimosti_uslug": {
    "instrument_number": 13,
    "title": "Калькулятор себестоимости услуг",
    "category": "cost_accounting",
    "description": "Детальный расчет себестоимости услуг с учетом всех видов затрат",
    
    "tasks": [
        "Калькуляция полной себестоимости услуг",
        "Распределение косвенных расходов по видам услуг",
        "Анализ структуры затрат на оказание услуг",
        "Оптимизация себестоимости через управление затратами"
    ],
    
    "calculation_algorithm": [
        "Выделить прямые затраты на оказание услуги",
        "Рассчитать долю косвенных расходов на единицу услуги",
        "Учесть амортизацию и операционные расходы",
        "Добавить административные и коммерческие расходы",
        "Рассчитать полную себестоимость единицы услуги"
    ],
    
    "auto_calculated_fields": [
        "direct_costs_per_service",      # Прямые затраты на услугу
        "indirect_costs_allocation",     # Распределение косвенных затрат
        "full_service_cost",            # Полная себестоимость услуги
        "cost_structure_analysis",      # Анализ структуры затрат
        "unit_profitability",           # Прибыльность единицы услуги
        "break_even_service_volume"     # Объем безубыточности
    ],
    
    "manual_input_fields": [
        "service_categories",           # Категории услуг (list)
        "direct_labor_costs",          # Прямые трудовые затраты (dict)
        "direct_material_costs",       # Прямые материальные затраты (dict)
        "indirect_overhead_costs",     # Косвенные накладные расходы (dict)
        "service_volumes",             # Объемы оказания услуг (dict)
        "allocation_basis",            # База распределения затрат (dict)
        "administrative_expenses",     # Административные расходы (float)
        "commercial_expenses",         # Коммерческие расходы (float)
        "depreciation_expenses"        # Амортизационные расходы (float)
    ],
    
    "editable_calculation_fields": [
        "overhead_allocation_method",    # Метод распределения накладных расходов (str, default: "ABC")
        "labor_efficiency_factor",      # Коэффициент эффективности труда (float, default: 1.0)
        "capacity_utilization_rate",    # Коэффициент использования мощностей (float, default: 0.85)
        "quality_cost_factor",          # Фактор затрат на качество (float, default: 0.05)
        "learning_curve_effect",        # Эффект кривой обучения (float, default: 0.95)
        "indirect_cost_inflation"       # Инфляция косвенных затрат (float, default: 0.03)
    ],
    
    "main_formulas": [
        "unit_cost = (direct_costs + allocated_indirect_costs) / service_volume",
        "indirect_allocation = total_indirect_costs * (service_volume / total_volume)",
        "margin_per_service = service_price - unit_cost",
        "contribution_margin = (service_price - variable_costs) / service_price",
        "cost_variance = actual_cost - standard_cost",
        "efficiency_ratio = standard_hours / actual_hours"
    ],
    
    "key_metrics": [
        "cost_competitiveness_index",
        "service_margin_analysis",
        "cost_structure_efficiency",
        "indirect_cost_ratio",
        "labor_productivity_ratio",
        "cost_reduction_potential"
    ],
    
    "data_visualization": [
        "Водопадная диаграмма формирования себестоимости",
        "Структура затрат по видам услуг (столбчатая диаграмма)",
        "Сравнительный анализ себестоимости услуг",
        "Тенденции изменения себестоимости во времени",
        "ABC-анализ затрат по значимости",
        "Матрица услуг по объему и прибыльности"
    ],
    
    "ai_analysis_prompts": [
        "Проанализируй структуру себестоимости услуг и выяви возможности оптимизации",
        "Определи наиболее затратные элементы в калькуляции услуг",
        "Оцени конкурентоспособность ценообразования на основе себестоимости",
        "Предложи мероприятия по снижению себестоимости услуг"
    ],
    
    "python_implementation_notes": [
        "Создать класс ServiceCostCalculator для калькуляции услуг",
        "Реализовать различные методы распределения косвенных затрат",
        "Использовать pandas для анализа больших объемов данных по затратам",
        "Добавить модули ABC и XYZ анализа затрат",
        "Создать систему мониторинга изменений себестоимости"
    ]
},

# Инструмент 14
"14_zarplatnaya_vedomost": {
    "instrument_number": 14,
    "title": "Зарплатная ведомость",
    "category": "payroll_management",
    "description": "Управление фондом оплаты труда и анализ кадровых затрат",
    
    "tasks": [
        "Расчет фонда оплаты труда по подразделениям",
        "Анализ структуры и динамики зарплатных затрат",
        "Планирование кадрового бюджета",
        "Оценка эффективности инвестиций в персонал"
    ],
    
    "calculation_algorithm": [
        "Собрать данные о штатном расписании и окладах",
        "Рассчитать основную и дополнительную зарплату",
        "Учесть социальные взносы и налоги с ФОТ",
        "Распределить затраты по центрам ответственности",
        "Проанализировать структуру и динамику кадровых затрат"
    ],
    
    "auto_calculated_fields": [
        "total_payroll_fund",           # Общий фонд оплаты труда
        "social_contributions",         # Социальные взносы
        "payroll_taxes",               # Налоги с ФОТ
        "labor_cost_per_employee",     # Затраты на персонал на сотрудника
        "payroll_efficiency_metrics",  # Метрики эффективности ФОТ
        "budget_variance_analysis"     # Анализ отклонений бюджета ФОТ
    ],
    
    "manual_input_fields": [
        "employee_data",               # Данные о сотрудниках (dict)
        "salary_scales",               # Тарифные сетки (dict)
        "bonuses_and_incentives",      # Премии и стимулирующие выплаты (dict)
        "social_benefits",             # Социальные льготы (dict)
        "working_hours_data",          # Данные о рабочем времени (dict)
        "department_allocation",       # Распределение по подразделениям (dict)
        "tax_rates",                   # Налоговые ставки (dict)
        "social_contribution_rates",   # Ставки социальных взносов (dict)
        "overtime_rates"               # Ставки сверхурочных (dict)
    ],
    
    "editable_calculation_fields": [
        "average_salary_growth_rate",  # Средний рост зарплат (float, default: 7.0)
        "social_contribution_rate",    # Ставка социальных взносов (float, default: 30.2)
        "income_tax_rate",             # Ставка подоходного налога (float, default: 13.0)
        "productivity_bonus_rate",     # Ставка премии за производительность (float, default: 15.0)
        "annual_bonus_provision",      # Резерв на годовые премии (float, default: 8.33)
        "vacation_provision_rate"      # Резерв на отпуска (float, default: 8.33)
    ],
    
    "main_formulas": [
        "gross_payroll = base_salary + bonuses + overtime + benefits",
        "social_contributions = gross_payroll * social_contribution_rate",
        "net_salary = gross_salary - income_tax - employee_contributions",
        "total_labor_cost = gross_payroll + employer_contributions + other_benefits",
        "labor_cost_per_revenue = total_labor_cost / total_revenue * 100",
        "productivity_index = revenue_per_employee / labor_cost_per_employee"
    ],
    
    "key_metrics": [
        "payroll_cost_ratio",
        "labor_productivity_index",
        "average_compensation_level",
        "payroll_budget_accuracy",
        "employee_cost_efficiency",
        "compensation_competitiveness"
    ],
    
    "data_visualization": [
        "Структура фонда оплаты труда по подразделениям",
        "Динамика изменения ФОТ по месяцам",
        "Сравнение фактических и плановых затрат на персонал",
        "Анализ производительности труда по отделам",
        "Распределение затрат на персонал по категориям",
        "Бенчмаркинг уровня оплаты труда"
    ],
    
    "ai_analysis_prompts": [
        "Проанализируй эффективность затрат на персонал",
        "Оцени соответствие уровня оплаты труда рыночным стандартам",
        "Определи подразделения с наибольшими отклонениями по ФОТ",
        "Предложи меры по оптимизации кадровых затрат"
    ],
    
    "python_implementation_notes": [
        "Создать класс PayrollManager для управления ФОТ",
        "Реализовать автоматизированные расчеты налогов и взносов",
        "Использовать pandas для анализа кадровых данных",
        "Добавить интеграцию с HR-системами",
        "Создать систему контроля бюджета ФОТ"
    ]
},

# Инструмент 15
"15_uchet_logistiki": {
    "instrument_number": 15,
    "title": "Учет логистики",
    "category": "logistics_accounting",
    "description": "Учет и анализ логистических затрат, оптимизация транспортных расходов",
    
    "tasks": [
        "Учет всех видов логистических затрат",
        "Анализ эффективности транспортных маршрутов",
        "Оптимизация складских операций",
        "Контроль затрат на логистические услуги"
    ],
    
    "calculation_algorithm": [
        "Классифицировать логистические затраты по видам операций",
        "Рассчитать стоимость логистических услуг на единицу груза",
        "Проанализировать эффективность различных видов доставки",
        "Оптимизировать маршруты и способы транспортировки",
        "Рассчитать ключевые показатели эффективности логистики"
    ],
    
    "auto_calculated_fields": [
        "total_logistics_costs",        # Общие логистические затраты
        "cost_per_delivery",           # Стоимость доставки
        "warehouse_cost_per_unit",     # Складские затраты на единицу
        "transport_efficiency_index",  # Индекс эффективности транспорта
        "logistics_cost_ratio",        # Доля логистических затрат
        "delivery_performance_metrics" # Метрики эффективности доставки
    ],
    
    "manual_input_fields": [
        "transportation_costs",        # Транспортные расходы (dict)
        "warehouse_costs",             # Складские расходы (dict)
        "packaging_costs",             # Затраты на упаковку (dict)
        "handling_costs",              # Затраты на погрузку/разгрузку (dict)
        "fuel_costs",                  # Затраты на топливо (dict)
        "delivery_volumes",            # Объемы доставки (dict)
        "route_data",                  # Данные по маршрутам (dict)
        "service_provider_costs",      # Затраты на логистических провайдеров (dict)
        "insurance_costs"              # Страховые расходы (dict)
    ],
    
    "editable_calculation_fields": [
        "fuel_price_forecast",         # Прогноз цен на топливо (float, default: 50.0)
        "vehicle_utilization_rate",    # Коэффициент использования транспорта (float, default: 0.75)
        "warehouse_utilization_rate",  # Коэффициент использования складов (float, default: 0.80)
        "delivery_time_target",        # Целевое время доставки в часах (float, default: 24.0)
        "damage_rate_assumption",      # Предполагаемый процент порчи (float, default: 0.5)
        "seasonal_demand_factor"       # Сезонный фактор спроса (dict)
    ],
    
    "main_formulas": [
        "cost_per_km = (fuel_costs + maintenance_costs + driver_costs) / total_km",
        "warehouse_cost_per_unit = total_warehouse_costs / total_units_stored",
        "delivery_cost_efficiency = delivery_revenue / total_delivery_costs",
        "logistics_roi = (logistics_savings - logistics_investments) / logistics_investments",
        "on_time_delivery_rate = on_time_deliveries / total_deliveries * 100",
        "inventory_turnover = cost_of_goods_sold / average_inventory_value"
    ],
    
    "key_metrics": [
        "logistics_cost_optimization",
        "delivery_reliability_score",
        "warehouse_efficiency_index",
        "transport_cost_per_unit",
        "logistics_service_level",
        "supply_chain_agility"
    ],
    
    "data_visualization": [
        "Структура логистических затрат по видам операций",
        "Карта маршрутов с анализом эффективности",
        "Динамика логистических затрат по периодам",
        "Сравнительный анализ поставщиков логистических услуг",
        "KPI дашборд логистических показателей",
        "Анализ загрузки складских мощностей"
    ],
    
    "ai_analysis_prompts": [
        "Проанализируй эффективность текущей логистической системы",
        "Определи возможности снижения транспортных затрат",
        "Оцени оптимальность размещения складских мощностей",
        "Предложи меры по улучшению качества логистических услуг"
    ],
    
    "python_implementation_notes": [
        "Создать класс LogisticsAccountingSystem",
        "Реализовать алгоритмы оптимизации маршрутов",
        "Использовать геолокационные API для расчета расстояний",
        "Добавить модули прогнозирования спроса",
        "Интегрировать с WMS и TMS системами"
    ]
}

}

print("Создана структура для инструментов 11-15...")
print("Продолжение следует...")