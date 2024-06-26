import os

# Đường dẫn đến thư mục chứa các tệp ảnh .jpg
input_dir = 'D:/machine_learning/detect_behavious/test_model_detect_behaveour/training/data/dog'

# Đường dẫn đến thư mục đích để lưu các tệp ảnh .png
output_dir = 'D:/machine_learning/detect_behavious/test_model_detect_behaveour/training/data/dog'

# Tạo thư mục đích nếu chưa tồn tại
if not os.path.exists(output_dir):
    os.makedirs(output_dir)


# Lấy danh sách các tệp ảnh .jpg trong thư mục input
jpg_files = [f for f in os.listdir(input_dir) if f.endswith(('.jpg',  '.jfif'))]

# Chuyển đổi và lưu các tệp ảnh .jpg sang .png
print(jpg_files)
def a():

    for jpg_file in jpg_files:
 
        input_path = os.path.join(input_dir, jpg_file)
        output_path = os.path.join(output_dir, os.path.splitext(jpg_file)[0] + '.png')
        
        # Đọc và lưu ảnh
        with open(input_path, 'rb') as f:
            image_data = f.read()
        with open(output_path, 'wb') as f:
            f.write(image_data)
        print(jpg_file)
        os.remove(input_dir+'/'+ jpg_file)

        print(f'Đã chuyển đổi {jpg_file} sang {os.path.basename(output_path)}')
    
    
a()