- [x]  Khởi tạo dữ liệu ma trận từ bản đồ google map, gồm 1 vùng diện tích có tối thiểu 100 đỉnh vs 100 cạnh trong khu vực Tp.HCM. (2) - Road, Place, Geocoding API
- [x]  Cài đặt 3 thuật toán Dijstra, Bellman-Ford, Floyd warshall trên dữ liệu khởi tạo và đưa ra đánh giá về performance – chọn ngẫu nhiên các cặp đỉnh (3)
- [ ]  Đánh giá performance bằng cách chọn 2 điểm -> đưa ra lý do tại sao chọn 2 điểm đó. Chọn các điểm 1 cách tổng quan, bao quát nhiều trường hợp
- [x]  Cho phép nhập điểm đầu và điểm cuối trên bản đồ và xuất ra 3 đường đi ngắn nhất. Minh họa 3 đường đi trên bản đồ (google map là 1 điểm cộng) (4) Road, Place, Geocoding API
- [ ]  So sánh kết quả giải thuật vs dữ liệu thực tế từ google. (1) - Direction (+ Distance Matrix) API

#Content of Report 

## Các thuật toán tìm đường đi ngắn nhất
 
**1. Dijkstra's Algorithm**
Thuật toán Dijkstra tìm đường đi ngắn nhất giữa một đỉnh cho trước đến tất cả các đỉnh còn lại trong đồ thị. Thuật toán này sử dụng trọng số của từng cạnh để tìm được đi sao cho tổng trọng số của đường đi là ngắn nhất.
Thuật toán này áp dụng cho đồ thị có trọng số dương, độ phức tạp là $O(|V|^2)$
```pseudo
procedure Dijkstra(G,a)  
// Initialization Step  
	forall vertices v  
		Label[v] := ∞  
		Prev[v] := -1  
	endfor  
	Label(a) := 0 // a is the source node  
	S := ∅;  
// Iteration Step  
	while z ∉ S  
		u := a vertex not in S with minimal Label  
		S := S ∪ {u}  
		forall vertices v not in S  
			if (Label[u] + Wt(u,v)) < Label(v)  
				then begin  
					Label[v] := Label[u] + Wt(u,v)  
					Pred[v] := u  
				end  
	endwhile
```
**2. Bellman-Ford Algorithm**
Tương tự như thuật toán Dijkstra, thuật toán Bellman-Ford cũng đảm bảo tìm được đường đi ngắn nhất từ một đỉnh cho trước đến toàn bộ các đỉnh còn lại trong đồ thị. 
Tuy nhiên, thuật toán Bellman-Ford có thể áp dụng được cho đồ thị có trọng số bất kỳ (dương hoặc âm) và có thể phát hiện xem trong đồ thị này có tồn tại chu trình âm hay không. Thuật toán Bellman-Ford có độ phức tạp $O(|V| \times |E|)$

```pseudo
procedure BellmanFord(G,a)  
// Initialization Step  
	forall vertices v  
		Label[v] := ∞  
		Prev[v] := -1  
	Label(a) := 0 // a is the source node  
// Iteration Step  
	for i from 1 to size(vertices)-1  
		forall vertices v  
			if (Label[u] + Wt(u,v)) < Label[v]  
			then  
				Label[v] := Label[u] + Wt(u,v)  
				Prev[v] := u  
// Check circuit of negative weight  
	forall vertices v  
		if (Label[u] + Wt(u,v)) < Label(v)  
			error "Contains circuit of negative weight"
```
**3. Floyd-Warshall**
Floyd-Warshall là một thuật toán trong lĩnh vực khoa học máy tính và lý thuyết đồ thị. Thuật toán này được dùng để tìm đường đi ngắn nhất giữa tất cả các cặp đỉnh trên một đồ thị có trọng số, có thể áp dụng được trên cả đồ thị có trọng số cạnh là dương hoặc âm.
Thuật toán Floyd-Warshall có độ phức tạp là $O(|V|^3)$

```pseudo
procedure FloydWarshall ()  
	for k := 1 to n  
		for i := 1 to n  
			for j := 1 to n  
				path[i,j] = min (path[i,j],path[i,k]+path[k,j]);
```

## Xây dựng đồ thị trong khu vực TP. HCM

Để xây dựng được một đồ thị trong khu vực Thành phố Hồ Chí Minh, nhóm sử dụng thư viện **OSMnx** để hiện thực một đồ thị với các thông số:

 - Diện tích:
 - Số cạnh:
 - Số đỉnh: 

## Giao diện tương tác của người dùng
Nhóm đã sử dụng **Next.js** để xây dựng giao diện giúp người dùng có thể dễ dàng tương tác với các thuật toán cũng như trực quan hóa kết quả tìm kiếm đường đi ngắn nhất.
Đồng thời, giao diện cũng giúp so sánh hiệu quả tìm kiếm của 3 thuật toán Dijkstra, Bellman-Ford và Floyd-Warshall với thuật toán tìm kiếm của Google Map
