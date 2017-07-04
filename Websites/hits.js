var numberOfVisits = 0;
//Can seperate by comma and exclude var

var newdate;
var oldDate;

if(numberofVisits > 10)
{
	console.log("Frequent visitor");
	if(newDate == null)
	{
		newdate = new Date();
		oldDate = newdate;
	}
	else
	{
		oldDate = newdate;
		newdate = new Date();
	}
}