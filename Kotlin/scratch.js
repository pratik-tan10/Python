<!DOCTYPE html>
<html>
<body>
<h2>JavaScript Sets</h2>
<p>Add variables to a Set:</p>

<p id="demo"></p>

<script>
// Create a Set
const letters = new Set();

// Create Variables
const a = "a";
const b = "b";
const c = "c";

// Add the Variables to the Set
letters.add(a);
letters.add(b);
letters.add(c);

// Display set.size
document.getElementById("demo").innerHTML = letters.size;
</script>

</body>
</html>
