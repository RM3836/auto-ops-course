#!/bin/bash
# Java安装包文件
java_tar="jdk-17_linux-x64_bin.tar.gz"
 
# 检查已配置的Java环境变量并进行处理
function checkJavaEnv (){
  java_env1=$(grep -n "export JAVA_HOME=.*" /etc/profile | cut -f1 -d':')
  if [ -n "$java_env1" ];then
    echo "删除已配置的JAVA_HOME环境变量"
    sed -i "${java_env1}d" /etc/profile
  fi
  java_env2=$(grep -n "export JRE_HOME=.*" /etc/profile | cut -f1 -d':')
    if [ -n "$java_env2" ];then
        echo "删除已配置的JRE_HOME环境"
        sed -i "${java_env2}d" /etc/profile
    fi   
  java_env3=$(grep -n "export CLASSPATH=.*" /etc/profile | cut -f1 -d':')
    if [ -n "$java_env3" ];then
        echo "删除已配置的CLASSPATH环境变量"
        sed -i "${java_env3}d" /etc/profile
    fi
  java_env4=$(grep -n "export PATH=.*\${JAVA_HOME}.*" /etc/profile | cut -f1 -d':')
    if [ -n "$java_env4" ];then
        echo "删除已配置的JAVA路径"
        sed -i "${java_env4}d" /etc/profile
    fi
} 
# 创建Java安装目录
mkdir -p /usr/lib/jvm
echo "正在解压Java压缩包..."
tar -zxvf ${java_tar} -C /usr/lib/jvm
if [ -e "/usr/lib/jvm/java-17-oracle" ];then
 echo "存在该文件夹，删除..."
 rm -rf /usr/lib/jvm/java-17-oracle
fi

# 修改Java版本的目录名
mv /usr/lib/jvm/jdk-17.0.2 /usr/lib/jvm/java-17-oracle
# 检查环境变量配置并进行处理
checkJavaEnv 
echo "正在配置Java环境变量..."
sed -i '$a export JAVA_HOME=/usr/lib/jvm/java-17-oracle' /etc/profile
sed -i '$a export JRE_HOME=${JAVA_HOME}/jre' /etc/profile
sed -i '$a export CLASSPATH=.:${JAVA_HOME}/lib:${JRE_HOME}/lib' /etc/profile
sed -i '$a export PATH=${JAVA_HOME}/bin:$PATH' /etc/profile
echo "重新加载配置文件使环境变量生效"
source /etc/profile
echo "---------------------------------"
echo "检查当前的Java版本以测试安装："
java -version

