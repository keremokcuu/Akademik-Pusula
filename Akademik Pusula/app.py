from flask import Flask, render_template, request
import sqlite3
from datetime import datetime

app = Flask(__name__)

def db_query(query, params=()):
    conn = sqlite3.connect('firsat_pusulasi.db')
    cursor = conn.cursor()
    cursor.execute(query, params)
    data = cursor.fetchall()
    conn.close()
    return data

@app.route('/', methods=['GET', 'POST'])
def index():
    all_opps = db_query("SELECT * FROM opportunities")
    
    # Kullanıcı arama yaptıysa onu göster
    if request.method == 'POST':
        user_tags = request.form.get('user_tags', '')
        if user_tags:
            all_opps = [row for row in all_opps if any(user_tags.lower() in str(cell).lower() for cell in row)]
    else:
        # Arama yapılmadıysa: Sadece son 10 günü kalan veya yaklaşan kritik ilanları (veya ilk 8 popüler ilanı) filtreleyelim
        today = datetime.strptime('2026-09-27', '%Y-%m-%d')
        kritik_opps = []
        for opp in all_opps:
            try:
                deadline = datetime.strptime(opp[3], '%Y-%m-%d')
                diff = (deadline - today).days
                if 0 <= diff <= 15:  # 15 gün içinde süresi bitecekler
                    kritik_opps.append(opp)
            except:
                pass
        
        # Eğer kritik ilan sayısı azsa, ana sayfa boş kalmasın diye en azından ilk 6-8 ilanı basalım
        if len(kritik_opps) >= 4:
            all_opps = kritik_opps[:8]
        else:
            all_opps = all_opps[:8]
            
    return render_template('index.html', all_opps=all_opps, active='home')

@app.route('/tum-firsatlar')
def tum_firsatlar():
    opps = db_query("SELECT * FROM opportunities")
    return render_template('kategori.html', title="Tüm İlanlar", opps=opps, active='tum')

@app.route('/stajlar')
def stajlar():
    search = request.args.get('search', '').lower()
    bolum = request.args.get('bolum', '').lower()
    
    all_opps = db_query("SELECT * FROM opportunities")
    opps = [row for row in all_opps if 'staj' in str(row[2]).lower() or 'staj' in str(row[1]).lower() or 'staj' in str(row[5]).lower()]
    
    if search:
        opps = [row for row in opps if any(search in str(cell).lower() for cell in row)]
    if bolum and bolum != 'tümü':
        opps = [row for row in opps if bolum in str(row[5]).lower() or bolum in str(row[1]).lower() or bolum in str(row[6]).lower()]
        
    return render_template('kategori.html', title="Staj Programları", opps=opps, active='staj', search_val=search, selected_bolum=bolum)

@app.route('/burslar')
def burslar():
    all_opps = db_query("SELECT * FROM opportunities")
    opps = [row for row in all_opps if any('burs' in str(cell).lower() for cell in row)]
    return render_template('kategori.html', title="Burs Programları", opps=opps, active='burs')

@app.route('/teknofest')
def teknofest():
    all_opps = db_query("SELECT * FROM opportunities")
    opps = [row for row in all_opps if any(keyword in str(cell).lower() for cell in row for keyword in ['teknofest', 'yarışma', 'proje', 'tubitak', 'tübitak'])]
    return render_template('kategori.html', title="TEKNOFEST & Projeler", opps=opps, active='tekno')

@app.route('/etkinlikler')
def etkinlikler():
    events = db_query("SELECT * FROM events")
    return render_template('etkinlikler.html', events=events, active='events')

@app.route('/kaydedilenler')
def kaydedilenler():
    return render_template('kaydedilenler.html', active='saved')

if __name__ == '__main__':
    app.run(debug=True)