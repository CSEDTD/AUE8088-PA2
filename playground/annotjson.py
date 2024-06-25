import json
import os

def txt_to_json(input_file, label_dir, output_file):
    data = {}
    data["info"] = {
        "dataset": "KAIST Multispectral Pedestrian Benchmark",
        "url": "https://soonminhwang.github.io/rgbt-ped-detection/",
        "related_project_url": "http://multispectral.kaist.ac.kr",
        "publish": "CVPR 2015"
    }
    data["info_improved"] = {
        "sanitized_annotation": {
            "publish": "BMVC 2018",
            "url": "https://li-chengyang.github.io/home/MSDS-RCNN/",
            "target": "files in train-all-02.txt (set00-set05)"
        },
        "improved_annotation": {
            "url": "https://github.com/denny1108/multispectral-pedestrian-py-faster-rcnn",
            "publish": "BMVC 2016",
            "target": "files in test-all-20.txt (set06-set11)"
        }
    }

    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            images = []
            images_id = 0
            for line in f:
                im_name = line.split("/")[-1].split(".")[0]
                im_name = im_name.replace("_", "/") # required?
                item = {
                    "id": images_id,
                    "im_name": im_name,
                    "height": height,
                    "width": width
                }
                images.append(item)
                images_id += 1
            data["images"] = images

    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")
    except Exception as e:
        print(f"오류 발생: {e}")


    try:
        annotations = []
        annotations_id = 0
        for image_dict in images:
            image_id = image_dict["id"]
            filename = image_dict["im_name"] + ".txt"
            filename = filename.replace("/", "_") # required?
            file_path = os.path.join(label_dir, filename)

            if not os.path.isfile(file_path):
                continue

            with open(file_path, 'r', encoding='utf-8') as f:
                for line in f:
                    str_list = line.split(" ")
                    c, x, y, w, h, o = [float(val) for val in str_list]
                    c = int(c)
                    x = round(x * width)
                    y = round(y * height)
                    w = round(w * width)
                    h = round(h * height)
                    o = int(o)
                    item = {
                        "id": annotations_id,
                        "image_id": image_id,
                        "category_id": c,
                        "bbox": [
                            x,
                            y,
                            w,
                            h
                        ],
                        "height": h,
                        "occlusion": o,
                        "ignore": 0
                    }
                    annotations.append(item)
                    annotations_id += 1
        data["annotations"] = annotations
        
    except FileNotFoundError:
        print("디렉토리를 찾을 수 없습니다.")
    except Exception as e:
        print(f"오류 발생: {e}")


    data["categories"] = [
        {
            "id": 0,
            "name": "person"
        },
        {
            "id": 1,
            "name": "cyclist"
        },
        {
            "id": 2,
            "name": "people"
        },
        {
            "id": 3,
            "name": "person?"
        }
    ]

    try:
        with open(output_file, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)
        
        print(f'텍스트 파일들을 JSON 파일 {output_file}로 변환하였습니다.')
    
    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")
    except Exception as e:
        print(f"오류 발생: {e}")

# 사용 예시
input_txt_file = 'split/train-v000true.txt'
label_directory = 'labels'
output_json_file = 'KAIST_annotation0.json'
height = 512
width = 640

txt_to_json(input_txt_file, label_directory, output_json_file)
