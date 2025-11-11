# Создание полного файла с описанием всех 25 аналитических инструментов 
# в формате для разработчика Python-приложения

instruments_data = {

# Инструмент 1
"01_platezhnyy_kalendar": {
    "instrument_number": 1,
    "title": "Платежный календарь",
    "category": "cash_flow_management",
    "description": "Планирование денежных потоков компании по датам, предотвращение кассовых разрывов",
    
    "tasks": [
        "Планирование денежных потоков компании по датам",
        "Предотвращение кассовых разрывов",
        "Контроль своевременности оплаты счетов и поступлений",
        "Оптимизация ликвидности"
    ],
    
    "calculation_algorithm": [
        "Собрать прогнозируемые поступления и платежи с разбивкой по дням",
        "Внести начальный остаток по счету",
        "Для каждого дня: остаток = остаток_вчера + поступления - платежи",
        "Выделить дни с отрицательным остатком (кассовый разрыв)",
        "Ранжировать платежи по срочности — налоги, кредиты, зарплата как обязательные"
    ],
    
    "auto_calculated_fields": [
        "daily_balance",  # Остаток на каждый день
        "cash_gaps",      # Кассовые разрывы
        "cumulative_inflow",  # Накопленные поступления
        "cumulative_outflow"  # Накопленные расходы
    ],
    
    "manual_input_fields": [
        "initial_balance",        # Начальный остаток (float)
        "planned_receipts",       # Планируемые поступления по дням (dict: date -> float)
        "planned_payments",       # Планируемые платежи по дням (dict: date -> float)
        "payment_priorities",     # Приоритеты платежей (dict: payment_id -> priority_level)
        "credit_limit"           # Кредитный лимит (float)
    ],
    
    "editable_calculation_fields": [
        "forecast_period_days",   # Период прогнозирования в днях (int, default: 90)
        "critical_balance_level", # Критический уровень остатка (float, default: 0)
        "payment_delay_buffer"    # Буфер на задержку платежей в днях (int, default: 3)
    ],
    
    "main_formulas": [
        "daily_balance[i] = daily_balance[i-1] + receipts[i] - payments[i]",
        "cash_gap = daily_balance[i] < critical_balance_level",
        "coverage_ratio = current_assets / short_term_liabilities"
    ],
    
    "key_metrics": [
        "average_daily_balance",
        "number_of_cash_gaps", 
        "max_cash_gap_amount",
        "days_with_negative_balance",
        "liquidity_coverage_ratio"
    ],
    
    "data_visualization": [
        "Линейный график остатка денежных средств по дням",
        "Гистограмма поступлений и платежей по дням", 
        "Выделение дат с кассовым разрывом цветом",
        "Календарная тепловая карта с уровнями остатков",
        "Столбчатая диаграмма платежей по приоритетам"
    ],
    
    "ai_analysis_prompts": [
        "Проанализируй тенденции денежных потоков и выяви риски кассовых разрывов",
        "Определи оптимальный график платежей для минимизации рисков", 
        "Оцени достаточность текущих резервов ликвидности",
        "Предложи меры по оптимизации платежного календаря"
    ],
    
    "python_implementation_notes": [
        "Использовать pandas для работы с временными рядами",
        "Создать класс PaymentCalendar с методами расчета остатков",
        "Реализовать алгоритм выявления кассовых разрывов",
        "Добавить валидацию корректности дат и сумм",
        "Использовать plotly для интерактивных графиков"
    ]
},

# Инструмент 2  
"02_dds_klassicheskiy": {
    "instrument_number": 2,
    "title": "ДДС классический",
    "category": "cash_flow_analysis", 
    "description": "Анализ движения денежных средств по операционной, инвестиционной и финансовой деятельности",
    
    "tasks": [
        "Анализ реальных потоков денег компании",
        "Выявление источников поступлений и направлений расходов", 
        "Оценка платежеспособности и финансовой устойчивости",
        "Сравнение структуры денежных потоков между периодами"
    ],
    
    "calculation_algorithm": [
        "Классифицировать все поступления по видам деятельности",
        "Классифицировать все расходы по видам деятельности", 
        "Рассчитать чистый денежный поток по каждому виду деятельности",
        "Рассчитать итоговое изменение денежных средств",
        "Проанализировать структуру и динамику потоков"
    ],
    
    "auto_calculated_fields": [
        "operating_cash_flow",     # Операционный денежный поток
        "investing_cash_flow",     # Инвестиционный денежный поток 
        "financing_cash_flow",     # Финансовый денежный поток
        "net_cash_flow",          # Чистый денежный поток
        "cash_flow_structure"      # Структура денежных потоков
    ],
    
    "manual_input_fields": [
        "operating_receipts",      # Поступления от операционной деятельности (dict)
        "operating_payments",      # Платежи по операционной деятельности (dict)
        "investing_receipts",      # Поступления от инвестиционной деятельности (dict)
        "investing_payments",      # Платежи по инвестиционной деятельности (dict)
        "financing_receipts",      # Поступления от финансовой деятельности (dict)
        "financing_payments",      # Платежи по финансовой деятельности (dict)
        "period_start_date",       # Дата начала периода (date)
        "period_end_date"         # Дата окончания периода (date)
    ],
    
    "editable_calculation_fields": [
        "analysis_period_months",  # Период анализа в месяцах (int, default: 12)
        "comparison_periods",      # Количество периодов для сравнения (int, default: 3)
        "significant_change_threshold"  # Порог значимого изменения в % (float, default: 10.0)
    ],
    
    "main_formulas": [
        "operating_cash_flow = operating_receipts - operating_payments",
        "investing_cash_flow = investing_receipts - investing_payments", 
        "financing_cash_flow = financing_receipts - financing_payments",
        "net_cash_flow = operating_cash_flow + investing_cash_flow + financing_cash_flow",
        "cash_coverage_ratio = operating_cash_flow / average_monthly_expenses"
    ],
    
    "key_metrics": [
        "operating_cash_margin",
        "free_cash_flow",
        "cash_conversion_cycle", 
        "cash_flow_volatility",
        "cash_flow_adequacy_ratio"
    ],
    
    "data_visualization": [
        "Водопадная диаграмма движения денежных средств",
        "Круговая диаграмма структуры поступлений и расходов",
        "График динамики денежных потоков по месяцам",
        "Столбчатая диаграмма по видам деятельности",
        "Тренд-анализ операционного денежного потока"
    ],
    
    "ai_analysis_prompts": [
        "Оцени качество денежных потоков компании",
        "Выяви основные драйверы изменения денежных потоков",
        "Проанализируй сбалансированность операционной и инвестиционной деятельности", 
        "Определи устойчивость генерации денежных средств"
    ],
    
    "python_implementation_notes": [
        "Создать класс CashFlowStatement для обработки данных ДДС",
        "Реализовать методы классификации операций по видам деятельности",
        "Использовать numpy для расчета агрегированных показателей",
        "Добавить валидацию балансировки денежных потоков",
        "Создать шаблоны для стандартных отчетов ДДС"
    ]
}

}

print("Создана структура для первых 2 инструментов...")
print("Продолжаю создание остальных инструментов...")