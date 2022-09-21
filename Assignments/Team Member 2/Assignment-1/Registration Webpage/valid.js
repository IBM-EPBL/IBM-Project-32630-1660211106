function fncValidate() 
{
	
			
	var d=document.getElementById("dob");
	
	if(d.value == null || d.value == "") 
	{
		alert("select the DOB!");
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
		alert("Enter 10 digits");
		return false;
	}
	if(p.length<10) 
	{
		alert("Enter 10 digits");
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
		alert("Ivalid email id");
		return false;
	}
	alert("Registration successful!");
	document.form1.submit();
}