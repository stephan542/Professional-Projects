<?php


?>
<html>

<head>
	<meta charset="utf-8">
	<title>Login Website</title>
	<link href="https://fonts.googleapis.com/css?family=Raleway|Roboto+Condensed" rel="stylesheet">
	<link href="styles/style.css" rel="stylesheet" type="text/css">
	<script src="https://code.jquery.com/jquery-3.1.1.min.js" type="text/javascript"></script>
	<script src="scripts/jquery-3.1.1.min.js" type="text/javascript"></script>
</head>
<body>
	<div id="banner_container">
		<div id="top_banner">
			
		</div>
	</div>
	<div id="content_container">
		<div id="form_container">
			<table id="tab_group">
				<tbody>
					<tr>
						<td class="tab active">Log In</td>
						<td class="tab">Register</td>	
					</tr>
				</tbody>
			</table>
			<div class="form_pane active_form">
				<form id="login_form">
					<table id="login_info">
						<tbody>
							<tr>
								<td id="welcome_q" class="input_field"><h1>Welcome?</h1></td>
							</tr>
							<tr>
								<td class="input_field"><input placeholder="Email" type="text" name="username" class="input_box"></td>
							</tr>
							<tr>
								<td class="input_field2"><span class="info">Email Address</span><span class="error"><img src="images/error.png" alt="Error">Invalid Email Address</span><span class="sucess"><img src="images/sucess.png" alt="Success"></span></td>
							</tr>
							<tr>
								<td class="input_field"><input placeholder="Password" type="text" name="username" class="input_box"></td>
							</tr>
							<tr>
								<td class="input_field2"><span class="info">Password</span><span class="error"><img src="images/error.png" alt="Error">Invalid Password</span><span class="sucess"><img src="images/sucess.png" alt="Success"></span></td>
							</tr>
							<tr>
								<td class="input_field"><input type="submit" disabled="disabled" value="Login In" class="submit_btn"></td>
							</tr>
							<tr>
								<td class="input_field2"></td>
							</tr>
							<tr>
								<td class="input_field2 spec"><a href="" class="spec">Forgot Password?</a></td>
							</tr>
						</tbody>
					</table>
				</form>
			</div>
			<div class="form_pane">
				<form id="signup_form" onSubmit="return Validate_form(1)">
					<table id="signup_info">
						<tbody>
							<tr>
								<td id="create_account" class="input_field"><h1>Create an Account</h1></td>
							</tr>
							<tr>
								<td class="input_field3"><strong>Name</strong></td>
							</tr>
							<tr>
								<td class="input_field3"><input placeholder="First name" type="text" name="firstname" onKeyUp="validate_name()" class="input_box sml"><input placeholder="Last name" type="text" name="lastname" onKeyUp="validate_name();" class="input_box sml"></td>
							</tr>
							<tr>
								<td class="input_field2"><span class="error"><img src="images/error.png" alt="Error"><strong>Invalid First Name</strong></span><span class="sucess"><img src="images/sucess.png" alt="Success"><strong>Valid</strong></span><span class="error spec2"><img src="images/error.png" alt="Error"><strong>Invalid Last Name</strong></span><span class="sucess spec2 spec8"><img src="images/sucess.png" alt="Success"><strong>Valid</strong></span></td>
							</tr>
							<tr>
								<td class="input_field3"><strong>Gender</strong><input class="spec4" name="gender" type="checkbox" value="male" > Male <input class="spec4" name="gender" type="checkbox" value="female" > Female &#9;<span class="spec6 spec2">(optional)</span></td>
							</tr>
							<tr>
								<td class="input_field3"><strong>Date of Birth</strong>
								<select name="month" class="dob" onChange="validate_dob_day()"><option disabled="disabled" selected="selected">Month</option><option>January</option><option>February</option><option>March</option><option>April</option><option>May</option><option>June</option><option>July</option><option>August</option><option>September</option><option>October</option><option>November</option><option>December</option></select><input placeholder="Day" class="dob spec5" type="number" name="day" min="1" max="31" onKeyUp="validate_dob_day()"><input class="dob spec5" placeholder="Year" type="number" name="year" min="1500" max="2018" onKeyUp="validate_dob_year()">
								</td>
							</tr>
							<tr>
								<td class="input_field2"><span class="error"><img src="images/error.png" alt="Error"><strong>Invalid Date of Birth</strong></span><span class="sucess"><img src="images/sucess.png" alt="Success"><strong>Valid</strong></span></td>
							</tr>
							<tr>
								<td class="input_field3"><strong>Create a Username</strong></td>
							</tr>
							<tr>
								<td class="input_field3"><input placeholder="User name" type="text" name="username_2" onKeyUp="validate_username()" class="input_box spec3"></td>
							</tr>
							<tr>
								<td class="input_field2"><span class="error"><img src="images/error.png" alt="Error"><strong>Invalid Username</strong></span><span class="error_server">Username already taken</span><span class="sucess"><img src="images/sucess.png" alt="Success"><strong>Valid</strong></span></td>
							</tr>
							<tr>
								<td class="input_field3"><strong>Email</strong></td>
							</tr>
							<tr>
								<td class="input_field3"><input placeholder="Email Address (optional)" type="text" name="email" onKeyUp="validate_email()" class="input_box spec3"></td>
							</tr>
							<tr>
								<td class="input_field2"><span class="error"><img src="images/error.png" alt="Error"><strong>Invalid Email</strong></span><span class="sucess"><img src="images/sucess.png" alt="Success"><strong>Valid</strong></span></td>
							</tr>
							<tr>
								<td class="input_field3"><strong>Create a Password</strong></td>
							</tr>
							<tr>
								<td class="input_field3"><input placeholder="Password" type="password" name="password_set" onKeyUp="validate_password()" class="input_box spec3"></td>
							</tr>
							<tr>
								<td class="input_field2"><span class="pass_stat"><hr></span><span class="error"><img src="images/error.png" alt="Error"><strong>Invalid Password.Must have a least 8 characters which includes at least one uppercase letter ,a digit and a symbol.</strong></span><span class="sucess"><img src="images/sucess.png" alt="Success"><strong>Valid</strong></span></td>
							</tr>
							<tr>
								<td class="input_field3"><strong>Confirm Password</strong></td>
							</tr>
							<tr>
								<td class="input_field3"><input placeholder="Re-type Password" type="password" disabled name="conf_pass" onKeyUp="confirm_password()" class="input_box spec3"></td>
							</tr>
							<tr>
								<td class="input_field2"><span class="error"><img src="images/error.png" alt="Error"><strong>Password does not match.</strong></span><span class="sucess"><img src="images/sucess.png" alt="Success"><strong>Valid</strong></span></td>
							</tr>
							<tr>
								<td class="input_field3" ><input type="checkbox" name="terms" value="agree"><strong id="terms_agree">I agree to the <a href="" id="">Tems and Services</a>.</strong></td>
							</tr>
							<tr>
								<td class="input_field"><input type="submit" value="Sign Up" class="submit_btn spec7"></td>
							</tr>
						</tbody>
					</table>
				</form>
			</div>
		</div>
		<div id="opening" class="slide"></div>
	</div>
	<script src="scripts/script.js" type="text/javascript"></script>
</body>
</html>