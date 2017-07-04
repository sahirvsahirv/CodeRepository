//rollcaller is the function's name
var rollcaller = function(noofstudents)
{	
	//Cannot be local
	//var noofstudents = 15; 

	for(var rollcall =0; rollcall < noofstudents; rollcall++)
	{
		console.log("Hi! " + rollcall + " is very much here.")
	}
}

//15 = noofstudents and is a parameter
rollcaller(15);

//rollcaller function call does not return everything hence it is undefined
