from flask import Flask, render_template, request, redirect, url_for, session, flash
import json
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

# 商品データ
PRODUCTS = [
    {
        'id': 1,
        'name': 'ベーシック白Tシャツ',
        'price': 2980,
        'image': 'white-tshirt.jpg',
        'description': 'シンプルで着回しやすい定番の白Tシャツ',
        'sizes': ['S', 'M', 'L', 'XL']
    },
    {
        'id': 2,
        'name': 'ブラック Tシャツ',
        'price': 2980,
        'image': 'black-tshirt.jpg',
        'description': 'クールでスタイリッシュな黒Tシャツ',
        'sizes': ['S', 'M', 'L', 'XL']
    },
    {
        'id': 3,
        'name': 'グラフィック Tシャツ',
        'price': 3480,
        'image': 'graphic-tshirt.jpg',
        'description': 'オリジナルデザインのグラフィックTシャツ',
        'sizes': ['S', 'M', 'L', 'XL']
    },
    {
        'id': 4,
        'name': 'ストライプ Tシャツ',
        'price': 3280,
        'image': 'stripe-tshirt.jpg',
        'description': 'カジュアルなストライプ柄Tシャツ',
        'sizes': ['S', 'M', 'L', 'XL']
    }
]

def load_cart():
    """カートデータを読み込み"""
    if 'cart' not in session:
        session['cart'] = []
    return session['cart']

def save_cart(cart):
    """カートデータを保存"""
    session['cart'] = cart

@app.route('/')
def index():
    """トップページ"""
    return render_template('index.html', products=PRODUCTS)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    """商品詳細ページ"""
    product = next((p for p in PRODUCTS if p['id'] == product_id), None)
    if not product:
        flash('商品が見つかりません', 'error')
        return redirect(url_for('index'))
    return render_template('product_detail.html', product=product)

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    """カートに商品を追加"""
    product_id = int(request.form['product_id'])
    size = request.form['size']
    quantity = int(request.form.get('quantity', 1))
    
    product = next((p for p in PRODUCTS if p['id'] == product_id), None)
    if not product:
        flash('商品が見つかりません', 'error')
        return redirect(url_for('index'))
    
    cart = load_cart()
    
    # 既存のアイテムをチェック
    existing_item = next((item for item in cart if item['product_id'] == product_id and item['size'] == size), None)
    
    if existing_item:
        existing_item['quantity'] += quantity
    else:
        cart.append({
            'product_id': product_id,
            'name': product['name'],
            'price': product['price'],
            'size': size,
            'quantity': quantity,
            'image': product['image']
        })
    
    save_cart(cart)
    flash(f'{product["name"]} (サイズ: {size}) をカートに追加しました', 'success')
    return redirect(url_for('product_detail', product_id=product_id))

@app.route('/cart')
def cart():
    """カートページ"""
    cart_items = load_cart()
    total = sum(item['price'] * item['quantity'] for item in cart_items)
    return render_template('cart.html', cart_items=cart_items, total=total)

@app.route('/remove_from_cart/<int:index>')
def remove_from_cart(index):
    """カートから商品を削除"""
    cart = load_cart()
    if 0 <= index < len(cart):
        removed_item = cart.pop(index)
        save_cart(cart)
        flash(f'{removed_item["name"]} をカートから削除しました', 'info')
    return redirect(url_for('cart'))

@app.route('/checkout')
def checkout():
    """チェックアウトページ"""
    cart_items = load_cart()
    if not cart_items:
        flash('カートが空です', 'error')
        return redirect(url_for('cart'))
    
    total = sum(item['price'] * item['quantity'] for item in cart_items)
    return render_template('checkout.html', cart_items=cart_items, total=total)

@app.route('/order_complete', methods=['POST'])
def order_complete():
    """注文完了処理"""
    # 注文情報を取得
    customer_info = {
        'name': request.form['name'],
        'email': request.form['email'],
        'address': request.form['address'],
        'phone': request.form['phone']
    }
    
    cart_items = load_cart()
    total = sum(item['price'] * item['quantity'] for item in cart_items)
    
    # 実際のアプリケーションでは、ここでデータベースに注文を保存
    # 今回はセッションをクリア
    session['cart'] = []
    
    flash('ご注文ありがとうございました！', 'success')
    return render_template('order_complete.html', customer_info=customer_info, total=total)

if __name__ == '__main__':
    app.run(debug=True, port=5000)