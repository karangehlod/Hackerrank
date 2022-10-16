def f(arr:List[Int]):List[Int] = {
    var l = scala.collection.mutable.ListBuffer.empty[Int]
    //using Math.abs to only  negative values
    arr.foreach(i => {if (i<0) l+=Math.abs(i) else l+=i})
    return l.toList
}

def f(arr:List[Int]):List[Int] = {
    var l = scala.collection.mutable.ListBuffer.empty[Int]
    //using Math.abs to all values     
    arr.foreach(i => l+=Math.abs(i))
    return l.toList
}
