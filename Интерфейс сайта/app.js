// Глобальные переменные
let currentOrganization = null;
let organizations = {};
let testData = {};

// Конфигурация налоговых режимов
const taxRegimes = {
    usn_income: {
        name: "УСН \"Доходы\"",
        rate: 6,
        quarterly_reports: ["28.04", "28.07", "28.10"],
        annual_declaration: { ip: "25.04", ooo: "25.03" },
        min_tax: false
    },
    usn_profit: {
        name: "УСН \"Доходы-расходы\"", 
        rate: 15,
        quarterly_reports: ["28.04", "28.07", "28.10"],
        annual_declaration: { ip: "25.04", ooo: "25.03" },
        min_tax: 1
    },
    osno: {
        name: "ОСНО",
        vat_rate: 20,
        profit_tax: 20,
        monthly_vat: true,
        quarterly_profit: true
    },
    patent: {
        name: "Патент",
        fixed_payment: true,
        payment_schedule: "1/3 в первые 90 дней, остаток до окончания срока"
    }
};

// Все 24 аналитических инструмента
const analyticsTools = [
    { id: "platezhnyy_kalendar", title: "Платежный календарь", category: "finance", description: "Планирование денежных потоков и предотвращение кассовых разрывов" },
    { id: "dds_klassicheskiy", title: "ДДС классический", category: "finance", description: "Анализ реальных потоков денег компании" },
    { id: "finansovaya_model", title: "Финансовая модель", category: "finance", description: "Комплексная оценка прибыльности и рентабельности бизнеса" },
    { id: "vliyanie_skidki", title: "Влияние скидки на прибыль", category: "sales", description: "Расчет оптимального размера скидки" },
    { id: "byudget", title: "Бюджет", category: "finance", description: "Организация планирования и контроля бюджета" },
    { id: "otdel_prodazh", title: "Отчет отдела продаж", category: "sales", description: "Анализ эффективности работы отдела продаж" },
    { id: "faktory_prodazh", title: "Факторы продаж", category: "sales", description: "Анализ факторов, влияющих на объем продаж" },
    { id: "marketing_otchet", title: "Отчет по маркетингу", category: "marketing", description: "Анализ эффективности маркетинговых каналов" },
    { id: "unit_ekonomika", title: "Юнит-экономика", category: "sales", description: "Расчет показателей юнит-экономики" },
    { id: "finmodel_mp", title: "Финмодель для маркетплейсов", category: "sales", description: "Финансовая модель для продавцов на маркетплейсах" },
    { id: "plan_dohodov_rashodov", title: "План доходов и расходов", category: "finance", description: "Планирование и анализ доходов и расходов" },
    { id: "kalkulator_finkochagi", title: "Калькулятор финансового рычага", category: "finance", description: "Расчет эффективности использования заемных средств" },
    { id: "kalkulator_sebest", title: "Калькулятор себестоимости услуг", category: "finance", description: "Расчет полной себестоимости услуг" },
    { id: "zarplata", title: "Зарплатная ведомость", category: "hr", description: "Управление фондом оплаты труда" },
    { id: "logistika", title: "Учет логистики", category: "logistics", description: "Анализ логистических затрат и эффективности" },
    { id: "dz_kz", title: "Учёт ДЗ и КЗ поставщиков", category: "finance", description: "Управление дебиторской и кредиторской задолженностью" },
    { id: "zapasy", title: "Управление запасами", category: "logistics", description: "Оптимизация уровня запасов" },
    { id: "fin_deyatelnost", title: "Учёт финансовой деятельности", category: "finance", description: "Анализ финансовой деятельности предприятия" },
    { id: "sdelki", title: "Учёт сделок", category: "sales", description: "Управление и анализ сделок" },
    { id: "osnovnye_sredstva", title: "Учёт основных средств", category: "finance", description: "Управление основными средствами" },
    { id: "finmodel_trade", title: "Финмодель для торговых компаний", category: "sales", description: "Финансовая модель для торгового бизнеса" },
    { id: "kalkulator_rent", title: "Калькулятор рентабельности", category: "finance", description: "Расчет показателей рентабельности" },
    { id: "opiu", title: "ОПиУ (отчет о прибылях и убытках)", category: "finance", description: "Анализ прибылей и убытков" },
    { id: "balans", title: "Баланс", category: "finance", description: "Анализ активов и пассивов предприятия" }
];

// Инициализация приложения
document.addEventListener('DOMContentLoaded', function() {
    console.log('Начало инициализации приложения');
    try {
        loadOrganizations();
        renderOrganizations();
        setupEventListeners();
        setTodayDate();
        console.log('Приложение инициализировано успешно');
    } catch (error) {
        console.error('Ошибка инициализации:', error);
    }
});

function setTodayDate() {
    const today = new Date().toISOString().split('T')[0];
    const dateInput = document.getElementById('operation-date');
    if (dateInput) {
        dateInput.value = today;
    }
}

// Настройка обработчиков событий
function setupEventListeners() {
    console.log('Настройка обработчиков событий');
    
    // Главная страница - кнопка создания организации
    const createOrgBtn = document.getElementById('create-org-btn');
    console.log('Create org button found:', createOrgBtn);
    
    if (createOrgBtn) {
        createOrgBtn.addEventListener('click', function(e) {
            e.preventDefault();
            e.stopPropagation();
            console.log('Клик по кнопке создания организации');
            showCreateOrgModal();
        });
        console.log('Обработчик кнопки создания организации установлен');
    } else {
        console.error('Кнопка создания организации не найдена!');
    }
    
    // Модальное окно - обработчики
    setupModalEventListeners();
    
    // Остальные обработчики
    setupOrgPageEventListeners();
    setupTabEventListeners();
    setupToolsEventListeners();
    setupQuarterToggles();
    
    // Автосохранение данных
    document.addEventListener('input', function(e) {
        if (e.target.classList.contains('form-control') && currentOrganization) {
            clearTimeout(window.autoSaveTimer);
            window.autoSaveTimer = setTimeout(() => {
                if (currentOrganization) {
                    saveOrgData();
                    updateDashboard();
                }
            }, 1000);
        }
    });
    
    console.log('Все обработчики событий установлены');
}

