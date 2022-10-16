import java.io._
import java.math._
import java.security._
import java.text._
import java.util._
import java.util.concurrent._
import java.util.function._
import java.util.regex._
import java.util.stream._

object Solution {
    // As we have factorial in denominator in each term 
    def factorial(n: Int): Int = {
        var f = 1
        for(i <- 1 to n)
        {
            f = f * i;
        }
        return f
    }

    def main(args: Array[String]) {
        val stdin = scala.io.StdIn
        val n = stdin.readLine.trim.toInt

        for (nItr <- 1 to n) {
            val x = stdin.readLine.trim.toDouble
            // map 0-9 as we need results till 10th term
            // apply formula using Math as (pow(number,term)/factorial of term) 
            // i.e for first term (x^0)/ factorial(0) = x^0 = 1
            // sum all the term using inbuild sum
            val result = (0 to 9).map( i=> Math.pow(x, i)/factorial(i)).sum
            println(result)
        }
    }
}
