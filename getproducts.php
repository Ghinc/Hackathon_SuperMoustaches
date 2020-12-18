

<?php
//$connect = new PDO('mysql:host=localhost;dbname=lvm;charset=utf8', 'root', '');
try{
	$connect=new PDO("mysql:host=mysql.hostinger.fr;dbname=u604012333_lboun;charset=utf8","u604012333_lboun","56umQEklxoA8MUg5E1");
}catch(Exception $ex){
echo ": ".$ex;
}

$reponse = $connect->query("SELECT * FROM product");

$don[] = $reponse->fetchAll(PDO::FETCH_ASSOC);
echo json_encode($don[0]);
?>