fun main() {
    val numbers = listOf(0, 3, 8, 4, 0, 5, 5, 8, 9, 2)
    println("list:   ${numbers}")
    println("sorted: ${numbers.sorted()}")
    val setOfNumbers = numbers.toSet()
    println("set:    ${setOfNumbers}")
    val set1 = setOf(1,2,3)
    val set2 = mutableSetOf(3,2,1)
    println("$set1 == $set2: ${set1 == set2}")
    println("contains 7: ${setOfNumbers.contains(7)}")
    
    val peopleAges = mutableMapOf<String, Int>(
        "Fred" to 30,
        "Ann" to 23
    )
    peopleAges.put("Barbara", 42)
    peopleAges["Joe"] = 51
    println(peopleAges)
    println(peopleAges)
    
    peopleAges.forEach { print("${it.key} is ${it.value}, ") }
println(peopleAges.map { "${it.key} is ${it.value}" }.joinToString(", ") )
val filteredNames = peopleAges.filter { it.key.length < 4 }
println(filteredNames)
peopleAges.forEach { print("${it.key} is ${it.value}") }

val triple: (Int) -> Int = { a: Int -> a * 3 }
    println(triple(5))
peopleAges.filter { it.key.length < 4 }
val peopleNames = listOf("Fred", "Ann", "Barbara", "Joe")
println(peopleNames.sorted()
println(peopleNames.sortedWith { str1: String, str2: String -> str1.length - str2.length })
}
