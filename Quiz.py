def pregnancyQuiz():
    #Questions in tuple to store multi questions
    pregnancyQuestions = ("During pregnancy, which vitamin is particularly important for fetal development?",
                 "What is the average length of a full-term pregnancy in weeks? ",
                 "Which hormone is commonly referred to as the 'pregnancy hormone'? ",
                 "What is the medical term for severe morning sickness during pregnancy?",
                 "Is Edna Lynn Pregnant ")


    # Double tuple for choices for each pregnancy Questions. Per inner tuple corresponds to opt A , B , C for
    # above quiz question

    choices = (("A. Vitamin A", "B. Folic Acid", "C. Vitamin C"),
               ("A. 40 Weeks ", "B. 42 Weeks", "C. 30 Weeks"),
               ("A. Progesterone", "B. Insulin", "C. Estrogen"),
               ("A. Hypertension", "B. Hyperemesis gravidarum", "C. Preeclampsia"),
               ("A. Yes", "B. No", "C. I dont know" ))

    # Using another tuple, but singular storing the correct choices for answer.

    answers = ("B", "A", "A", "B", "A")

    # Initializing guesses in an empty list
    guesses = []

    #initialize score to 0
    score = 0

    #initialize to 0 to keep track of current question in index
    questionCount = 0

    for question in pregnancyQuestions:
        print("★★★★★")
        print(question)
        for option in choices[questionCount]:
            print(option)

        theGuess = input("★Enter your answer: A B C  ").upper()
        guesses.append(theGuess)
        if theGuess == answers[questionCount]:
            score += 1
            print("★CORRECT!")
        else:
            print("INCORRECT!")
            print(f"{answers[questionCount]} is the correct answer")
        questionCount += 1

    print("★★★FINAL★★")

    score = int(score / len(pregnancyQuestions) * 100) # Calculate the final score ; score divide by length of pregnancy question multiply by 100
    print(f"Final Score {score}%")