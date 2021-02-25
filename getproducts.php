

<?php
//$connect = new PDO('mysql:host=localhost;dbname=lvm;charset=utf8', 'root', '');
try{
	$connect=new PDO("mysql:host=localhost;dbname=pro;charset=utf8","root","");
}catch(Exception $ex){
echo ": ".$ex;
}

$reponse = $connect->query("SELECT * FROM product");

$don[] = $reponse->fetchAll(PDO::FETCH_ASSOC);
echo json_encode($don[0]);
?>