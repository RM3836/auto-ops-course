#!/bin/bash
#获取主机名
host_name=` hostname `
mem_total=$( free -m  |awk 'NR==2 {print $2}' )
mem_used=$( free -m  |awk 'NR==2 {print $3}' )
# 计算内存使用率
mem_percent=$[ ($mem_used * 100) / $mem_total ]
echo "$host_name主机内存使用率：$mem_percent%"

