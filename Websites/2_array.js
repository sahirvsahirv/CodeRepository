var library = ["Habits", "what if", "winnie the pooh"]

library

var newlibrary = [];
//Populate the next through the loop asking the user
newlibrary[0] = "Habits";
newlibrary[1] = "what if";
newlibrary[2] = "winnie the pooh";

newlibrary;

//notice the undefined * 97
newlibrary[100] = "mylastbook";
newlibrary;

newlibrary.length;

//Stack data structure
//try newlibrary.push("Another one"); //adds to the end
//try newlibrary.unshift("My first one"); //adds the first one
//var removeLast = newlibrary.pop(); //Pops the last book
//var firstBook = newlibrary.shift(); //returns first dequeue in queue data structure
//yoursAndMine = library.concat(newlibrary);
//newlibrary("what if"); //returns the index

//Array to a string
//Joins the array into a single string
mycommaSeparatedString = newlibrary.join();
myhyphenSeparatedString = newlibrary.join(" - ");


Math.random(); //returns a number between 0 and 1
//What if you want between 0 and 100
//Multiply by 100

Math.floor(3.666); //Try cieling

//Exercise
//Write code for joining the array into a string, without using "join"
//Write another version of join, that takes a separator

//Let us see object oriented concepts with this

//Exercise
//Mimic throwing a dice and store the thrown numbers
//Check what series of thrown numbers can reach the 100 fastest in snake and //ladders
//How would you do it?
//Just think for now!
