data class Dog(
    val name: String,
    val age: Int
)

fun main() {
    println(dog.copy()) // Dog(name=Pluto, age=7)
    println(dog.copy(age = 8)) // Dog(name=Pluto, age=8)
    println(dog.copy(name = "Neptune")) // Dog(name=Neptune, age=7)
}