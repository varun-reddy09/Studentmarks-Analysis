# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html



import sys
sys.path.append('C:/Users/Varun Reddy/PycharmProjects/ScrapyTutorial/studentApp')
from main.models import Profile, SemMarks, SemPercentage,User





class QuotetutorialPipeline(object):
    def process_item(self, item, spider):
        print("print:",item['title'][0])
        semesters_list=[item['first_semester'],item['second_semester'],item['third_semester'],item['fourth_semester'],item['fifth_semester'],item['sixth_semester']]
        for thing in semesters_list:
            k=0
            count=0
            for i in range(2,len(thing)):
                count += 1
                if ((i!=k+3+19)&((thing[i]== '-')|(thing[i]=='Ab')|(thing[i]=='A'))):
                    thing[i]=0

                if count==40:
                    k+=21
                    count=20


        user1 = User.objects.get(username= item[ 'hall_ticket'][0][1:])
        try:
            person = Profile.objects.get(user=user1)
            person= Profile.objects.filter(user=user1).update(user = user1, title = item['title'][0],hall_ticket= item[ 'hall_ticket'][0][1:], student_name = item['student_name'][0], current_branch = item['current_branch'][0], proctor_id = item['proctor_id'][0])


        except (Profile.DoesNotExist):
            print("exception arised in profile")
            profile = Profile(user = user1, title = item['title'][0],hall_ticket= item[ 'hall_ticket'][0][1:], student_name = item['student_name'][0], current_branch = item['current_branch'][0], proctor_id = item['proctor_id'][0])
            profile.save()

        print("im here")
        j = 0
        for i in range(12):

                i=i+j
                try:
                    marks = SemMarks.objects.get(user=user1, semester = 1,subject_name= item['first_semester'][i+3])
                    marks = SemMarks.objects.filter(user=user1, semester =1,subject_name= item['first_semester'][i+3]).update(user=user1, semester=1,subject_name = item['first_semester'][i+3],int1_maxMarks = float(item['first_semester'][i+3+1]),int1_secMarks = float(item['first_semester'][i+3+2]), int2_maxMarks = float(item['first_semester'][i+3+3]), int2_secMarks = float(item['first_semester'][i+3+4]), ass1_maxMarks = float(item['first_semester'][i+3+5]), ass1_secMarks = float(item['first_semester'][i+3+6]), ass2_maxMarks = float(item['first_semester'][i+3+7]), ass2_secMarks = float(item['first_semester'][i+3+8]), ass3_maxMarks = float(item['first_semester'][i+3+9]), ass3_secMarks = float(item['first_semester'][i+3+10]), quiz1_maxMarks = float(item['first_semester'][i+3+11]), quiz1_secMarks = float(item['first_semester'][i+3+12]), quiz2_maxMarks = float(item['first_semester'][i+3+13]), quiz2_secMarks = float(item['first_semester'][i+3+14]), quiz3_maxMarks = float(item['first_semester'][i+3+15]), quiz3_secMarks = float(item['first_semester'][i+3+16]), sessional_maxMarks = float(item['first_semester'][i+3+17]), sessional_secMarks = float(item['first_semester'][i+3+18]), External_grade = item['first_semester'][i+3+19])
                    print("entered try")
                except (SemMarks.DoesNotExist):
                    print("exception occured in marks table")
                    marks = SemMarks(user=user1,semester=1, subject_name = item['first_semester'][i+3],int1_maxMarks = float(item['first_semester'][i+3+1]),int1_secMarks = float(item['first_semester'][i+3+2]), int2_maxMarks = float(item['first_semester'][i+3+3]), int2_secMarks = float(item['first_semester'][i+3+4]), ass1_maxMarks = float(item['first_semester'][i+3+5]), ass1_secMarks = float(item['first_semester'][i+3+6]), ass2_maxMarks = float(item['first_semester'][i+3+7]), ass2_secMarks = float(item['first_semester'][i+3+8]), ass3_maxMarks = float(item['first_semester'][i+3+9]), ass3_secMarks = float(item['first_semester'][i+3+10]), quiz1_maxMarks = float(item['first_semester'][i+3+11]), quiz1_secMarks = float(item['first_semester'][i+3+12]), quiz2_maxMarks = float(item['first_semester'][i+3+13]), quiz2_secMarks = float(item['first_semester'][i+3+14]), quiz3_maxMarks = float(item['first_semester'][i+3+15]), quiz3_secMarks = float(item['first_semester'][i+3+16]), sessional_maxMarks = float(item['first_semester'][i+3+17]), sessional_secMarks = float(item['first_semester'][i+3+18]), External_grade = item['first_semester'][i+3+19])
                    marks.save()
                j+=20

        try:
            percentage = SemPercentage.objects.get(user=user1,semester=1)
            percentage = SemPercentage.objects.filter(user=user1,semester=1).update(user =user1,semester=1, int1_percentage = item['first_semester'][-10], int2_percentage = float(item['first_semester'][-9]), ass1_percentage = float(item['first_semester'][-8]), ass2_percentage = float(item['first_semester'][-7]), ass3_percentage = float(item['first_semester'][-6]), quiz1_percentage = float(item['first_semester'][-5]), quiz2_percentage = float(item['first_semester'][-4]), quiz3_percentage = float(item['first_semester'][-3]) , sessional_pecentage =float(item['first_semester'][-2]) ,SGPA =item['first_semester'][-1][-4:])
            print("try has",float(item['first_semester'][-1][-4:]))
        except(SemPercentage.DoesNotExist):
            print("exception occured in Percentage table")
            percentage = SemPercentage(user =user1,semester=1, int1_percentage = float(item['first_semester'][-10]), int2_percentage = float(item['first_semester'][-9]), ass1_percentage = float(item['first_semester'][-8]), ass2_percentage = float(item['first_semester'][-7]), ass3_percentage = float(item['first_semester'][-6]), quiz1_percentage = float(item['first_semester'][-5]), quiz2_percentage = float(item['first_semester'][-4]), quiz3_percentage = float(item['first_semester'][-3]) , sessional_pecentage =float(item['first_semester'][-2]) ,SGPA =float(item['first_semester'][-1][-4:]))
            percentage.save()
