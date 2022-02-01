import tkinter
from tkinter import DISABLED
from tkinter.constants import HORIZONTAL
from tkinter.constants import X
from tkinter.ttk import Separator

# 语文、数学、英语、科学 的数组
import xlrd

chinese = []
mathematics = []
english = []
science = []

choice_sum: int
choice_correct: int
fill_sum: int
fill_correct: int
answer_sum: int
answer_correct: int

# 定义显示窗口的标签
label_chinese_average: tkinter.Label
label_chinese_median: tkinter.Label
label_mathematics_average: tkinter.Label
label_mathematics_median: tkinter.Label
label_english_average: tkinter.Label
label_english_median: tkinter.Label
label_science_average: tkinter.Label
label_science_median: tkinter.Label
label_choice_score: tkinter.Label
label_fill_score: tkinter.Label
label_answer_score: tkinter.Label

text_comment: tkinter.Text


# 读入1门课的成绩
def read_one_scores(filename: str, subject: list):
    # 先清空数组
    subject.clear()

    # 打开文件
    with open(filename, 'r') as f:
        # 文件里的每一行字，都存到数组里
        for line in f.readlines():
            line = line.strip('\n')
            subject.append(int(line))


# 读入所有课的成绩
def read_all_scores():
    # 读入语文
    read_one_scores('Chinese.txt', chinese)
    # 读入数学
    read_one_scores('Mathematics.txt', mathematics)
    # 读入英语
    read_one_scores('English.txt', english)
    # 读入科学
    read_one_scores('Science.txt', science)


# 计算1门课的平均分
def compute_one_average(subject: list):
    # 先让总和为0
    sum_subject = 0

    # 把每一个分数都加到 总和 里
    for score in subject:
        sum_subject += score

    # 返回 总和 除以 个数
    return sum_subject / len(subject)


# 计算所有课的平均分
def compute_all_average():
    # 计算语文
    label_chinese_average['text'] = '语文成绩平均数\n' + str(compute_one_average(chinese))
    # 计算数学
    label_mathematics_average['text'] = '数学成绩平均数\n' + str(compute_one_average(mathematics))
    # 计算英语
    label_english_average['text'] = '英语成绩平均数\n' + str(compute_one_average(english))
    # 计算科学
    label_science_average['text'] = '科学成绩平均数\n' + str(compute_one_average(science))


# 找到队伍里最大的
def find_largest_in_list(subject: list):
    # 设 最大的数为0
    num_largest = 0
    # 从第0个位置开始，看看谁更大
    num_index = 0
    while num_index < len(subject):
        # 找到更大的数，就记下来
        if subject[num_index] >= subject[num_largest]:
            num_largest = num_index
        num_index += 1
    # 返回最大的数
    return num_largest


# 计算1门课的中位数
def compute_one_median(parameter: list):
    # 计算 一共有多少个数
    subject = parameter[:]
    len_subject = len(subject)

    # 如果有 奇数个
    if len_subject % 2 == 1:
        half_len_subject = len_subject // 2 + 1
        index = 0
        while index < half_len_subject - 1:
            # 一直找最大的数，然后丢掉最大的数
            largest_in_subject = find_largest_in_list(subject)
            subject.pop(largest_in_subject)
            index += 1
        # 返回最中间的1个数
        return subject[find_largest_in_list(subject)]

    # 如果有 偶数个
    else:
        half_len_subject = len_subject // 2
        index = 0
        while index < half_len_subject - 1:
            # 一直找最大的数，然后丢掉最大的数
            largest_in_subject = find_largest_in_list(subject)
            subject.pop(largest_in_subject)
            index += 1

        # 把最中间的2个数求平均，返回
        num_median_former = find_largest_in_list(subject)
        median_former = subject[num_median_former]
        subject.pop(num_median_former)
        num_median_latter = find_largest_in_list(subject)
        median_latter = subject[num_median_latter]
        return (median_former + median_latter) / 2


# 计算所有课的中位数
def compute_all_median():
    # 重复4次
    label_chinese_median['text'] = '语文成绩中位数\n' + str(compute_one_median(chinese))
    label_mathematics_median['text'] = '数学成绩中位数\n' + str(compute_one_median(mathematics))
    label_english_median['text'] = '英语成绩中位数\n' + str(compute_one_median(english))
    label_science_median['text'] = '科学成绩中位数\n' + str(compute_one_median(science))


# 显示1门课的折线图
def show_subject_details(name: str, subject: list):
    # 根据数组里取出来的成绩，画折线图
    window_subject_details = tkinter.Tk()
    window_subject_details.title(name + '详情')
    canvas_subject = tkinter.Canvas(window_subject_details)
    canvas_subject['width'] = '1200'
    canvas_subject['height'] = '150'
    index = 0
    while index < len(subject) - 1:
        x1 = (index + 1) * 100
        y1 = 120 - subject[index]
        x2 = (index + 2) * 100
        y2 = 120 - subject[index + 1]
        canvas_subject.create_oval(x1 - 5, y1 - 5, x1 + 5, y1 + 5)
        canvas_subject.create_text(x1 - 20, y1, text=subject[index])
        canvas_subject.create_text(x1, 140, text='第' + str(index + 1) + '次')
        canvas_subject.create_line(x1, y1, x2, y2)
        canvas_subject.create_oval(x2 - 5, y2 - 5, x2 + 5, y2 + 5)
        canvas_subject.create_text(x2 - 20, y2, text=subject[index + 1])
        canvas_subject.create_text(x2, 140, text='第' + str(index + 2) + '次')
        index += 1
    canvas_subject.pack()
    window_subject_details.mainloop()


