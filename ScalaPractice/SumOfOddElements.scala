 def f(arr:List[Int]):Int = {
  var sum = 0
  arr.foreach(i => {
    //if number is odd increase the sum 
    if (i % 2 != 0) sum+=i
  })
  return sum
 }
