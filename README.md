# 🤖 自动化运维技术 — 课程代码仓库

> **作者：YURM** | **广州应用科技学院 网络工程专业**
> **课程：自动化运维技术** | **学期：2025-2026**
> **声明：本仓库为课程学习代码，仅供教学参考。**

---

## 📖 课程概述

本课程通过 Python + Shell + Ansible 实现自动化运维的八大核心场景，从基础脚本到综合实战，覆盖运维工程师日常工作的主要技术栈。

## 🗂️ 模块结构

| 模块 | 目录 | 主题 | 核心技术 |
|------|------|------|----------|
| 01 | `01start/` | 脚本入门 | Shell 批量脚本、Python 基础 |
| 02 | `02sysmon/` | 系统监控 | `psutil`、`watchdog`、`pycurl`、`APScheduler` |
| 03 | `03file/` | 文件操作 | `json`、`yaml`、`xml`、`ini`、`Jinja2` |
| 04 | `04log/` | 日志与告警 | `logging`、`smtplib` 邮件告警 |
| 05 | `05report/` | 报表可视化 | `matplotlib`、`Dash`、`sqlite3`、`openpyxl` |
| 06 | `06batch/` | 批量管理 | `paramiko`（SSH）、`fabric`（批量执行） |
| 07 | `07net/` | 网络工具 | `scapy`、`nmap`、DNS 解析 |
| 08 | `08comp/` | 综合实战 | `Ansible` Playbook、Role、Jinja2 模板 |

---

## 📁 各模块文件清单

### 01 — 脚本入门

```
01start/
├── host_batchPing.py          # Python 批量 ping 主机
├── host_list                  # 主机列表文件
├── run_cmd.py                 # Python 执行系统命令
├── sys_mon.py                 # Python 系统监控脚本
└── shell/
    ├── host_batchPing.sh      # Shell 批量 ping
    ├── jdk_install.sh         # JDK 自动安装脚本
    ├── sys_mon.sh             # Shell 系统监控
    ├── user_batchAdd.sh       # Shell 批量添加用户
    └── user_batchDel.sh       # Shell 批量删除用户
```

**学习目标：** 掌握 Shell 和 Python 基础脚本，理解自动化运维的起点。

---

### 02 — 系统监控

```
02sysmon/
├── sysinfo_bypsutil.py        # psutil 采集 CPU/内存/磁盘/网络信息
├── sysinfo_byapscheduer.py    # APScheduler 定时采集系统信息
├── killproc_bypsutil.py       # psutil 按名称杀死进程
├── webmon_bypycurl.py         # pycurl 监控网站可用性
├── fsmon_bywatchdog01.py      # watchdog 文件系统监控（基础）
├── fsmon_bywatchdog02.py      # watchdog 文件系统监控（模式匹配）
├── fsmon_bypyinotify.py       # pyinotify 文件系统监控（Linux）
└── baknewfile_bywatchdog.py   # watchdog 自动备份新文件
```

**核心技术：**

```python
# psutil — 系统信息采集
import psutil
cpu = psutil.cpu_percent(interval=1)
mem = psutil.virtual_memory().percent
disk = psutil.disk_usage('/').percent

# watchdog — 文件系统监控
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# APScheduler — 定时任务
from apscheduler.schedulers.blocking import BlockingScheduler
scheduler = BlockingScheduler()
scheduler.add_job(func, 'interval', seconds=60)
```

---

### 03 — 文件操作

