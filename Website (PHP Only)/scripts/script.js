// JavaScript Document
var tabs,welcome_sign,form,create_a,signin,login_form;
var errors,sucesss,gender,info,submit_button,terms_agree;


$(document).ready(function(){      //document.onload
	tabs = $('.tab');
	form = $('.form_pane');
	welcome_sign = $('#welcome_q');
	create_a = $('#create_account');
	errors = $('.error');
	sucesss = $('.sucess');
	info = $('.info');
	gender = $("input[name='gender']");
	terms_agree = $("input[name='terms']");
	submit_button = $(".submit_btn");
	signin = $(".signin");
	login_form = $('#login_form');
	
	welcome_sign.fadeOut(0,function(){welcome_sign.css({visibility:'visible'});welcome_sign.toggle(1000);});
	
	setTimeout(function(){slideshow();},1000);	
	
	tabs.on('click',function(){
		if($(this).hasClass("active") === false || $(this).hasClass("hid")  ){
			
			tabs.removeClass("active");
			$(this).addClass("active");
			
			if(tabs.eq(0).hasClass("hid")){
				$('#forgot_password').fadeOut(0);
				$('#login_form').fadeIn(500);
			}
			

			if(form.eq(0).hasClass("active_form") && $(this).hasClass("hid") === false){
				tabs.removeClass("hid");
				form.eq(0).removeClass("active_form");
				form.eq(1).addClass("active_form");
				$('#form_container').animate({height:getnw_height()});
				create_a.fadeOut(0,function(){create_a.css({visibility:'visible'});create_a.toggle(1000);});
			}else{
				form.eq(1).removeClass("active_form");
				form.eq(0).addClass("active_form");
				$('#form_container').animate({height:'450px'},1000,"linear");
				welcome_sign.fadeOut(0,function(){welcome_sign.css({visibility:'visible'});welcome_sign.toggle(1000);});
			}
			tabs.removeClass("hid");
		}
    });
	
	signin.keyup(function(){
		var e = signin.index($(this));
		if($(this).val() === ""){
			sucesss.eq(e).css({visibility:'hidden'});
			errors.eq(e).css({visibility:'hidden'});
			$(this).css({backgroundColor:"white"});
		}else if($(this).val() !== ""){
			errors.eq(e).css({visibility:'hidden'});
			$(this).css({backgroundColor:"white"});
		}else{
			errors.eq(e).css({visibility:'visible'});
			$(this).css({backgroundColor:"rgba(255, 0, 0,0.1)"});
		}
	});
	
	submit_button.eq(0).hover(function(){
		if(Validate_login() === true){
			submit_button.addClass("spec0");
		}else{
			submit_button.removeClass("spec0");
		}
		
	});
	
	submit_button.eq(1).hover(function(){
		if(Validate_form(0) === true){
			submit_button.addClass("spec9");
		}else{
			submit_button.removeClass("spec9");
		}
		
	});
	
	gender.on("click",function(){
		if($(this).prop("checked") === true){
			if($(this).val() === "male"){
				gender.eq(1).prop("checked",false);
			}else{
				gender.eq(0).prop("checked",false);
		 }
		}
	});
	
	terms_agree.on("click",function(){
		$("#terms_agree").css({color:"black"});
	});
	
	$('#frg_pass').on("click",function(){
		tabs.eq(0).addClass('hid');
		$('#login_form').slideUp(500);
		$('#forgot_password').slideDown(500);
	});
	
	document.getElementsByName("username")[0].onkeyup = function(){
		if(document.getElementsByName("username")[0].value !== ""){
			info.eq(0).css({transition:"1.2s ease",visibility:"visible"});
		}else{
			info.eq(0).css({transition:"0.1s ease",visibility:"hidden"});
		}
	};
	
	document.getElementsByName("password")[0].onkeyup = function(){
		if(document.getElementsByName("password")[0].value !== ""){
			info.eq(1).css({transition:"1.2s ease",visibility:"visible"});
		}else{
			info.eq(1).css({transition:"0.1s ease",visibility:"hidden"});
		}
	};
	
	document.getElementsByName("month")[0].onclick = function(){
		document.getElementsByName("month")[0].style.background = "white";
	};
	
	document.getElementsByName("day")[0].onclick = function(){
		if(["February"].indexOf(document.getElementsByName("month")[0].value) >=0 ){
			document.getElementsByName("day")[0].setAttribute("max",28);
		}else{
			if(["September","April","June","November"].indexOf(document.getElementsByName("month")[0].value)>=0){
				document.getElementsByName("day")[0].setAttribute("max",30);
			}else{
				document.getElementsByName("day")[0].setAttribute("max",31);
			}
		}
	};
	
});

