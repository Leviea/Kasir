from flask import Flask, render_template, request, redirect, url_for
import mysql.connector


app = Flask(__name__)

db_config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'minimarket'
}

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/barang')
def barang():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM barang")
    data = cursor.fetchall()
    conn.close()
    return render_template('barang.html', barang=data)

@app.route('/tambah_barang', methods=['GET', 'POST'])
def tambah_barang():
    if request.method == 'POST':
        nama_barang = request.form['nama_barang']
        kategori = request.form['kategori']
        harga = request.form['harga']
        stok = request.form['stok']
        deskripsi = request.form['deskripsi']

        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO barang (nama_barang, kategori, harga, stok, deskripsi) VALUES (%s, %s, %s, %s, %s)",
                       (nama_barang, kategori, harga, stok, deskripsi))
        conn.commit()
        conn.close()
        return redirect(url_for('barang'))
    return render_template('tambah_barang.html')

@app.route('/detail_pesanan')
def detail_pesanan():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM detail_pesanan")
    data = cursor.fetchall()
    conn.close()
    return render_template('detail.html', detail_pesanan=data)

@app.route('/tambah_pesanan', methods=['GET', 'POST'])
def tambah_pesanan():
    if request.method == 'POST':
        id_barang = request.form['id_barang']
        jumlah = request.form['jumlah']
        total_harga = request.form['total_harga']
        tanggal_pesanan = request.form['tanggal_pesanan']

        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO detail_pesanan (id_barang, jumlah, total_harga, tanggal_pesanan) VALUES (%s, %s, %s, %s)",
                       (id_barang, jumlah, total_harga, tanggal_pesanan))
        conn.commit()
        conn.close()
        return redirect(url_for('detail_pesanan'))
    return render_template('tambah.html')

if __name__ == '__main__':
    app.run(debug=True)
