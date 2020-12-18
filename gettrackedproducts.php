

<?php

try{
	$connect=new PDO("mysql:host=mysql.hostinger.fr;dbname=u604012333_lboun;charset=utf8","u604012333_lboun","56umQEklxoA8MUg5E1");


	$id_product	= isset($_GET['id_product']) ? $_GET['id_product']:null;
	$reference	= isset($_GET['reference']) ? $_GET['reference']:null;
	
    $reponse = $connect->query("SELECT * FROM product where id_product_google = $reference or id_product = '$id_product'");

    $don[] = $reponse->fetchAll(PDO::FETCH_ASSOC);
    echo json_encode($don[0]);

}catch(Exception $ex){
    echo ": ".$ex;
}
?>