function setupModalEventListeners() {
    const modalCloseBtn = document.getElementById('modal-close-btn');
    const modalCancelBtn = document.getElementById('modal-cancel-btn');
    const modalCreateBtn = document.getElementById('modal-create-btn');
    const modalOverlay = document.querySelector('.modal-overlay');
    
    if (modalCloseBtn) {
        modalCloseBtn.addEventListener('click', function(e) {
            e.preventDefault();
            console.log('Закрытие модального окна (крестик)');
            hideCreateOrgModal();
        });
    }
    
    if (modalCancelBtn) {
        modalCancelBtn.addEventListener('click', function(e) {
            e.preventDefault();
            console.log('Отмена создания организации');
            hideCreateOrgModal();
        });
    }
    
    if (modalCreateBtn) {
        console.log('%c[SETUP] Кнопка #modal-create-btn НАЙДЕНА. Назначаю обработчик...', 'color: green');
        modalCreateBtn.addEventListener('click', function(e) {
            e.preventDefault();
            console.log('[EVENT] Клик по кнопке #modal-create-btn');
            createOrganization();
        });
    } else {
        console.error('%c[SETUP] Кнопка #modal-create-btn НЕ НАЙДЕНА!', 'color: red; font-weight: bold;');
    }
    
    if (modalOverlay) {
        modalOverlay.addEventListener('click', function(e) {
            if (e.target === modalOverlay) {
                console.log('Закрытие модального окна (клик по overlay)');
                hideCreateOrgModal();
            }
        });
    }
    
    // Escape для закрытия модального окна
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape') {
            const modal = document.getElementById('create-org-modal');
            if (modal && !modal.classList.contains('hidden')) {
                console.log('Закрытие модального окна (Escape)');
                hideCreateOrgModal();
            }
        }
    });
}

function setupOrgPageEventListeners() {
    const backHomeBtn = document.getElementById('back-home-btn');
    const showToolsBtn = document.getElementById('show-tools-btn');
    const showTaxCalendarBtn = document.getElementById('show-tax-calendar-btn');
    const generateDataBtn = document.getElementById('generate-data-btn');
    const saveDataBtn = document.getElementById('save-data-btn');
    const addOperationBtn = document.getElementById('add-operation-btn');
    
    if (backHomeBtn) {
        backHomeBtn.addEventListener('click', function(e) {
            e.preventDefault();
            showHome();
        });
    }
    
    if (showToolsBtn) {
        showToolsBtn.addEventListener('click', function(e) {
            e.preventDefault();
            showAnalyticsTools();
        });
    }
    
    if (showTaxCalendarBtn) {
        showTaxCalendarBtn.addEventListener('click', function(e) {
            e.preventDefault();
            showTaxCalendar();
        });
    }
    
    if (generateDataBtn) {
        generateDataBtn.addEventListener('click', function(e) {
            e.preventDefault();
            generateTestData();
        });
    }
    
    if (saveDataBtn) {
        saveDataBtn.addEventListener('click', function(e) {
            e.preventDefault();
            saveOrgData();
        });
    }
    
    if (addOperationBtn) {
        addOperationBtn.addEventListener('click', function(e) {
            e.preventDefault();
            addDailyOperation();
        });
    }
    
    // Налоговый календарь
    const backOrgFromCalendarBtn = document.getElementById('back-org-from-calendar-btn');
    if (backOrgFromCalendarBtn) {
        backOrgFromCalendarBtn.addEventListener('click', function(e) {
            e.preventDefault();
            showOrganization();
        });
    }
}

function setupTabEventListeners() {
    const tabButtons = document.querySelectorAll('.tab-button');
    tabButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            const tabName = this.getAttribute('data-tab');
            switchTab(tabName);
        });
    });
}

function setupToolsEventListeners() {
    const backOrgBtn = document.getElementById('back-org-btn');
    const categoryFilter = document.getElementById('category-filter');
    
    if (backOrgBtn) {
        backOrgBtn.addEventListener('click', function(e) {
            e.preventDefault();
            showOrganization();
        });
    }
    
    if (categoryFilter) {
        categoryFilter.addEventListener('change', function() {
            filterTools();
        });
    }
    
    // Страница инструмента
    const backToolsBtn = document.getElementById('back-tools-btn');
    if (backToolsBtn) {
        backToolsBtn.addEventListener('click', function(e) {
            e.preventDefault();
            showAnalyticsTools();
        });
    }
}

