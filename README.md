# Recommendation System for Be Beauty

## Content
1. [Recommendation System](#Recommendation-System)

   1.1 [Định nghĩa](#Định-nghĩa)

   1.2 [Các thành phần cơ bản](#Các-thành-phần-cơ-bản)

   1.3 [Hướng tiếp cận](#Hướng-tiếp-cận)
   
   1.4 [Những bước cần làm để xây dựng một Recommendation System:](#Những-bước-cần-làm-để-xây-dựng-một-Recommendation-System:)

1. [CONTENT-BASED FILTERING RECOMMENDERS VÀ COLLABORATIVE FILTERING RECOMMENDERS](#CONTENT-BASED-FILTERING-RECOMMENDERS-VÀ-COLLABORATIVE-FILTERING-RECOMMENDERS)

   2.1  [Content-based Filtering Recommenders](#Content-based-Filtering-Recommenders)
   
   2.2  [Collaborative Filtering Recommenders](#Collaborative-Filtering-Recommenders)

   2.3 [So sánh](#So-sánh)

1. [Ý tưởng cho Be Beauty](#Ý-tưởng-cho-Be-Beauty)

# Recommendation System
### Định nghĩa
Recommendation System (Recommender System) là một dạng của hệ hỗ trợ ra quyết định, cung cấp giải pháp mang tính cá nhân hóa mà không phải trải qua quá trình tìm kiếm phức tạp. Recommendation System học từ người dùng và gợi ý các sản phẩm tốt nhất trong số các sản phẩm phù hợp.

Recommendation System sử dụng các tri thức về sản phẩm, các tri thức của chuyên gia hay tri thức khai phá học được từ hành vi con người dùng để đưa ra các gợi ý về sản phẩm mà họ thích trong hàng ngàn hàng vạn sản phẩm có trong hệ thống.

Các sản phẩm được gợi ý dựa trên số lượng sản phẩm đó đã được bán, dựa trên các thông tin cá nhân của người sử dụng, dựa trên sự phân tích hành vi mua hàng trước đó của người sử dụng để đưa ra các dự đoán về hành vi mua hàng trong tương lai của chính khách hàng đó.

Các dạng gợi ý bao gồm: 
- Gợi ý các sản phẩm tới người tiêu dùng, 
- Các thông tin sản phẩm mang tính cá nhân hóa, 
- Tổng kết các ý kiến cộng đồng, 
- Cung cấp các chia sẻ, các phê bình, đánh giá mang tính cộng đồng liên quan tới yêu cầu, mục đích của người sử dụng đó.

### Các thành phần cơ bản:

- Thứ nhất: Điều đầu tiên cần phải quan tâm đó chính là ***Người dùng (User)***, hiển nhiên rồi, nếu không có user thì chúng ta biết gợi ý cho ai.

- Thứ hai: Chúng ta cần phải quan tâm đến các mục tin (Items) - các mục tin này có thể là sản phẩm trên các trang bán hàng, bài hát trên các trang nghe nhạc,…

- Thứ ba: Chúng ta cần phải quan tâm đến phản hồi (feedback) của mỗi user lên mục tin đó. Nó có thể là điểm đánh giá, có thể là một chỉ số thể hiện sự quan tâm của user lên item đó....

### Hướng tiếp cận:

Bước 1: Tìm các đặc trưng (features) có ảnh hưởng đến việc đánh giá của người dùng, thông qua việc phân tích và thăm dò dữ liệu.

Bước 2: Phân tích và áp dụng giải thuật filtering phù hợp.

Bước 3: Tiến hành training mô hình.

Nhìn chung, hệ thống Recommender System có thể được chia thành 4 loại chính:

<p align="center">
    <img src="https://github.com/Votrungtin2001/recommendation-system/blob/main/picture/image32.png" width="auto">
   </p>
   
- Simple Recommenders (Đề xuất đơn giản): Đưa ra các đề xuất tổng quát cho mọi người dùng, dựa trên mức độ phổ biến và/hoặc thể loại của đối tượng đang chọn để gợi ý (có thể là một bộ phim, một bài nhạc, một sản phẩm, vv…).

- Content-based Filtering Recommenders (Đề xuất dựa trên nội dung): Đề xuất các đối tượng muốn gợi ý tương tự dựa trên một đối tượng cụ thể khác.

- Collaborative Filtering Recommenders (Đề xuất dựa trên lọc cộng tác): Những hệ thống này được sử dụng rộng rãi và chúng cố gắng dự đoán “ratings” hoặc “preference” mà người dùng sẽ đưa ra một mặt hàng dựa trên xếp hạng trước đây và sở thích của những người dùng khác.

- Hybrid Recommenders: Hybrid Filtering là sự kết hợp của hai giải thuật Content-based Filtering và Collaborative Filtering: Hybrid Filtering được sử dụng mềm dẻo khi hệ thống Collaborative Filtering không có các hành vi (ratings), khi đó hệ thống sẽ sử dụng Content-based Filtering và ngược lại, khi Content-based Filtering không có các feature cần thiết trong việc đánh giá thì hệ thống sẽ sử dụng Collaborative Filtering để thay thế.

### Những bước cần làm để xây dựng một Recommendation System:

Thu thập dữ liệu:

Biểu diễn thông tin bằng ma trận users-items:

Chuẩn hóa dữ liệu:

Chạy mô hình, lọc ra top N item phù hợp:

## CONTENT-BASED FILTERING RECOMMENDERS VÀ COLLABORATIVE FILTERING RECOMMENDERS

### Content-based Filtering Recommenders

#### Ý tưởng 

Phương pháp lọc dựa trên nội dung sẽ dựa trên các đặc tính của items được recommended. Nó sẽ gợi ý các item dựa trên hồ sơ (profiles) của người dùng hoặc dựa vào nội dung, thuộc tính (attributes) của những item tương tự như item mà người dùng đã chọn trong quá khứ. 

Ví dụ: một người dùng xem các bộ phim của siêu anh hùng DC Comics, hệ thống sẽ đề xuất các phim siêu anh hùng của Marvel, cùng thuộc thể loại siêu anh hùng, siêu năng lực với bộ phim người dùng thích. 

Hệ thống chỉ cần biết người dùng xem phim nào chứ không cần dữ liệu về ratings, giúp nó hoạt động ngay cả khi người dùng không có thói quen đánh giá đối tượng đó.

#### Xây dựng phương pháp Content-based Filtering

Khởi tạo dữ liệu

Thiết lập ma trận TF-IDF

Tính độ tương đồng giữa các item

#### Ưu điểm

- Không cần tri thức miền.
- Chất lượng tăng theo thời gian.
- Đủ thông tin phản hồi không tường minh.

#### Nhược điểm

- Thứ nhất, khi xây dựng mô hình cho một user, các hệ thống Content-based không tận dụng được thông tin từ các users khác.

- Thứ hai, không phải lúc nào chúng ta cũng có bản mô tả cho mỗi item. 

### Collaborative Filtering Recommenders

#### Ý tưởng

Ý tưởng cơ bản của thuật toán này là dự đoán mức độ yêu thích của một user đối với một item dựa trên các users khác “gần giống” với user đang xét. Việc xác định độ “giống nhau” giữa các users có thể dựa vào mức độ quan tâm (rating) của các users này với các items khác mà hệ thống đã biết trong quá khứ.

Ví dụ: Hai users A, B đều thích các phim về trinh thám (tức là đều đánh giá các bộ phim thuộc thể loại này 4 -> 5 sao). Dựa vào lịch sử xem phim của B, ta thấy B thích bộ phim “Sherlock Holmes”, vậy nhiều khả năng A cũng thích phim này, từ đó hệ thống sẽ đề xuất “Sherlock Holmes” cho A.

#### Xây dựng phương pháp Collaborative Filtering

Khởi tạo dữ liệu

Khởi tạo ma trận dữ liệu

Chuẩn hóa ma trận dữ liệu

Tính toán độ tương đồng

Dự đoán ratings

#### Ưu điểm: 
- Có thể ánh xạ giữa nhu cầu người dùng và sản phẩm/đối tượng.

#### Nhược điểm:
- Cần phải thu thập dữ liệu, tri thức.

### So sánh

#### Dữ liệu cơ sở
Content-based Filtering: Các đặc điểm của các đối tượng trong I.

Collaborative Filtering: Các điểm số đánh giá của những người sử dụng trong U đối với các đối tượng trong I.

#### Dữ liệu đầu ra

Content-based Filtering: Các điểm số đánh giá của u cho các đối tượng trong I.

Collaborative Filtering: Các điểm số đánh giá của u cho các đối tượng trong I.

#### Tiến trình xử lý

Content-based Filtering: Tạo ra một mô hình mô tả sở thích của người sử dụng u, sau đó sử dụng để đánh giá mức độ ưa thích của u với i.

Collaborative Filtering: Nhận ra người sử dụng trong U tượng tự với u ( về sở thích) và sau đó ngoại suy điểm số đánh giá của u cho i.


# Ý tưởng cho Be Beauty

Áp dựng Content-based Filtering Recommender

<p align="center">
    <img src="https://github.com/Votrungtin2001/recommendation-system/blob/main/picture/image5.png" width="auto">
   </p>
Bước 1: Ở flutter trước khi request danh sách các sản phẩm phù hợp với sở thích người dùng sẽ dựa trên database phần Preference để chọn ra criteria (bộ 5 tiêu chí xem xét với tần số xuất hiện cao nhất). 
	Ví dụ: Trong 50 lượt thao tác với sản phẩm gần nhất của người dùng
		brandHistory : 
- Corsx (id: 1), tần số xuất hiện 45
- Paula Choice (id: 5), tần số xuất hiện 5
		skinTypeHistory : 
- Dầu (id: 2), tần số xuất hiện 40
- Mụn (id: 1), tần số xuất hiện 10
categoryHistory : 
- Sửa rửa mặt  (id: 3), tần số xuất hiện 20
- Tẩy trang (id: 2), tần số xuất hiện 30
sessionHistory : 
- Tối (id: 2), tần số xuất hiện 44
- Sáng (id: 1), tần số xuất hiện 6
structureHistory : 
- Kem (id: 4), tần số 15
- Nước (id: 2) tần số 25
- Dầu (id 3), tần số 10
Dữ liệu khi post từ flutter đến flask sau khi tính toán xong:
‘products’: products (danh sách sản phẩm)
‘criteria’: criteria (tiêu chí xét, với ví dụ số liệu trên thì criteria sẽ gửi đi giá trị là 
((1, 45), (2, 40), (2, 30), (2, 44) ,(2, 25)), trong criteria là bộ các ID và tần số trong đó phần tử đầu tương đương với tiêu chí brand, phần tử 2 tương đương với tiêu chí skin, phần tử 3 là category, phần tử 4 là session, phần tử 5 là structure)

Bước 2: Flask nhận dữ liệu từ flutter và thực hiện hàm tính toán:
Tạo một mảng một chiều và xét từng product có trong list products được gửi từ flutter:
Quy tắc xét: Lấy 5 thuộc tính tương tự của product đang xét bao gồm brandID, skinID, categoryID, sessionID và structureID. Trong đó, do xu hướng thực tế người dùng sẽ tìm kiếm ưu tiên về loại sản phẩm (category), rồi tới tên hang (brand) rồi tới loại da (skin) nên sẽ có một giá trị là hệ số ưu tiên (hsut) lần lượt là 3 cho category, 2 cho brand và 2 cho skin, còn lại các tiêu chí khác hệ số ưu tiên là 1. Sau đó so sánh với giá trị của criteria tương ứng với từng tiêu chí.
	
   Ví dụ: Product 1 (3,1,2,2,5): Nếu giá trị tương ứng với criteria thì giá trị biến matching sẽ là 1. Nếu khác thì sẽ là 0. Công thức tính similarities trong trường hợp này:
	
   <p align="center">
    <img src="https://github.com/Votrungtin2001/recommendation-system/blob/main/picture/C%C3%B4ng%20th%E1%BB%A9c.png" width="auto">
   </p>

Tính toán tương tự với các sản phẩm còn lại: Sau mỗi lần tính sẽ thêm vào mảng một chiều phần tử đó bao gồm (id, độ tương tự).
Sau đó thực hiện thuật toán sắp xếp độ tương tự giảm dần.
Trả về flutter danh sách các id product có độ tương tự từ cao tới thấp theo số lượng đặt ra.

Bước 3: Flutter nhận dữ liệu trả về từ flask và dùng thuật toán tìm kiếm để tìm ra danh sách các sản phẩm có id tương ứng và hiển thị.






 
