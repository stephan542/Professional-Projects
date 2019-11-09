<?php
	class Database{
			private $data;
			private $db;
		
		public function __construct(){
			
			$hostname = $_SERVER['SERVER_NAME'];
			$user = "GrinchUWI";
			$pass = "stephan97";
			$dbname = "ServerDatabasesw00";
			$GLOBALS['db'] = new mysqli($hostname,$user,$pass,$dbname);

		}
		
		
		public function getdata($query,$field){
			$this->__construct();
			$sql = "SELECT * FROM users WHERE $field LIKE '$query';";
			$GLOBALS['data'] = $GLOBALS['db']->query($sql);
		
			
			if($GLOBALS['data'] == false || mysqli_num_rows($GLOBALS['data']) == 0){
				return false;
			}else{
				return $GLOBALS['data'];
			}
		}
		
		public function setdata($field,$data,$loc){
			$sql = "UPDATE users SET $field = '$data' WHERE username='$loc';";
			$GLOBALS['db']->query($sql);
		}
		
		public function setrow($para){
			$sql = "INSERT INTO users (firstname, lastname, gender ,dob, username, email, password_digest, last_login, failed_login, salt) VALUES ('$para[0]','$para[1]','$para[2]','$para[3]','$para[4]','$para[5]','$para[6]','$para[7]','$para[8]','$para[9]');";
			$data = $GLOBALS['db']->prepare($sql);
			$data->execute();
		}
		
		
	}

	if(isset($_GET['q']) && !empty($_GET['q'])){
		$q = $_GET['q'];
		$d = $_GET['d'];
		$db = new Database();
		$res =  $db->getdata($q,$d);
		if($res == false){
			echo "false";
		}else{
			echo "true";
		}
	}
?>