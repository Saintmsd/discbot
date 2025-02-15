# Discord Administration Bot

Бот для управления серверами Discord с интеграцией GitHub

## Установка

Установите зависимости:
1. pip install -r requirements.txt
2. Переименуйте config.example.py в config.py и заполните данные


Команды:

!kick @user [причина] - Кикнуть пользователя

!ban @user [причина] - Забанить пользователя

!clear N - Удалить N сообщений

Остальные важные команды бот выдает по команде !help 

3. Файл `requirements.txt`
discord.py>=2.0.0
python-dotenv>=0.19.0


4. Файл `config.example.py`
```python
TOKEN = "ВАШ_ТОКЕН_БОТА"
GITHUB_REPO_PATH = "/полный/путь/к/вашему/репозиторию"