# 显示语文课的折线图
def show_chinese_details():
    show_subject_details('语文', chinese)


# 显示数学课的折线图
def show_mathematics_details():
    show_subject_details('数学', mathematics)


# 显示英语课的折线图
def show_english_details():
    show_subject_details('英语', english)


# 显示科学课的折线图
def show_science_details():
    show_subject_details('科学', science)


def read_question_scores():
    question_scores_workbook = xlrd.open_workbook('Question Type Score.xls')
    question_scores_worksheet = question_scores_workbook.sheet_by_name('Sheet1')
    global choice_sum
    global choice_correct
    global fill_sum
    global fill_correct
    global answer_sum
    global answer_correct
    choice_sum = int(question_scores_worksheet.cell(1, 0).value)
    choice_correct = int(question_scores_worksheet.cell(1, 1).value)
    fill_sum = int(question_scores_worksheet.cell(1, 2).value)
    fill_correct = int(question_scores_worksheet.cell(1, 3).value)
    answer_sum = int(question_scores_worksheet.cell(1, 4).value)
    answer_correct = int(question_scores_worksheet.cell(1, 5).value)
    label_choice_score['text'] = '选择判断题\n' + str(choice_correct) + '/' + str(choice_sum)
    label_fill_score['text'] = '填空题\n' + str(fill_correct) + '/' + str(fill_sum)
    label_answer_score['text'] = '简答题\n' + str(answer_correct) + '/' + str(answer_sum)


def show_comment():
    state = 1
    if choice_correct / choice_sum > 0.67: state += 4
    if fill_correct / fill_sum > 0.67: state += 2
    if answer_correct / answer_sum > 0.67: state += 1
    comments_workbook = xlrd.open_workbook('Comments.xls')
    comments_worksheet = comments_workbook.sheet_by_name('Sheet1')

    text_comment.insert('0.0', comments_worksheet.cell(state, 4).value)


if __name__ == '__main__':
    # 主函数，显示出窗口界面

    window = tkinter.Tk()
    window.title('成绩分析')

    label_chinese_average = tkinter.Label(window, text='语文成绩平均数\n')
    label_chinese_average.grid(row=1, column=1)
    label_chinese_median = tkinter.Label(window, text='语文成绩中位数\n')
    label_chinese_median.grid(row=1, column=2)
    label_mathematics_average = tkinter.Label(window, text='数学成绩平均数\n')
    label_mathematics_average.grid(row=2, column=1)
    label_mathematics_median = tkinter.Label(window, text='数学成绩中位数\n')
    label_mathematics_median.grid(row=2, column=2)
    label_english_average = tkinter.Label(window, text='英语成绩平均数\n')
    label_english_average.grid(row=3, column=1)
    label_english_median = tkinter.Label(window, text='英语成绩中位数\n')
    label_english_median.grid(row=3, column=2)
    label_science_average = tkinter.Label(window, text='科学成绩平均数\n')
    label_science_average.grid(row=4, column=1)
    label_science_median = tkinter.Label(window, text='科学成绩中位数\n')
    label_science_median.grid(row=4, column=2)

    button_read_scores = tkinter.Button(window, text='读入全科成绩', command=read_all_scores)
    button_read_scores.grid(row=0, column=0)
    button_compute_average_scores = tkinter.Button(window, text='计算成绩平均数', command=compute_all_average)
    button_compute_average_scores.grid(row=0, column=1)
    button_compute_median_scores = tkinter.Button(window, text='计算成绩中位数', command=compute_all_median)
    button_compute_median_scores.grid(row=0, column=2)

    button_show_chinese_details = tkinter.Button(window, text='显示语文详情', command=show_chinese_details)
    button_show_chinese_details.grid(row=1, column=0)
    button_show_mathematics_details = tkinter.Button(window, text='显示数学详情', command=show_mathematics_details)
    button_show_mathematics_details.grid(row=2, column=0)
    button_show_english_details = tkinter.Button(window, text='显示英语详情', command=show_english_details)
    button_show_english_details.grid(row=3, column=0)
    button_show_science_details = tkinter.Button(window, text='显示科学详情', command=show_science_details)
    button_show_science_details.grid(row=4, column=0)

    sep = Separator(window, orient=HORIZONTAL)
    sep.grid(row=5, columnspan=5, sticky=(tkinter.W, tkinter.E))

    label_choice_score = tkinter.Label(window, text='选择判断题\n')
    label_choice_score.grid(row=6, column=1)
    label_fill_score = tkinter.Label(window, text='填空题\n')
    label_fill_score.grid(row=6, column=2)
    label_answer_score = tkinter.Label(window, text='简答题\n')
    label_answer_score.grid(row=6, column=3)

    button_read_scores = tkinter.Button(window, text='读入题型答对情况', command=read_question_scores)
    button_read_scores.grid(row=6, column=0)
    button_read_scores = tkinter.Button(window, text='智能诊断', command=show_comment)
    button_read_scores.grid(row=7, column=0)

    text_comment = tkinter.Text(window, height=5, width=30)
    #text_comment.config(state=DISABLED)
    text_comment.grid(row=7, column=1, columnspan=3)
    window.mainloop()