// Настройка раскрывающихся блоков
function setupQuarterToggles() {
    // Обработчики для кварталов
    document.querySelectorAll('.quarter-header').forEach(header => {
        header.addEventListener('click', function(e) {
            e.preventDefault();
            const quarter = this.getAttribute('data-quarter');
            const content = document.getElementById(`quarter-${quarter}`);
            const toggle = this.querySelector('.quarter-toggle');
            
            if (content && toggle) {
                if (content.classList.contains('expanded')) {
                    content.classList.remove('expanded');
                    toggle.classList.remove('expanded');
                } else {
                    content.classList.add('expanded');
                    toggle.classList.add('expanded');
                }
            }
        });
    });
    
    // Обработчики для месяцев
    document.querySelectorAll('.month-header').forEach(header => {
        header.addEventListener('click', function(e) {
            e.preventDefault();
            const month = this.getAttribute('data-month');
            const content = document.getElementById(`month-${month}`);
            const toggle = this.querySelector('.month-toggle');
            
            if (content && toggle) {
                if (content.classList.contains('expanded')) {
                    content.classList.remove('expanded');
                    toggle.classList.remove('expanded');
                } else {
                    content.classList.add('expanded');
                    toggle.classList.add('expanded');
                    // Загружаем данные месяца при первом открытии
                    loadMonthData(month);
                }
            }
        });
    });
}

// Управление организациями
function loadOrganizations() {
    try {
        const stored = localStorage.getItem('organizations');
        if (stored) {
            organizations = JSON.parse(stored);
            console.log('Организации загружены:', Object.keys(organizations).length);
        } else {
            console.log('Нет сохраненных организаций');
        }
    } catch (error) {
        console.error('Ошибка загрузки организаций:', error);
        organizations = {};
    }
}

function saveOrganizations() {
    console.log('[SAVE] Вызвана функция saveOrganizations.');
    console.log('[SAVE] Данные для сохранения:', JSON.stringify(organizations, null, 2));
    try {
        if (!organizations || Object.keys(organizations).length === 0) {
            console.warn('[SAVE] Попытка сохранить пустой объект организаций. Это может быть нормально при удалении последней организации.');
        }
        localStorage.setItem('organizations', JSON.stringify(organizations));
        console.log('%c[SAVE] Успешно сохранено в localStorage!', 'color: green; font-weight: bold;');
    } catch (error) {
        console.error('%c[SAVE] КРИТИЧЕСКАЯ ОШИБКА при сохранении в localStorage:', 'color: red; font-weight: bold;', error);
    }
}

function createOrganization() {
    console.log('Начало создания организации');
    try {
        const nameInput = document.getElementById('new-org-name');
        const descInput = document.getElementById('new-org-description');
        const legalFormInput = document.getElementById('new-org-legal-form');
        const taxRegimeInput = document.getElementById('new-org-tax-regime');
        const regionInput = document.getElementById('new-org-region');
        const okvedInput = document.getElementById('new-org-okved');
        const employeesInput = document.getElementById('new-org-employees');
        const registrationDateInput = document.getElementById('new-org-registration-date');
        
        const name = nameInput?.value.trim() || '';
        const description = descInput?.value.trim() || '';
        const legalForm = legalFormInput?.value || '';
        const taxRegime = taxRegimeInput?.value || '';
        const region = regionInput?.value || '';
        const okved = okvedInput?.value.trim() || '';
        const employees = employeesInput?.value || '0';
        const registrationDate = registrationDateInput?.value || '';
        
        console.log('Данные формы:', { name, legalForm, taxRegime, region });
        
        if (!name || !legalForm || !taxRegime || !region) {
            showNotification('Заполните все обязательные поля (название, форма, режим налогообложения, регион)', 'error');
            return;
        }
        
        const orgId = 'org_' + Date.now();
        const newOrg = {
            id: orgId,
            name: name,
            description: description,
            legalForm: legalForm,
            taxRegime: taxRegime,
            region: region,
            okved: okved,
            employees: employees,
            registrationDate: registrationDate,
            createdAt: new Date().toISOString(),
            data: getEmptyOrgData(),
            operations: [],
            monthlyData: {}
        };
        
        organizations[orgId] = newOrg;
        console.log('Попытка сохранить организацию...');
        saveOrganizations();
        hideCreateOrgModal();
        renderOrganizations();
        clearCreateOrgForm();
        
        showNotification(`Организация "${name}" успешно создана!`, 'success');
        
        // Автоматически выбираем созданную организацию
        setTimeout(() => {
            selectOrganization(orgId);
        }, 500);
        
    } catch (error) {
        console.error('Ошибка создания организации:', error);
        showNotification('Произошла ошибка при создании организации', 'error');
    }
}

function clearCreateOrgForm() {
    const inputs = [
        'new-org-name', 'new-org-description', 'new-org-legal-form', 
        'new-org-tax-regime', 'new-org-region', 'new-org-okved', 
        'new-org-employees', 'new-org-registration-date'
    ];
    
    inputs.forEach(id => {
        const element = document.getElementById(id);
        if (element) {
            element.value = '';
        }
    });
}

function getEmptyOrgData() {
    return {
        revenue: 0, cogs: 0, opex: 0, receivables: 0, payables: 0, current_assets: 0,
        customers: 0, avg_check: 0, conversion: 0, deals_count: 0,
        marketing_spend: 0, cac: 0, ltv: 0,
        inventory: 0, logistics_costs: 0,
        employees: 0, payroll: 0
    };
}

