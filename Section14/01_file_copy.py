#파일 복사
# 원본 파일 --> 변수 --> 복사 파일
buffer_size = 1024 # 1024byte ---> 1kb
with open('monk.jpg','rb') as source:
    with open('copy.jpg','wb') as copy:
        while True:
            buffer = source.read(buffer_size)
            if not buffer:
                break
            copy.write(buffer)

print('파일 복사가 끝났습니다.')