```
03file/
├── json_read.py / json_chg.py     # JSON 读写
├── yaml_read.py / yaml_chg.py     # YAML 读写
├── xml_read.py / xml_chg.py       # XML 读写
├── ini_read.py / ini_chg.py       # INI 配置文件读写
├── conf_view.py                   # 配置文件查看器
├── user_sum.py                    # 用户数据汇总
├── sysinfo_tohtml.py              # 系统信息生成 HTML 报告
├── xml_byjinja.py                 # Jinja2 模板生成 XML
├── cmp_dirs.py                    # 目录比较
├── diff_files.py                  # 文件差异比较
├── example1.json / example2.json  # JSON 示例文件
├── example1.yaml / example2.yaml  # YAML 示例文件
├── example1.xml / example2.xml    # XML 示例文件
├── example1.ini / example2.ini    # INI 示例文件
├── net_tmpl.xml                   # XML 网络模板
└── rpt_tmpl.html                  # HTML 报告模板
```

**学习目标：** 掌握运维中常见的配置文件格式（JSON/YAML/XML/INI）读写操作。

---

### 04 — 日志与告警

```
04log/
├── sysinfo_bypsutil.py       # 系统信息采集模块（被其他脚本引用）
├── log_tofile.py             # logging 输出到文件
├── log_toboth.py             # logging 同时输出到文件和控制台
├── log_tracerback.py         # logging 记录异常堆栈
├── sysinfo_tolog.py          # 定时采集 + 写入日志
├── sysinfo_log_alert.py      # 定时采集 + 日志 + 阈值告警
├── sysinfo_html_email.py     # Jinja2 生成 HTML 报告 + 邮件发送
└── email_send.py             # smtplib 邮件发送模块
```

**核心技术：**

```python
# logging — 日志管理
import logging
logging.basicConfig(filename='ops.log', level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s')

# smtplib — 邮件告警
import smtplib
from email.message import EmailMessage
msg = EmailMessage()
msg.set_content('CPU 使用率超过 90%！')
```

---

### 05 — 报表与可视化

```
05report/
├── plt_basic.py              # matplotlib 基础绑图
├── plt_subplots.py           # matplotlib 子图布局
├── sysinfo_chart.py          # 系统信息可视化图表
├── sysinfo_tocsv.py          # 系统信息导出 CSV
├── sysinfo_fromcsv.py        # 从 CSV 读取系统信息
├── sysinfo_tosqlite.py       # 系统信息存入 SQLite
├── sysinfo_fromsqlite.py     # 从 SQLite 读取系统信息
├── excel_create.py           # openpyxl 创建 Excel
├── excel_bar.py              # openpyxl Excel 柱状图
├── dash_layout.py            # Dash 布局基础
├── dash_table.py             # Dash 数据表格
├── dash_interact.py          # Dash 交互式图表
├── dash_mon.py               # Dash 监控面板
├── sysinfo_bydash.py         # Dash 系统监控 Web 面板
└── pages/
    ├── mon_table.py          # Dash 多页应用 - 表格页
    └── mon_scatter.py        # Dash 多页应用 - 散点图页
```

**核心技术栈：**

```
数据采集 → CSV/SQLite 存储 → matplotlib 绘图 → Dash Web 面板
```

---

### 06 — 批量管理（SSH）

```
06batch/
├── paramiko_pwd.py            # paramiko 密码认证 SSH
├── paramiko_key.py            # paramiko 密钥认证 SSH
├── paramiko_sudo.py           # paramiko 执行 sudo 命令
├── paramiko_sftp.py           # paramiko SFTP 文件传输
├── paramiko_transport.py      # paramiko Transport 对象
├── paramiko_tty.py            # paramiko 交互式 Shell
├── fabric_basic.py            # fabric 基础用法
├── fabric_group1.py           # fabric 分组管理（串行）
├── fabric_group2.py           # fabric 分组管理（并行）
├── fabric_sudo1.py            # fabric sudo 命令
├── fabric_sudo2.py            # fabric sudo 配置
├── sysinfo_byfabric.py        # fabric 批量采集系统信息
├── upload_byfabric.py         # fabric 批量上传文件（含 MD5 校验）
└── lamp_byfabric.py           # fabric 一键部署 LAMP 环境
```

**核心技术对比：**

