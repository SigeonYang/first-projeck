for i in range(1,51):
    with open("{0}.주차.txt".format(str(i)), "w", encoding="utf8") as report:
      report.write("- {0} 주차 주간보고 -\n부서 :\n이름 :\n업무 요약".format(str(i)))