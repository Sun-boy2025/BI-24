# Продолжение создания файла с инструментами 3-10

# Добавляем остальные инструменты к существующей структуре
additional_instruments = {

# Инструмент 3
"03_finansovaya_model": {
    "instrument_number": 3,
    "title": "Финансовая модель",
    "category": "business_performance",
    "description": "Комплексная оценка прибыльности, рентабельности и устойчивости бизнеса",
    
    "tasks": [
        "Комплексная оценка прибыльности, рентабельности и устойчивости бизнеса",
        "Калькуляция ключевых финансовых показателей",
        "Моделирование различных сценариев развития",
        "Анализ точки безубыточности"
    ],
    
    "calculation_algorithm": [
        "Разделить доходы на фиксированные и переменные по месяцам",
        "Учесть все категории расходов: постоянные, переменные, налоговые",
        "Рассчитать EBITDA, чистую прибыль, рентабельность",
        "Провести сценарное моделирование изменений",
        "Оценить влияние изменений на устойчивость компании"
    ],
    
    "auto_calculated_fields": [
        "revenue",               # Выручка
        "gross_profit",          # Валовая прибыль
        "ebitda",               # EBITDA
        "net_profit",           # Чистая прибыль
        "break_even_point",     # Точка безубыточности
        "profitability_ratios"  # Коэффициенты рентабельности
    ],
    
    "manual_input_fields": [
        "fixed_revenue",         # Фиксированные доходы по месяцам (dict)
        "variable_revenue_rate", # Ставка переменных доходов (float)
        "fixed_costs",          # Постоянные расходы по статьям (dict)
        "variable_cost_rate",   # Доля переменных расходов (float)
        "tax_rate",             # Налоговая ставка (float)
        "interest_expenses",    # Процентные расходы (float)
        "one_time_expenses"     # Единовременные расходы (dict)
    ],
    
    "editable_calculation_fields": [
        "planning_horizon_months",   # Горизонт планирования (int, default: 12)
        "scenario_variations",       # Вариации для сценариев в % (dict, default: {"pessimistic": -20, "optimistic": 20})
        "minimum_margin_threshold",  # Минимальный порог маржинальности (float, default: 15.0)
        "growth_rate_assumption"     # Предполагаемый темп роста (float, default: 5.0)
    ],
    
    "main_formulas": [
        "gross_profit = revenue - variable_costs",
        "ebitda = gross_profit - fixed_costs",
        "net_profit = ebitda - interest_expenses - taxes",
        "margin_ratio = gross_profit / revenue * 100",
        "break_even_point = fixed_costs / (1 - variable_cost_rate)",
        "roe = net_profit / equity"
    ],
    
    "key_metrics": [
        "gross_margin_percentage",
        "ebitda_margin",
        "net_profit_margin", 
        "return_on_equity",
        "return_on_assets",
        "financial_leverage"
    ],
    
    "data_visualization": [
        "Линейный график динамики ключевых показателей",
        "Водопадная диаграмма формирования прибыли",
        "Сценарный анализ в виде торнадо-диаграммы",
        "График безубыточности",
        "Дашборд ключевых финансовых метрик"
    ],
    
    "ai_analysis_prompts": [
        "Оцени финансовую устойчивость компании на основе рассчитанных показателей",
        "Определи наиболее критичные факторы для прибыльности бизнеса",
        "Проанализируй чувствительность бизнеса к изменениям выручки и затрат",
        "Предложи меры по повышению рентабельности"
    ],
    
    "python_implementation_notes": [
        "Создать класс FinancialModel с методами расчета всех показателей",
        "Реализовать сценарное моделирование через изменение параметров",
        "Использовать scipy для оптимизационных расчетов",
        "Добавить методы чувствительности к изменению параметров",
        "Создать интерактивный дашборд с помощью dash/streamlit"
    ]
},

# Инструмент 4
"04_vliyanie_skidki": {
    "instrument_number": 4,
    "title": "Влияние скидки на прибыль",
    "category": "pricing_optimization",
    "description": "Определение оптимального размера скидки для максимизации прибыли",
    
    "tasks": [
        "Определение оптимального размера скидки",
        "Анализ эластичности спроса по цене",
        "Расчет влияния ценовой политики на финансовые результаты",
        "Моделирование компенсирующего роста продаж"
    ],
    
    "calculation_algorithm": [
        "Определить текущую маржинальность товара/услуги",
        "Рассчитать необходимое увеличение объема для компенсации скидки",
        "Оценить реальную эластичность спроса в сегменте",
        "Смоделировать различные варианты скидок",
        "Учесть дополнительные затраты на увеличение объемов"
    ],
    
    "auto_calculated_fields": [
        "current_margin",           # Текущая маржинальность
        "break_even_volume_increase", # Компенсирующий рост объема
        "profit_impact",            # Влияние на прибыль
        "optimal_discount_range",   # Оптимальный диапазон скидок
        "price_elasticity"          # Эластичность по цене
    ],
    
    "manual_input_fields": [
        "current_price",            # Текущая цена (float)
        "unit_cost",               # Себестоимость единицы (float)
        "current_volume",          # Текущий объем продаж (int)
        "fixed_costs",             # Постоянные расходы (float)
        "demand_elasticity",       # Коэффициент эластичности спроса (float)
        "competitor_prices",       # Цены конкурентов (list)
        "max_production_capacity"  # Максимальная производственная мощность (int)
    ],
    
    "editable_calculation_fields": [
        "discount_range_min",      # Минимальная скидка для анализа (float, default: 1.0)
        "discount_range_max",      # Максимальная скидка для анализа (float, default: 50.0)
        "discount_step",           # Шаг изменения скидки (float, default: 1.0)
        "additional_cost_factor",  # Коэффициент дополнительных затрат (float, default: 1.05)
        "market_share_factor"      # Фактор влияния на долю рынка (float, default: 1.2)
    ],
    
    "main_formulas": [
        "current_margin = (current_price - unit_cost) / current_price",
        "compensating_growth = discount_percent / (current_margin - discount_percent)",
        "new_profit = (current_price * (1 - discount) - unit_cost) * new_volume - fixed_costs",
        "equilibrium_discount = current_margin / 2",
        "price_sensitivity = volume_change_percent / price_change_percent"
    ],
    
    "key_metrics": [
        "optimal_discount_percent",
        "profit_maximizing_price",
        "volume_at_optimal_discount",
        "revenue_impact",
        "margin_preservation_threshold"
    ],
    
    "data_visualization": [
        "График зависимости прибыли от размера скидки",
        "Диаграмма компенсирующего роста продаж",
        "Сравнительный анализ сценариев прибыльности",
        "Кривая спроса и предложения",
        "Тепловая карта прибыльности по цене и объему"
    ],
    
    "ai_analysis_prompts": [
        "Определи оптимальную ценовую стратегию для максимизации прибыли",
        "Проанализируй риски от предоставления скидок",
        "Оцени конкурентоспособность текущих цен",
        "Предложи тактику динамического ценообразования"
    ],
    
    "python_implementation_notes": [
        "Создать класс PricingOptimizer для расчетов оптимизации",
        "Реализовать алгоритмы поиска оптимума функции прибыли",
        "Использовать matplotlib для построения кривых прибыльности",
        "Добавить валидацию реалистичности параметров эластичности",
        "Интегрировать с базой данных конкурентного анализа"
    ]
},

# Инструмент 5
"05_byudzhet": {
    "instrument_number": 5,
    "title": "Бюджет",
    "category": "budget_management",
    "description": "Планирование и контроль финансовых ресурсов по подразделениям",
    
    "tasks": [
        "Планирование финансовых ресурсов по подразделениям",
        "Обеспечение координации между центрами ответственности",
        "Мониторинг исполнения плановых показателей",
        "Анализ отклонений план/факт"
    ],
    
    "calculation_algorithm": [
        "Определить центры финансовой ответственности (ЦФО)",
        "Установить плановые показатели доходов и расходов по ЦФО",
        "Распределить общие расходы между подразделениями",
        "Настроить мониторинг план/факт отклонений",
        "Создать механизмы корректировки бюджетов"
    ],
    
    "auto_calculated_fields": [
        "plan_fact_deviations",     # Отклонения план/факт
        "budget_execution_rate",    # Коэффициент исполнения бюджета
        "efficiency_by_department", # Эффективность по подразделениям
        "budget_utilization",       # Использование бюджета
        "variance_analysis"         # Анализ отклонений
    ],
    
    "manual_input_fields": [
        "departments",              # Список подразделений (list)
        "planned_revenues_by_dept", # Плановые доходы по подразделениям (dict)
        "planned_expenses_by_dept", # Плановые расходы по подразделениям (dict)
        "actual_revenues_by_dept",  # Фактические доходы по подразделениям (dict)
        "actual_expenses_by_dept",  # Фактические расходы по подразделениям (dict)
        "shared_costs",            # Общие расходы для распределения (dict)
        "allocation_keys"          # Ключи распределения расходов (dict)
    ],
    
    "editable_calculation_fields": [
        "budget_period_months",     # Период бюджетирования (int, default: 12)
        "variance_threshold",       # Порог значимого отклонения (float, default: 5.0)
        "budget_revision_frequency", # Частота пересмотра бюджета (int, default: 3)
        "performance_weight",       # Вес показателей эффективности (dict)
        "allocation_method"         # Метод распределения затрат (str, default: "proportional")
    ],
    
    "main_formulas": [
        "revenue_deviation = actual_revenues - planned_revenues",
        "expense_deviation = actual_expenses - planned_expenses", 
        "execution_rate = actual_result / planned_result",
        "department_efficiency = department_result / department_budget",
        "variance_percentage = (actual - plan) / plan * 100"
    ],
    
    "key_metrics": [
        "overall_budget_execution",
        "revenue_achievement_rate",
        "cost_control_efficiency",
        "department_ranking",
        "budget_accuracy_score"
    ],
    
    "data_visualization": [
        "Дашборд исполнения бюджета по ЦФО",
        "Водопадная диаграмма отклонений от плана",
        "Тепловая карта эффективности подразделений",
        "Столбчатая диаграмма план/факт по периодам",
        "Круговая диаграмма распределения бюджета"
    ],
    
    "ai_analysis_prompts": [
        "Проанализируй эффективность бюджетного планирования",
        "Выяви подразделения с наибольшими отклонениями от плана",
        "Оцени качество прогнозирования по статьям бюджета",
        "Предложи меры по повышению бюджетной дисциплины"
    ],
    
    "python_implementation_notes": [
        "Создать класс BudgetManager для управления бюджетами",
        "Реализовать различные методы распределения затрат",
        "Использовать pandas для анализа временных рядов",
        "Добавить систему уведомлений о превышениях бюджета",
        "Создать API для интеграции с ERP-системами"
    ]
}

}

# Объединяем с существующими инструментами
instruments_data.update(additional_instruments)

print(f"Добавлены инструменты 3-5. Всего инструментов: {len(instruments_data)}")
print("Продолжение следует...")