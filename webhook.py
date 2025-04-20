from flask import Flask, request
import sqlite3
import os

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    if data.get("status") == "completed":
        numero = data.get("phone")
        montant = data.get("amount")

        # 🔒 Connexion à SQLite (inutile sur Render, mais on laisse pour structure locale)
        try:
            conn = sqlite3.connect("market.db")
            cursor = conn.cursor()
            cursor.execute("UPDATE vendeurs SET statut_pack = 'actif' WHERE contact = ?", (numero,))
            conn.commit()
            conn.close()
        except Exception as e:
            print("Erreur DB:", e)

        print(f"✅ Paiement reçu : {montant} FCFA de {numero}")
        return "Pack activé", 200

    print("❌ Paiement non validé :", data)
    return "Pas payé", 200

# ⛅ Partie nécessaire pour Render.com
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
