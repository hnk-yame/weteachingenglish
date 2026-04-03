<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8">
  <title>Giriş Ekranı</title>
  <style>
    body {
      margin: 0;
      font-family: Arial, sans-serif;
      background: linear-gradient(135deg, #4facfe, #00f2fe);
      height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
    }

    .container {
      background: white;
      padding: 30px;
      border-radius: 15px;
      width: 300px;
      box-shadow: 0 10px 25px rgba(0,0,0,0.2);
      text-align: center;
    }

    h2 {
      margin-bottom: 20px;
    }

    input {
      width: 100%;
      padding: 10px;
      margin: 10px 0;
      border-radius: 8px;
      border: 1px solid #ccc;
      outline: none;
    }

    input:focus {
      border-color: #4facfe;
    }

    button {
      width: 100%;
      padding: 10px;
      background: #4facfe;
      border: none;
      color: white;
      border-radius: 8px;
      cursor: pointer;
      font-size: 16px;
    }

    button:hover {
      background: #3a8dde;
    }

    .footer {
      margin-top: 15px;
      font-size: 12px;
      color: #777;
    }
  </style>
</head>
<body>

  <div class="container">
    <h2>Giriş Yap</h2>
    <input type="text" placeholder="Kullanıcı adı">
    <input type="password" placeholder="Şifre">
    <button>Giriş</button>
    <div class="footer">© 2026</div>
  </div>

</body>
</html>
