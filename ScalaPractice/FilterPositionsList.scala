//create mutable listbuffer 
// using foreach loop access each element
//track index and check if it is even add to list else nothing 
// if index is even add element to listbuffer
// after each element access increase index
// return list created
def f(arr: List[Int]): List[Int] = {
  var l = scala.collection.mutable.ListBuffer.empty[Int]
  var index = 1
  arr.foreach(i => {
    if (index % 2 == 0) l += i
    index += 1
  })
  return l.toList
}
