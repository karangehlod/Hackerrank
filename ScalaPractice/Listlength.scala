//using inbuild function
def f(arr:List[Int]):Int = arr.length

//using foreach loop 
def f(arr:List[Int]):Int = 
{
    var count =0
    arr.foreach(i => {count+=1})
    return count
}
