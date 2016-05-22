sudo service mysql start
mysql -uroot -e "CREATE DATABASE askweb;"
mysql -uroot -e "GRANT ALL PRIVILEGES ON *.* TO 'box'@'localhost' WITH GRANT OPTION;"
mysql -uroot -e "FLUSH PRIVILEGES;"
cd ask/
python manage.py validate
python manage.py syncdb
