from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

# 加载环境变量
load_dotenv()

# 初始化Flask应用
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///contacts.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 设置调试模式
if os.getenv('FLASK_DEBUG', '').lower() == 'true':
    app.debug = True

# 初始化CORS以允许跨域请求
CORS(app)

# 初始化数据库
db = SQLAlchemy(app)

# 创建联系人模型
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20))
    email = db.Column(db.String(100))
    address = db.Column(db.String(200))
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'phone': self.phone,
            'email': self.email,
            'address': self.address
        }

# 创建数据库表
with app.app_context():
    db.create_all()

# API端点：获取所有联系人
@app.route('/api/contacts', methods=['GET'])
def get_contacts():
    contacts = Contact.query.all()
    return jsonify([contact.to_dict() for contact in contacts])

# API端点：创建新联系人
@app.route('/api/contacts', methods=['POST'])
def create_contact():
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({'error': 'Name is required'}), 400
    
    new_contact = Contact(
        name=data['name'],
        phone=data.get('phone', ''),
        email=data.get('email', ''),
        address=data.get('address', '')
    )
    
    db.session.add(new_contact)
    db.session.commit()
    
    return jsonify(new_contact.to_dict()), 201

# API端点：获取单个联系人
@app.route('/api/contacts/<int:contact_id>', methods=['GET'])
def get_contact(contact_id):
    contact = Contact.query.get_or_404(contact_id)
    return jsonify(contact.to_dict())

# API端点：更新联系人
@app.route('/api/contacts/<int:contact_id>', methods=['PUT'])
def update_contact(contact_id):
    contact = Contact.query.get_or_404(contact_id)
    data = request.get_json()
    
    if 'name' in data:
        contact.name = data['name']
    if 'phone' in data:
        contact.phone = data['phone']
    if 'email' in data:
        contact.email = data['email']
    if 'address' in data:
        contact.address = data['address']
    
    db.session.commit()
    
    return jsonify(contact.to_dict())

# API端点：删除联系人
@app.route('/api/contacts/<int:contact_id>', methods=['DELETE'])
def delete_contact(contact_id):
    contact = Contact.query.get_or_404(contact_id)
    db.session.delete(contact)
    db.session.commit()
    
    return jsonify({'message': 'Contact deleted successfully'}), 200

if __name__ == '__main__':
    app.run(host='localhost', port=5000)