function slideshow(){
	var backgrounds = ["../Website/images/autumn_bench.jpg","../Website/images/summer_snacks.jpg","../Website/images/winter_lights.jpg","../Website/images/spring_trees.jpg"];
	var open_con = document.getElementById("opening");
	
	
	open_con.style.background = "url("+backgrounds[Math.floor(Math.random()*backgrounds.length)]+")";
	open_con.style.backgroundPosition = "center";
	open_con.style.backgroundSize = "cover";
	
	setTimeout(function(){slideshow();},4000);
}

function confirm_password(){
	var pass_1 = $("input[name='password_set']");
	var pass_2 = $("input[name='conf_pass']");
	
	if(pass_2.val() === ""){
		sucesss.eq(8).fadeOut(0);
		errors.eq(8).fadeOut(0);
		pass_2.css({backgroundColor:"white"});
	}else if(pass_2.val() === pass_1.val()){
		sucesss.eq(8).fadeIn();
		errors.eq(8).fadeOut(0);
		pass_2.css({backgroundColor:"white"});
	}else{
		sucesss.eq(8).fadeOut(0);
		errors.eq(8).fadeIn();
		pass_2.css({backgroundColor:"rgba(255, 0, 0,0.1)"});
	}
	
	$('#form_container').css({height:getnw_height()});
	setTimeout(function(){$('#form_container').css({height:getnw_height()});},500);
}

