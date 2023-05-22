import subprocess


def run_script(value):
    if value == '1':
        subprocess.run(["python", "DWT.py"])
    elif value == '2':
        subprocess.run(["python", "pic.py"])
    elif value == '3':
        subprocess.run(["python", "vid.py"])
    else:
        print("Giá trị không hợp lệ")


if __name__ == '__main__':
    print("-----Vui lòng lựa chọn-----")
    value = input(
        "Chọn Nhúng bằng DWT(Nhập 1)/Chọn Nhúng ảnh(Nhập 2)/Chọn Nhúng Video(Nhập 3): ")
    run_script(value)
