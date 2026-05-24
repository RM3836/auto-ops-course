#!/bin/bash
# 定义获取CPU使用率的函数
function getCpu {
  # grep 'cpu '过滤出CPU总的使用情况，输出2-8列对应的时间
  cpu_time1=$(cat /proc/stat | grep 'cpu ' | awk '{print $2" "$3" "$4" "$5" "$6" "$7" "$8}')
  # 获取CPU空闲的时间（不包含IO等待）
  cpu_idle1=$(echo $cpu_time1 | awk '{print $4}')
  # 合计cpu_time1中各列的值
  cpu_total1=$(echo $cpu_time1 | awk '{print $1+$2+$3+$4+$5+$6+$7}')
  # 等5秒钟之后再测下一次CPU时间
  sleep 5
  cpu_time2=$(cat /proc/stat | grep 'cpu ' | awk '{print $2" "$3" "$4" "$5" "$6" "$7" "$8}')
  cpu_idle2=$(echo $cpu_time2 | awk '{print $4}')
  cpu_total2=$(echo $cpu_time2 | awk '{print $1+$2+$3+$4+$5+$6+$7}')
  # 计算CPU总的空闲时间
  cpu_idle=$(expr $cpu_idle2 - $cpu_idle1)
  # 计算CPU总的使用时间
  cpu_total=$(expr $cpu_total2 - $cpu_total1)
  # 计算CPU使用率
  cpu_usage=`echo "scale=4;($cpu_total-$cpu_idle)/$cpu_total*100" | bc | awk '{printf "%.2f",$1}'`

}

# 定义获取内存使用率的函数
function getMem {
  mem_info=$(cat /proc/meminfo)
  mem_total=$(echo "$mem_info" | grep "MemTotal" | awk '{print $2}' )
  mem_free=$(echo "$mem_info" | grep "MemFree" | awk '{print $2}' )
  mem_inactive=$(echo "$mem_info" | grep "Inactive:" | awk '{print $2}' )
  mem_used=$(echo "$mem_total - $mem_free - $mem_inactive "|bc)
  mem_usage=$(echo "scale=4;$mem_used/$mem_total*100"|bc | awk '{printf "%.2f",$1}')
}
# 依次执行以上两个函数
getCpu;getMem
# 获取当前时间并采用特定格式
cur_time=$(date "+%Y-%m-%d %H:%M:%S")  
cur_dir=$(cd $(dirname $0); pwd)
echo "$cur_time CPU使用率：$cpu_usage%  内存使用率：$mem_usage%" >> $cur_dir/sysinfo.txt
# 取百分比整数部分
cpu_usage=$(echo $cpu_usage | cut -d. -f1)
mem_usage=$(echo $mem_usage | cut -d. -f1)
# CPU或内存使用率超出限制报警
# 设置百分比限额
limit_value=10
if  [ $cpu_usage -ge $limit_value ];  then
    echo "$cur_time CPU超限" >> $cur_dir/warning.txt
fi
if  [ $mem_usage -ge $limit_value ];  then
    echo "$cur_time 内存超限"  >> $cur_dir/warning.txt
fi

