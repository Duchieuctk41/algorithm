from operator import truediv

# calculate average of student
def calculateAverageOfStudent(totalScoreOfStudent, numberOfStudent):
    averageScore = totalScoreOfStudent/numberOfStudent
    return averageScore


# input number of student, only accept integer
def inputNumberOfStudent():
    num = 'str'
    inLoop = True
    while inLoop:
        num = input('Nhập số lượng học sinh: ')
        if num.isdigit():
            inLoop = False

    return int(num)

# input score of student, check type integer and only accept score from 0 - 10
def inputScoreOfStudent(i):
    inLoop = True
    while inLoop:
        print('Nhập điểm học sinh thứ ',i, ':', end = ' ')
        num = input()
        try:
            val = float(num)
            if 0 <= val and val <= 10:
                inLoop = False
                break
            print('Giá trị truyền vào trong khoảng từ [0 - 10] ')
        except ValueError:
            print('Giá trị truyền vào phải là số thực')

    return float(num)
    
# find student have maxScore and calculate total score of all student
def findMaxScoreAndCalculateTotalScore(numberOfStudent):
    totalScoreOfStudent = 0
    maxScore = 0
    for i in range(1,numberOfStudent+1):
        scoreOfStudent = inputScoreOfStudent(i)

        totalScoreOfStudent = totalScoreOfStudent + scoreOfStudent
        maxScore = max(maxScore, scoreOfStudent)
    
    return maxScore, totalScoreOfStudent

# main
def calculatetScoreOfStudent():
    numberOfStudent = inputNumberOfStudent()
    
    maxScore, totalScoreOfStudent = findMaxScoreAndCalculateTotalScore(numberOfStudent)
    print('\n\n')
    print('Số điểm cao nhất là: ',maxScore)

    averageScore = calculateAverageOfStudent(totalScoreOfStudent, numberOfStudent)
    print('Điểm trung bình: ',round(averageScore,2))

# call main function
calculatetScoreOfStudent()

def findMax(listScore):
    maxScore = 0
    for i in listScore:
        if i > maxScore:
            maxScore = i
    return maxScore

fdafds = [1,8,4,10]
print(findMax(fdafds))
print(max(fdafds))
