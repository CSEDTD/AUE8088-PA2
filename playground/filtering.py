def split_lines(input_file, condition, output_file_true, output_file_false):
    try:
        with open(input_file, 'r', encoding='utf-8') as f_input, \
             open(output_file_true, 'w', encoding='utf-8') as f_true, \
             open(output_file_false, 'w', encoding='utf-8') as f_false:
            
            for line in f_input:
                if condition(line):
                    f_true.write(line)
                else:
                    f_false.write(line)
        
        print(f'파일 {input_file}을(를) 조건에 맞게 분류하여 {output_file_true}와 {output_file_false}로 저장하였습니다.')
    
    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")
    
    except Exception as e:
        print(f"오류 발생: {e}")

# 사용 예시
input_file = 'train-all-04.txt'         # 입력 파일명
output_file_true = 'true.txt'    # 조건을 만족하는 줄을 저장할 파일명
output_file_false = 'false.txt'  # 조건을 만족하지 않는 줄을 저장할 파일명

# 예시 조건: 줄의 길이가 10자 이상인 경우를 조건으로 설정
def condition(line):
    return (line.strip())[-12] >= '5'

split_lines(input_file, condition, output_file_true, output_file_false)
