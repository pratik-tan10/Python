<!DOCTYPE html>
<html>
<body>
<h2>JavaScript Sets</h2>
<p>forEach() calls a function for each element:</p>

<p id="demo"></p>

<script>
// Create a Set
const letters = new Set(["a","b","c"]);

// List all Elements
let text = "";
letters.forEach (function(value) {
  text += value + "<br>";
})

document.getElementById("demo").innerHTML = text;
</script>

</body>
</html>
