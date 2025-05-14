const express = require('express');
const bodyParser = require('body-parser');
const app = express();
const port = process.env.PORT || 3000;

app.use(bodyParser.json());

// Route callback IPN de PayDunya
app.post('/paydunya-callback', (req, res) => {
  const paiement = req.body;

  console.log("Notification PayDunya reçue :", paiement);

  if (paiement.status === 'completed') {
    // Tu peux ici appeler Supabase pour valider le paiement
    console.log("Paiement réussi pour :", paiement.invoice_token);
  }

  res.sendStatus(200); // Important pour PayDunya
});

app.get('/', (req, res) => {
  res.send("Mini backend PayDunya actif !");
});

app.listen(port, () => {
  console.log(`Serveur en ligne sur le port ${port}`);
});