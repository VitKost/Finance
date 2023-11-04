import psycopg


class DBConnector:
    def __init__(self):
        self.connector = psycopg.connect('postgresql://postgres:test_pass@localhost:5432/Finance')

    def __del__(self):
        self.connector.close()

    def call_sp_ins_account(self, in_account_id: str, in_account_name: str, in_account_description: str, in_currency: str):
        cursor = self.connector.cursor()
        try:
            cursor.execute('call accounting.ins_account(%s, %s, %s, %s)', [in_account_id, in_account_name, in_account_description, in_currency])
            self.connector.commit()
        finally:
            cursor.close()
