# 등급에 따른 과목평점 정의
grade_to_point = {
    "A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0,
    "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0,
    "F": 0.0
}

# 총 학점과 총 평점 계산 변수 초기화
total_credits = 0.0
total_points = 0.0

# 입력 처리
for _ in range(20):
    subject, credit, grade = input().split()
    credit = float(credit)  # 학점은 실수로 변환

    # P 등급은 계산 제외
    if grade == "P":
        continue

    # 총합 계산
    total_credits += credit
    total_points += credit * grade_to_point[grade]

# 전공평점 계산
major_gpa = total_points / total_credits

# 결과 출력 (소수점 4자리)
print(f"{major_gpa:.6f}")