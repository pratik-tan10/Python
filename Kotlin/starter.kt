import kotlin.math.PI
import kotlin.math.sqrt
fun main() {
	val squareCabin = SquareCabin(6, 50.0)
	val roundHut = RoundHut(3, 10.0)
	val roundTower = RoundTower(4, 15.5)
    with (squareCabin){
        println("\nSquare Cabin\n============")
        println("Capacity: ${capacity}")
        println("Material: ${squareCabin.buildingMaterial}")
        println("Has room? ${hasRoom()}")
        getRoom()
        println("Floor area: %.2f".format(floorArea()))
        println("Carpet size: %.2f".format(length))
    }
}