function renderOrganizations() {
    try {
        const grid = document.getElementById('organizations-grid');
        if (!grid) {
            console.error('Элемент organizations-grid не найден');
            return;
        }
        
        const orgCount = Object.keys(organizations).length;
        console.log('Рендеринг организаций:', orgCount);
        
        if (orgCount === 0) {
            grid.innerHTML = `
                <div class="empty-state">
                    <h3>Нет организаций</h3>
                    <p>Создайте первую организацию для начала работы с аналитикой</p>
                </div>
            `;
            return;
        }
        
        grid.innerHTML = Object.values(organizations).map(org => {
            const taxRegimeInfo = taxRegimes[org.taxRegime];
            return `
                <div class="org-card" data-org-id="${org.id}">
                    <h3>${org.name}</h3>
                    <p>${org.description || 'Нет описания'}</p>
                    <div class="tax-regime-label tax-regime--${org.taxRegime}">
                        ${taxRegimeInfo?.name || org.taxRegime}
                    </div>
                    <div class="org-stats">
                        ${org.legalForm?.toUpperCase()} • ${org.region} • ${new Date(org.createdAt).toLocaleDateString('ru-RU')}
                    </div>
                </div>
            `;
        }).join('');
        
        // Добавляем обработчики для карточек организаций
        const orgCards = grid.querySelectorAll('.org-card');
        console.log('Найдено карточек организаций:', orgCards.length);
        
        orgCards.forEach(card => {
            card.addEventListener('click', function(e) {
                e.preventDefault();
                const orgId = this.getAttribute('data-org-id');
                console.log('Клик по организации:', orgId);
                selectOrganization(orgId);
            });
        });
        
    } catch (error) {
        console.error('Ошибка рендера организаций:', error);
    }
}

function selectOrganization(orgId) {
    try {
        console.log('Выбор организации:', orgId);
        currentOrganization = organizations[orgId];
        
        if (!currentOrganization) {
            console.error('Организация не найдена:', orgId);
            return;
        }
        
        const orgTitle = document.getElementById('org-title');
        const taxRegimeBadge = document.getElementById('tax-regime-badge');
        const orgDetails = document.getElementById('org-details');
        
        if (orgTitle) {
            orgTitle.textContent = currentOrganization.name;
        }
        
        if (taxRegimeBadge) {
            const taxInfo = taxRegimes[currentOrganization.taxRegime];
            taxRegimeBadge.textContent = taxInfo?.name || currentOrganization.taxRegime;
            taxRegimeBadge.className = `status tax-regime--${currentOrganization.taxRegime}`;
        }
        
        if (orgDetails) {
            orgDetails.textContent = `${currentOrganization.legalForm?.toUpperCase()} • ${currentOrganization.region}`;
        }
        
        loadOrgData();
        updateDashboard();
        updateQuarterlyData();
        showView('org-view');
        
        console.log('Организация выбрана:', currentOrganization.name);
    } catch (error) {
        console.error('Ошибка выбора организации:', error);
    }
}

// Генерация тестовых данных
function generateTestData() {
    if (!currentOrganization) {
        showNotification('Сначала выберите организацию', 'warning');
        return;
    }
    
    try {
        showNotification('Генерация тестовых данных...', 'info');
        
        // Генерируем данные по месяцам 2025 года
        const monthlyData = {};
        const operations = [];
        
        for (let month = 1; month <= 12; month++) {
            const monthKey = `2025-${month.toString().padStart(2, '0')}`;
            
            // Базовые суммы с сезонностью
            const seasonalityFactor = 0.8 + (Math.sin(month * Math.PI / 6) + 1) * 0.3;
            const baseIncome = (800000 + Math.random() * 400000) * seasonalityFactor;
            const baseExpenses = baseIncome * (0.4 + Math.random() * 0.2);
            const taxes = baseIncome * (currentOrganization.taxRegime === 'usn_income' ? 0.06 : 0.15);
            
            monthlyData[monthKey] = {
                income: Math.floor(baseIncome),
                expenses: Math.floor(baseExpenses),
                profit: Math.floor(baseIncome - baseExpenses),
                taxes: Math.floor(taxes),
                operations: []
            };
            
            // Генерируем ежедневные операции для каждого месяца (только для последних 3 месяцев чтобы не перегружать)
            if (month >= 7 && month <= 9) { // Только июль-сентябрь для демонстрации
                const daysInMonth = new Date(2025, month, 0).getDate();
                for (let day = 1; day <= daysInMonth; day++) {
                    const date = `2025-${month.toString().padStart(2, '0')}-${day.toString().padStart(2, '0')}`;
                    
                    // 1-3 операции в день
                    const numOperations = Math.floor(Math.random() * 3) + 1;
                    for (let i = 0; i < numOperations; i++) {
                        const operationType = Math.random() < 0.6 ? 'income' : 'expense';
                        const amount = Math.floor(Math.random() * 50000) + 5000;
                        
                        const operation = {
                            id: `op_${Date.now()}_${Math.random()}`,
                            date: date,
                            type: operationType,
                            amount: amount,
                            description: operationType === 'income' ? 
                                ['Поступление от клиента', 'Оплата по договору', 'Продажа услуг', 'Консультационные услуги'][Math.floor(Math.random() * 4)] :
                                ['Аренда офиса', 'Зарплата сотрудников', 'Закупка материалов', 'Реклама', 'Коммунальные услуги'][Math.floor(Math.random() * 5)],
                            createdAt: new Date().toISOString()
                        };
                        
                        operations.push(operation);
                        monthlyData[monthKey].operations.push(operation);
                    }
                    
                    // Иногда добавляем налоговые платежи
                    if (day === 25 && Math.random() < 0.3) {
                        const taxOperation = {
                            id: `op_tax_${Date.now()}_${Math.random()}`,
                            date: date,
                            type: 'tax-payment',
                            amount: Math.floor(taxes / 4),
                            description: 'Авансовый платеж по УСН',
                            createdAt: new Date().toISOString()
                        };
                        operations.push(taxOperation);
                        monthlyData[monthKey].operations.push(taxOperation);
                    }
                }
            }
        }
        
        // Генерируем накопительные данные для форм
        const totalIncome = Object.values(monthlyData).reduce((sum, month) => sum + month.income, 0);
        const testData = {
            revenue: totalIncome,
            cogs: Math.floor(totalIncome * (0.3 + Math.random() * 0.2)),
            opex: Math.floor(totalIncome * (0.2 + Math.random() * 0.1)),
            receivables: Math.floor(totalIncome * 0.15),
            payables: Math.floor(totalIncome * 0.1),
            current_assets: Math.floor(totalIncome * 0.25),
            customers: Math.floor(Math.random() * 500) + 100,
            avg_check: Math.floor(totalIncome / (Math.floor(Math.random() * 500) + 100)),
            conversion: Math.floor(Math.random() * 20) + 5,
            deals_count: Math.floor(Math.random() * 300) + 50,
            marketing_spend: Math.floor(totalIncome * 0.08),
            cac: Math.floor(Math.random() * 3000) + 500,
            ltv: Math.floor(Math.random() * 50000) + 10000,
            inventory: Math.floor(totalIncome * 0.2),
            logistics_costs: Math.floor(totalIncome * 0.05),
            employees: Math.floor(Math.random() * 50) + 5,
            payroll: Math.floor(totalIncome * 0.25)
        };
        
        // Сохраняем данные в организацию
        currentOrganization.data = testData;
        currentOrganization.operations = operations;
        currentOrganization.monthlyData = monthlyData;
        
        organizations[currentOrganization.id] = currentOrganization;
        saveOrganizations();
        loadOrgData();
        updateDashboard();
        updateQuarterlyData();
        
        showNotification('Тестовые данные за 2025 год сгенерированы и готовы для анализа!', 'success');
    } catch (error) {
        console.error('Ошибка генерации тестовых данных:', error);
        showNotification('Ошибка при генерации данных', 'error');
    }
}

