#!/usr/bin/bash
#定义3种颜色来区分主机状态
redFont="\e[31m"
greenFont="\e[32m"
whiteFont="\e[0m"
while read host
do
  for count in {1..3}
  do
    ping -c1 -W1 $host &>/dev/null
    if [ $? -eq 0 ];then
    # echo命令以不同颜色显示内容需要使用-e选项
      echo -e "${greenFont}"${host}主机 ${whiteFont}" 正在运行"
      break
    else
      fail_count[$count]=$host
    fi
  done
  if [ ${#fail_count[*]} -eq 3  ] ;then
    echo -e "${redFont}"${host}主机 ${whiteFont}" 停止运行"
    unset fail_count[*]
  fi
done <host_list
echo -e "${whiteFont}"
