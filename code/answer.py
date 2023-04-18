answer_list=[]
num=0

def set_answer(aw):
    global answer_list
    answer_list=aw
    print("set answer --> ",answer_list)
def get_answer():
    return answer_list
def set_num(n):
    global num
    num+=1
    print("set num --> ",num)
def get_num():
    return num