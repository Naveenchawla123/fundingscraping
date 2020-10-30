from bs4 import BeautifulSoup
import sys
from botapp.models import *
from .helpers import HttpHelpers

class FundingPro:
    def __init__(self, url):
        self.url = url
        self.helpers = HttpHelpers()

    def get(self):
        print("Searching .......")
        funding_prog_return = []
        
        page = self.helpers.download_page(self.url)
        
        
        if page is None:
            sys.exit('Error Downloading Paga, cannot continue further, so fix this first')

        funding_prog_return = funding_prog_return + self.__parse_index(page)
        
        for value in funding_prog_return:
            each_content = self.helpers.download_page(value["href"])
            
            if each_content is None:
                continue
            
            about_the_program,who_can_apply,deadline,how_to_apply  = self.__parse_details(each_content)
            
         
            value["about_the_program"] = about_the_program
            value["who_can_apply"] = who_can_apply
            value["deadline"] = deadline
            value["how_to_apply"] = how_to_apply
            
        return funding_prog_return

    def __parse_index(self, htmlcontent):
        soup = BeautifulSoup(htmlcontent, 'lxml')
        sections = soup.find_all('section')
        
        if sections is None or len(sections) == 0:
            return []
        
        all_programs = []

        for section in sections:
            
            for link in section.find_all('h2'):
                if(link.text == "Name of  funding program"):
                    for a in section.findAll('a'):
                        program = a.text
                        if('https' in a.get('href')):
                            link = a.get('href')
                        else:
                            link = "https://www.sac-isc.gc.ca"+a.get('href')

                            
                        item = {"program_name": program,
                                "href" : link,
                                "about_the_program" : "",
                                "who_can_apply" : "",
                                "deadline" : "",
                                "how_to_apply" : ""
                                }
                        all_programs.append(item)
        
        return all_programs

    def __parse_details(self, htmlcontent):
        soup = BeautifulSoup(htmlcontent, 'lxml')
        apply_sections =  soup.find_all('section')
        about_the_program = ""
        who_can_apply = ""
        deadline = ""
        how_to_apply = ""
        for section in apply_sections:
            for data in section.find_all('h2'):
                if(data.text == "About the program"):
                    for p in section.findAll('p'):
                        about_the_program += p.text

                elif(data.text == "Who can apply?"): 
                    for p in section.findAll('p'):
                        who_can_apply+=p.text

                elif(data.text == "Deadline"): 
                    for p in section.findAll('p'):
                        deadline+=p.text

                elif(data.text == "How to apply?"): 
                    for p in section.findAll('p'):
                        how_to_apply+=p.text
                      
        return (str(about_the_program),str(who_can_apply),str(deadline),str(how_to_apply))

        