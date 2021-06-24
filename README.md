# Image Retrieval System using global feature

# Acknowledgement
Ý tưởng và cấu trúc code chính được tham khảo từ hai nguồn sau:
* http://www.pyimagesearch.com/2014/12/01/complete-guide-building-image-search-engine-python-opencv/
* https://github.com/danuzclaudes/image-retrieval-OpenCV

Thư viện và phiên bản:
* python 3.7
* opencv-python, opencv-contrib-python, tensorflow, Keras, mysqlclient, Pillow, numpy: mới nhất

### Các bước cài đặt và chạy chương trình
* Trong MySQL, tạo một cơ sở dữ liệu tên là <b>image_retrieval</b>, có lược đồ như hình <b>schema.png</b><br/>

* Trong file <b>Index.py</b> có 4 phương thức, điền mật khẩu của cơ sở dữ liệu cho tham số <b>passwd</b> của câu lệnh 
MySQL.connect() trong cả 4 phương thức này

* Tải xuống tập dữ liệu:
    ```
    python prepare_dataset.py --dataset_test <Tên folder tập test> --dataset_train <Tên folder tập train>
    ```
    Ví dụ:
    ```
    python prepare_dataset.py --dataset_test test --dataset_train train
    ```
<br/>

* Trích chọn đặc trưng và lưu vecto đặc trưng vào cơ sở dũ liệu:
    ```
    python feature_extraction.py --dataset <Đường dẫn thư mục tập train>
    ```
    Ví dụ:
    ```
    python feature_extraction.py --dataset D:/PersonalProjects/image-retrieval/train
    ```
<br/>

* Truy vấn:
    ```
    python retrieve_index.py --query <Đường dẫn file truy vấn> --result-path <Đường dẫn thư mục tập train>
    ```
    Ví dụ:
    ```
    python retrieve_index.py --query D:/PersonalProjects/image-retrieval/test/6_test.png --result-path D:/PersonalProjects/image-retrieval/train
    ```
<br/>

### Mô tả một số file chính
<b>Bước 1: Định nghĩa bộ đặc tả đặc trưng - FeatureDescriptor.py</b></p> 

Bước đầu tiên là trích chọn các đặc trưng từ tập dữ liệu. Nhóm chọn <b>color histograms</b> là 
đặc trưng được trích chọn và vecto đặc trưng được sinh ra có thể biểu diễn trừu tượng bức ảnh ban đầu

Đây là ý tưởng chính của FeatureDescriptor.py: </p> 
1. Chuyển đổi sang HSV và khởi tạo các đặc trưng để định lượng và biểu diễn ảnh </p> 
2. Chia vùng ảnh bằng mặt nạ elip và mặt nạ các góc </p> 
3. Xây dựng danh sách đặc trưng bằng cách lặp qua các vùng đã chia </p> 
 
<b>Bước 2: Lập chỉ mục các đặc trưng từ tập dữ liệu - feature_extraction.py</b></p> 

Sau khi có bộ đặc tả, trích chọn đặc trưng từ các ảnh trong tập dữ liệu và lưu vào cơ sở dữ liệu
 
Đây là ý tưởng chính của feature_extraction.py: </p> 
1. Đọc danh sách tên file của tất cả các ảnh png trong thư mục</p>  
2. Ghi đường dẫn và tên file vào cơ sở dữ liệu </p> 
3. Trích xuất đặc trưng sử dụng bộ đặc tả đặc trưng và ghi vecto đặc trưng vào cơ sở dữ liệu </p> 
 
<b>Bước 3:  Truy xuất chỉ mục bởi ảnh truy vấn - Retriever.py</b></p> 

Bước này có mục đích tính khoảng cách hay độ tương tự giữa vecto đặc trưng của ảnh truy vấn
với các vecto đặc trưng đã được lập chỉ mục. Khoảng cách càng nhỏ thể hiện các bức ảnh càng liên quan
tới nhau. <br/>

Đây là ý tưởng chính của Retriever.py: </p> 
1. Đọc tất cả chỉ mục từ cơ sở dữ liệu </p> 
2. Tính khoảng cách vecto đặc trưng của ảnh truy vấn và mỗi hàng </p> 
3. Sắp xếp từ điển, trả về các bộ (id, khoảng cách) </p> 
 
<b>Bước 4: Thiết kế hệ thống truy xuất - retrieve_index.py</b></p> 
 
Đây là ý tưởng chính của retrieve_index.py: </p> 
1. Trích chọn đặc trưng từ ảnh truy vấn </p> 
2. Thực hiện truy xuất thông qua bảng chỉ mục </p> 
3. Duyệt qua và hiển thị các kết quả