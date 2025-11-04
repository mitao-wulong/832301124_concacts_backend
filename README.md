# 832301124_concacts_backend
# 学生通讯录管理系统 - 后端
项目信息
学号: [832301124]
姓名: [连泽政]
项目类型: 课程作业 - 前后端分离项目后端
# 技术栈: Python + Flask + SQLite/MySQL
# 项目简介
这是一个基于 Python Flask 框架开发的通讯录管理系统后端 API，提供完整的 RESTful 接口，支持联系人信息的增删改查操作。
🚀 快速开始
# 环境要求
Python 3.8+
Flask 2.0+
SQLite3（默认）或 MySQL 5.7+
# 项目结构
├── app.py                      # 应用入口文件
├── config.py                   # 配置文件
├── requirements.txt           # Python依赖包
├── init_db.py                 # 数据库初始化脚本
├── models/                    # 数据模型
│   ├── __init__.py
│   ├── contact.py             # 联系人模型
│   └── database.py            # 数据库连接
├── routes/                    # 路由模块
│   ├── __init__.py
│   ├── contacts.py            # 联系人路由
│   └── auth.py               # 认证路由（可选）
├── services/                 # 业务逻辑层
│   ├── __init__.py
│   └── contact_service.py    # 联系人服务
├── utils/                    # 工具函数
│   ├── __init__.py
│   ├── response.py           # 响应工具
│   └── validators.py         # 数据验证
├── tests/                    # 测试文件
│   ├── test_contacts.py
│   └── conftest.py
└── README.md
