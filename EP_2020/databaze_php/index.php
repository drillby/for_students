<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php
        $servername = "dbs.spskladno.cz";
        $username = "student22";
        $password = "spsnet";
        $dbname = "vyuka22";

        $conn = mysqli_connect($servername, $username, $password, $dbname);

        if (!$conn)
            die("Nepodařilo se navázat spojení se serverem. Zkuste to později.");

        $sql = "SELECT * FROM Hrac";
        $result = mysqli_query($conn, $sql);

        if (mysqli_num_rows($result) > 0) {
            while ($row = mysqli_fetch_assoc($result)) {
                foreach($row as $zaznam){
                    ?>
                        <h1 style="color:red"><?php echo $zaznam ?></h1>
                    <?php
                    echo "<br>";
                }
                echo "<br>";
            }
        }
    ?>
</body>
</html>