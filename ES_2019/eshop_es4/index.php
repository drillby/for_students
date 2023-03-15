<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <title>Document</title>
</head>
<body>
    <?php
    require "./conifg.php";
    require "./dlazdice.php";

    $conn = mysqli_connect($servername, $username, $password, $dbname);

    if (!$conn)
        die("Nepodařilo se navázat spojení se serverem. Zkuste to později.");

    $sql = "SELECT * FROM Produkt";
    $result = mysqli_query($conn, $sql);

    if (mysqli_num_rows($result) > 0) {
        while ($row = mysqli_fetch_assoc($result)) {
            zobrazDlazdici($row["nazev"], $row["cena"], $row["obrazek"], $row["mnozstvi"]);
        }
    }
    // příště zobrazit v tabukce/gridu
    ?>
</body>
</html>