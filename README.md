# dcinside-auto-collector
Deadly simple non official dcinside document collector for python3
```python
# 프로그래밍 갤러리 점진적자살 게시글 수집
def upload_to_archive(doc):
    print(doc["title"], doc["time"])
    print("------------------")
    print(doc["contents"])
    # for readability instead of doc["html"] 
    print("------------------")
    for comm in doc["comments"]:
        print("{}\t{}\t{}".format(comm["author"], comm["contents"], comm["time"]))
    print("------------------")
def download_img_and_upload_somewhere(imgsrc):
    # 크로스도메인 정책떄문에 외부에서 디시에 올라온 이미지를 태그할수 없음..
    # 디시에 올라온 이미지를 다운받아서 다른 어딘가에 올려야함
    NEW_IMG_SRC = ""
    return NEW_IMG_SRC
def callback(doc):
    for imgsrc in doc["images"]:
        doc["html"] = doc["html"].replace(imgsrc, download_img_and_upload_somewhere(imgsrc))
    upload_to_archive(doc)

dc_collector.start(board_id="programming", author="점진적자살(58.126)|점진적자살(114.70)", callback=callback)
```

# Dependency
python3 dc_api

# Usage
Place dc_collector.py in your working directory
