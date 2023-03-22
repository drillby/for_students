<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="../style.css">
</head>
<body>
    <?php
    require "../conifg.php";
    require "../produkt_template.php";

    // upravit sql příkaz na výběr konkrétního produktu
    $sql = "SELECT * FROM Produkt";
    $result = mysqli_query($conn, $sql);
    ?>
</body>
</html>