#-----------------------------------------------------------------------2nd semester--------------------------------------------------------------------------+

        j = 0
        for i in range(12):

            i = i + j
            try:
                marks = SemMarks.objects.get(user=user1, semester=2, subject_name=item['second_semester'][i + 3])
                marks = SemMarks.objects.filter(user=user1, semester=2,
                                                subject_name=item['second_semester'][i + 3]).update(user=user1,
                                                                                                   semester=2,
                                                                                                   subject_name=item[
                                                                                                       'second_semester'][
                                                                                                       i + 3],
                                                                                                   int1_maxMarks=float(
                                                                                                       item[
                                                                                                           'second_semester'][
                                                                                                           i + 3 + 1]),
                                                                                                   int1_secMarks=float(
                                                                                                       item[
                                                                                                           'second_semester'][
                                                                                                           i + 3 + 2]),
                                                                                                   int2_maxMarks=float(
                                                                                                       item[
                                                                                                           'second_semester'][
                                                                                                           i + 3 + 3]),
                                                                                                   int2_secMarks=float(
                                                                                                       item[
                                                                                                           'second_semester'][
                                                                                                           i + 3 + 4]),
                                                                                                   ass1_maxMarks=float(
                                                                                                       item[
                                                                                                           'second_semester'][
                                                                                                           i + 3 + 5]),
                                                                                                   ass1_secMarks=float(
                                                                                                       item[
                                                                                                           'second_semester'][
                                                                                                           i + 3 + 6]),
                                                                                                   ass2_maxMarks=float(
                                                                                                       item[
                                                                                                           'second_semester'][
                                                                                                           i + 3 + 7]),
                                                                                                   ass2_secMarks=float(
                                                                                                       item[
                                                                                                           'second_semester'][
                                                                                                           i + 3 + 8]),
                                                                                                   ass3_maxMarks=float(
                                                                                                       item[
                                                                                                           'second_semester'][
                                                                                                           i + 3 + 9]),
                                                                                                   ass3_secMarks=float(
                                                                                                       item[
                                                                                                           'second_semester'][
                                                                                                           i + 3 + 10]),
                                                                                                   quiz1_maxMarks=float(
                                                                                                       item[
                                                                                                           'second_semester'][
                                                                                                           i + 3 + 11]),
                                                                                                   quiz1_secMarks=float(
                                                                                                       item[
                                                                                                           'second_semester'][
                                                                                                           i + 3 + 12]),
                                                                                                   quiz2_maxMarks=float(
                                                                                                       item[
                                                                                                           'second_semester'][
                                                                                                           i + 3 + 13]),
                                                                                                   quiz2_secMarks=float(
                                                                                                       item[
                                                                                                           'second_semester'][
                                                                                                           i + 3 + 14]),
                                                                                                   quiz3_maxMarks=float(
                                                                                                       item[
                                                                                                           'second_semester'][
                                                                                                           i + 3 + 15]),
                                                                                                   quiz3_secMarks=float(
                                                                                                       item[
                                                                                                           'second_semester'][
                                                                                                           i + 3 + 16]),
                                                                                                   sessional_maxMarks=float(
                                                                                                       item[
                                                                                                           'second_semester'][
                                                                                                           i + 3 + 17]),
                                                                                                   sessional_secMarks=float(
                                                                                                       item[
                                                                                                           'second_semester'][
                                                                                                           i + 3 + 18]),
                                                                                                   External_grade=item[
                                                                                                       'second_semester'][
                                                                                                       i + 3 + 19])
                print("entered try")
            except (SemMarks.DoesNotExist):
                print("exception occured in marks table")
                marks = SemMarks(user=user1, semester=2, subject_name=item['second_semester'][i + 3],
                                 int1_maxMarks=float(item['second_semester'][i + 3 + 1]),
                                 int1_secMarks=float(item['second_semester'][i + 3 + 2]),
                                 int2_maxMarks=float(item['second_semester'][i + 3 + 3]),
                                 int2_secMarks=float(item['second_semester'][i + 3 + 4]),
                                 ass1_maxMarks=float(item['second_semester'][i + 3 + 5]),
                                 ass1_secMarks=float(item['second_semester'][i + 3 + 6]),
                                 ass2_maxMarks=float(item['second_semester'][i + 3 + 7]),
                                 ass2_secMarks=float(item['second_semester'][i + 3 + 8]),
                                 ass3_maxMarks=float(item['second_semester'][i + 3 + 9]),
                                 ass3_secMarks=float(item['second_semester'][i + 3 + 10]),
                                 quiz1_maxMarks=float(item['second_semester'][i + 3 + 11]),
                                 quiz1_secMarks=float(item['second_semester'][i + 3 + 12]),
                                 quiz2_maxMarks=float(item['second_semester'][i + 3 + 13]),
                                 quiz2_secMarks=float(item['second_semester'][i + 3 + 14]),
                                 quiz3_maxMarks=float(item['second_semester'][i + 3 + 15]),
                                 quiz3_secMarks=float(item['second_semester'][i + 3 + 16]),
                                 sessional_maxMarks=float(item['second_semester'][i + 3 + 17]),
                                 sessional_secMarks=float(item['second_semester'][i + 3 + 18]),
                                 External_grade=item['second_semester'][i + 3 + 19])
                marks.save()
            j += 20

        try:
            percentage = SemPercentage.objects.get(user=user1, semester=2)
            percentage = SemPercentage.objects.filter(user=user1, semester=2).update(user=user1, semester=2,
                                                                                     int1_percentage=
                                                                                     item['second_semester'][-10],
                                                                                     int2_percentage=float(
                                                                                         item['second_semester'][-9]),
                                                                                     ass1_percentage=float(
                                                                                         item['second_semester'][-8]),
                                                                                     ass2_percentage=float(
                                                                                         item['second_semester'][-7]),
                                                                                     ass3_percentage=float(
                                                                                         item['second_semester'][-6]),
                                                                                     quiz1_percentage=float(
                                                                                         item['second_semester'][-5]),
                                                                                     quiz2_percentage=float(
                                                                                         item['second_semester'][-4]),
                                                                                     quiz3_percentage=float(
                                                                                         item['second_semester'][-3]),
                                                                                     sessional_pecentage=float(
                                                                                         item['second_semester'][-2]),
                                                                                     SGPA=item['second_semester'][-1][
                                                                                          -4:])
            print("try has", float(item['second_semester'][-1][-4:]))
        except(SemPercentage.DoesNotExist):
            print("exception occured in Percentage table")
            percentage = SemPercentage(user=user1, semester=2, int1_percentage=float(item['second_semester'][-10]),
                                       int2_percentage=float(item['second_semester'][-9]),
                                       ass1_percentage=float(item['second_semester'][-8]),
                                       ass2_percentage=float(item['second_semester'][-7]),
                                       ass3_percentage=float(item['second_semester'][-6]),
                                       quiz1_percentage=float(item['second_semester'][-5]),
                                       quiz2_percentage=float(item['second_semester'][-4]),
                                       quiz3_percentage=float(item['second_semester'][-3]),
                                       sessional_pecentage=float(item['second_semester'][-2]),
                                       SGPA=float(item['second_semester'][-1][-4:]))
            percentage.save()
        # -------------------------------------------------------3rd semester-----------------------------------

        j = 0
        for i in range(12):

            i = i + j
            try:
                marks = SemMarks.objects.get(user=user1, semester=3, subject_name=item['third_semester'][i + 3])
                marks = SemMarks.objects.filter(user=user1, semester=3,
                                                subject_name=item['third_semester'][i + 3]).update(user=user1,
                                                                                                   semester=3,
                                                                                                   subject_name=item[
                                                                                                       'third_semester'][
                                                                                                       i + 3],
                                                                                                   int1_maxMarks=float(
                                                                                                       item[
                                                                                                           'third_semester'][
                                                                                                           i + 3 + 1]),
                                                                                                   int1_secMarks=float(
                                                                                                       item[
                                                                                                           'third_semester'][
                                                                                                           i + 3 + 2]),
                                                                                                   int2_maxMarks=float(
                                                                                                       item[
                                                                                                           'third_semester'][
                                                                                                           i + 3 + 3]),
                                                                                                   int2_secMarks=float(
                                                                                                       item[
                                                                                                           'third_semester'][
                                                                                                           i + 3 + 4]),
                                                                                                   ass1_maxMarks=float(
                                                                                                       item[
                                                                                                           'third_semester'][
                                                                                                           i + 3 + 5]),
                                                                                                   ass1_secMarks=float(
                                                                                                       item[
                                                                                                           'third_semester'][
                                                                                                           i + 3 + 6]),
                                                                                                   ass2_maxMarks=float(
                                                                                                       item[
                                                                                                           'third_semester'][
                                                                                                           i + 3 + 7]),
                                                                                                   ass2_secMarks=float(
                                                                                                       item[
                                                                                                           'third_semester'][
                                                                                                           i + 3 + 8]),
                                                                                                   ass3_maxMarks=float(
                                                                                                       item[
                                                                                                           'third_semester'][
                                                                                                           i + 3 + 9]),
                                                                                                   ass3_secMarks=float(
                                                                                                       item[
                                                                                                           'third_semester'][
                                                                                                           i + 3 + 10]),
                                                                                                   quiz1_maxMarks=float(
                                                                                                       item[
                                                                                                           'third_semester'][
                                                                                                           i + 3 + 11]),
                                                                                                   quiz1_secMarks=float(
                                                                                                       item[
                                                                                                           'third_semester'][
                                                                                                           i + 3 + 12]),
                                                                                                   quiz2_maxMarks=float(
                                                                                                       item[
                                                                                                           'third_semester'][
                                                                                                           i + 3 + 13]),
                                                                                                   quiz2_secMarks=float(
                                                                                                       item[
                                                                                                           'third_semester'][
                                                                                                           i + 3 + 14]),
                                                                                                   quiz3_maxMarks=float(
                                                                                                       item[
                                                                                                           'third_semester'][
                                                                                                           i + 3 + 15]),
                                                                                                   quiz3_secMarks=float(
                                                                                                       item[
                                                                                                           'third_semester'][
                                                                                                           i + 3 + 16]),
                                                                                                   sessional_maxMarks=float(
                                                                                                       item[
                                                                                                           'third_semester'][
                                                                                                           i + 3 + 17]),
                                                                                                   sessional_secMarks=float(
                                                                                                       item[
                                                                                                           'third_semester'][
                                                                                                           i + 3 + 18]),
                                                                                                   External_grade=item[
                                                                                                       'third_semester'][
                                                                                                       i + 3 + 19])
                print("entered try")
            except (SemMarks.DoesNotExist):
                print("exception occured in marks table")
                marks = SemMarks(user=user1, semester=3, subject_name=item['third_semester'][i + 3],
                                 int1_maxMarks=float(item['third_semester'][i + 3 + 1]),
                                 int1_secMarks=float(item['third_semester'][i + 3 + 2]),
                                 int2_maxMarks=float(item['third_semester'][i + 3 + 3]),
                                 int2_secMarks=float(item['third_semester'][i + 3 + 4]),
                                 ass1_maxMarks=float(item['third_semester'][i + 3 + 5]),
                                 ass1_secMarks=float(item['third_semester'][i + 3 + 6]),
                                 ass2_maxMarks=float(item['third_semester'][i + 3 + 7]),
                                 ass2_secMarks=float(item['third_semester'][i + 3 + 8]),
                                 ass3_maxMarks=float(item['third_semester'][i + 3 + 9]),
                                 ass3_secMarks=float(item['third_semester'][i + 3 + 10]),
                                 quiz1_maxMarks=float(item['third_semester'][i + 3 + 11]),
                                 quiz1_secMarks=float(item['third_semester'][i + 3 + 12]),
                                 quiz2_maxMarks=float(item['third_semester'][i + 3 + 13]),
                                 quiz2_secMarks=float(item['third_semester'][i + 3 + 14]),
                                 quiz3_maxMarks=float(item['third_semester'][i + 3 + 15]),
                                 quiz3_secMarks=float(item['third_semester'][i + 3 + 16]),
                                 sessional_maxMarks=float(item['third_semester'][i + 3 + 17]),
                                 sessional_secMarks=float(item['third_semester'][i + 3 + 18]),
                                 External_grade=item['third_semester'][i + 3 + 19])
                marks.save()
            j += 20

        try:
            percentage = SemPercentage.objects.get(user=user1, semester=3)
            percentage = SemPercentage.objects.filter(user=user1, semester=3).update(user=user1, semester=3,
                                                                                     int1_percentage=
                                                                                     item['third_semester'][-10],
                                                                                     int2_percentage=float(
                                                                                         item['third_semester'][-9]),
                                                                                     ass1_percentage=float(
                                                                                         item['third_semester'][-8]),
                                                                                     ass2_percentage=float(
                                                                                         item['third_semester'][-7]),
                                                                                     ass3_percentage=float(
                                                                                         item['third_semester'][-6]),
                                                                                     quiz1_percentage=float(
                                                                                         item['third_semester'][-5]),
                                                                                     quiz2_percentage=float(
                                                                                         item['third_semester'][-4]),
                                                                                     quiz3_percentage=float(
                                                                                         item['third_semester'][-3]),
                                                                                     sessional_pecentage=float(
                                                                                         item['third_semester'][-2]),
                                                                                     SGPA=item['third_semester'][-1][
                                                                                          -4:])
            print("try has", float(item['third_semester'][-1][-4:]))
        except(SemPercentage.DoesNotExist):
            print("exception occured in Percentage table")
            percentage = SemPercentage(user=user1, semester=3, int1_percentage=float(item['third_semester'][-10]),
                                       int2_percentage=float(item['third_semester'][-9]),
                                       ass1_percentage=float(item['third_semester'][-8]),
                                       ass2_percentage=float(item['third_semester'][-7]),
                                       ass3_percentage=float(item['third_semester'][-6]),
                                       quiz1_percentage=float(item['third_semester'][-5]),
                                       quiz2_percentage=float(item['third_semester'][-4]),
                                       quiz3_percentage=float(item['third_semester'][-3]),
                                       sessional_pecentage=float(item['third_semester'][-2]),
                                       SGPA=float(item['third_semester'][-1][-4:]))
            percentage.save()

