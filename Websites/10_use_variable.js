function changeToUpperCase()
{
	var name = document.getElementById('nametextbox').value;
	var uppercase = name.toUpperCase;
	return uppercase;
}

document.getElementById('nametextbox').value = changeToUpperCase();
console.log(document.getElementById('nametextbox').value);