# 后端代码风格指南
（https://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/python_language_rules.html）
# 1. 代码布局
缩进: 4个空格，不要用Tab
行长度: 不超过79字符
空行:
函数/类之间：2个空行
方法之间：1个空行
import os
from flask import Flask


class ContactService:
    
    def get_contacts(self):
        pass
    
    def create_contact(self, data):
        pass


def main():
    app = create_app()
    app.run()
# 2. 命名规范
# 变量/函数 - 蛇形命名
contact_list = []
current_page = 1

def get_user_by_id(user_id):
    pass

# 常量 - 全大写
API_BASE_URL = "http://api.example.com"
MAX_SIZE = 100

# 类 - 帕斯卡命名
class ContactService:
    pass
# 3. 导入顺序
# 1. 标准库
import os
import sys

# 2. 第三方库
from flask import Flask, request

# 3. 本地模块
from models.contact import Contact
# 4. 字符串规范
# 一般用单引号
name = '张三'

# f-string格式化（推荐）
message = f"姓名: {name}, 年龄: {age}"

# 多行用三引号
text = """
第一行
第二行
"""
# 5. 函数设计
def create_contact(name, phone, email=None):
    """
    创建联系人
    
    Args:
        name: 姓名
        phone: 手机号
        email: 邮箱(可选)
    """
    if not name or not phone:
        raise ValueError("姓名和手机号必填")
    
    return Contact(name=name, phone=phone, email=email)
# 6. 异常处理
try:
    result = some_operation()
except ValueError as e:
    print(f"参数错误: {e}")
except Exception as e:
    print(f"未知错误: {e}")
else:
    print("操作成功")
finally:
    print("清理资源")
# 7. 类型提示
from typing import List, Optional

def get_contacts(page: int = 1) -> List[dict]:
    """获取联系人列表"""
    pass

def find_contact(id: int) -> Optional[dict]:
    """查找联系人"""
    pass
# 8. 注释规范
def calculate_total(items):
    """计算商品总价"""
    # 计算小计
    subtotal = sum(item.price for item in items)
    
    # 添加税费
    tax = subtotal * 0.1
    return subtotal + tax
# 9. Flask 特定规范
from flask import Blueprint

contacts_bp = Blueprint('contacts', __name__)

@contacts_bp.route('/contacts', methods=['GET'])
def get_contacts():
    """获取联系人列表API"""
    page = request.args.get('page', 1, type=int)
    contacts = ContactService.get_contacts(page)
    return jsonify(contacts)

