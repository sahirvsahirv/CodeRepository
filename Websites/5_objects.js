//arrays are a list of strings/numbers/multiple  types

//objects are dictionaries with key-value pairs

//key is a string
//values are attributes representing that string

//object literal is the entire object between curly brackets
//literals are actual values - nummber literal is 37, string literal is "hello"

var mybookObject = {
	name: "What if",
	"isbn number": 1112233333,
	"noOfCopies": 10
};

//curly instead of [] brackets in arrays
//notice --name-- does not have quotes but --isbn number-- has quotes sinc it has //a space

mybookObject["name"];

//list all the keys
Object.keys(mybookObject);

//can be done through a loop
var mynewbookobj = {};
mynewbookobj["name"] = "habits";
mynewbookobj["isbn number"] = "1234";

//dot notation
mynewbookobj.noofcopies =  10;

mynewbookobj;
//undefined - we never defined a cover image
mynewbookobj.coverimage;

//arrays of objects - that is when you would need to display a list on the //webpage
//can use an array of different objects, just like an array of different types of //items. For it to be suitable to used in a UI list, should be similar objects
var listOfBooks = [
	
	{
		name: "name1", 
		isbn: "1234", 
		copies:10
	},
	
	{
		name:"cat", 
		price:123.56
	}

];


listOfBooks;
listOfBooks[0];
listOfBooks[0].name;
listOfBooks[0]["name"];
//objects in the debugger trianglecan be expanded
//see the __proto__: It is the prototype of the object. Prototype is like the  basic way the object looks

//prototype:  a first or preliminary version of a device or vehicle from which other forms are developed.

//since it is a hash table implementation, the keys are not stored in order and //you would not get Object.keys(objectname) in order

//hash table is a mathematical function on the key and decides which index in the 
//array should be occupied

//the order of the keys should not be expected to print as in the order of arrays
//next we shall do html and then put all these to use