function validate_password(){
	var password = $("input[name='password_set']");
	var progress = 0;
	var testers = [/^(?=.*[A-Z])([A-zaz\d\-\$\#\@!\^\%&\*\(\)\\,\'\"\|<>\s\/"]{1,})$/,/^(?=.*\d)([A-zaz\d\-\$\#\@!\^\%&\*\(\)\\,\'\"\|<>\s\/"]{1,})$/,/^(?=.*[\-\$\#\@!\^\%&\*\(\)\\,\'\"\|<>\s\/"])([A-zaz\d\-\$\#\@!\^\%&\*\(\)\\,\'\"\|<>\s\/"]{1,})$/, /^(?=.*[\-\$\#\@!\^\%&\*\(\)\\,\'\"\|<>\s\/"])(?=.*\d)(?=.*[A-Z])([A-zaz\d\-\$\#\@!\^\%&\*\(\)\\,\'\"\|<>\s\/"]{8,})$/];
	
	if(password.val() === ""){
		sucesss.eq(7).fadeOut(0);
		errors.eq(7).fadeOut(0);
		password.css({backgroundColor:"white"});
		$("input[name='conf_pass']").prop("disabled",true);
	}else{
		
		if(testers[0].test(password.val())){progress++;}
		if(testers[1].test(password.val())){progress++;}
		if(testers[2].test(password.val())){progress++;}
		
		if(testers[3].test(password.val())){
			progress++;
			sucesss.eq(7).fadeIn();
			errors.eq(7).fadeOut(0);
			$("input[name='conf_pass']").prop("disabled",false);
			password.css({backgroundColor:"white"});
		}else{
			sucesss.eq(7).fadeOut(0);
			errors.eq(7).fadeIn();
			password.css({backgroundColor:"rgba(255, 0, 0,0.1)"});
			$("input[name='conf_pass']").prop("disabled",true);
		}
	}
	
	progress = progress * 25;
	
	var temp = progress+"%";
	if(progress<50){
		$(".pass_stat hr").css({backgroundColor:"lightcoral",width:temp});
	}else if(progress === 100){
		$(".pass_stat hr").css({backgroundColor:"lawngreen",width:temp});
	}else{
		$(".pass_stat hr").css({backgroundColor:"rgb(208,123,29)",width:temp});
	}
	
	$('#form_container').css({height:getnw_height()});
	setTimeout(function(){$('#form_container').css({height:getnw_height()});},500);
	
}

function check_for_email(){
	var tester= /^(([^\-\$\#\@!\^\%&\*\(\)\\,\'\"\|<>\s\/"]+))@(([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
	var data = $("input[name='email_check']");
	
}


function validate_email(){
	validate_data($("input[name='email']"),/^(([^\-\$\#\@!\^\%&\*\(\)\\,\'\"\|<>\s\/"]+))@(([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/,6,6,"email");
}
function validate_username(){
	validate_data($("input[name='username_2']"),/^([^\-\$\#\@!\^\%&\*\(\)\\,\'\"\|<>\s\%]+)$/,5,5,"username");
}

function validate_data(data,tester,e,s,f){
	 var results = $.ajax({
        type: "GET",
        data:{q:data.val(),d:f},
        url: 'database.php',
        cache:false,
	 });
	
	results.done(
			function(r){
				if(data.val() === ""){
					sucesss.eq(s).fadeOut(0);
					errors.eq(e).fadeOut(0);
					data.css({backgroundColor:"white"});
				}else if(tester.test(data.val()) && r === "false"){
					sucesss.eq(s).fadeIn();
					errors.eq(e).fadeOut(0);
					data.css({backgroundColor:"white"});
				}else{
					errors.eq(e).fadeIn();
					data.css({backgroundColor:"rgba(255, 0, 0,0.1)"});
					sucesss.eq(s).fadeOut(0);
				}

				$('#form_container').css({height:getnw_height()});
				setTimeout(function(){$('#form_container').css({height:getnw_height()});},500);
	
			});
}

function validate_dob_day(){
	validate_dob($("input[name='day']"));
}
function validate_dob_year(){
	validate_dob($("input[name='year']"));
}

function validate_dob(dat){
	if(dat.val() === ""){
		sucesss.eq(4).fadeOut(0);
		errors.eq(4).fadeOut(0);
		dat.css({backgroundColor:"white"});
	}else if(parseInt(dat.val()) >= (parseInt(dat.attr("max"))+1) || parseInt(dat.val()) <= parseInt(dat.attr("min"))-1){
		dat.css({backgroundColor:"rgba(255, 0, 0,0.1)"});
		errors.eq(4).fadeIn();
		sucesss.eq(4).fadeOut(0);
	}else{
		dat.css({backgroundColor:"white"});	
		if($("input[name='year']").val() !== "" && $("input[name='day']").val() !== "" && $("select[name='month']").val() !== null){
			sucesss.eq(4).fadeIn();
		}
		errors.eq(4).fadeOut(0);
	}
	
	$('#form_container').css({height:getnw_height()});
	setTimeout(function(){$('#form_container').css({height:getnw_height()});},500);
}

function validate_name(){
	  var nametester = /^([^_\$\#\@!\^&\*\(\)\\\.,\'\"\|\d\%<>]+)$/;
	  var fields = ["firstname","lastname"];
	  var fieldindex = [2,3];
	  var input;
	  for(var x=0;x<fields.length;x++){
		  input = document.getElementsByName(fields[x])[0].value;
		  if(input !== ""){

				if(nametester.test(input)){	
					errors.eq(fieldindex[x]).fadeOut(0);
					document.getElementsByName(fields[x])[0].style.background = "white";
					sucesss.eq(fieldindex[x]).fadeIn();
				}else{
					errors.eq(fieldindex[x]).fadeIn();
					document.getElementsByName(fields[x])[0].style.background = "rgba(255, 0, 0,0.1)";
					sucesss.eq(fieldindex[x]).fadeOut(0);
				}
		  }else{
					errors.eq(fieldindex[x]).fadeOut(0);
					sucesss.eq(fieldindex[x]).fadeOut(0);
			  		document.getElementsByName(fields[x])[0].style.background = "white";
		  }
		}
	
	$('#form_container').css({height:getnw_height()});
	setTimeout(function(){$('#form_container').css({height:getnw_height()});},500);
}

function getnw_height(){
		if(tabs.eq(0).hasClass('hid') === false){
			var count =0;
			var temp;
			var specialerrors = [3];
			for(var x=0;x<errors.length;x++){
				if(errors.eq(x).css("display") === "block" || sucesss.eq(x).css("display") === "block"){
					for(var i=0;i<specialerrors.length;i++){
						if(x === specialerrors[i] && (errors.eq(specialerrors[i]-1).css("display") === "block" || sucesss.eq(specialerrors[i]-1).css("display") === "block")){
							count--;
						}else if((errors.eq(7).css("display") === "block" || sucesss.eq(7).css("display") === "block") && x === 7){count++;}
					}
					count++;
				}
			}
			temp = (count*20)+850;
			return temp+"px";
		}
}

function Validate_form(final){
  var state,fault=false;

  if(final === 1){
	  validate_name();
	  validate_dob_year();
	  validate_dob_day();
	  validate_username();
	  validate_email();
	  validate_password();
	  confirm_password();
	  
	  if(terms_agree.prop("checked") === false){
		  $("#terms_agree").css({color:"red"});
		  return false;
	  }
  }
	
  for(var x=2;x<sucesss.length;x++){
	  if(sucesss.eq(x).css("display") === "block" || x === 6){
		  state = true;
	  }else{
		  if(final === 1){
			  if(x === 4){
				  errors.eq(4).fadeIn();
				  $("select[name='month']").css({background:"rgba(255, 0, 0,0.1)"});
			  }else{
				  errors.eq(x).fadeIn();
			  }
	       }
		  
		  fault = true;
		  state = false;
	  }
    }
	
	$('#form_container').css({height:getnw_height()});
	setTimeout(function(){$('#form_container').css({height:getnw_height()});},500);
	
	if(fault === false){
		return state;
	}else{
		return false;
	}		
}

function Validate_login(){
	if($("input[name='username']").val() !== "" && $("input[name='password']").val() !== ""){
		return true;
	}else{
		return false;
	}
}

