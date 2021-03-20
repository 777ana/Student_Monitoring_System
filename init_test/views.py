from django.shortcuts import render, redirect
from .models import test, student_score


# Create your views here.
def take_test(request):
    # if request.method=='POST':
    #
    # else:
    user_id = request.user.id
    print(user_id)
    if request.method == 'POST':
        # import pdb
        # pdb.set_trace()
        is_conscientious = request.POST['1'][0]
        enjoy_meeting_new_people = request.POST['2'][0]
        like_helping_people = request.POST['3'][0]
        vivid_imagination = request.POST['4'][0]
        easily_disappointed = request.POST['5'][0]
        engage_in_Co_curriculars = request.POST['6']
        best_describe_your_skillset = request.POST['7']
        co_curricular_involves_teamwork = request.POST['8']
        describe_your_strength = request.POST['9']
        job_do_you_prefer = request.POST['10']

        # some variables
        organised = False
        stubborn = False
        introvert = False
        extrovert = False
        agreeable = False
        passive = False
        creative = False
        unpredictable = False
        neurotic = False
        regularity = False
        efficiency = False
        teamwork = False
        memory = False
        psa = False
        business = False
        management = False
        technical = False
        entrepreneur = False
        versatility = False

        if is_conscientious == '3' or is_conscientious == '4':
            organised = True
        else:
            stubborn = True
        if enjoy_meeting_new_people == '3' or enjoy_meeting_new_people == '4':
            extrovert = True
        else:
            introvert = True
        if like_helping_people == '3' or like_helping_people == '4':
            agreeable = True
        else:
            passive = True
        if vivid_imagination == '3' or vivid_imagination == '4':
            creative = True
        else:
            unpredictable = True
        if easily_disappointed == '3' or easily_disappointed == '4':
            neurotic = True
        if best_describe_your_skillset == 'Consistency ' or best_describe_your_skillset == 'Dexterity Explanation':
            regularity = True
        elif best_describe_your_skillset == 'Spontaneity':
            efficiency = True
        if job_do_you_prefer == 'Management':
            management = True
            business = True
        elif job_do_you_prefer == 'Technical':
            technical = True
        elif job_do_you_prefer == 'Entrepreneur':
            entrepreneur = True
            business = True
        else:
            pass
        if co_curricular_involves_teamwork == 'Yes ':
            teamwork = True
        if engage_in_Co_curriculars == 'Yes ':
            versatility = True
        if describe_your_strength == 'Memory ':
            memory = True
        elif describe_your_strength == 'Logical Reasoning Explanation' or describe_your_strength == 'Crirtical Thinking':
            psa = True

        result = {'organised': organised, 'stubborn': stubborn, 'introvert': introvert, 'extrovert': extrovert,
                  'agreeable': agreeable, 'passive': passive, 'creative': creative, 'unpredictable': unpredictable,
                  'neurotic': neurotic, 'regularity': regularity, 'efficiency': efficiency, 'teamwork': teamwork,
                  'memory': memory, 'psa': psa, 'business': business, 'management': management,
                  'technical': technical, 'entrepreneur': entrepreneur, 'versatility': versatility}
        if not student_score.objects.filter(student_id=user_id).exists():
            student = student_score.objects.create(organised=organised, stubborn=stubborn, introvert=introvert,
                                                   extrovert=extrovert, agreeable=agreeable, passive=passive,
                                                   creative=creative, unpredictable=unpredictable, neurotic=neurotic,
                                                   regularity=regularity, efficiency=efficiency, teamwork=teamwork,
                                                   memory=memory, psa=psa, business=business, management=management,
                                                   technical=technical, entrepreneur=entrepreneur,
                                                   versatility=versatility, student_id=user_id)
            student.save()
            print("result_created")
        else:
            student_score.objects.filter(student_id=user_id).update(organised=organised, stubborn=stubborn,
                                                                    introvert=introvert,
                                                                    extrovert=extrovert, agreeable=agreeable,
                                                                    passive=passive,
                                                                    creative=creative, unpredictable=unpredictable,
                                                                    neurotic=neurotic,
                                                                    regularity=regularity, efficiency=efficiency,
                                                                    teamwork=teamwork,
                                                                    memory=memory, psa=psa, business=business,
                                                                    management=management,
                                                                    technical=technical, entrepreneur=entrepreneur,
                                                                    versatility=versatility)
            return redirect('dashboard')

    if request.method == 'GET':
        exam = test.objects.all()
        return render(request, 'take_test.html', {'exam': exam})
