from src.tools.sql import DBConnector

connector = DBConnector()
connector.call_sp_ins_account('TEST1', 'TEST1_NAME', 'TEST1_DESCR', 'USD')
