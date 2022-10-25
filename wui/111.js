//var myParent = document.body;
var myParent1 = document.querySelector('div#myDiv');
var myParent2 = document.querySelector('div#myDiv11');

//Create array of options to be added
//var array = ["Volvo", "Saab", "Mercades", "Audi"];
//var array_value = ["Volvo_1", "Saab_1", "Mercades_1", "Audi_1"];

eel.expose(say_hello_js); // Expose this function to Python
function say_hello_js(array, array_value, array1, array_value1) {
  //console.log("Hello from " + x);

//Create and append select list
var selectList1 = document.createElement("select");
selectList1.id = "mySelect1";
myParent1.appendChild(selectList1);

//Create and append the options
for (var i = 0; i < array.length; i++) {
    var option = document.createElement("option");
    option.value = array_value[i];
    option.text = array[i];
    selectList1.appendChild(option);
}

var selectList2 = document.createElement("select");
selectList2.id = "mySelect2";
myParent2.appendChild(selectList2);

//Create and append the options
for (var i = 0; i < array1.length; i++) {
    var option = document.createElement("option");
    option.value = array_value1[i];
    option.text = array1[i];
    selectList2.appendChild(option);
}


}