#--------------------------------------fourth semester-----------------------------------------------------------------

        j = 0
        for i in range(12):

            i = i + j
            try:
                marks = SemMarks.objects.get(user=user1, semester=4, subject_name=item['fourth_semester'][i + 3])
                marks = SemMarks.objects.filter(user=user1, semester=4,
                                                subject_name=item['fourth_semester'][i + 3]).update(user=user1,
                                                                                                   semester=4,
                                                                                                   subject_name=item[
                                                                                                       'fourth_semester'][
                                                                                                       i + 3],
                                                                                                   int1_maxMarks=float(
                                                                                                       item[
                                                                                                           'fourth_semester'][
                                                                                                           i + 3 + 1]),
                                                                                                   int1_secMarks=float(
                                                                                                       item[
                                                                                                           'fourth_semester'][
                                                                                                           i + 3 + 2]),
                                                                                                   int2_maxMarks=float(
                                                                                                       item[
                                                                                                           'fourth_semester'][
                                                                                                           i + 3 + 3]),
                                                                                                   int2_secMarks=float(
                                                                                                       item[
                                                                                                           'fourth_semester'][
                                                                                                           i + 3 + 4]),
                                                                                                   ass1_maxMarks=float(
                                                                                                       item[
                                                                                                           'fourth_semester'][
                                                                                                           i + 3 + 5]),
                                                                                                   ass1_secMarks=float(
                                                                                                       item[
                                                                                                           'fourth_semester'][
                                                                                                           i + 3 + 6]),
                                                                                                   ass2_maxMarks=float(
                                                                                                       item[
                                                                                                           'fourth_semester'][
                                                                                                           i + 3 + 7]),
                                                                                                   ass2_secMarks=float(
                                                                                                       item[
                                                                                                           'fourth_semester'][
                                                                                                           i + 3 + 8]),
                                                                                                   ass3_maxMarks=float(
                                                                                                       item[
                                                                                                           'fourth_semester'][
                                                                                                           i + 3 + 9]),
                                                                                                   ass3_secMarks=float(
                                                                                                       item[
                                                                                                           'fourth_semester'][
                                                                                                           i + 3 + 10]),
                                                                                                   quiz1_maxMarks=float(
                                                                                                       item[
                                                                                                           'fourth_semester'][
                                                                                                           i + 3 + 11]),
                                                                                                   quiz1_secMarks=float(
                                                                                                       item[
                                                                                                           'fourth_semester'][
                                                                                                           i + 3 + 12]),
                                                                                                   quiz2_maxMarks=float(
                                                                                                       item[
                                                                                                           'fourth_semester'][
                                                                                                           i + 3 + 13]),
                                                                                                   quiz2_secMarks=float(
                                                                                                       item[
                                                                                                           'fourth_semester'][
                                                                                                           i + 3 + 14]),
                                                                                                   quiz3_maxMarks=float(
                                                                                                       item[
                                                                                                           'fourth_semester'][
                                                                                                           i + 3 + 15]),
                                                                                                   quiz3_secMarks=float(
                                                                                                       item[
                                                                                                           'fourth_semester'][
                                                                                                           i + 3 + 16]),
                                                                                                   sessional_maxMarks=float(
                                                                                                       item[
                                                                                                           'fourth_semester'][
                                                                                                           i + 3 + 17]),
                                                                                                   sessional_secMarks=float(
                                                                                                       item[
                                                                                                           'fourth_semester'][
                                                                                                           i + 3 + 18]),
                                                                                                   External_grade=item[
                                                                                                       'fourth_semester'][
                                                                                                       i + 3 + 19])
                print("entered try")
            except (SemMarks.DoesNotExist):
                print("exception occured in marks table")
                marks = SemMarks(user=user1, semester=4, subject_name=item['fourth_semester'][i + 3],
                                 int1_maxMarks=float(item['fourth_semester'][i + 3 + 1]),
                                 int1_secMarks=float(item['fourth_semester'][i + 3 + 2]),
                                 int2_maxMarks=float(item['fourth_semester'][i + 3 + 3]),
                                 int2_secMarks=float(item['fourth_semester'][i + 3 + 4]),
                                 ass1_maxMarks=float(item['fourth_semester'][i + 3 + 5]),
                                 ass1_secMarks=float(item['fourth_semester'][i + 3 + 6]),
                                 ass2_maxMarks=float(item['fourth_semester'][i + 3 + 7]),
                                 ass2_secMarks=float(item['fourth_semester'][i + 3 + 8]),
                                 ass3_maxMarks=float(item['fourth_semester'][i + 3 + 9]),
                                 ass3_secMarks=float(item['fourth_semester'][i + 3 + 10]),
                                 quiz1_maxMarks=float(item['fourth_semester'][i + 3 + 11]),
                                 quiz1_secMarks=float(item['fourth_semester'][i + 3 + 12]),
                                 quiz2_maxMarks=float(item['fourth_semester'][i + 3 + 13]),
                                 quiz2_secMarks=float(item['fourth_semester'][i + 3 + 14]),
                                 quiz3_maxMarks=float(item['fourth_semester'][i + 3 + 15]),
                                 quiz3_secMarks=float(item['fourth_semester'][i + 3 + 16]),
                                 sessional_maxMarks=float(item['fourth_semester'][i + 3 + 17]),
                                 sessional_secMarks=float(item['fourth_semester'][i + 3 + 18]),
                                 External_grade=item['fourth_semester'][i + 3 + 19])
                marks.save()
            j += 20

        try:
            percentage = SemPercentage.objects.get(user=user1, semester=4)
            percentage = SemPercentage.objects.filter(user=user1, semester=4).update(user=user1, semester=4,
                                                                                     int1_percentage=
                                                                                     item['fourth_semester'][-10],
                                                                                     int2_percentage=float(
                                                                                         item['fourth_semester'][-9]),
                                                                                     ass1_percentage=float(
                                                                                         item['fourth_semester'][-8]),
                                                                                     ass2_percentage=float(
                                                                                         item['fourth_semester'][-7]),
                                                                                     ass3_percentage=float(
                                                                                         item['fourth_semester'][-6]),
                                                                                     quiz1_percentage=float(
                                                                                         item['fourth_semester'][-5]),
                                                                                     quiz2_percentage=float(
                                                                                         item['fourth_semester'][-4]),
                                                                                     quiz3_percentage=float(
                                                                                         item['fourth_semester'][-3]),
                                                                                     sessional_pecentage=float(
                                                                                         item['fourth_semester'][-2]),
                                                                                     SGPA=item['fourth_semester'][-1][
                                                                                          -4:])
            print("try has", float(item['fourth_semester'][-1][-4:]))
        except(SemPercentage.DoesNotExist):
            print("exception occured in Percentage table")
            percentage = SemPercentage(user=user1, semester=4, int1_percentage=float(item['fourth_semester'][-10]),
                                       int2_percentage=float(item['fourth_semester'][-9]),
                                       ass1_percentage=float(item['fourth_semester'][-8]),
                                       ass2_percentage=float(item['fourth_semester'][-7]),
                                       ass3_percentage=float(item['fourth_semester'][-6]),
                                       quiz1_percentage=float(item['fourth_semester'][-5]),
                                       quiz2_percentage=float(item['fourth_semester'][-4]),
                                       quiz3_percentage=float(item['fourth_semester'][-3]),
                                       sessional_pecentage=float(item['fourth_semester'][-2]),
                                       SGPA=float(item['fourth_semester'][-1][-4:]))
            percentage.save()
