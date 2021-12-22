fun main() {
    val name = "Rosh"
    val amount = 500000
    val borderLines = 3
    var BorderChar = '+'
    println("Congratulaiotns!")
    println("${name}")
    //start printing cake
    printBorder(borderLines, borderChar)
    println("   ,,,,,   ")
    println("   |||||   ")
    println(" =========")
    println("@@@@@@@@@@@")
    println("{~@~@~@~@~}")
    println("@@@@@@@@@@@")
    println("") //empty line print
    println("You won the lottery of ${amount}!")
}
fun printBorder(n: Int, x: String){
    println("--------Congratulations---------")
    repeat(n){
        repeat(23){
        print(x)
        }
        println()
    }
}

fun main() {
    val myFirstDice = Dice(6)
    println("Your ${myFirstDice.numSides} sided dice rolled ${myFirstDice.roll()}!")
    
    val mySecondDice = Dice(20)
    println("Your ${mySecondDice.numSides} sided dice rolled ${mySecondDice.roll()}!")
}

class Dice (val numSides: Int) {

    fun roll(): Int {
        return (1..numSides).random()
    }
}
#Conditional
fun main() {
    val myFirstDice = Dice(6)
    val rollResult = myFirstDice.roll()
    val luckyNumber = 4

    if (rollResult == luckyNumber) {
        println("You win!")
    } else if (rollResult == 1) {
        println("So sorry! You rolled a 1. Try again!")
    } else if (rollResult == 2) {
        println("Sadly, you rolled a 2. Try again!")
    } else if (rollResult == 3) {
        println("Unfortunately, you rolled a 3. Try again!")
    } else if (rollResult == 5) {
        println("Don't cry! You rolled a 5. Try again!")
    } else {
        println("Apologies! You rolled a 6. Try again!")
    }
}
