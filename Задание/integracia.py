"""
integracia.py

Техническое задание на разработку облачной/локальной аналитической системы финансов

1. Общие требования:
   - Язык: Python 3.9+
   - Архитектура: микросервисы или модульная монолитная структура
   - Веб-интерфейс: REST API + SPA
   - Развертывание: Docker Compose на web-сервере (DigitalOcean, AWS EC2, локальный сервер)

2. Состав системы:
   2.1. Backend (Python):
       - Flask или FastAPI (высокая производительность, асинхронность)
       - SQLAlchemy + Alembic (ORM и миграции)
       - PostgreSQL (база данных)
       - Redis (кеширование, брокер задач)
       - Celery (фоновые задачи и планировщик)
       - Pydantic (валидация данных)
       - Uvicorn/Gunicorn (ASGI/WSGI сервер)

   2.2. Frontend:
       - React или Vue.js (SPA)
       - Redux/Vuex (управление состоянием)
       - Axios (HTTP-клиент)
       - TailwindCSS или Bootstrap (UI)
       - Vite/Webpack (сборка)

   2.3. DevOps и инфраструктура:
       - Docker, Docker Compose
       - Nginx (реверс-прокси)
       - Certbot (Let's Encrypt SSL)
       - GitHub Actions (CI/CD)
       - Terraform/Ansible (по желанию для IaC)

3. Функциональные модули:
   - Аутентификация/авторизация: JWT, OAuth2 (Keycloak или open-source решения)
   - Управление организациями, пользователями, ролями
   - Загрузка и трансформация данных (CSV, Excel, API)
   - ETL-процессы: Pandas или Apache Airflow (при масштабе)
   - Аналитика: построение отчетов, дашбордов (Plotly/Dash или Grafana)
   - Экспорт отчетов (PDF, Excel) (WeasyPrint, XlsxWriter)

4. Требования безопасности:
   - Аутентификация: JWT + HTTPS
   - Авторизация: RBAC
   - Шифрование: TLS на уровне транспорта, AES-256 для защиты чувствительных данных в БД
   - Менеджмент секретов: Vault или environment variables + Doppler (бесплатное ядро)
   - Защита API: rate limiting (Flask-Limiter), CORS
   - Сканирование уязвимостей: Bandit, Snyk Open Source (бесплатный план)
   - Логи и аудит: ELK-stack или бесплатный Graylog

5. Порядок внедрения:
   - Подготовка инфраструктуры (установка Docker, настройка сервера)
   - Развертывание базового стека (NGINX, Postgres, Redis)
   - CI/CD pipeline: настройка GitHub Actions (test->build->deploy)
   - Разработка backend API и модулей
   - Разработка frontend SPA
   - Интеграционное тестирование (pytest, Selenium/Playwright)
   - Настройка мониторинга (Prometheus + Grafana)

6. Документация:
   - OpenAPI/Swagger для API
   - MkDocs/Sphinx для техдокументации
   - README.md с инструкцией по развертыванию

Пример структуры репозитория:

/analytica
  /backend
    app.py
    models/
    schemas/
    services/
    alembic/
  /frontend
    src/
      components/
      store/
      views/
    public/
  docker-compose.yml
  nginx.conf
  .github/workflows/ci.yml
  README.md

"""