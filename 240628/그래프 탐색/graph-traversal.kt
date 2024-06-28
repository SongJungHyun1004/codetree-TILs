import java.io.*
import java.util.*

fun main() = with(System.`in`.bufferedReader()){
    
    val (n, m) = readLine().split(" ").map{ it.toInt() }
    val graph = Array<ArrayList<Int>>(n+1) {ArrayList()}
    val visited = BooleanArray(n+1)
    repeat(m) {
        val (x, y) = readLine().split(" ").map { it.toInt() }
        graph[x].add(y)
        graph[y].add(x)
    }
    var cnt = 0
    fun dfs(node:Int){
        visited[node] = true
        for (nxt in graph[node]) {
            if (!visited[nxt]) {
                dfs(nxt)
                cnt += 1
            }
        }
    }
    
    dfs(1)
    print(cnt)
}