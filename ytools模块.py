"""
tool模块
作者:二级教授
编写完成于2024-02-02 21:36:05
"""
import os
import shutil
import warnings
import subprocess
import time

def mds(path):
    if os.path.exists(path):
        warnings.warn("文件夹已存在")
    else:
        os.makedirs(path)

def again(func, num=3):
    for _ in range(num):
        func()

def writetxt(content, filename="Yunfei"):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)

def yexit():
    input("按回车键退出")
    exit()

def writebit(data, filename="bit_data.bin"):
    with open(filename, 'wb') as file:
        file.write(data)

def cd(path):
    os.chdir(path)

def ifod(path):
    return os.path.exists(path)

def md(path):
    os.makedirs(path, exist_ok=True)

def shutdown_computer():
    if os.name == 'nt':  # Windows系统
        os.system('shutdown /s /t 0')
    else:  # Linux和macOS系统
        os.system('shutdown -h now')

from datetime import datetime

def copy_file(src, dest):
    try:
        shutil.copy(src, dest)
        print(f"文件从 {src} 成功复制到 {dest}")
    except IOError as e:
        print(f"无法复制文件. {e}")

def delete_file(path):
    if os.path.isfile(path):
        try:
            os.remove(path)
            print(f"文件 {path} 已被删除")
        except:
            print('错误:该文件可能异常或者只读')
    
def cmd(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    if process.returncode == 0:
        print("命令执行成功:", out.decode())
    else:
        print("命令执行失败:", err.decode())

def nowdir():
    return os.getcwd()

def list_dir(path='.'):
    items = os.listdir(path)
    for item in items:
        print(item)

def create_timestamped_backup(path, backup_dir="backups"):
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    base_name = os.path.basename(path)
    backup_path = os.path.join(backup_dir, f"{base_name}_{timestamp}")
    if os.path.isdir(path):
        shutil.copytree(path, backup_path)
    else:
        shutil.copy2(path, backup_path)
    print(f"备份已创建在 {backup_path}")

def nowtime():
    # 获取当前时间
    now = datetime.now()
    # 格式化时间显示
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    print("当前时间:", current_time)

def tt():
    # 获取当前时间戳
    timestamp = time.time()
    print("当前时间戳:", timestamp)

import math

class MathLib:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero is not allowed."

    @staticmethod
    def square(a):
        return a ** 2

    @staticmethod
    def square_root(a):
        if a >= 0:
            return a ** 0.5
        else:
            return "Error: Square root of negative number is not allowed."

    @staticmethod
    def sin(a):
        return math.sin(a)

    @staticmethod
    def cos(a):
        return math.cos(a)

    @staticmethod
    def tan(a):
        return math.tan(a)

    @staticmethod
    def log(a, base=math.e):
        if a > 0:
            return math.log(a, base)
        else:
            return "Error: Logarithm of non-positive number is not allowed."

    @staticmethod
    def exp(a):
        return math.exp(a)

import logging

def log(message, reason=None):
    logging.basicConfig(filename='app.log', filemode='a', format='%(asctime)s - %(message)s', level=logging.INFO)
    if reason:
        logging.info("Timestamp: %s. Reason: %s. Message: %s", datetime.now(), reason, message)
    else:
        logging.info("Timestamp: %s. Message: %s", datetime.now(), message)




def help():
    print("help:\n以下是这个模块中所有函数和类的帮助信息：")
    print("-" * 50)
    print("mds(path): 创建一个文件夹，如果文件夹已存在则给出警告。")
    print("again(func, num=3): 重复执行一个函数指定的次数。")
    print("writetxt(content, filename='Yunfei'): 将文本内容写入指定的文件。")
    print("yexit(): 退出程序前提示用户按回车键。")
    print("writebit(data, filename='bit_data.bin'): 将二进制数据写入指定的文件。")
    print("cd(path): 切换当前工作目录到指定路径。")
    print("ifod(path): 检查指定路径是否存在。")
    print("md(path): 创建文件夹，如果已存在则忽略。")
    print("shutdown_computer(): 关闭计算机。")
    print("copy_file(src, dest): 复制文件从源路径到目标路径。")
    print("delete_file(path): 删除指定路径的文件。")
    print("cmd(command): 执行指定的命令行命令。")
    print("nowdir(): 返回当前工作目录。")
    print("list_dir(path='.'): 列出指定路径下的所有文件和文件夹。")
    print("create_timestamped_backup(path, backup_dir='backups'): 为指定路径的文件或文件夹创建带有时间戳的备份。")
    print("nowtime(): 打印当前时间。")
    print("tt(): 打印当前时间戳。")
    print("MathLib类： 包含一些基本的数学运算方法，如加、减、乘、除、平方、平方根、正弦、余弦、正切、对数和指数等。")
    print("log(message, reason=None): 将消息和原因（如果有）记录到日志文件中。")
    print("-" * 50)
