# Полное описание аналитических инструментов для программного комплекса
# Инструкция для разработчика Python (инструменты 6-25)

# Продолжение с инструмента 6
instruments_data_continued = {

# Инструмент 6
"06_otchet_otdela_prodazh": {
    "instrument_number": 6,
    "title": "Отчет отдела продаж",
    "category": "sales_analytics",
    "description": "Анализ эффективности продаж, оценка работы продавцов и каналов",
    
    "tasks": [
        "Анализ эффективности продаж по менеджерам и каналам",
        "Оценка выполнения планов продаж",
        "Выявление трендов и сезонности продаж",
        "Анализ воронки продаж и конверсии"
    ],
    
    "calculation_algorithm": [
        "Собрать данные о продажах по товарам, клиентам, каналам, менеджерам",
        "Рассчитать ключевые метрики продаж (конверсия, средний чек, цикл продаж)",
        "Проанализировать воронку продаж и узкие места",
        "Оценить рентабельность различных направлений продаж",
        "Спрогнозировать будущие продажи на основе трендов"
    ],
    
    "auto_calculated_fields": [
        "total_sales_revenue",           # Общая выручка от продаж
        "average_deal_size",            # Средний размер сделки
        "conversion_rate",              # Конверсия лидов в сделки
        "sales_cycle_length",           # Длительность цикла продаж
        "manager_performance_ranking",   # Рейтинг менеджеров по эффективности
        "sales_trend_analysis"          # Анализ трендов продаж
    ],
    
    "manual_input_fields": [
        "sales_data_by_manager",        # Данные продаж по менеджерам (dict)
        "leads_data",                   # Данные о лидах (dict)
        "deals_pipeline",               # Воронка сделок (dict)
        "sales_targets",                # Планы продаж (dict)
        "product_categories",           # Категории товаров (list)
        "sales_channels",               # Каналы продаж (list)
        "customer_segments",            # Сегменты клиентов (list)
        "time_period_start",            # Начало анализируемого периода (date)
        "time_period_end"               # Конец анализируемого периода (date)
    ],
    
    "editable_calculation_fields": [
        "target_conversion_rate",       # Целевая конверсия (float, default: 20.0)
        "minimum_deal_size",            # Минимальный размер сделки (float, default: 1000)
        "sales_cycle_benchmark",        # Эталонная длительность цикла в днях (int, default: 30)
        "performance_weight_revenue",   # Вес выручки в оценке (float, default: 0.6)
        "performance_weight_deals",     # Вес количества сделок в оценке (float, default: 0.4)
        "seasonality_factor"            # Коэффициент сезонности (dict)
    ],
    
    "main_formulas": [
        "conversion_rate = closed_deals / total_leads * 100",
        "average_deal_size = total_revenue / number_of_deals",
        "manager_efficiency = (actual_sales / planned_sales) * 100",
        "revenue_per_manager = total_revenue / number_of_managers",
        "customer_ltv = average_deal_size * purchase_frequency * customer_lifespan",
        "sales_velocity = (leads * conversion_rate * average_deal_size) / sales_cycle_length"
    ],
    
    "key_metrics": [
        "monthly_sales_growth",
        "plan_achievement_percentage",
        "customer_acquisition_cost",
        "revenue_per_lead",
        "top_performing_managers",
        "underperforming_segments"
    ],
    
    "data_visualization": [
        "Воронка продаж с конверсией по этапам",
        "График динамики продаж по месяцам",
        "Рейтинг менеджеров по ключевым метрикам",
        "Тепловая карта продаж по регионам/сегментам",
        "Столбчатая диаграмма план/факт по периодам",
        "Круговая диаграмма структуры продаж по каналам"
    ],
    
    "ai_analysis_prompts": [
        "Проанализируй эффективность работы отдела продаж",
        "Выяви менеджеров с наилучшими и наихудшими показателями",
        "Определи наиболее и наименее прибыльные каналы продаж",
        "Предложи меры по повышению конверсии и среднего чека"
    ],
    
    "python_implementation_notes": [
        "Создать класс SalesAnalytics для обработки данных продаж",
        "Реализовать методы расчета воронки продаж",
        "Использовать pandas для группировки данных по менеджерам",
        "Добавить функции прогнозирования продаж",
        "Создать дашборд с drill-down по менеджерам и периодам"
    ]
},

# Инструмент 7
"07_faktory_prodazh": {
    "instrument_number": 7,
    "title": "Факторы продаж",
    "category": "sales_factor_analysis",
    "description": "Факторный анализ изменения выручки и выявление драйверов роста",
    
    "tasks": [
        "Факторный анализ изменения выручки от продаж",
        "Выявление драйверов роста и падения продаж",
        "Оценка влияния цены, объема и структуры на результат",
        "Анализ влияния внешних и внутренних факторов"
    ],
    
    "calculation_algorithm": [
        "Разложить изменение выручки на ценовой и объемный факторы",
        "Проанализировать влияние изменения структуры продаж",
        "Оценить влияние сезонности и внешних факторов",
        "Рассчитать эластичность продаж по различным факторам",
        "Определить приоритетные направления для роста"
    ],
    
    "auto_calculated_fields": [
        "price_factor_impact",          # Влияние ценового фактора
        "volume_factor_impact",         # Влияние объемного фактора
        "mix_factor_impact",            # Влияние структурного фактора
        "total_revenue_change",         # Общее изменение выручки
        "factor_contribution_ranking",   # Ранжирование факторов по влиянию
        "elasticity_coefficients"      # Коэффициенты эластичности
    ],
    
    "manual_input_fields": [
        "current_period_data",          # Данные текущего периода (dict)
        "previous_period_data",         # Данные предыдущего периода (dict)
        "product_prices_current",       # Цены товаров текущий период (dict)
        "product_prices_previous",      # Цены товаров предыдущий период (dict)
        "sales_volumes_current",        # Объемы продаж текущий период (dict)
        "sales_volumes_previous",       # Объемы продаж предыдущий период (dict)
        "external_factors",             # Внешние факторы (dict)
        "marketing_spend",              # Расходы на маркетинг (float)
        "competitor_actions"            # Действия конкурентов (list)
    ],
    
    "editable_calculation_fields": [
        "price_elasticity_base",        # Базовая эластичность по цене (float, default: -1.5)
        "volume_sensitivity",           # Чувствительность к объему (float, default: 1.2)
        "seasonal_adjustment",          # Сезонная поправка (dict)
        "market_growth_rate",           # Темп роста рынка (float, default: 5.0)
        "inflation_rate",               # Уровень инфляции (float, default: 4.0)
        "competition_intensity"         # Интенсивность конкуренции (float, default: 1.0)
    ],
    
    "main_formulas": [
        "total_revenue_change = current_revenue - previous_revenue",
        "price_factor = (price_new - price_old) * volume_old",
        "volume_factor = price_new * (volume_new - volume_old)",
        "mix_factor = sum(share_change * margin_difference)",
        "price_elasticity = (volume_change_percent / price_change_percent)",
        "factor_significance = abs(factor_impact) / total_change * 100"
    ],
    
    "key_metrics": [
        "dominant_growth_factor",
        "price_optimization_potential",
        "volume_growth_opportunity",
        "market_share_change",
        "competitive_position_index",
        "revenue_volatility_score"
    ],
    
    "data_visualization": [
        "Водопадная диаграмма факторов изменения выручки",
        "Матрица факторов влияния (тепловая карта)",
        "График трендов по ключевым факторам",
        "Диаграмма эластичности спроса",
        "Сравнительный анализ периодов",
        "Торнадо-диаграмма чувствительности"
    ],
    
    "ai_analysis_prompts": [
        "Определи ключевые драйверы изменения выручки",
        "Проанализируй влияние ценовой политики на продажи",
        "Оцени потенциал роста через различные факторы",
        "Предложи стратегию оптимизации факторов продаж"
    ],
    
    "python_implementation_notes": [
        "Создать класс SalesFactorAnalysis для факторного разложения",
        "Реализовать методы расчета эластичности",
        "Использовать numpy для математических операций",
        "Добавить алгоритмы детекции структурных сдвигов",
        "Создать интерактивные графики чувствительности"
    ]
},

# Инструмент 8
"08_otchet_marketingu": {
    "instrument_number": 8,
    "title": "Отчет по маркетингу",
    "category": "marketing_analytics",
    "description": "Анализ эффективности маркетинговых каналов и ROI кампаний",
    
    "tasks": [
        "Оценка эффективности маркетинговых каналов",
        "Расчет ROI и ROAS рекламных кампаний",
        "Анализ стоимости привлечения клиентов (CAC)",
        "Оптимизация распределения маркетингового бюджета"
    ],
    
    "calculation_algorithm": [
        "Собрать данные о затратах по каналам привлечения",
        "Отследить конверсию и атрибуцию по каждому каналу",
        "Рассчитать CAC (Customer Acquisition Cost) и LTV",
        "Определить ROI и ROAS по каналам и кампаниям",
        "Провести атрибуционный анализ мультиканальных воронок"
    ],
    
    "auto_calculated_fields": [
        "channel_roi",                  # ROI по каналам
        "customer_acquisition_cost",    # Стоимость привлечения клиента
        "lifetime_value",               # Жизненная ценность клиента
        "ltv_cac_ratio",               # Соотношение LTV/CAC
        "channel_performance_ranking",  # Рейтинг каналов по эффективности
        "budget_allocation_optimal"     # Оптимальное распределение бюджета
    ],
    
    "manual_input_fields": [
        "marketing_channels",           # Список маркетинговых каналов (list)
        "channel_costs",               # Затраты по каналам (dict)
        "channel_conversions",          # Конверсии по каналам (dict)
        "campaign_data",               # Данные кампаний (dict)
        "customer_journey_data",        # Данные пути клиента (dict)
        "attribution_model",            # Модель атрибуции (str)
        "brand_awareness_metrics",      # Метрики узнаваемости бренда (dict)
        "organic_traffic_data",         # Данные органического трафика (dict)
        "competitor_spending"           # Расходы конкурентов (dict)
    ],
    
    "editable_calculation_fields": [
        "target_roi_threshold",         # Целевой порог ROI (float, default: 300.0)
        "attribution_window_days",      # Окно атрибуции в днях (int, default: 30)
        "ltv_calculation_period",       # Период расчета LTV в месяцах (int, default: 24)
        "brand_value_weight",           # Вес брендинговых метрик (float, default: 0.3)
        "organic_attribution_share",    # Доля органической атрибуции (float, default: 0.2)
        "seasonality_factors"           # Сезонные коэффициенты (dict)
    ],
    
    "main_formulas": [
        "cac = total_marketing_spend / number_of_acquired_customers",
        "roi_marketing = (revenue_from_channel - channel_cost) / channel_cost * 100",
        "roas = revenue_from_ads / ad_spend",
        "ltv_cac_ratio = lifetime_value / customer_acquisition_cost",
        "channel_efficiency = conversions / impressions * 100",
        "payback_period = cac / average_monthly_revenue_per_customer"
    ],
    
    "key_metrics": [
        "best_performing_channel",
        "worst_performing_channel",
        "overall_marketing_roi",
        "customer_payback_period",
        "channel_saturation_points",
        "incremental_revenue_impact"
    ],
    
    "data_visualization": [
        "Воронка маркетинга по каналам",
        "Дашборд ROI и ROAS по кампаниям",
        "Тепловая карта эффективности каналов",
        "График динамики CAC и LTV",
        "Водопадная диаграмма атрибуции",
        "Матрица каналов по объему и эффективности"
    ],
    
    "ai_analysis_prompts": [
        "Проанализируй эффективность маркетинговых каналов",
        "Определи оптимальное распределение маркетингового бюджета",
        "Выяви каналы с лучшим соотношением LTV/CAC",
        "Предложи стратегию масштабирования успешных каналов"
    ],
    
    "python_implementation_notes": [
        "Создать класс MarketingAnalytics для анализа каналов",
        "Реализовать различные модели атрибуции",
        "Использовать sklearn для прогнозного моделирования",
        "Добавить интеграцию с рекламными API",
        "Создать алгоритмы оптимизации бюджета"
    ]
},

# Инструмент 9
"09_yunit_ekonomika_marketpleysy": {
    "instrument_number": 9,
    "title": "Юнит-экономика для маркетплейсов",
    "category": "marketplace_economics",
    "description": "Расчет прибыльности на единицу товара на маркетплейсах",
    
    "tasks": [
        "Расчет прибыльности на единицу товара на маркетплейсах",
        "Учет всех комиссий и затрат маркетплейса",
        "Оптимизация ценовой стратегии с учетом комиссий",
        "Анализ влияния различных факторов на unit-экономику"
    ],
    
    "calculation_algorithm": [
        "Рассчитать себестоимость товара с доставкой до склада маркетплейса",
        "Учесть все комиссии маркетплейса (эквайринг, фулфилмент, реклама)",
        "Включить затраты на возвраты, брак и штрафы",
        "Рассчитать налоговую нагрузку с учетом режима",
        "Определить чистую прибыль с единицы товара"
    ],
    
    "auto_calculated_fields": [
        "unit_profit",                  # Прибыль с единицы товара
        "unit_margin_percentage",       # Маржинальность в процентах
        "break_even_volume",            # Точка безубыточности в штуках
        "roi_per_unit",                # ROI на единицу товара
        "marketplace_commission_total", # Общая комиссия маркетплейса
        "profitability_ranking"         # Рейтинг товаров по прибыльности
    ],
    
    "manual_input_fields": [
        "product_cost_price",           # Себестоимость товара (float)
        "marketplace_selling_price",    # Цена продажи на маркетплейсе (float)
        "marketplace_commission_rate",  # Ставка комиссии маркетплейса (float)
        "fulfillment_cost",            # Стоимость фулфилмента (float)
        "advertising_cost_per_unit",    # Затраты на рекламу на единицу (float)
        "return_rate_percentage",       # Процент возвратов (float)
        "logistics_cost",               # Логистические затраты (float)
        "tax_rate",                     # Налоговая ставка (float)
        "packaging_cost",               # Стоимость упаковки (float)
        "defect_rate_percentage"        # Процент брака (float)
    ],
    
    "editable_calculation_fields": [
        "target_margin_threshold",      # Целевой порог маржинальности (float, default: 20.0)
        "minimum_roi_threshold",        # Минимальный порог ROI (float, default: 30.0)
        "volume_discount_tiers",        # Уровни объемных скидок (dict)
        "seasonal_price_adjustment",    # Сезонная корректировка цен (dict)
        "competitor_price_factor",      # Фактор конкурентных цен (float, default: 0.95)
        "inventory_carrying_cost"       # Стоимость содержания запасов (float, default: 2.0)
    ],
    
    "main_formulas": [
        "unit_profit = selling_price - cost_price - marketplace_commission - fulfillment - advertising - logistics - packaging - tax",
        "unit_margin = unit_profit / selling_price * 100",
        "marketplace_commission = selling_price * commission_rate",
        "break_even_volume = fixed_costs / unit_profit",
        "roi_per_unit = unit_profit / (cost_price + inventory_investment) * 100",
        "effective_commission_rate = total_marketplace_costs / selling_price * 100"
    ],
    
    "key_metrics": [
        "average_unit_margin",
        "most_profitable_products",
        "loss_making_products",
        "commission_impact_analysis",
        "price_optimization_potential",
        "volume_profitability_correlation"
    ],
    
    "data_visualization": [
        "Водопадная диаграмма структуры затрат на единицу",
        "График рентабельности по товарам",
        "Сравнение эффективности маркетплейсов",
        "Матрица товаров по объему и марже",
        "Анализ чувствительности к изменению комиссий",
        "График точки безубыточности"
    ],
    
    "ai_analysis_prompts": [
        "Проанализируй прибыльность товаров на маркетплейсе",
        "Определи товары с наилучшей unit-экономикой",
        "Оцени влияние изменения комиссий на прибыльность",
        "Предложи стратегию ценообразования для маркетплейса"
    ],
    
    "python_implementation_notes": [
        "Создать класс MarketplaceUnitEconomics для расчетов",
        "Реализовать методы учета различных типов комиссий",
        "Использовать pandas для анализа портфеля товаров",
        "Добавить интеграцию с API маркетплейсов",
        "Создать алгоритмы оптимизации цен"
    ]
},

# Инструмент 10
"10_finmodel_marketpleysy": {
    "instrument_number": 10,
    "title": "Финмодель для маркетплейсов",
    "category": "marketplace_financial_modeling",
    "description": "Комплексное финансовое планирование деятельности на маркетплейсах",
    
    "tasks": [
        "Комплексное финансовое планирование на маркетплейсах",
        "Прогнозирование развития с учетом специфики маркетплейсов",
        "Планирование инвестиций в товарные запасы",
        "Моделирование различных сценариев роста"
    ],
    
    "calculation_algorithm": [
        "Спрогнозировать объемы продаж по категориям товаров",
        "Рассчитать потребность в оборотном капитале для запасов",
        "Учесть сезонность и тренды продаж на маркетплейсах",
        "Смоделировать различные сценарии развития бизнеса",
        "Рассчитать ключевые финансовые показатели с учетом специфики"
    ],
    
    "auto_calculated_fields": [
        "inventory_turnover_rate",      # Оборачиваемость запасов
        "working_capital_requirement",  # Потребность в оборотном капитале
        "roi_inventory_investment",     # ROI инвестиций в запасы
        "cash_conversion_cycle",        # Цикл оборота денежных средств
        "marketplace_revenue_forecast", # Прогноз выручки
        "profitability_by_category"     # Прибыльность по категориям
    ],
    
    "manual_input_fields": [
        "product_categories",           # Категории товаров (list)
        "historical_sales_data",       # Исторические данные продаж (dict)
        "inventory_levels",             # Уровни запасов (dict)
        "supplier_terms",               # Условия поставщиков (dict)
        "marketplace_growth_rates",     # Темпы роста маркетплейсов (dict)
        "seasonal_patterns",            # Сезонные паттерны (dict)
        "marketing_budget_plan",        # План маркетингового бюджета (dict)
        "expansion_plans",              # Планы расширения (dict)
        "investment_capacity"           # Инвестиционные возможности (float)
    ],
    
    "editable_calculation_fields": [
        "planning_horizon_months",      # Горизонт планирования (int, default: 24)
        "target_inventory_turnover",    # Целевая оборачиваемость (float, default: 12.0)
        "safety_stock_percentage",      # Процент страхового запаса (float, default: 15.0)
        "growth_rate_conservative",     # Консервативный темп роста (float, default: 15.0)
        "growth_rate_aggressive",       # Агрессивный темп роста (float, default: 50.0)
        "cash_reserve_percentage"       # Процент денежного резерва (float, default: 10.0)
    ],
    
    "main_formulas": [
        "inventory_turnover = cost_of_goods_sold / average_inventory",
        "working_capital = inventory + receivables - payables",
        "cash_conversion_cycle = days_in_inventory + days_in_receivables - days_in_payables",
        "roi_inventory = gross_profit / average_inventory_investment * 100",
        "revenue_forecast = base_revenue * (1 + growth_rate) * seasonality_factor",
        "optimal_inventory = forecasted_demand * (lead_time + safety_stock_days)"
    ],
    
    "key_metrics": [
        "inventory_optimization_potential",
        "cash_flow_breakeven_point",
        "return_on_invested_capital",
        "revenue_growth_sustainability",
        "marketplace_dependency_risk",
        "scalability_indicators"
    ],
    
    "data_visualization": [
        "Прогноз продаж по месяцам и категориям",
        "График потребности в финансировании",
        "Матрица товаров по прибыльности и оборачиваемости",
        "Сценарный анализ роста",
        "Дашборд ключевых метрик маркетплейса",
        "График планируемых инвестиций в запасы"
    ],
    
    "ai_analysis_prompts": [
        "Проанализируй финансовую модель маркетплейс-бизнеса",
        "Определи оптимальную стратегию управления запасами",
        "Оцени потребность в финансировании для роста",
        "Предложи план масштабирования бизнеса"
    ],
    
    "python_implementation_notes": [
        "Создать класс MarketplaceFinancialModel",
        "Реализовать алгоритмы прогнозирования спроса",
        "Использовать scikit-learn для временных рядов",
        "Добавить оптимизацию управления запасами",
        "Создать сценарное моделирование роста"
    ]
}

}

print("Создана структура для инструментов 6-10...")
print("Продолжение со следующими инструментами...")