#--------------------------------------------------fifth semester-------------------------------------------------------
        j = 0
        for i in range(12):

            i = i + j
            try:
                marks = SemMarks.objects.get(user=user1, semester=5, subject_name=item['fifth_semester'][i + 3])
                marks = SemMarks.objects.filter(user=user1, semester=5,
                                                subject_name=item['fifth_semester'][i + 3]).update(user=user1,
                                                                                                   semester=5,
                                                                                                   subject_name=item[
                                                                                                       'fifth_semester'][
                                                                                                       i + 3],
                                                                                                   int1_maxMarks=float(
                                                                                                       item[
                                                                                                           'fifth_semester'][
                                                                                                           i + 3 + 1]),
                                                                                                   int1_secMarks=float(
                                                                                                       item[
                                                                                                           'fifth_semester'][
                                                                                                           i + 3 + 2]),
                                                                                                   int2_maxMarks=float(
                                                                                                       item[
                                                                                                           'fifth_semester'][
                                                                                                           i + 3 + 3]),
                                                                                                   int2_secMarks=float(
                                                                                                       item[
                                                                                                           'fifth_semester'][
                                                                                                           i + 3 + 4]),
                                                                                                   ass1_maxMarks=float(
                                                                                                       item[
                                                                                                           'fifth_semester'][
                                                                                                           i + 3 + 5]),
                                                                                                   ass1_secMarks=float(
                                                                                                       item[
                                                                                                           'fifth_semester'][
                                                                                                           i + 3 + 6]),
                                                                                                   ass2_maxMarks=float(
                                                                                                       item[
                                                                                                           'fifth_semester'][
                                                                                                           i + 3 + 7]),
                                                                                                   ass2_secMarks=float(
                                                                                                       item[
                                                                                                           'fifth_semester'][
                                                                                                           i + 3 + 8]),
                                                                                                   ass3_maxMarks=float(
                                                                                                       item[
                                                                                                           'fifth_semester'][
                                                                                                           i + 3 + 9]),
                                                                                                   ass3_secMarks=float(
                                                                                                       item[
                                                                                                           'fifth_semester'][
                                                                                                           i + 3 + 10]),
                                                                                                   quiz1_maxMarks=float(
                                                                                                       item[
                                                                                                           'fifth_semester'][
                                                                                                           i + 3 + 11]),
                                                                                                   quiz1_secMarks=float(
                                                                                                       item[
                                                                                                           'fifth_semester'][
                                                                                                           i + 3 + 12]),
                                                                                                   quiz2_maxMarks=float(
                                                                                                       item[
                                                                                                           'fifth_semester'][
                                                                                                           i + 3 + 13]),
                                                                                                   quiz2_secMarks=float(
                                                                                                       item[
                                                                                                           'fifth_semester'][
                                                                                                           i + 3 + 14]),
                                                                                                   quiz3_maxMarks=float(
                                                                                                       item[
                                                                                                           'fifth_semester'][
                                                                                                           i + 3 + 15]),
                                                                                                   quiz3_secMarks=float(
                                                                                                       item[
                                                                                                           'fifth_semester'][
                                                                                                           i + 3 + 16]),
                                                                                                   sessional_maxMarks=float(
                                                                                                       item[
                                                                                                           'fifth_semester'][
                                                                                                           i + 3 + 17]),
                                                                                                   sessional_secMarks=float(
                                                                                                       item[
                                                                                                           'fifth_semester'][
                                                                                                           i + 3 + 18]),
                                                                                                   External_grade=item[
                                                                                                       'fifth_semester'][
                                                                                                       i + 3 + 19])
                print("entered try")
            except (SemMarks.DoesNotExist):
                print("exception occured in marks table")
                marks = SemMarks(user=user1, semester=5, subject_name=item['fifth_semester'][i + 3],
                                 int1_maxMarks=float(item['fifth_semester'][i + 3 + 1]),
                                 int1_secMarks=float(item['fifth_semester'][i + 3 + 2]),
                                 int2_maxMarks=float(item['fifth_semester'][i + 3 + 3]),
                                 int2_secMarks=float(item['fifth_semester'][i + 3 + 4]),
                                 ass1_maxMarks=float(item['fifth_semester'][i + 3 + 5]),
                                 ass1_secMarks=float(item['fifth_semester'][i + 3 + 6]),
                                 ass2_maxMarks=float(item['fifth_semester'][i + 3 + 7]),
                                 ass2_secMarks=float(item['fifth_semester'][i + 3 + 8]),
                                 ass3_maxMarks=float(item['fifth_semester'][i + 3 + 9]),
                                 ass3_secMarks=float(item['fifth_semester'][i + 3 + 10]),
                                 quiz1_maxMarks=float(item['fifth_semester'][i + 3 + 11]),
                                 quiz1_secMarks=float(item['fifth_semester'][i + 3 + 12]),
                                 quiz2_maxMarks=float(item['fifth_semester'][i + 3 + 13]),
                                 quiz2_secMarks=float(item['fifth_semester'][i + 3 + 14]),
                                 quiz3_maxMarks=float(item['fifth_semester'][i + 3 + 15]),
                                 quiz3_secMarks=float(item['fifth_semester'][i + 3 + 16]),
                                 sessional_maxMarks=float(item['fifth_semester'][i + 3 + 17]),
                                 sessional_secMarks=float(item['fifth_semester'][i + 3 + 18]),
                                 External_grade=item['fifth_semester'][i + 3 + 19])
                marks.save()
            j += 20

        try:
            percentage = SemPercentage.objects.get(user=user1, semester=5)
            percentage = SemPercentage.objects.filter(user=user1, semester=5).update(user=user1, semester=5,
                                                                                     int1_percentage=
                                                                                     item['fifth_semester'][-10],
                                                                                     int2_percentage=float(
                                                                                         item['fifth_semester'][-9]),
                                                                                     ass1_percentage=float(
                                                                                         item['fifth_semester'][-8]),
                                                                                     ass2_percentage=float(
                                                                                         item['fifth_semester'][-7]),
                                                                                     ass3_percentage=float(
                                                                                         item['fifth_semester'][-6]),
                                                                                     quiz1_percentage=float(
                                                                                         item['fifth_semester'][-5]),
                                                                                     quiz2_percentage=float(
                                                                                         item['fifth_semester'][-4]),
                                                                                     quiz3_percentage=float(
                                                                                         item['fifth_semester'][-3]),
                                                                                     sessional_pecentage=float(
                                                                                         item['fifth_semester'][-2]),
                                                                                     SGPA=item['fifth_semester'][-1][
                                                                                          -4:])
            print("try has", float(item['fifth_semester'][-1][-4:]))
        except(SemPercentage.DoesNotExist):
            print("exception occured in Percentage table")
            percentage = SemPercentage(user=user1, semester=5, int1_percentage=float(item['fifth_semester'][-10]),
                                       int2_percentage=float(item['fifth_semester'][-9]),
                                       ass1_percentage=float(item['fifth_semester'][-8]),
                                       ass2_percentage=float(item['fifth_semester'][-7]),
                                       ass3_percentage=float(item['fifth_semester'][-6]),
                                       quiz1_percentage=float(item['fifth_semester'][-5]),
                                       quiz2_percentage=float(item['fifth_semester'][-4]),
                                       quiz3_percentage=float(item['fifth_semester'][-3]),
                                       sessional_pecentage=float(item['fifth_semester'][-2]),
                                       SGPA=float(item['fifth_semester'][-1][-4:]))
            percentage.save()

