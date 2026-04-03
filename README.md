# weteachingenglish
in this site we are teaching some english and you can learn with games
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Benim Sitem</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: Arial, sans-serif;
        }

        body {
            background: #f5f5f5;
        }

        header {
            background: #222;
            color: white;
            padding: 15px 30px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        nav a {
            color: white;
            margin-left: 20px;
            text-decoration: none;
        }

        nav a:hover {
            color: #00adb5;
        }

        .hero {
            height: 300px;
            background: linear-gradient(135deg, #00adb5, #393e46);
            color: white;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-direction: column;
            text-align: center;
        }

        .hero h1 {
            font-size: 40px;
        }

        .hero p {
            margin-top: 10px;
        }

        .content {
            padding: 40px;
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
        }

        .card {
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        }

        footer {
            background: #222;
            color: white;
            text-align: center;
            padding: 15px;
            margin-top: 20px;
        }
    </style>
</head>
<body>

<header>
    <h2>Benim Sitem</h2>
    <nav>
        <a href="#">Ana Sayfa</a>
        <a href="#">Hakkında</a>
        <a href="#">İletişim</a>
    </nav>
</header>

<section class="hero">
    <h1>Hoş Geldin!</h1>
    <p>Bu benim ilk web sitem 🚀</p>
</section>

<section class="content">
    <div class="card">
        <h3>Başlık 1</h3>
        <p>Buraya içerik yazabilirsin.</p>
    </div>
    <div class="card">
        <h3>Başlık 2</h3>
        <p>Buraya içerik yazabilirsin.</p>
    </div>
    <div class="card">
        <h3>Başlık 3</h3>
        <p>Buraya içerik yazabilirsin.</p>
    </div>
</section>

<footer>
    <p>© 2026 Tüm Hakları Saklıdır</p>
</footer>

</body>
</html>
