list_questions=["capital of india,{c}".format(c="delhi"),"mp biggest city,{s}".format(s="indore"),"capital of rajasthan,{r}".format(r="jaipur")]
l=len(list_questions)
print("hello!,welcome to the 🎮")
score=0
for i in list_questions :
    p=i.split(",")
    print(p[0])
    ans=input("entered answer: ")
    final_ans= ans.lower().strip()
    if p[1]==final_ans:
        score+=1
    print("move for next question")
print("your score is{j}".format(j=score))
if score==l:
    print("you give all the correct answer of the questions")
elif score==0:
    print("your all answer of the questions is wrong")
elif score<l:
    print("wrong answer of any questions")
print("THANKS FOR PLAYING THESE INTRESTING GAME")
print("END OF THE GAME")