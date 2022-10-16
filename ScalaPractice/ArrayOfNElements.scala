//Prints n times 1's
object Solution extends App {
    def f(num:Int) : List[Int] = {
        val list =  List.fill[Int](num)(1).toList// Write your code here  
        return list
    }
    def readInt(): Int = scala.io.StdIn.readInt()
    println(f(readInt))
}

// prints 0 to n-1 numbers in list
object Solution extends App {

    def f(num:Int) : List[Int] = (0 until num).toList
    def readInt(): Int = scala.io.StdIn.readInt()
    println(f(readInt))
}
