<?php
	class Register{
		function __construct(){
			
			$months_of_year = array(1 =>'January',2=>'February',3=>'March',4=>'April',5=>'May',6=>'June',7=>'July',8=>'August',9=>'September',10=>'October',11=>'November',12=>'December');
			
			$firstname = $_POST['firstname'];
			$lastname = $_POST['lastname'];
			
			if(isset($_POST['gender']) == false){
				$gender = '';
			}else{
				$gender = $_POST['gender'];
			}
			
			$dob = $_POST['year'] ."-". array_search($_POST['month'],$months_of_year) ."-".  $_POST['day'];
			
			$username = $_POST['username_2'];
			$email = $_POST['email'];
			
			$salt = mt_rand();
			$digest = $_POST['password_set'].$salt;
			
			$timestamp = date('Y-m-d H:i:s');
			$password = md5($digest);
			
			if($this->testdata('/^([^_\$\#\@!\^&\*\(\)\\\.,\'\"\|\d\%<>]+)$/',$firstname) && $this->testdata('/^([^_\$\#\@!\^&\*\(\)\\\.,\'\"\|\d\%<>]+)$/',$lastname) && $this->testdata('/^([^\-\$\#\@!\^\%&\*\(\)\\,\'\"\|<>\s\%]+)$/',$username) && $this->testdata('/^(([^\-\$\#\@!\^\%&\*\(\)\\,\'\"\|<>\s\/"]+))@(([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/',$email) && $this->testdata('/^(([[0-9]{4})-([0-9]{2})-([0-9]{2}))$/',$dob)){
				require("database.php");
				$database = new Database();
					
				$database->setrow([$firstname,$lastname,$gender,$dob,$username,$email,$password,$timestamp,0,$salt]);	
			}
			
			$pssword = $digest = $salt= "";
			
		}
		
	public function testdata($tester,$data){
			if(preg_match($tester,$data)){
				return true;
			}else{
				return false;
			}
		}
	}

	if($_SERVER['REQUEST_METHOD'] == "POST"){	
		new Register();
	}else{
		require 'markups\index.html';
		echo "<script>$('.tab').removeClass('active');$('.tab').eq(1).addClass('active');$('.form_pane').eq(0).removeClass('active_form');$('.form_pane').eq(1).addClass('active_form');$('#form_container').animate({height:'850px'});$('#create_account').fadeOut(0,function(){"."$('#create_account').css({visibility:'visible'});$('#create_account').toggle(1000);});</script>";
	}

?>