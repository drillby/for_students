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
	$username = "student17";
	$password = "spsnet";
	$dbname = "vyuka17";

	$conn = mysqli_connect($servername, $username, $password, $dbname);

	if (!$conn)
        die("Nepodařilo se navázat spojení se serverem. Zkuste to později.");
	//throw new Exception("Chybová hláška");	

	$sql = "SELECT * FROM Automobil";
    //$sql_insert = "INSERT INTO Automobil (...atributy) VALUES (...hodnoty)";
	$result = mysqli_query($conn, $sql);

	if (mysqli_num_rows($result) > 0) {
		while ($row = mysqli_fetch_assoc($result)) {
			echo $row;
            echo "<br>";
            echo $row["spz"];
            echo "<br>";
            echo $row["datum_vyroby"];
        }
	}
    ?>
</body>
</html>