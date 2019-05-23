import scrapy
from scrapy.http import FormRequest
import collections
from ..items import MarksItem
class QuoteSpider(scrapy.Spider):

    name = "vasavi"

    # def __init__(self,*args,**kwargs):
    #     self.LoginID = kwargs.get('LoginID')
    #     self.Password = kwargs.get('Password')

    start_urls = [
        "http://vce.ac.in/student_info.aspx#",
    ]

    set_links={}
    i=0
    def parse(self, response):

        return FormRequest.from_response(response, formdata={
            'LoginID' : '1602-16-737-026',
            'Password' : 'danzig'
        }, callback=self.scrap_basepage)

    def scrap_basepage(self,response):
        i=0
        attendance_links=response.css("td:nth-child(7) a").xpath("@onclick").extract()
        attendance_links=[x[7:-2] for x in attendance_links]
        marks_link=response.css("tr:nth-child(2) td:nth-child(8) a").xpath("@onclick")[0].extract()
        marks_link=marks_link[7:-2]
        url = response.urljoin(marks_link)
        yield scrapy.Request(url, callback=self.extracting_marks)
        # for link in attendance_links:
        #     url = response.urljoin(link)
        #     yield scrapy.Request(url, callback=self.extracting_attendance)


    def extracting_attendance(self,response):

            # data=response.css("#TdAttSummaryHeading table").extract()
            #
            # QuoteSpider.i += 1
            # print("the value of i is:", QuoteSpider.i)
            # print("the attendance list data",data)
            pass

    def extracting_marks(self,response):
        items = MarksItem()
        title = response.css("#TdStudentHeading font::text").extract()
        hall_ticket = response.css("#TdDispStudentProfile table:nth-child(1) .tableclass tr:nth-child(2) td:nth-child(3) font::text").extract()
        student_name =response.css("#TdDispStudentProfile table:nth-child(1) .tableclass tr:nth-child(2) td:nth-child(6) font::text").extract()
        current_branch = response.css("#TdDispStudentProfile table:nth-child(1) .tableclass tr:nth-child(3) td:nth-child(3) font::text").extract()
        proctor_id = response.css("#TdDispStudentProfile table:nth-child(1) .tableclass tr:nth-child(9) td:nth-child(6) font::text").extract()
        first_semester = response.css("table:nth-child(11) tr+ tr font::text").extract()
        second_semester = response.css("table:nth-child(13) tr+ tr font::text").extract()
        third_semester = response.css("table:nth-child(15) tr+ tr font::text").extract()
        fourth_semester =response.css("table:nth-child(17) tr+ tr font::text").extract()
        fifth_semester = response.css("table:nth-child(19) tr+ tr font::text").extract()
        sixth_semester = response.css("table:nth-child(21) tr+ tr font::text").extract()

        items['title'] = title
        items ['hall_ticket'] = hall_ticket
        items['student_name'] = student_name
        items['current_branch'] = current_branch
        items['proctor_id'] = proctor_id
        items['first_semester'] = first_semester
        items['second_semester'] = second_semester
        items ['third_semester'] = third_semester
        items['fourth_semester'] = fourth_semester
        items['fifth_semester'] = fifth_semester
        items['sixth_semester'] = sixth_semester


        yield items













