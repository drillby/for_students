<?php
$servername = "dbs.spskladno.cz";
$username = "student22";
$password = "spsnet";
$dbname = "vyuka22";

$conn = mysqli_connect($servername, $username, $password, $dbname);
if (!$conn)
        die("Nepodařilo se navázat spojení se serverem. Zkuste to později.");