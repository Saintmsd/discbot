import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('database.db')
        self.cursor = self.conn.cursor()
        self._initialize_db()

    def _initialize_db(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS servers (
                guild_id INTEGER PRIMARY KEY,
                log_channel INTEGER,
                prefix TEXT DEFAULT '!'
            )
        ''')
        self.conn.commit()

    def set_log_channel(self, guild_id, channel_id):
        self.cursor.execute('''
            INSERT OR REPLACE INTO servers (guild_id, log_channel)
            VALUES (?, ?)
        ''', (guild_id, channel_id))
        self.conn.commit()

    def get_log_channel(self, guild_id):
        self.cursor.execute('''
            SELECT log_channel FROM servers WHERE guild_id = ?
        ''', (guild_id,))
        result = self.cursor.fetchone()
        return result[0] if result else None
