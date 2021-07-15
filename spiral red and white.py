# 8.4
'''fname = input("Enter file name: ")
fh = open(fname)
lst = list()                       
for line in fh:                    
   
    word = line.rstrip().split()
    for element in word:
        if element in lst:         
            continue               
        else:                     
            lst.append(element)
lst.sort()
print(lst)'''


# 8.5
'''fhand = open("mbox-short.txt")
count = 0
for line in fhand:
    line = line.rstrip()
    if line == "":
        continue

    words = line.split()
    if words[0] != "From":
        continue

    print(words[1])
    count = count+1

print("There were", count, "lines in the file with From as the first word")'''

# 10.2
'''name = raw_input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
d = dict()
for line in handle:
    if not line.startswith("From "):
        continue
    else:
        line = line.split()
        line = line[5]
        line = line[0:2]
        d[line] = d.get(line, 0)+1

lst = list()
for value, count in d.items():
    lst.append((value, count))

lst.sort()
for value, count in lst:
    print (value, count)'''


'''def exam_grade(score):
    if score > 95:
        grade = "Top Score"
    elif 95 >= score > 60:
        grade = "Pass"
    else:
        grade = "Fail"
    return(grade)


print(exam_grade(65))  # Should be Pass
print(exam_grade(55))  # Should be Fail
print(exam_grade(60))  # Should be Pass
print(exam_grade(95))  # Should be Pass
print(exam_grade(100))  # Should be Top Score
print(exam_grade(0))  # Should be Fail
'''


'''def sum(x, y):
    return(x+y)


print(sum(sum(1, 2), sum(3, 4)))'''

'''sports = ['cricket', 'football', 'volleyball', 'baseball',
          'softball', 'track and field', 'curling', 'ping pong', 'hockey']
last = sports[-3:]
print(last)'''

'''by = "You are"
az = "doing a great "
io = "job"
qy = "keep it up!"
message = str(by), + str(az) + io + qy
print(message)'''


'''import turtle
wn = turtle.Screen()
wn.bgcolor("black")

alex = turtle.Turtle()
alex.pensize(1)
alex.color("yellow")
alex.speed(0)
alex.hideturtle()

for o in range(17):
    alex.forward(80)
    alex.left(90)
    alex.right(175)
    alex.circle(20)

wn.exitonclick()'''


'''import turtle
turtle.bgcolor("white")

star = turtle.Turtle()
star.speed(0)
for i in range(6):
    for colors in ["red", "yellow", "green", "cyan", "black", "pink", "magenta"]:
        star.fillcolor(colors)
        star.tiltangle(50)
        star.circle(80)
turtle.done()'''


def counter(start, stop):
    x = start
    if x > stop:
        return_string = "Counting down: "
        while x >= stop:
            return_string += str(x)
            if x > stop:
                return_string += ","
        x = x - 1
    else:
        return_string = "Counting up: "
        while x <= stop:
            return_string += str(x)
            if x < stop:
                return_string += ","
            x = x+1
    return return_string


print(counter(1, 10))
print(counter(2, 1))
print(counter(5, 5))
