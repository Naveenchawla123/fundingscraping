from django.shortcuts import render
from django.http import HttpResponse
from botapp.scraping import fund
from botapp.models import FundingProgramTbl


def home(request):
    return HttpResponse ("hello world")

def index(request):
    funding_programs = []
    fund_obj = fund.FundingPro("https://www.aadnc-aandc.gc.ca/eng/1425576051772/1425576078345")
    print('\nGetting Funding Programs')
    funding_prog_return = fund_obj.get()
    print('Saved Funding Prgrams')
    funding_programs = funding_programs + funding_prog_return
    
    for program in funding_programs:
         
        
        import pdb; pdb.set_trace()
        print('Saving Program Name ' + program["program_name"] + ' in database')
        print('About_Program: ' + program["about_the_program"])
        print('Who_can_apply: ' + program["who_can_apply"])
        print('Deadline: ' + program["deadline"])
        print('Link' + program["href"])
        print('How_to_apply' + program["how_to_apply"])
        print('============================================================================================')
            
        
        FundingProgramTbl.objects.create(
            program_name=program["program_name"],
            about_program=program["about_the_program"],
            who_can_apply=program["who_can_apply"],
            deadline=program["deadline"],
            link=program["href"],
            how_to_apply=program["how_to_apply"],

            
        )
        print('%s added' % program["program_name"] )
        
    return HttpResponse("Data")