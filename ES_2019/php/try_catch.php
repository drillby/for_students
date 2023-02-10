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
        $servername = "...";
        $username = "student17";
        $password = "spsnet";
        $dbname = "vyuka17";
    
    try {
        $conn = mysqli_connect($servername, $username, $password, $dbname);
    }
    catch (Exception $e){
        echo $e;
    }
    function FunctionName(int $var)
    {
        // ...
        throw new Exception("Chybová hláška");
    }
    ?>
</body>
</html>