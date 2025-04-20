from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    if data.get("status") == "completed":
        numero = data.get("phone")
        montant = data.get("amount")

        conn = sqlite3.connect("market.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE vendeurs SET statut_pack = 'actif' WHERE contact = ?", (numero,))
        conn.commit()
        conn.close()

        return "Pack activé", 200
    return "Pas payé", 200

if __name__ == '__main__':
    app.run()