// Обновление квартальных данных
function updateQuarterlyData() {
    if (!currentOrganization || !currentOrganization.monthlyData) return;
    
    try {
        const monthlyData = currentOrganization.monthlyData;
        let totalIncome = 0, totalExpenses = 0, totalProfit = 0, totalTaxes = 0;
        
        // Кварталы
        const quarters = {
            Q1: ['2025-01', '2025-02', '2025-03'],
            Q2: ['2025-04', '2025-05', '2025-06'],
            Q3: ['2025-07', '2025-08', '2025-09'],
            Q4: ['2025-10', '2025-11', '2025-12']
        };
        
        Object.keys(quarters).forEach(quarter => {
            let qIncome = 0, qExpenses = 0, qProfit = 0;
            
            quarters[quarter].forEach(month => {
                if (monthlyData[month]) {
                    qIncome += monthlyData[month].income;
                    qExpenses += monthlyData[month].expenses;
                    qProfit += monthlyData[month].profit;
                }
            });
            
            updateMetric(`${quarter.toLowerCase()}-income`, qIncome);
            updateMetric(`${quarter.toLowerCase()}-expenses`, qExpenses);
            updateMetric(`${quarter.toLowerCase()}-profit`, qProfit);
            
            totalIncome += qIncome;
            totalExpenses += qExpenses;
            totalProfit += qProfit;
        });
        
        // Обновляем месячные показатели
        Object.keys(monthlyData).forEach(month => {
            const data = monthlyData[month];
            updateMetric(`month-${month}-profit`, data.profit);
            totalTaxes += data.taxes;
        });
        
        // Обновляем общие показатели
        updateMetric('total-income', totalIncome);
        updateMetric('total-expenses', totalExpenses);
        updateMetric('total-profit', totalProfit);
        updateMetric('total-taxes', totalTaxes);
        
    } catch (error) {
        console.error('Ошибка обновления квартальных данных:', error);
    }
}

// Загрузка данных месяца в раскрывающийся блок
function loadMonthData(month) {
    if (!currentOrganization || !currentOrganization.monthlyData) return;
    
    try {
        const monthData = currentOrganization.monthlyData[month];
        if (!monthData) return;
        
        const container = document.getElementById(`month-${month}`);
        if (!container) return;
        
        container.innerHTML = `
            <div class="month-data">
                <div class="month-metric">
                    <div class="month-metric-value">${formatCurrency(monthData.income)}</div>
                    <div class="month-metric-label">Доходы</div>
                </div>
                <div class="month-metric">
                    <div class="month-metric-value">${formatCurrency(monthData.expenses)}</div>
                    <div class="month-metric-label">Расходы</div>
                </div>
                <div class="month-metric">
                    <div class="month-metric-value">${formatCurrency(monthData.profit)}</div>
                    <div class="month-metric-label">Прибыль</div>
                </div>
                <div class="month-metric">
                    <div class="month-metric-value">${formatCurrency(monthData.taxes)}</div>
                    <div class="month-metric-label">Налоги</div>
                </div>
            </div>
            
            ${monthData.operations && monthData.operations.length > 0 ? `
            <div class="month-operations">
                <h5>Операции (показаны первые 10)</h5>
                <div class="operation-list">
                    ${monthData.operations.slice(0, 10).map(op => `
                        <div class="operation-item">
                            <div class="operation-info">
                                <div class="operation-description">${op.description}</div>
                                <div class="operation-date">${new Date(op.date).toLocaleDateString('ru-RU')}</div>
                            </div>
                            <div class="operation-amount operation-amount--${op.type}">
                                ${op.type === 'income' ? '+' : '-'}${formatCurrency(op.amount)}
                            </div>
                        </div>
                    `).join('')}
                    ${monthData.operations.length > 10 ? `<div class="text-center" style="padding: 8px; color: var(--color-text-secondary);">... и еще ${monthData.operations.length - 10} операций</div>` : ''}
                </div>
            </div>` : ''}
        `;
        
        container.classList.add('expanded');
        
    } catch (error) {
        console.error('Ошибка загрузки данных месяца:', error);
    }
}

