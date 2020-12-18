
<?php
try{
	$connect=new PDO("mysql:host=mysql.hostinger.fr;dbname=u604012333_lboun;charset=utf8","u604012333_lboun","56umQEklxoA8MUg5E1");


	$id_product_google = isset($_GET['id_product_google']) ? $_GET['id_product_google']:null;
	$price = isset($_GET['price']) ? $_GET['price']:null;
	$date_creation= date("Y-m-d H:i:s");
	$date_update = 	date("Y-m-d H:i:s");
	$id_product	= isset($_GET['id_product']) ? $_GET['id_product']:null;
	$reference	= isset($_GET['reference']) ? $_GET['reference']:null;
	
	$lastID_n_produit = $connect->query("SELECT id_product FROM product where id_product = '".$id_product."'");
	$rowID_n_produit=$lastID_n_produit->fetch();
	//$diff = date_diff()
	
	    $reponse = $connect->exec("INSERT INTO product(id_product_google,price,date_creation,date_update,id_product,reference) values ('".$id_product_google."','".$price."','".$date_creation."','".$date_update."','".$id_product."','".$reference."')");    
	//create table productUnique(id_product_google varchar(100) primary key)
	$reponse1 = $connect->exec("INSERT INTO productUnique(id_product_google,reference) values ('".$id_product_google."','".$reference."') ");
	

	//$connect->commit();
}catch(Exception $ex){
	echo ": ".$ex;
	//$connect->rollBack();
	
}
?>