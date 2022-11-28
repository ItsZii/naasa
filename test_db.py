import os
import requests
import mysql.connector

from worker_2_db import *
from configparser import ConfigParser

# Checking if all MYSQL related config options are present in the config file
print("Checking if config has MYSQL related options -->")
assert config.has_option('mysql_config', 'mysql_host') == True
assert config.has_option('mysql_config', 'mysql_db') == True
assert config.has_option('mysql_config', 'mysql_user') == True
assert config.has_option('mysql_config', 'mysql_pass') == True
print("OK")
print("----------")

# Checking if possible to connect to MySQL with the existing config options
print("Checking if it is possible to connect to MYSQL with the given config options -->")
mysql_config_mysql_host = config.get('mysql_config', 'mysql_host')
mysql_config_mysql_db = config.get('mysql_config', 'mysql_db')
mysql_config_mysql_user = config.get('mysql_config', 'mysql_user')
mysql_config_mysql_pass = config.get('mysql_config', 'mysql_pass')
connection = mysql.connector.connect(host=mysql_config_mysql_host, database=mysql_config_mysql_db, user=mysql_config_mysql_user, password=mysql_config_mysql_pass)
assert connection.is_connected() == True
print("OK")
print("----------")

print("Test DONE -> ALL OK")
print("----------------------------------------")