#----------------------------------- sixth semester --------------------------------------------------------------------------
        j = 0
        for i in range(14):

            i = i + j
            try:
                marks = SemMarks.objects.get(user=user1, semester=6, subject_name=item['sixth_semester'][i + 3])
                marks = SemMarks.objects.filter(user=user1, semester=6,
                                                subject_name=item['sixth_semester'][i + 3]).update(user=user1,
                                                                                                   semester=6,
                                                                                                   subject_name=item[
                                                                                                       'sixth_semester'][
                                                                                                       i + 3],
                                                                                                   int1_maxMarks=float(
                                                                                                       item[
                                                                                                           'sixth_semester'][
                                                                                                           i + 3 + 1]),
                                                                                                   int1_secMarks=float(
                                                                                                       item[
                                                                                                           'sixth_semester'][
                                                                                                           i + 3 + 2]),
                                                                                                   int2_maxMarks=float(
                                                                                                       item[
                                                                                                           'sixth_semester'][
                                                                                                           i + 3 + 3]),
                                                                                                   int2_secMarks=float(
                                                                                                       item[
                                                                                                           'sixth_semester'][
                                                                                                           i + 3 + 4]),
                                                                                                   ass1_maxMarks=float(
                                                                                                       item[
                                                                                                           'sixth_semester'][
                                                                                                           i + 3 + 5]),
                                                                                                   ass1_secMarks=float(
                                                                                                       item[
                                                                                                           'sixth_semester'][
                                                                                                           i + 3 + 6]),
                                                                                                   ass2_maxMarks=float(
                                                                                                       item[
                                                                                                           'sixth_semester'][
                                                                                                           i + 3 + 7]),
                                                                                                   ass2_secMarks=float(
                                                                                                       item[
                                                                                                           'sixth_semester'][
                                                                                                           i + 3 + 8]),
                                                                                                   ass3_maxMarks=float(
                                                                                                       item[
                                                                                                           'sixth_semester'][
                                                                                                           i + 3 + 9]),
                                                                                                   ass3_secMarks=float(
                                                                                                       item[
                                                                                                           'sixth_semester'][
                                                                                                           i + 3 + 10]),
                                                                                                   quiz1_maxMarks=float(
                                                                                                       item[
                                                                                                           'sixth_semester'][
                                                                                                           i + 3 + 11]),
                                                                                                   quiz1_secMarks=float(
                                                                                                       item[
                                                                                                           'sixth_semester'][
                                                                                                           i + 3 + 12]),
                                                                                                   quiz2_maxMarks=float(
                                                                                                       item[
                                                                                                           'sixth_semester'][
                                                                                                           i + 3 + 13]),
                                                                                                   quiz2_secMarks=float(
                                                                                                       item[
                                                                                                           'sixth_semester'][
                                                                                                           i + 3 + 14]),
                                                                                                   quiz3_maxMarks=float(
                                                                                                       item[
                                                                                                           'sixth_semester'][
                                                                                                           i + 3 + 15]),
                                                                                                   quiz3_secMarks=float(
                                                                                                       item[
                                                                                                           'sixth_semester'][
                                                                                                           i + 3 + 16]),
                                                                                                   sessional_maxMarks=float(
                                                                                                       item[
                                                                                                           'sixth_semester'][
                                                                                                           i + 3 + 17]),
                                                                                                   sessional_secMarks=float(
                                                                                                       item[
                                                                                                           'sixth_semester'][
                                                                                                           i + 3 + 18]),
                                                                                                   External_grade=item[
                                                                                                       'sixth_semester'][
                                                                                                       i + 3 + 19])
                print("entered try")
            except (SemMarks.DoesNotExist):
                print("exception occured in marks table")
                marks = SemMarks(user=user1, semester=6, subject_name=item['sixth_semester'][i + 3],
                                 int1_maxMarks=float(item['sixth_semester'][i + 3 + 1]),
                                 int1_secMarks=float(item['sixth_semester'][i + 3 + 2]),
                                 int2_maxMarks=float(item['sixth_semester'][i + 3 + 3]),
                                 int2_secMarks=float(item['sixth_semester'][i + 3 + 4]),
                                 ass1_maxMarks=float(item['sixth_semester'][i + 3 + 5]),
                                 ass1_secMarks=float(item['sixth_semester'][i + 3 + 6]),
                                 ass2_maxMarks=float(item['sixth_semester'][i + 3 + 7]),
                                 ass2_secMarks=float(item['sixth_semester'][i + 3 + 8]),
                                 ass3_maxMarks=float(item['sixth_semester'][i + 3 + 9]),
                                 ass3_secMarks=float(item['sixth_semester'][i + 3 + 10]),
                                 quiz1_maxMarks=float(item['sixth_semester'][i + 3 + 11]),
                                 quiz1_secMarks=float(item['sixth_semester'][i + 3 + 12]),
                                 quiz2_maxMarks=float(item['sixth_semester'][i + 3 + 13]),
                                 quiz2_secMarks=float(item['sixth_semester'][i + 3 + 14]),
                                 quiz3_maxMarks=float(item['sixth_semester'][i + 3 + 15]),
                                 quiz3_secMarks=float(item['sixth_semester'][i + 3 + 16]),
                                 sessional_maxMarks=float(item['sixth_semester'][i + 3 + 17]),
                                 sessional_secMarks=float(item['sixth_semester'][i + 3 + 18]),
                                 External_grade=item['sixth_semester'][i + 3 + 19])
                marks.save()
            j += 20

        try:
            percentage = SemPercentage.objects.get(user=user1, semester=6)
            percentage = SemPercentage.objects.filter(user=user1, semester=6).update(user=user1, semester=6,
                                                                                     int1_percentage=
                                                                                     item['sixth_semester'][-10],
                                                                                     int2_percentage=float(
                                                                                         item['sixth_semester'][-9]),
                                                                                     ass1_percentage=float(
                                                                                         item['sixth_semester'][-8]),
                                                                                     ass2_percentage=float(
                                                                                         item['sixth_semester'][-7]),
                                                                                     ass3_percentage=float(
                                                                                         item['sixth_semester'][-6]),
                                                                                     quiz1_percentage=float(
                                                                                         item['sixth_semester'][-5]),
                                                                                     quiz2_percentage=float(
                                                                                         item['sixth_semester'][-4]),
                                                                                     quiz3_percentage=float(
                                                                                         item['sixth_semester'][-3]),
                                                                                     sessional_pecentage=float(
                                                                                         item['sixth_semester'][-2]),
                                                                                     SGPA=item['sixth_semester'][-1][
                                                                                          -4:])
            print("try has", float(item['sixth_semester'][-1][-4:]))
        except(SemPercentage.DoesNotExist):
            print("exception occured in Percentage table")
            percentage = SemPercentage(user=user1, semester=6, int1_percentage=float(item['sixth_semester'][-10]),
                                       int2_percentage=float(item['sixth_semester'][-9]),
                                       ass1_percentage=float(item['sixth_semester'][-8]),
                                       ass2_percentage=float(item['sixth_semester'][-7]),
                                       ass3_percentage=float(item['sixth_semester'][-6]),
                                       quiz1_percentage=float(item['sixth_semester'][-5]),
                                       quiz2_percentage=float(item['sixth_semester'][-4]),
                                       quiz3_percentage=float(item['sixth_semester'][-3]),
                                       sessional_pecentage=float(item['sixth_semester'][-2]),
                                       SGPA=0)
            percentage.save()

        return item