// Модальные окна
function showCreateOrgModal() {
    console.log('Показ модального окна создания организации');
    try {
        const modal = document.getElementById('create-org-modal');
        console.log('Modal element:', modal);
        
        if (modal) {
            modal.classList.remove('hidden');
            console.log('Modal classes after show:', modal.className);
            
            // Фокус на поле ввода названия
            setTimeout(() => {
                const nameInput = document.getElementById('new-org-name');
                if (nameInput) {
                    nameInput.focus();
                }
            }, 100);
        } else {
            console.error('Модальное окно не найдено!');
        }
    } catch (error) {
        console.error('Ошибка показа модального окна:', error);
    }
}

function hideCreateOrgModal() {
    console.log('Скрытие модального окна');
    try {
        const modal = document.getElementById('create-org-modal');
        if (modal) {
            modal.classList.add('hidden');
            console.log('Modal classes after hide:', modal.className);
        }
    } catch (error) {
        console.error('Ошибка скрытия модального окна:', error);
    }
}

// Остальные функции остаются без изменений...
function addDailyOperation() {
    if (!currentOrganization) {
        showNotification('Сначала выберите организацию', 'warning');
        return;
    }
    
    try {
        const dateInput = document.getElementById('operation-date');
        const typeInput = document.getElementById('operation-type');
        const amountInput = document.getElementById('operation-amount');
        const descInput = document.getElementById('operation-description');
        
        const date = dateInput?.value || '';
        const type = typeInput?.value || '';
        const amount = parseFloat(amountInput?.value) || 0;
        const description = descInput?.value?.trim() || '';
        
        if (!date || !type || amount <= 0 || !description) {
            showNotification('Заполните все поля операции', 'warning');
            return;
        }
        
        const operation = {
            id: 'op_' + Date.now(),
            date: date,
            type: type,
            amount: amount,
            description: description,
            createdAt: new Date().toISOString()
        };
        
        if (!currentOrganization.operations) {
            currentOrganization.operations = [];
        }
        
        currentOrganization.operations.unshift(operation);
        
        // Добавляем в месячные данные
        const monthKey = date.substring(0, 7); // YYYY-MM
        if (!currentOrganization.monthlyData) {
            currentOrganization.monthlyData = {};
        }
        if (!currentOrganization.monthlyData[monthKey]) {
            currentOrganization.monthlyData[monthKey] = {
                income: 0, expenses: 0, profit: 0, taxes: 0, operations: []
            };
        }
        
        currentOrganization.monthlyData[monthKey].operations.push(operation);
        
        if (type === 'income') {
            currentOrganization.monthlyData[monthKey].income += amount;
        } else if (type === 'expense') {
            currentOrganization.monthlyData[monthKey].expenses += amount;
        }
        
        currentOrganization.monthlyData[monthKey].profit = 
            currentOrganization.monthlyData[monthKey].income - 
            currentOrganization.monthlyData[monthKey].expenses;
        
        // Обновляем накопительные данные
        updateAccumulatedData(operation);
        
        organizations[currentOrganization.id] = currentOrganization;
        console.log('[ADD OP] Попытка сохранить данные после добавления операции...');
        saveOrganizations();
        
        // Очищаем форму
        if (amountInput) amountInput.value = '';
        if (descInput) descInput.value = '';
        
        updateDashboard();
        updateQuarterlyData();
        showNotification('Операция добавлена успешно', 'success');
        
    } catch (error) {
        console.error('Ошибка добавления операции:', error);
        showNotification('Ошибка при добавлении операции', 'error');
    }
}

function updateAccumulatedData(operation) {
    if (!currentOrganization.data) {
        currentOrganization.data = getEmptyOrgData();
    }
    
    switch (operation.type) {
        case 'income':
            currentOrganization.data.revenue += operation.amount;
            break;
        case 'expense':
            currentOrganization.data.opex += operation.amount;
            break;
        // tax-payment не влияет на накопительные данные
    }
    
    loadOrgData();
}

// Налоговые расчеты
function calculateTaxes() {
    if (!currentOrganization || !currentOrganization.data) {
        return { amount: 0, burden: 0 };
    }
    
    const data = currentOrganization.data;
    const regime = currentOrganization.taxRegime;
    const regimeInfo = taxRegimes[regime];
    
    if (!regimeInfo) {
        return { amount: 0, burden: 0 };
    }
    
    let taxAmount = 0;
    
    switch (regime) {
        case 'usn_income':
            taxAmount = data.revenue * (regimeInfo.rate / 100);
            break;
            
        case 'usn_profit':
            const profit = Math.max(0, data.revenue - data.cogs - data.opex);
            const minTax = data.revenue * (regimeInfo.min_tax / 100);
            taxAmount = Math.max(profit * (regimeInfo.rate / 100), minTax);
            break;
            
        case 'osno':
            const vat = data.revenue * (regimeInfo.vat_rate / 100);
            const profitTax = Math.max(0, (data.revenue - data.cogs - data.opex) * (regimeInfo.profit_tax / 100));
            taxAmount = vat + profitTax;
            break;
            
        case 'patent':
            taxAmount = 20000; // Примерная стоимость патента в год
            break;
    }
    
    const taxBurden = data.revenue > 0 ? (taxAmount / data.revenue * 100) : 0;
    
    return { amount: Math.max(0, taxAmount), burden: taxBurden };
}

