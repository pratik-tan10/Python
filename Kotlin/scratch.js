<!DOCTYPE html>
<html>
<body>

<h2>Create Object from JSON String</h2>

<p id="demo"></p>

<script>
let text = '{"employees":[' +
'{"firstName":"Aaron","lastName":"Stone" },' +
'{"firstName":"Lancaster","lastName":"Brimmer" },' +
'{"firstName":"Michael","lastName":"Morningstar" }]}';

const obj = JSON.parse(text);
document.getElementById("demo").innerHTML =
obj.employees[1].firstName + " " + obj.employees[1].lastName;
</script>

</body>
</html>
