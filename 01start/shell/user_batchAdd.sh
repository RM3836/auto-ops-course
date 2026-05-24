#!/bin/bash
# 添加一个名为testers的用户组
groupadd testers
if [ $? -eq 0 ]; then
  echo "添加用户组testers成功!"
fi
# 创建10个用户账户，命名为tester01至tester10，并将他们加入到testers组
for i in `seq -w 1 10`
do
  useradd -m -G testers tester$i  
  if [ $? -eq 0 ]; then
    echo "添加用户账户tester$i成功!"
  fi
# 将每个用户账户的初始密码设置为其用户名，这是一种修改密码的非交互方式
  echo tester$i:tester$i | chpasswd  
  if [ $? -eq 0 ]; then
    echo "用户账户tester$i的初始密码：tester$i "
  fi
done