// Дашборд
function updateDashboard() {
    if (!currentOrganization) return;
    
    try {
        const data = currentOrganization.data || getEmptyOrgData();
        const taxes = calculateTaxes();
        const netProfit = data.revenue - data.cogs - data.opex - taxes.amount;
        
        updateMetric('total-revenue', data.revenue);
        updateMetric('tax-amount', taxes.amount);
        updateMetric('net-profit', netProfit);
        
        const taxBurdenElement = document.getElementById('tax-burden');
        if (taxBurdenElement) {
            taxBurdenElement.textContent = taxes.burden.toFixed(1) + '%';
        }
        
    } catch (error) {
        console.error('Ошибка обновления дашборда:', error);
    }
}

function updateMetric(elementId, value) {
    const element = document.getElementById(elementId);
    if (element) {
        element.textContent = formatCurrency(value);
    }
}

// Управление видами
function showView(viewId) {
    try {
        document.querySelectorAll('.view').forEach(view => {
            view.classList.add('hidden');
        });
        
        const targetView = document.getElementById(viewId);
        if (targetView) {
            targetView.classList.remove('hidden');
        }
    } catch (error) {
        console.error('Ошибка переключения видов:', error);
    }
}

function showHome() {
    showView('home-view');
    currentOrganization = null;
}

function showOrganization() {
    if (!currentOrganization) {
        showHome();
        return;
    }
    showView('org-view');
}

function showAnalyticsTools() {
    if (!currentOrganization) {
        showHome();
        return;
    }
    renderToolsGrid();
    showView('tools-view');
}

// Управление вкладками
function switchTab(tabName) {
    try {
        document.querySelectorAll('.tab-button').forEach(btn => {
            btn.classList.remove('active');
        });
        document.querySelectorAll('.tab-content').forEach(content => {
            content.classList.remove('active');
        });
        
        const tabButton = document.querySelector(`[data-tab="${tabName}"]`);
        const tabContent = document.getElementById(`${tabName}-tab`);
        
        if (tabButton && tabContent) {
            tabButton.classList.add('active');
            tabContent.classList.add('active');
        }
    } catch (error) {
        console.error('Ошибка переключения вкладок:', error);
    }
}

function loadOrgData() {
    if (!currentOrganization) return;
    
    try {
        const data = currentOrganization.data || getEmptyOrgData();
        
        Object.keys(data).forEach(key => {
            const element = document.getElementById(key);
            if (element && element.type === 'number') {
                element.value = data[key] || 0;
            }
        });
        
        console.log('Данные организации загружены');
    } catch (error) {
        console.error('Ошибка загрузки данных организации:', error);
    }
}

function saveOrgData() {
    if (!currentOrganization) return;
    
    try {
        const formData = {};
        const inputs = document.querySelectorAll('input[type="number"].form-control');
        
        inputs.forEach(input => {
            if (input.id) {
                formData[input.id] = parseFloat(input.value) || 0;
            }
        });
        
        currentOrganization.data = { ...currentOrganization.data, ...formData };
        organizations[currentOrganization.id] = currentOrganization;
        saveOrganizations();
        
        console.log('Данные организации сохранены');
    } catch (error) {
        console.error('Ошибка сохранения данных:', error);
    }
}

// Налоговый календарь и инструменты (сокращены для экономии места)
function showTaxCalendar() {
    if (!currentOrganization) {
        showNotification('Сначала выберите организацию', 'warning');
        return;
    }
    showNotification('Налоговый календарь будет добавлен в следующей версии', 'info');
}

function renderToolsGrid() {
    try {
        const grid = document.getElementById('tools-grid');
        const categoryFilter = document.getElementById('category-filter');
        
        if (!grid) return;
        
        const categoryValue = categoryFilter ? categoryFilter.value : '';
        
        let filteredTools = analyticsTools;
        if (categoryValue) {
            filteredTools = analyticsTools.filter(tool => tool.category === categoryValue);
        }
        
        grid.innerHTML = filteredTools.map(tool => {
            const dataStatus = getDataStatus(tool.category);
            return `
                <div class="tool-card" data-tool-id="${tool.id}">
                    <div class="category-badge category-${tool.category}">${getCategoryName(tool.category)}</div>
                    <h3>${tool.title}</h3>
                    <p>${tool.description}</p>
                    <div class="status-indicator status-${dataStatus.status}">
                        <span class="status-dot"></span>
                        ${dataStatus.text}
                    </div>
                </div>
            `;
        }).join('');
        
        const toolCards = grid.querySelectorAll('.tool-card');
        toolCards.forEach(card => {
            card.addEventListener('click', function(e) {
                e.preventDefault();
                const toolId = this.getAttribute('data-tool-id');
                openTool(toolId);
            });
        });
        
    } catch (error) {
        console.error('Ошибка рендера инструментов:', error);
    }
}

function getDataStatus(category) {
    if (!currentOrganization || !currentOrganization.data) {
        return { status: 'empty', text: 'Нет данных' };
    }
    
    const data = currentOrganization.data;
    let hasData = false;
    
    switch (category) {
        case 'finance':
            hasData = data.revenue > 0 || data.cogs > 0 || data.opex > 0;
            break;
        case 'sales':
            hasData = data.customers > 0 || data.avg_check > 0 || data.deals_count > 0;
            break;
        case 'marketing':
            hasData = data.marketing_spend > 0 || data.cac > 0 || data.ltv > 0;
            break;
        case 'logistics':
            hasData = data.inventory > 0 || data.logistics_costs > 0;
            break;
        case 'hr':
            hasData = data.employees > 0 || data.payroll > 0;
            break;
    }
    
    return hasData ? 
        { status: 'ready', text: 'Готов к анализу' } : 
        { status: 'empty', text: 'Нужны данные' };
}

