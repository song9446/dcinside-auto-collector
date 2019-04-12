import dc_api
import time
def start(board_id="programming", author="", callback=print, last_doc_id=None, interval=600):
    if last_doc_id is None:
        for doc in dc_api.board(board_id, num=1):
            last_doc_id = int(doc["id"])
    while True:
        docs = [doc for doc in dc_api.board(board_id, doc_id_lower_limit=last_doc_id)]
        docs.reverse()
        for doc in docs:
            last_doc_id = doc["id"]
            for _author in author.split("|"):
                if _author in doc["author"] and doc["author"].split("(")[0] == _author.split("(")[0]:
                    callback(doc)
                    break
        time.sleep(interval)

if __name__ == "__main__":
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
    start(board_id="programming", author="점진적자살(58.126)|점진적자살(114.70)", callback=callback)
