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
    val diceRoll = myFirstDice.roll()
    println("Your ${myFirstDice.numSides} sided dice rolled ${diceRoll}!")
    
    val mySecondDice = Dice(20)
    println("Your ${mySecondDice.numSides} sided dice rolled ${mySecondDice.roll()}!")
}

class Dice (val numSides: Int) {

    fun roll(): Int {
        val randomNumber = (1..numSides).random()
        return randomNumber
    }
}