function getCategoryName(category) {
    const names = {
        finance: 'Финансы',
        sales: 'Продажи',
        marketing: 'Маркетинг',
        logistics: 'Логистика',
        hr: 'Персонал'
    };
    return names[category] || category;
}

function filterTools() {
    renderToolsGrid();
}

function openTool(toolId) {
    try {
        const tool = analyticsTools.find(t => t.id === toolId);
        if (!tool) {
            console.error('Инструмент не найден:', toolId);
            return;
        }
        
        renderToolContent(tool);
        showView('tool-view');
    } catch (error) {
        console.error('Ошибка открытия инструмента:', error);
    }
}

function renderToolContent(tool) {
    try {
        const container = document.getElementById('tool-content');
        if (!container) return;
        
        container.innerHTML = `
            <div class="tool-header">
                <h1>${tool.title}</h1>
                <p style="color: var(--color-text-secondary); margin: 8px 0 0 0;">${tool.description}</p>
            </div>
            
            <div class="tool-sections">
                <div class="tool-section">
                    <div class="flex justify-between items-center mb-8">
                        <h3>📊 Получить аналитику</h3>
                        <button class="btn btn--primary" onclick="generateAnalysis('${tool.id}')">Анализировать</button>
                    </div>
                    <div id="metrics-${tool.id}"></div>
                </div>
                
                <div class="tool-section">
                    <h3>📈 Визуализация</h3>
                    <div class="chart-container" style="position: relative;">
                        <canvas id="chart-${tool.id}"></canvas>
                    </div>
                </div>
                
                <div class="ai-recommendations">
                    <h4>ИИ Рекомендации</h4>
                    <div id="recommendations-${tool.id}">
                        <p>Нажмите "Анализировать" для получения персонализированных рекомендаций на основе ваших данных.</p>
                    </div>
                </div>
            </div>
        `;
        
    } catch (error) {
        console.error('Ошибка рендера контента инструмента:', error);
    }
}

// Базовая аналитика
window.generateAnalysis = function(toolId) {
    if (!currentOrganization || !currentOrganization.data) {
        showNotification('Недостаточно данных для анализа', 'warning');
        return;
    }
    
    const tool = analyticsTools.find(t => t.id === toolId);
    if (!tool) {
        showNotification('Инструмент не найден', 'error');
        return;
    }
    
    const data = currentOrganization.data;
    const revenue = data.revenue || 0;
    const profit = revenue - (data.cogs || 0) - (data.opex || 0);
    const margin = revenue ? (profit / revenue * 100) : 0;
    
    const metricsElement = document.getElementById(`metrics-${toolId}`);
    if (metricsElement) {
        metricsElement.innerHTML = `
            <div class="metrics-grid">
                <div class="metric-card">
                    <div class="metric-value">${formatCurrency(revenue)}</div>
                    <div class="metric-label">Выручка</div>
                </div>
                <div class="metric-card">
                    <div class="metric-value">${formatCurrency(profit)}</div>
                    <div class="metric-label">Прибыль</div>
                </div>
                <div class="metric-card">
                    <div class="metric-value">${margin.toFixed(1)}%</div>
                    <div class="metric-label">Рентабельность</div>
                </div>
            </div>
        `;
    }
    
    const chartCanvas = document.getElementById(`chart-${toolId}`);
    if (chartCanvas) {
        const ctx = chartCanvas.getContext('2d');
        new Chart(ctx, {
            type: 'doughnut',
            data: {
                labels: ['Выручка', 'Себестоимость', 'Операционные расходы'],
                datasets: [{
                    data: [revenue, data.cogs || 0, data.opex || 0],
                    backgroundColor: ['#1FB8CD', '#FFC185', '#B4413C']
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false
            }
        });
    }
    
    let recommendations = [`Анализ по инструменту "${tool.title}" выполнен`];
    if (profit > 0) recommendations.push('Бизнес показывает положительную рентабельность');
    else recommendations.push('Рекомендуется оптимизировать расходы для увеличения прибыли');
    
    const recommendationsElement = document.getElementById(`recommendations-${toolId}`);
    if (recommendationsElement) {
        recommendationsElement.innerHTML = '<ul>' + recommendations.map(rec => `<li>${rec}</li>`).join('') + '</ul>';
    }
    
    showNotification('Анализ выполнен успешно', 'success');
};

// Утилитарные функции
function formatCurrency(amount) {
    return new Intl.NumberFormat('ru-RU', {
        style: 'currency',
        currency: 'RUB',
        maximumFractionDigits: 0
    }).format(amount);
}

function showNotification(message, type = 'info') {
    console.log(`[${type.toUpperCase()}] ${message}`);
    
    const notification = document.createElement('div');
    notification.className = `notification notification--${type}`;
    notification.textContent = message;
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        z-index: 10000;
        max-width: 300px;
        padding: 12px 16px;
        border-radius: 8px;
        font-size: 14px;
        font-weight: 500;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        color: white;
        background-color: ${type === 'success' ? '#10b981' : type === 'error' ? '#ef4444' : type === 'warning' ? '#f59e0b' : '#3b82f6'};
    `;
    
    document.body.appendChild(notification);
    
    setTimeout(() => {
        if (notification.parentNode) {
            notification.parentNode.removeChild(notification);
        }
    }, 3000);
}

console.log('Система бизнес-аналитики с полной функциональностью загружена');