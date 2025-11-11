"""
backend_full.py

ПОЛНОЕ ТЕХНИЧЕСКОЕ ЗАДАНИЕ ДЛЯ BACKEND РАЗРАБОТЧИКА
Система бизнес-аналитики с поддержкой российских налоговых режимов и импорта из 1С

===============================================================================
СОДЕРЖАНИЕ:
1. Введение в проект
2. Архитектура системы  
3. Этапы разработки (11 этапов)
4. Модели данных
5. API endpoints
6. Импорт данных из 1С
7. Налоговые расчеты
8. Аналитические инструменты
9. Критерии приемки
===============================================================================

ВВЕДЕНИЕ В ПРОЕКТ

Вы создаете backend для системы бизнес-аналитики, предназначенной для российского 
малого и среднего бизнеса. Это веб-приложение помогает предпринимателям:
- Вести ежедневный учет доходов и расходов
- Автоматически рассчитывать налоги по российским режимам
- Получать аналитику по 24 различным инструментам
- Импортировать данные из 1С:Бухгалтерия
- Принимать обоснованные бизнес-решения

АРХИТЕКТУРА СИСТЕМЫ

Технологический стек:
- Python 3.9+
- FastAPI (веб-фреймворк)
- SQLAlchemy (ORM)
- SQLite (база данных для локального развертывания)
- Pydantic (валидация данных)
- Uvicorn (ASGI сервер)

Структура проекта:
backend/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── organization.py
│   │   ├── daily_transaction.py
│   │   └── analytics_cache.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── organization.py
│   │   └── transaction.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── organizations.py
│   │   ├── transactions.py
│   │   ├── analytics.py
│   │   └── import_1c.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── tax_calculator.py
│   │   ├── data_generator.py
│   │   ├── one_c_import.py
│   │   ├── aggregator.py
│   │   └── analytics_tools.py
│   ├── utils/
│   │   └── __init__.py
│   └── database.py
├── requirements.txt
├── tests/
└── README.md

===============================================================================
ЭТАПЫ РАЗРАБОТКИ
===============================================================================

ЭТАП 1: ИНИЦИАЛИЗАЦИЯ ПРОЕКТА (День 1)
Цель: Создать базовую структуру проекта

Задачи:
1. Создать структуру папок проекта
2. Настроить виртуальное окружение Python
3. Установить зависимости (requirements.txt):
   fastapi==0.104.1
   uvicorn[standard]==0.24.0
   sqlalchemy==2.0.23
   pydantic==2.5.0
   python-multipart==0.0.6
   pytest==7.4.3

4. Создать базовый main.py с FastAPI приложением
5. Настроить CORS для работы с frontend
6. Проверить запуск сервера на localhost:8000

Пример main.py:
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Business Analytics API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Business Analytics API"}

Критерии готовности:
- Сервер запускается без ошибок
- Доступна документация API на /docs
- CORS настроен для localhost:3000

ЭТАП 2: НАСТРОЙКА БАЗЫ ДАННЫХ (День 1-2)
Цель: Подключить SQLite и настроить SQLAlchemy

Задачи:
1. Создать database.py с подключением к SQLite
2. Настроить SQLAlchemy engine и session
3. Создать базовый класс Base для моделей
4. Настроить автоматическое создание таблиц
5. Добавить функции для работы с сессиями БД

Пример database.py:
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./business_analytics.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_tables():
    Base.metadata.create_all(bind=engine)

Критерии готовности:
- Создается файл business_analytics.db
- Подключение к БД работает без ошибок

ЭТАП 3: МОДЕЛИ ДАННЫХ (День 2-3)
Цель: Создать все необходимые модели данных

Модель Organization (models/organization.py):
from sqlalchemy import Column, Integer, String, Date, DateTime, Text
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime

class Organization(Base):
    __tablename__ = "organizations"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(Text)
    legal_form = Column(String(10))  # ИП, ООО
    tax_regime = Column(String(50))  # usn_income, usn_profit, osno, patent
    region = Column(String(100))
    okved = Column(String(20))
    employee_count = Column(String(10))
    registration_date = Column(Date)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    transactions = relationship("DailyTransaction", back_populates="organization")

Модель DailyTransaction (models/daily_transaction.py):
from sqlalchemy import Column, Integer, ForeignKey, Date, Numeric, Text, DateTime, String
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime

class DailyTransaction(Base):
    __tablename__ = "daily_transactions"
    
    id = Column(Integer, primary_key=True, index=True)
    organization_id = Column(Integer, ForeignKey("organizations.id"))
    date = Column(Date, nullable=False)
    income = Column(Numeric(12, 2), default=0)
    expenses = Column(Numeric(12, 2), default=0)
    balance = Column(Numeric(12, 2))
    tax_amount = Column(Numeric(12, 2))
    category = Column(String(50))
    description = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    organization = relationship("Organization", back_populates="transactions")

Модель AnalyticsCache (models/analytics_cache.py):
from sqlalchemy import Column, Integer, ForeignKey, String, DateTime, JSON
from app.database import Base
from datetime import datetime

class AnalyticsCache(Base):
    __tablename__ = "analytics_cache"
    
    id = Column(Integer, primary_key=True, index=True)
    organization_id = Column(Integer, ForeignKey("organizations.id"))
    tool_name = Column(String(50))
    period = Column(String(20))
    data = Column(JSON)
    calculated_at = Column(DateTime, default=datetime.utcnow)

Критерии готовности:
- Все таблицы создаются в БД
- Связи между таблицами работают
- Можно создать тестовые записи

ЭТАП 4: PYDANTIC СХЕМЫ (День 3)
Цель: Создать схемы для валидации данных API

Схемы для Organization (schemas/organization.py):
from pydantic import BaseModel, validator
from datetime import date, datetime
from typing import Optional, List
from enum import Enum

class TaxRegime(str, Enum):
    USN_INCOME = "usn_income"
    USN_PROFIT = "usn_profit"
    OSNO = "osno"
    PATENT = "patent"

class OrganizationCreate(BaseModel):
    name: str
    description: Optional[str] = None
    legal_form: str
    tax_regime: TaxRegime
    region: str
    okved: Optional[str] = None
    employee_count: Optional[str] = None
    registration_date: Optional[date] = None

class OrganizationResponse(BaseModel):
    id: int
    name: str
    description: Optional[str]
    legal_form: str
    tax_regime: str
    region: str
    okved: Optional[str]
    employee_count: Optional[str]
    registration_date: Optional[date]
    created_at: datetime
    
    class Config:
        orm_mode = True

Схемы для DailyTransaction (schemas/transaction.py):
from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional

class DailyTransactionCreate(BaseModel):
    date: date
    income: float
    expenses: float
    category: Optional[str] = None
    description: Optional[str] = None

class DailyTransactionResponse(BaseModel):
    id: int
    date: date
    income: float
    expenses: float
    balance: float
    tax_amount: float
    category: Optional[str]
    description: Optional[str]
    created_at: datetime
    
    class Config:
        orm_mode = True

Критерии готовности:
- Валидация входных данных работает
- Схемы покрывают все модели
- Ошибки валидации возвращают понятные сообщения

ЭТАП 5: API ДЛЯ ОРГАНИЗАЦИЙ (День 3-4)
Цель: Создать CRUD операции для организаций

API endpoints (api/organizations.py):
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import models, schemas
from app.database import get_db

router = APIRouter(prefix="/api/organizations", tags=["organizations"])

@router.post("/", response_model=schemas.OrganizationResponse)
def create_organization(
    org: schemas.OrganizationCreate, 
    db: Session = Depends(get_db)
):
    db_org = models.Organization(**org.dict())
    db.add(db_org)
    db.commit()
    db.refresh(db_org)
    return db_org

@router.get("/", response_model=List[schemas.OrganizationResponse])
def get_organizations(db: Session = Depends(get_db)):
    return db.query(models.Organization).all()

@router.get("/{org_id}", response_model=schemas.OrganizationResponse)
def get_organization(org_id: int, db: Session = Depends(get_db)):
    org = db.query(models.Organization).filter(models.Organization.id == org_id).first()
    if not org:
        raise HTTPException(status_code=404, detail="Organization not found")
    return org

@router.put("/{org_id}", response_model=schemas.OrganizationResponse)
def update_organization(
    org_id: int, 
    org_update: schemas.OrganizationCreate, 
    db: Session = Depends(get_db)
):
    org = db.query(models.Organization).filter(models.Organization.id == org_id).first()
    if not org:
        raise HTTPException(status_code=404, detail="Organization not found")
    
    for key, value in org_update.dict().items():
        setattr(org, key, value)
    
    db.commit()
    db.refresh(org)
    return org

@router.delete("/{org_id}")
def delete_organization(org_id: int, db: Session = Depends(get_db)):
    org = db.query(models.Organization).filter(models.Organization.id == org_id).first()
    if not org:
        raise HTTPException(status_code=404, detail="Organization not found")
    
    db.delete(org)
    db.commit()
    return {"detail": "Organization deleted"}

Критерии готовности:
- Все CRUD операции работают
- Ошибки обрабатываются корректно
- API документация генерируется автоматически

ЭТАП 6: API ДЛЯ ЕЖЕДНЕВНЫХ ОПЕРАЦИЙ (День 4-5)
Цель: Создать API для учета доходов и расходов

API transactions (api/transactions.py):
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import date
from app import models, schemas
from app.database import get_db
from app.services.tax_calculator import calculate_tax

router = APIRouter(prefix="/api/organizations/{org_id}/transactions", tags=["transactions"])

@router.post("/", response_model=schemas.DailyTransactionResponse)
def create_transaction(
    org_id: int,
    transaction: schemas.DailyTransactionCreate,
    db: Session = Depends(get_db)
):
    # Проверяем существование организации
    org = db.query(models.Organization).filter(models.Organization.id == org_id).first()
    if not org:
        raise HTTPException(status_code=404, detail="Organization not found")
    
    # Рассчитываем налог
    tax_amount = calculate_tax(transaction.income, transaction.expenses, org.tax_regime)
    
    # Создаем транзакцию
    db_transaction = models.DailyTransaction(
        organization_id=org_id,
        **transaction.dict(),
        tax_amount=tax_amount,
        balance=transaction.income - transaction.expenses
    )
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction

@router.get("/", response_model=List[schemas.DailyTransactionResponse])
def get_transactions(
    org_id: int,
    start_date: Optional[date] = Query(None),
    end_date: Optional[date] = Query(None),
    db: Session = Depends(get_db)
):
    query = db.query(models.DailyTransaction).filter(
        models.DailyTransaction.organization_id == org_id
    )
    
    if start_date:
        query = query.filter(models.DailyTransaction.date >= start_date)
    if end_date:
        query = query.filter(models.DailyTransaction.date <= end_date)
    
    return query.all()

@router.post("/generate-test-data")
def generate_test_data(org_id: int, db: Session = Depends(get_db)):
    from app.services.data_generator import generate_test_data
    generate_test_data(org_id, db)
    return {"detail": "Test data generated"}

Критерии готовности:
- Можно добавлять ежедневные операции
- Налоги рассчитываются автоматически
- Фильтрация по датам работает

ЭТАП 7: НАЛОГОВЫЕ РАСЧЕТЫ (День 5-6)
Цель: Реализовать расчет налогов по российским режимам

Налоговый калькулятор (services/tax_calculator.py):
def calculate_tax(income: float, expenses: float, tax_regime: str) -> float:
    \"\"\"
    Рассчитывает налог в зависимости от налогового режима
    \"\"\"
    if tax_regime == "usn_income":
        return income * 0.06  # 6% с доходов
    
    elif tax_regime == "usn_profit":
        profit = income - expenses
        if profit > 0:
            return max(profit * 0.15, income * 0.01)  # 15% с прибыли, минимум 1%
        return 0
    
    elif tax_regime == "osno":
        vat = income * 0.20 / 1.20  # НДС 20%
        profit_tax = (income - expenses - vat) * 0.20  # Налог на прибыль 20%
        return vat + profit_tax
    
    elif tax_regime == "patent":
        return 0  # Фиксированный платеж, рассчитывается отдельно
    
    return 0

def get_tax_calendar(tax_regime: str, legal_form: str) -> dict:
    \"\"\"
    Возвращает календарь налоговых платежей
    \"\"\"
    calendars = {
        "usn_income": {
            "quarterly_payments": ["25.04", "25.07", "25.10"],
            "annual_declaration": "25.04" if legal_form == "ip" else "25.03"
        },
        "usn_profit": {
            "quarterly_payments": ["25.04", "25.07", "25.10"],
            "annual_declaration": "25.04" if legal_form == "ip" else "25.03"
        },
        "osno": {
            "monthly_vat": "25 числа каждого месяца",
            "quarterly_profit": ["28.04", "28.07", "28.10"],
            "annual_declaration": "31.03"
        },
        "patent": {
            "payment_schedule": "1/3 в первые 90 дней, остаток до окончания срока"
        }
    }
    return calendars.get(tax_regime, {})

Критерии готовности:
- Налоги рассчитываются корректно для всех режимов
- Календарь налоговых платежей генерируется
- Минимальный налог учитывается для УСН

ЭТАП 8: ИМПОРТ ДАННЫХ ИЗ 1С (День 6)
Цель: Реализовать импорт XML/CSV файлов из 1С:Бухгалтерия

Сервис импорта (services/one_c_import.py):
import xml.etree.ElementTree as ET
from datetime import datetime
from app import models
from app.services.tax_calculator import calculate_tax

def parse_1c_export(file_path: str):
    \"\"\"
    Парсит XML файл экспорта из 1С
    \"\"\"
    tree = ET.parse(file_path)
    root = tree.getroot()
    
    for doc in root.findall(".//Документ"):
        try:
            date_str = doc.find("Дата").text
            amount = float(doc.find("Сумма").text)
            doc_type = doc.find("ВидДокумента").text
            
            yield {
                "date": datetime.strptime(date_str, "%Y-%m-%d").date(),
                "amount": amount,
                "type": doc_type,
                "description": doc.find("Комментарий").text if doc.find("Комментарий") is not None else ""
            }
        except (AttributeError, ValueError) as e:
            print(f"Error parsing document: {e}")
            continue

def import_1c(file_path: str, org_id: int, db):
    \"\"\"
    Импортирует данные из файла 1С в базу данных
    \"\"\"
    org = db.query(models.Organization).filter(models.Organization.id == org_id).first()
    if not org:
        raise ValueError("Organization not found")
    
    for record in parse_1c_export(file_path):
        # Определяем тип операции
        income = record["amount"] if record["type"] in ["Поступление", "Реализация"] else 0
        expenses = record["amount"] if record["type"] in ["Расход", "Закупка"] else 0
        
        # Рассчитываем налог
        tax_amount = calculate_tax(income, expenses, org.tax_regime)
        
        # Создаем транзакцию
        db_transaction = models.DailyTransaction(
            organization_id=org_id,
            date=record["date"],
            income=income,
            expenses=expenses,
            balance=income - expenses,
            tax_amount=tax_amount,
            category="1c_import",
            description=record["description"]
        )
        db.add(db_transaction)
    
    db.commit()

API для импорта (api/import_1c.py):
from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.one_c_import import import_1c
import os
import tempfile

router = APIRouter(prefix="/api/organizations/{org_id}/import", tags=["import"])

@router.post("/1c")
async def upload_1c_export(
    org_id: int,
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    \"\"\"
    Загрузка и импорт файла экспорта из 1С
    Ссылка на руководство по экспорту: https://its.1c.ru/db/metod8dev#content:78:hdoc
    \"\"\"
    if not file.filename.endswith((".xml", ".csv")):
        raise HTTPException(status_code=400, detail="Поддерживаются только XML и CSV файлы")
    
    # Сохраняем временный файл
    with tempfile.NamedTemporaryFile(delete=False, suffix=f"_{file.filename}") as tmp_file:
        content = await file.read()
        tmp_file.write(content)
        tmp_file_path = tmp_file.name
    
    try:
        # Импортируем данные
        import_1c(tmp_file_path, org_id, db)
        
        # Очищаем кэш аналитики для этой организации
        from app.models.analytics_cache import AnalyticsCache
        db.query(AnalyticsCache).filter(AnalyticsCache.organization_id == org_id).delete()
        db.commit()
        
        return {"detail": "Данные из 1С успешно импортированы"}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ошибка при импорте: {str(e)}")
    
    finally:
        # Удаляем временный файл
        os.unlink(tmp_file_path)

Критерии готовности:
- XML файлы из 1С парсятся корректно
- Данные записываются в daily_transactions
- API endpoint работает с multipart/form-data
- Кэш аналитики очищается после импорта

ЭТАП 9: БАЗОВЫЕ АНАЛИТИЧЕСКИЕ ФУНКЦИИ (День 6-7)
Цель: Создать основу для аналитических расчетов

Генератор тестовых данных (services/data_generator.py):
from datetime import date, timedelta
import random
from app import models
from app.services.tax_calculator import calculate_tax

def generate_test_data(org_id: int, db):
    \"\"\"
    Генерирует тестовые данные с января 2025 по текущую дату
    \"\"\"
    org = db.query(models.Organization).filter(models.Organization.id == org_id).first()
    if not org:
        raise ValueError("Organization not found")
    
    start_date = date(2025, 1, 1)
    end_date = date.today()
    
    current_date = start_date
    running_balance = 0
    
    while current_date <= end_date:
        # Генерируем случайные доходы и расходы
        income = random.randint(10000, 100000)
        expenses = random.randint(5000, 50000)
        daily_balance = income - expenses
        running_balance += daily_balance
        
        # Рассчитываем налог
        tax_amount = calculate_tax(income, expenses, org.tax_regime)
        
        # Создаем транзакцию
        transaction = models.DailyTransaction(
            organization_id=org_id,
            date=current_date,
            income=income,
            expenses=expenses,
            balance=daily_balance,
            tax_amount=tax_amount,
            category="test_data",
            description=f"Тестовые данные за {current_date.strftime('%d.%m.%Y')}"
        )
        db.add(transaction)
        
        current_date += timedelta(days=1)
    
    db.commit()

Агрегатор данных (services/aggregator.py):
from datetime import date
from sqlalchemy.orm import Session
from app import models

def aggregate_by_period(org_id: int, start_date: date, end_date: date, db: Session):
    \"\"\"
    Агрегирует данные по периоду
    \"\"\"
    transactions = db.query(models.DailyTransaction).filter(
        models.DailyTransaction.organization_id == org_id,
        models.DailyTransaction.date >= start_date,
        models.DailyTransaction.date <= end_date
    ).all()
    
    if not transactions:
        return {
            "income": 0,
            "expenses": 0,
            "profit": 0,
            "tax": 0,
            "net_profit": 0,
            "transaction_count": 0
        }
    
    total_income = sum(float(t.income) for t in transactions)
    total_expenses = sum(float(t.expenses) for t in transactions)
    total_tax = sum(float(t.tax_amount) for t in transactions)
    profit = total_income - total_expenses
    net_profit = profit - total_tax
    
    return {
        "income": total_income,
        "expenses": total_expenses,
        "profit": profit,
        "tax": total_tax,
        "net_profit": net_profit,
        "transaction_count": len(transactions)
    }

def get_quarterly_data(org_id: int, year: int, db: Session):
    \"\"\"
    Возвращает данные по кварталам
    \"\"\"
    quarters = {}
    
    for q in range(1, 5):
        if q == 1:
            start = date(year, 1, 1)
            end = date(year, 3, 31)
        elif q == 2:
            start = date(year, 4, 1)
            end = date(year, 6, 30)
        elif q == 3:
            start = date(year, 7, 1)
            end = date(year, 9, 30)
        else:
            start = date(year, 10, 1)
            end = date(year, 12, 31)
        
        quarters[f"Q{q}"] = aggregate_by_period(org_id, start, end, db)
    
    return quarters

Критерии готовности:
- Данные агрегируются по месяцам и кварталам
- Тестовые данные генерируются корректно
- Базовые расчеты работают

ЭТАП 10: API ДЛЯ АНАЛИТИКИ - ОСНОВНЫЕ ИНСТРУМЕНТЫ (День 7-8)
Цель: Реализовать API для получения аналитики

API аналитики (api/analytics.py):
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from datetime import date, datetime
from typing import Optional
from app.database import get_db
from app.services.aggregator import aggregate_by_period, get_quarterly_data
from app.services.analytics_tools import analyze_payment_calendar, analyze_cash_flow

router = APIRouter(prefix="/api/organizations/{org_id}/analytics", tags=["analytics"])

def parse_period(period: str):
    \"\"\"Парсит строку периода в даты\"\"\"
    today = date.today()
    
    if period == "current_month":
        start = date(today.year, today.month, 1)
        end = today
    elif period == "current_quarter":
        quarter = (today.month - 1) // 3 + 1
        start = date(today.year, (quarter - 1) * 3 + 1, 1)
        end = today
    elif period == "current_year":
        start = date(today.year, 1, 1)
        end = today
    else:
        # Формат: "2025-01-01_2025-03-31"
        try:
            start_str, end_str = period.split("_")
            start = datetime.strptime(start_str, "%Y-%m-%d").date()
            end = datetime.strptime(end_str, "%Y-%m-%d").date()
        except ValueError:
            raise HTTPException(status_code=400, detail="Invalid period format")
    
    return start, end

@router.get("/{tool_name}")
def get_analytics(
    org_id: int,
    tool_name: str,
    period: str = Query("current_month"),
    db: Session = Depends(get_db)
):
    \"\"\"
    Получить аналитику по конкретному инструменту
    \"\"\"
    # Проверяем существование организации
    org = db.query(models.Organization).filter(models.Organization.id == org_id).first()
    if not org:
        raise HTTPException(status_code=404, detail="Organization not found")
    
    # Парсим период
    start_date, end_date = parse_period(period)
    
    # Получаем агрегированные данные
    data = aggregate_by_period(org_id, start_date, end_date, db)
    
    # Применяем конкретный аналитический инструмент
    if tool_name == "platezhnyy_kalendar":
        result = analyze_payment_calendar(org_id, start_date, end_date, db)
    elif tool_name == "dds_klassicheskiy":
        result = analyze_cash_flow(org_id, start_date, end_date, db)
    elif tool_name == "finansovaya_model":
        result = analyze_financial_model(org_id, start_date, end_date, db, data)
    else:
        # Базовая аналитика для остальных инструментов
        result = {
            "summary": data,
            "charts": [],
            "recommendations": ["Инструмент находится в разработке"]
        }
    
    return {
        "tool_name": tool_name,
        "period": period,
        "start_date": start_date.isoformat(),
        "end_date": end_date.isoformat(),
        "organization": {
            "id": org.id,
            "name": org.name,
            "tax_regime": org.tax_regime
        },
        "data": result,
        "calculated_at": datetime.utcnow().isoformat()
    }

@router.get("/dashboard")
def get_dashboard(
    org_id: int,
    year: int = Query(2025),
    db: Session = Depends(get_db)
):
    \"\"\"
    Получить данные для дашборда организации
    \"\"\"
    quarterly_data = get_quarterly_data(org_id, year, db)
    
    # Общие показатели за год
    year_data = aggregate_by_period(org_id, date(year, 1, 1), date(year, 12, 31), db)
    
    return {
        "year": year,
        "summary": year_data,
        "quarters": quarterly_data,
        "generated_at": datetime.utcnow().isoformat()
    }

Основные аналитические функции (services/analytics_tools.py):
from datetime import date
from sqlalchemy.orm import Session
from app import models

def analyze_payment_calendar(org_id: int, start_date: date, end_date: date, db: Session):
    \"\"\"
    Анализ платежного календаря
    \"\"\"
    # Получаем транзакции по дням
    transactions = db.query(models.DailyTransaction).filter(
        models.DailyTransaction.organization_id == org_id,
        models.DailyTransaction.date >= start_date,
        models.DailyTransaction.date <= end_date
    ).order_by(models.DailyTransaction.date).all()
    
    # Рассчитываем остатки по дням
    daily_balances = []
    running_balance = 0
    cash_gaps = []
    
    for transaction in transactions:
        running_balance += float(transaction.income) - float(transaction.expenses)
        
        balance_record = {
            "date": transaction.date.isoformat(),
            "income": float(transaction.income),
            "expenses": float(transaction.expenses),
            "balance": running_balance,
            "tax": float(transaction.tax_amount),
            "cash_gap": running_balance < 0
        }
        
        daily_balances.append(balance_record)
        
        if balance_record["cash_gap"]:
            cash_gaps.append(balance_record)
    
    # Генерируем рекомендации
    if not cash_gaps:
        recommendation = "У Вас все хорошо, так держать!"
        status = "good"
    else:
        recommendation = f"Ситуация настораживает, возможны кассовые разрывы. Обнаружено {len(cash_gaps)} дней с отрицательным остатком."
        status = "warning"
    
    return {
        "daily_balances": daily_balances,
        "cash_gaps_count": len(cash_gaps),
        "cash_gaps": cash_gaps,
        "total_income": sum(b["income"] for b in daily_balances),
        "total_expenses": sum(b["expenses"] for b in daily_balances),
        "final_balance": daily_balances[-1]["balance"] if daily_balances else 0,
        "recommendation": recommendation,
        "status": status,
        "charts": {
            "balance_chart": [
                {"date": b["date"], "balance": b["balance"]} for b in daily_balances
            ],
            "income_expenses_chart": [
                {"date": b["date"], "income": b["income"], "expenses": b["expenses"]} 
                for b in daily_balances
            ]
        }
    }

def analyze_cash_flow(org_id: int, start_date: date, end_date: date, db: Session):
    \"\"\"
    Анализ движения денежных средств
    \"\"\"
    from app.services.aggregator import aggregate_by_period
    
    data = aggregate_by_period(org_id, start_date, end_date, db)
    
    # Анализ структуры доходов и расходов
    if data["income"] > 0:
        income_structure = {
            "operational": data["income"] * 0.8,  # Условно
            "financial": data["income"] * 0.15,
            "other": data["income"] * 0.05
        }
    else:
        income_structure = {"operational": 0, "financial": 0, "other": 0}
    
    # Рекомендации
    if data["profit"] > 0 and data["income"] > data["expenses"]:
        recommendation = "Ваша платежеспособность на хорошем уровне."
        status = "good"
    elif data["profit"] < 0:
        recommendation = "Расходы превышают доходы. Необходимо проанализировать структуру затрат."
        status = "bad"
    else:
        recommendation = "Финансовое состояние стабильное, но есть потенциал для улучшения."
        status = "neutral"
    
    return {
        "cash_flow": {
            "operational": data["profit"],
            "investment": 0,  # Пока не реализовано
            "financing": 0   # Пока не реализовано
        },
        "income_structure": income_structure,
        "total_income": data["income"],
        "total_expenses": data["expenses"],
        "net_cash_flow": data["profit"],
        "recommendation": recommendation,
        "status": status,
        "charts": {
            "structure_chart": income_structure,
            "flow_chart": {
                "income": data["income"],
                "expenses": data["expenses"],
                "net_flow": data["profit"]
            }
        }
    }

def analyze_financial_model(org_id: int, start_date: date, end_date: date, db: Session, data: dict):
    \"\"\"
    Анализ финансовой модели
    \"\"\"
    revenue = data["income"]
    costs = data["expenses"]
    profit = data["profit"]
    
    # Рассчитываем ключевые показатели
    gross_margin = (profit / revenue * 100) if revenue > 0 else 0
    operating_margin = (profit / revenue * 100) if revenue > 0 else 0
    
    # EBITDA (упрощенный расчет)
    ebitda = profit  # В упрощенной модели равен прибыли
    
    # Точка безубыточности (условный расчет)
    variable_costs = costs * 0.6  # Условно 60% переменные
    fixed_costs = costs * 0.4     # Условно 40% постоянные
    
    if revenue > variable_costs:
        contribution_margin = revenue - variable_costs
        breakeven_point = fixed_costs / (contribution_margin / revenue) if contribution_margin > 0 else 0
    else:
        breakeven_point = 0
    
    # Рекомендации
    if gross_margin > 20 and profit > 0:
        recommendation = "Перспективы бизнеса хорошие"
        status = "good"
    elif gross_margin < 5 or profit < 0:
        recommendation = "Необходима оптимизация расходов и увеличение маржинальности"
        status = "bad"
    else:
        recommendation = "Финансовые показатели в норме, есть потенциал для роста"
        status = "neutral"
    
    return {
        "financial_metrics": {
            "revenue": revenue,
            "costs": costs,
            "profit": profit,
            "ebitda": ebitda,
            "gross_margin_percent": round(gross_margin, 2),
            "operating_margin_percent": round(operating_margin, 2),
            "breakeven_point": round(breakeven_point, 2)
        },
        "cost_structure": {
            "variable_costs": variable_costs,
            "fixed_costs": fixed_costs
        },
        "recommendation": recommendation,
        "status": status,
        "charts": {
            "profitability_chart": {
                "revenue": revenue,
                "costs": costs,
                "profit": profit
            },
            "margin_chart": {
                "gross_margin": gross_margin,
                "target_margin": 25  # Целевая маржа
            }
        }
    }

Критерии готовности:
- API возвращает структурированные данные для 3+ инструментов
- Рекомендации генерируются на основе критериев
- Дашборд показывает ключевые метрики
- Данные группируются по периодам

ЭТАП 11: ОПТИМИЗАЦИЯ И ТЕСТИРОВАНИЕ (День 9-10)
Цель: Довести систему до продакшн-готовности

Тестирование (tests/test_tax_calculator.py):
import pytest
from app.services.tax_calculator import calculate_tax, get_tax_calendar

def test_usn_income_tax():
    tax = calculate_tax(100000, 50000, "usn_income")
    assert tax == 6000  # 6% от 100000

def test_usn_profit_tax():
    tax = calculate_tax(100000, 50000, "usn_profit")
    assert tax == 7500  # 15% от (100000-50000)

def test_usn_profit_minimum_tax():
    tax = calculate_tax(100000, 95000, "usn_profit")
    assert tax == 1000  # минимальный налог 1% от оборота

def test_osno_tax():
    tax = calculate_tax(120000, 60000, "osno")  # С НДС
    expected_vat = 120000 * 0.20 / 1.20  # НДС
    expected_profit_tax = (120000 - 60000 - expected_vat) * 0.20
    assert abs(tax - (expected_vat + expected_profit_tax)) < 0.01

def test_tax_calendar():
    calendar = get_tax_calendar("usn_income", "ip")
    assert "quarterly_payments" in calendar
    assert calendar["annual_declaration"] == "25.04"

Логирование (utils/logger.py):
import logging
from logging.handlers import RotatingFileHandler

def setup_logger():
    logger = logging.getLogger("business_analytics")
    logger.setLevel(logging.INFO)
    
    handler = RotatingFileHandler("app.log", maxBytes=10000000, backupCount=5)
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    
    return logger

Middleware для логирования (main.py дополнение):
from fastapi import Request, Response
from utils.logger import setup_logger
import time

logger = setup_logger()

@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    
    logger.info(
        f"{request.method} {request.url.path} - "
        f"Status: {response.status_code} - "
        f"Time: {process_time:.4f}s"
    )
    
    return response

Критерии готовности:
- Все тесты проходят
- API документация полная и актуальная
- Логирование работает
- Система готова к интеграции с frontend
- Производительность оптимизирована

===============================================================================
КРИТЕРИИ ПРИЕМКИ РАБОТЫ
===============================================================================

Обязательные требования:
1. ✅ Все API endpoints работают согласно спецификации
2. ✅ Поддержка всех российских налоговых режимов
3. ✅ Импорт данных из 1С (XML формат)
4. ✅ Генерация тестовых данных за каждый день
5. ✅ API аналитики возвращает данные для frontend
6. ✅ Автоматическая документация на /docs
7. ✅ Система обрабатывает ошибки корректно

Дополнительные требования:
1. ✅ Unit тесты покрывают основную логику (>70%)
2. ✅ Логирование всех операций
3. ✅ Оптимизированные SQL запросы
4. ✅ Код соответствует PEP 8

Технические метрики:
- Время ответа API < 2 сек
- База данных растет корректно
- Нет утечек памяти
- Документация API актуальна

===============================================================================
ССЫЛКИ И РЕСУРСЫ
===============================================================================

Документация:
- FastAPI: https://fastapi.tiangolo.com/
- SQLAlchemy: https://docs.sqlalchemy.org/
- Pydantic: https://docs.pydantic.dev/
- 1С экспорт: https://its.1c.ru/db/metod8dev#content:78:hdoc

Примеры российского налогового законодательства:
- УСН: ставки 6% и 15%
- ОСНО: НДС 20%, налог на прибыль 20%
- Патент: фиксированная стоимость по регионам

Контакты для вопросов:
- Тимлид: для архитектурных решений
- Frontend разработчик: для согласования API контрактов

===============================================================================
ЗАКЛЮЧЕНИЕ
===============================================================================

Данное техническое задание предоставляет полную инструкцию для создания
backend системы бизнес-аналитики с поддержкой российской специфики и
интеграцией с 1С:Бухгалтерия. Следуя этапам разработки, вы создадите
масштабируемую и производительную систему, готовую для интеграции с frontend
и дальнейшего развития.

Удачи в разработке!
"""