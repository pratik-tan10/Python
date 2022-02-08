<!DOCTYPE html>
<html>
<body>

<h2>JavaScript String Methods</h2>

<p>Search a string for "W3Schools", and display the position of the match:</p>

<p id="demo"></p>

<script>
let text = "Visit W3Schools!"; 
let n = text.search("W3Schools");
document.getElementById("demo").innerHTML = n;
</script>

</body>
</html>
