# 采用ThreadingGroupd对象并发执行
from fabric import ThreadingGroup as Group
hosts = (
    "root@192.168.10.50", "root@192.168.10.51"
)
group = Group(*hosts, connect_kwargs={"password": "abc123"})
print("自动安装LAMP ......")
# 安装Apache服务器
group.run("yum install httpd -y")
# 安装并启动MariaDB服务器
group.run("yum install mariadb mariadb-server -y")
group.run("systemctl start mariadb")
group.run("systemctl enable mariadb")
# 以非交互方式运行MariaDB数据库安全配置向导
group.run("echo -e '\ny\nabc123\nabc123\ny\ny\ny\ny\n' | /usr/bin/mysql_secure_installation")
# 安装PHP
group.run("yum install pcre gcc-c++ zlib* php php-mysqlnd php-gd libjpeg* php-ldap php-odbc php-pear php-xml* php-json php-mbstring php-bcmath php-mhash -y")
# 生成PHP测试文件
group.run("echo '<?php phpinfo(); ?>' |  tee /var/www/html/test.php")
# 启动Apache服务器
group.run("systemctl start httpd")
group.run("systemctl enable httpd")
# 防火墙开启HTTP和HTTPS服务
group.run("systemctl start firewalld",warn=True)
group.run("firewall-cmd --permanent --zone=public --add-service=http  --add-service=https",warn=True)
group.run("firewall-cmd  --reload")
# 安装phpMyAdmin
group.run("curl -o phpMyAdmin.zip https://files.phpmyadmin.net/phpMyAdmin/4.9.10/phpMyAdmin-4.9.10-all-languages.zip")
group.run("mv phpMyAdmin.zip /var/www/html")
group.run("unzip -d /var/www/html /var/www/html/phpMyAdmin.zip")
group.run("rm /var/www/html/phpMyAdmin.zip")
group.run("mv /var/www/html/phpMyAdmin-4.9.10-all-languages /var/www/html/phpmyadmin")
group.run("mv /var/www/html/phpmyadmin/config.sample.inc.php /var/www/html/phpmyadmin/config.inc.php")
group.close()
