<!DOCTYPE html>
<html>
<body>

<h2>JavaScript Objects</h2>

<p id="demo"></p>

<script>
// Create an object:
const Car = {
  owner: "Vicky Bahl",
  model: "Tesla tx",
  milage: 24,
  color: "brown",
  
};

// Display some data from the object:
document.getElementById("demo").innerHTML =
Car.owner + " has a " + Car.model + " of " + Car.color + " color, that gives " + Car.milage + "milage.";
</script>

</body>
</html>
