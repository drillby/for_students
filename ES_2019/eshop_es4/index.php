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

    $sql = "SELECT * FROM Produkt";
    $result = mysqli_query($conn, $sql);

    if (mysqli_num_rows($result) > 0) {
        $pocet_produktu = 0;
        ?>
        <table>
            <tr>
        <?php
        while ($row = mysqli_fetch_assoc($result)) {
            $pocet_produktu = $pocet_produktu + 1;
            if ($pocet_produktu % 4 == 0){
                ?>
                </tr>
                <tr>
                <?php
            }
            ?>
            <td>
                <?php zobrazDlazdici($row["nazev"], $row["cena"], $row["obrazek"], $row["mnozstvi"]); ?>
            </td>
            <?php
        }
        ?>
            </tr>
        </table>
        <?php
    }
    // příště zobrazit v tabukce/gridu
    ?>
</body>
</html>