| 工具 | 适用场景 | 特点 |
|------|----------|------|
| `paramiko` | 底层 SSH 控制 | 灵活，需要手动管理连接 |
| `fabric` | 批量任务执行 | 高层封装，支持分组/并行/sudo |

---

### 07 — 网络工具

```
07net/
├── dns_rslv.py               # DNS 域名解析
├── ipy_rslv.py               # IP 地址反向解析
├── nmap_active.py            # nmap 主机发现
├── nmap_service.py           # nmap 服务探测
├── scapy_scan.py             # scapy 端口扫描
├── scapy_sniff.py            # scapy 抓包嗅探
├── scapy_replay.py           # scapy 数据包重放
└── scapy_route.py            # scapy 路由追踪
```

**核心技术：**

```python
# scapy — 网络数据包操作
from scapy.all import IP, TCP, sr1, sniff
pkt = IP(dst="192.168.1.1")/TCP(dport=80, flags="S")
resp = sr1(pkt, timeout=1)

# python-nmap — Nmap 封装
import nmap
nm = nmap.PortScanner()
nm.scan('192.168.1.0/24', arguments='-sP')
```

---

### 08 — 综合实战（Ansible）

```
08comp/
├── add_users.yml              # Ansible Playbook：批量添加用户
├── user_pwd.yml               # 用户密码管理
├── pwd_file                   # 密码文件
├── ntp.yml                    # NTP 时间同步
├── ntp_hosts                  # NTP 主机列表
├── redis.yml                  # Redis 部署
├── redis_hosts                # Redis 主机列表
├── zabbix_agent.yml           # Zabbix Agent 部署
├── zabbix_hosts               # Zabbix 主机列表
├── mem_usage.sh               # 内存使用率检查脚本
└── weblb/                     # Web 负载均衡（HAProxy + Nginx）
    ├── weblb.yml              # 主 Playbook
    ├── weblb_hosts            # 主机清单
    └── roles/
        ├── nginx/
        │   ├── tasks/main.yml
        │   ├── vars/main.yml
        │   └── handlers/main.yml
        └── haproxy/
            ├── tasks/main.yml
            ├── defaults/main.yml
            ├── handlers/main.yml
            └── templates/haproxy.cfg.j2   # Jinja2 模板
```

**Ansible 核心概念：**

```yaml
# Playbook 基本结构
- hosts: webservers
  become: yes
  tasks:
    - name: Install Nginx
      yum: name=nginx state=present
    - name: Start Nginx
      service: name=nginx state=started enabled=yes
```

---

## 🔧 依赖安装

```bash
# 系统监控
pip install psutil watchdog pycurl apscheduler

# 文件操作
pip install pyyaml jinja2

# 批量管理
pip install paramiko fabric

# 网络工具
pip install python-nmap scapy

# 报表可视化
pip install matplotlib dash openpyxl

# Ansible（综合实战）
pip install ansible
```

## 🚀 快速开始

```bash
# 克隆仓库
git clone https://github.com/RM3836/auto-ops-course.git
cd auto-ops-course

# 示例：运行系统监控
python3 02sysmon/sysinfo_bypsutil.py

# 示例：运行文件监控
python3 02sysmon/fsmon_bywatchdog01.py /path/to/watch

# 示例：批量 SSH 执行
python3 06batch/paramiko_pwd.py

# 示例：启动 Dash 监控面板
python3 05report/sysinfo_bydash.py
# 访问 http://localhost:8050
```

---

## 📚 技术栈总结

```
Shell 脚本 ──→ Python 脚本 ──→ 第三方库 ──→ Ansible 自动化
   │              │              │              │
 基础运维      系统监控       批量管理       编排部署
 用户管理      文件操作       网络工具       配置管理
 定时任务      日志告警       报表可视       负载均衡
```

---

> **作者：YURM** | **GitHub: [RM3836](https://github.com/RM3836)** | **最后更新：2026-05-23**
