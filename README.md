# discbot
# Discord Administration Bot

Бот для управления серверами Discord с интеграцией GitHub

## Установка

1. Установите зависимости:
```bash
pip install -r requirements.txt
Переименуйте config.example.py в config.py и заполните данные

Запустите бота:

bash
Copy
python main.py
Команды
!kick @user [причина] - Кикнуть пользователя

!ban @user [причина] - Забанить пользователя

!clear N - Удалить N сообщений

!push [сообщение] - Выгрузить код на GitHub

Copy

3. Файл `requirements.txt`
discord.py>=2.0.0
python-dotenv>=0.19.0

Copy

4. Файл `config.example.py`
```python
TOKEN = "ВАШ_ТОКЕН_БОТА"
GITHUB_REPO_PATH = "/полный/путь/к/вашему/репозиторию"
