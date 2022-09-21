function fncValidate() 
{
	var fn=document.form1.first_name.value; 
	var ln=document.form1.last_name.value; 
	var patt = /[^a-z]/i; 
	var first_name = patt.test(fn); 
	var last_name = patt.test(ln); 
			
	if(fn == "") 
	{
		alert('Enter First name!'); 
		return false;
	}
	if ( fn == null || first_name == true ) 
	{
		alert("Enter valid input!"); 
		return false;
	}
	if(ln == "")
	{
		alert('Enter Last name!');
		return false;
	}
	if ( ln == null || last_name == true )
	{
		alert("Enter valid input!");
		return false;
	}
			
	var d=document.getElementById("dob");
	
	if(d.value == null || d.value == "") 
	{
		alert("Select the DOB!");
		return false;
	}
			
	var m = document.getElementById('male'); 
	var f = document.getElementById('female'); 

	if ( (m.checked == false ) && (f.checked == false ) ) 
	{
		alert ( "Please choose Gender" );
		document.getElementById("gen"); 
		return false;
	}
	
	var r=document.form1.regno.value; 

	if(r == null || r == "") 
	{
		alert("Enter register number!");
		return false;
	}
	if(r.length>12) 
	{
		alert("Enter 12 digits");
		return false;
	}
	if(r.length<12) 
	{
		alert("Enter 12 digits");
		return false;
	}

	var c = document.getElementById("course") 

	if(c.value == null || c.value == "") 
	{ 
		alert("Select a course"); 
		return false;
	}

	var p=document.form1.phone.value; 

	if(p == null || p == "") 
	{
		alert("Enter Mobile number!");
		return false;
	}
	if(p.length>10) 
	{
		alert("Enter 10 digits!");
		return false;
	}
	if(p.length<10) 
	{
		alert("Enter 10 digits!");
		return false;
	}

	var em=document.form1.email.value; 
	var atpos=em.indexOf("@"); 
	var dotpos=em.lastIndexOf(".");	

	if(em == "")
	{
		alert("Enter Email id!");
		return false;
	}
	if(atpos<1 || dotpos<atpos+2 || dotpos+2>=em.length)
	{
		alert("Ivalid email id!");
		return false;
	}
	alert("Registration successful!");
	document.form1.submit();
}
