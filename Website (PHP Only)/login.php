<?php
	class Login{
		function __construct(){
				if(!empty($_POST['username']) && !empty($_POST['password'])){
				
					$username = $_POST['username'];
					$password = $_POST['password'];
					
					require("database.php");
					$database = new Database();
					
					$data = $database->getdata($username,'username');
					
					if($data != false){
		
						$timestamp = date('Y-m-d H:i:s');
						
						foreach($data as $row){
							
							$nbrfailed = $row['failed_login'];
							$sercpass = $row['password_digest'];
							$sercsalt = $row['salt'];
						}
						
						$testpassword = md5($password.$sercsalt);
						
						if($sercpass == $testpassword){
							$data = $database->getdata('last_login',$timestamp,$username);
							$testpassword = "";
							echo "<script>alert('loggedin')</script>";
							
						}else{
							$nbrfailed++;
							$testpassword = "";
							$data = $database->getdata('failed_login',$nbrfailed,$username);
							require 'markups\index.html';
							$script = "<script>".
								  "document.getElementsByName('username')[0].setAttribute('value','$username');".
								  "document.getElementsByName('password')[0].setAttribute('value','$password');".
							      "document.getElementsByName('password')[0].style.background = 'rgba(255, 0, 0,0.1)';".
								  "document.getElementsByClassName('error')[1].style.display = 'block';".
								  "document.getElementsByClassName('info')[1].style.visibility = 'visible';".
								  "document.getElementsByClassName('info')[0].style.visibility = 'visible';".
							      "</script>";
							echo $script;
						}
						
					}else{
						require 'markups\index.html';
						$script = "<script>".
								  "document.getElementsByName('username')[0].setAttribute('value','$username');".
							      "document.getElementsByName('username')[0].style.background = 'rgba(255, 0, 0,0.1)';".
								  "document.getElementsByClassName('error')[0].style.display = 'block';".
								  "document.getElementsByClassName('info')[0].style.visibility = 'visible';".
							      "</script>";
						echo $script;
					}
					
			
				}
		}
		
	}
	
	if($_SERVER['REQUEST_METHOD'] == "POST"){	
		new Login();
	}else{
		require 'markups\index.html';
	}
?>