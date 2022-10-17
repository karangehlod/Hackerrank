 def f(delim:Int,arr:List[Int]):List[Int] = 
{
    // inclusing scala lib for mutable collection
    var ls = scala.collection.mutable.ListBuffer.empty[Int]
    // checking each element
    arr.foreach(i => 
    { 
        if(i<delim) ls+= i    
    })
    return ls.toList
}
