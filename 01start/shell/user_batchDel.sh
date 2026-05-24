#!/bin/bash
for i in `seq -w 1 10`
do
  userdel -r tester$i
  if [ $? -eq 0 ]; then
    echo "删除用户账户tester$i成功!"
  fi
done
groupdel testers
if [ $? -eq 0 ]; then
  echo "删除用户组testers成功!"
fi

