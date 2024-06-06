import streamlit as st
import numpy as np
import pandas as pd
import requests 
#import json
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

st.set_page_config(page_title='Remote Federal Jobs Finder', page_icon=':🇺🇸:' )

occ_series = ['Any','0006-CORRECTIONAL INSTITUTION ADMINISTRATION','0007-CORRECTIONAL OFFICER','0011-BOND SALES PROMOTION SERIES','0017-EXPLOSIVES SAFETY','0018-SAFETY AND OCCUPATIONAL HEALTH MANAGEMENT','0019-SAFETY TECHNICIAN','0020-COMMUNITY PLANNING','0021-COMMUNITY PLANNING TECHNICIAN','0023-OUTDOOR RECREATION PLANNING','0025-PARK RANGER','0028-ENVIRONMENTAL PROTECTION SPECIALIST','0029-ENVIRONMENTAL PROTECTION ASSISTANT','0030-SPORTS SPECIALIST','0050-FUNERAL DIRECTING','0060-CHAPLAIN','0062-CLOTHING DESIGN','0072-FINGERPRINT IDENTIFICATION','0080-SECURITY ADMINISTRATION','0081-FIRE PROTECTION AND PREVENTION','0082-UNITED STATES MARSHAL','0083-POLICE','0084-NUCLEAR MATERIALS COURIER','0085-SECURITY GUARD','0086-SECURITY CLERICAL AND ASSISTANCE','0089-EMERGENCY MANAGEMENT SPECIALIST','0090-GUIDE','0095-FOREIGN LAW SPECIALIST SERIES','0099-GENERAL STUDENT TRAINEE','0101-SOCIAL SCIENCE','0102-SOCIAL SCIENCE AID AND TECHNICIAN','0105-SOCIAL INSURANCE ADMINISTRATION','0106-UNEMPLOYMENT INSURANCE','0107-HEALTH INSURANCE ADMINISTRATION','0110-ECONOMIST','0119-ECONOMICS ASSISTANT','0130-FOREIGN AFFAIRS','0131-INTERNATIONAL RELATIONS','0132-INTELLIGENCE','0134-INTELLIGENCE AID AND CLERK','0135-FOREIGN AGRICULTURAL AFFAIRS','0136-INTERNATIONAL COOPERATION','0140-WORKFORCE RESEARCH AND ANALYSIS SERIES','0142-WORKFORCE DEVELOPMENT','0150-GEOGRAPHY','0160-CIVIL RIGHTS ANALYSIS','0170-HISTORY','0180-PSYCHOLOGY','0181-PSYCHOLOGY AID AND TECHNICIAN','0184-SOCIOLOGY','0185-SOCIAL WORK','0186-SOCIAL SERVICES AID AND ASSISTANT','0187-SOCIAL SERVICES','0188-RECREATION SPECIALIST','0189-RECREATION AID AND ASSISTANT','0190-GENERAL ANTHROPOLOGY','0193-ARCHEOLOGY','0199-SOCIAL SCIENCE STUDENT TRAINEE','0201-HUMAN RESOURCES MANAGEMENT','0203-HUMAN RESOURCES ASSISTANCE','0241-MEDIATION','0243-APPRENTICESHIP AND TRAINING','0244-LABOR-MANAGEMENT RELATIONS EXAMINING','0260-EQUAL EMPLOYMENT OPPORTUNITY','0299-HUMAN RESOURCES MANAGEMENT STUDENT TRAINEE','0301-MISCELLANEOUS ADMINISTRATION AND PROGRAM','0302-MESSENGER','0303-MISCELLANEOUS CLERK AND ASSISTANT','0304-INFORMATION RECEPTIONIST','0305-MAIL AND FILE','0306-GOVERNMENT INFORMATION SPECIALIST','0309-CORRESPONDENCE CLERK','0313-WORK UNIT SUPERVISING','0318-SECRETARY','0319-CLOSED MICROPHONE REPORTER','0322-CLERK-TYPIST','0326-OFFICE AUTOMATION CLERICAL AND ASSISTANCE','0332-COMPUTER OPERATION','0335-COMPUTER CLERK AND ASSISTANT','0340-PROGRAM MANAGEMENT','0341-ADMINISTRATIVE OFFICER','0342-SUPPORT SERVICES ADMINISTRATION','0343-MANAGEMENT AND PROGRAM ANALYSIS','0344-MANAGEMENT AND PROGRAM CLERICAL AND ASSISTANCE','0346-LOGISTICS MANAGEMENT','0347-GAO EVALUATOR','0350-EQUIPMENT OPERATOR','0356-DATA TRANSCRIBER','0357-CODING','0360-EQUAL OPPORTUNITY COMPLIANCE','0361-EQUAL OPPORTUNITY ASSISTANCE','0382-TELEPHONE OPERATING','0390-TELECOMMUNICATIONS PROCESSING','0391-TELECOMMUNICATIONS','0392-GENERAL TELECOMMUNICATIONS','0394-COMMUNICATIONS CLERICAL','0399-ADMINISTRATION AND OFFICE SUPPORT STUDENT TRAINEE','0401-GENERAL NATURAL RESOURCES MANAGEMENT AND BIOLOGICAL SCIENCES','0403-MICROBIOLOGY','0404-BIOLOGICAL SCIENCE TECHNICIAN','0405-PHARMACOLOGY SERIES','0408-ECOLOGY','0410-ZOOLOGY','0413-PHYSIOLOGY','0414-ENTOMOLOGY','0415-TOXICOLOGY','0421-PLANT PROTECTION TECHNICIAN','0430-BOTANY','0434-PLANT PATHOLOGY','0435-PLANT PHYSIOLOGY','0437-HORTICULTURE','0440-GENETICS','0454-RANGELAND MANAGEMENT','0455-RANGE TECHNICIAN','0457-SOIL CONSERVATION','0458-SOIL CONSERVATION TECHNICIAN','0459-IRRIGATION SYSTEM OPERATION','0460-FORESTRY','0462-FORESTRY TECHNICIAN','0470-SOIL SCIENCE','0471-AGRONOMY','0480-FISH AND WILDLIFE ADMINISTRATION','0482-FISH BIOLOGY','0485-WILDLIFE REFUGE MANAGEMENT','0486-WILDLIFE BIOLOGY','0487-ANIMAL SCIENCE','0499-BIOLOGICAL SCIENCE STUDENT TRAINEE','0501-FINANCIAL ADMINISTRATION AND PROGRAM','0503-FINANCIAL CLERICAL AND ASSISTANCE','0505-FINANCIAL MANAGEMENT','0510-ACCOUNTING','0511-AUDITING','0512-INTERNAL REVENUE AGENT','0525-ACCOUNTING TECHNICIAN','0526-TAX SPECIALIST','0530-CASH PROCESSING','0540-VOUCHER EXAMINING','0544-CIVILIAN PAY','0545-MILITARY PAY','0560-BUDGET ANALYSIS','0561-BUDGET CLERICAL AND ASSISTANCE','0570-FINANCIAL INSTITUTION EXAMINING','0580-CREDIT UNION EXAMINER','0592-TAX EXAMINING','0593-INSURANCE ACCOUNTS','0599-FINANCIAL MANAGEMENT STUDENT TRAINEE','0601-GENERAL HEALTH SCIENCE SERIES','0602-MEDICAL OFFICER','0603-PHYSICIAN ASSISTANT SERIES','0610-NURSE','0620-PRACTICAL NURSE','0621-NURSING ASSISTANT','0622-MEDICAL SUPPLY AIDE AND TECHNICIAN','0625-AUTOPSY ASSISTANT','0630-DIETITIAN AND NUTRITIONIST','0631-OCCUPATIONAL THERAPIST','0633-PHYSICAL THERAPIST','0635-KINESIOTHERAPY','0636-REHABILITATION THERAPY ASSISTANT','0637-MANUAL ARTS THERAPIST','0638-RECREATION/CREATIVE ARTS THERAPIST','0639-EDUCATIONAL THERAPIST','0640-HEALTH AID AND TECHNICIAN','0642-NUCLEAR MEDICINE TECHNICIAN','0644-MEDICAL TECHNOLOGIST','0645-MEDICAL TECHNICIAN','0646-PATHOLOGY TECHNICIAN','0647-DIAGNOSTIC RADIOLOGIC TECHNOLOGIST','0648-THERAPEUTIC RADIOLOGIC TECHNOLOGIST','0649-MEDICAL INSTRUMENT TECHNICIAN','0650-MEDICAL TECHNICAL ASSISTANT SERIES','0651-RESPIRATORY THERAPIST','0660-PHARMACIST','0661-PHARMACY TECHNICIAN','0662-OPTOMETRIST','0665-SPEECH PATHOLOGY AND AUDIOLOGY','0667-ORTHOTIST AND PROSTHETIST','0668-PODIATRIST SERIES','0669-MEDICAL RECORDS ADMINISTRATION','0670-HEALTH SYSTEM ADMINISTRATION','0671-HEALTH SYSTEM SPECIALIST','0672-PROSTHETIC REPRESENTATIVE','0673-HOSPITAL HOUSEKEEPING MANAGEMENT','0675-MEDICAL RECORDS TECHNICIAN','0679-MEDICAL SUPPORT ASSISTANCE','0680-DENTAL OFFICER','0681-DENTAL ASSISTANT','0682-DENTAL HYGIENE','0683-DENTAL LABORATORY AID AND TECHNICIAN','0685-PUBLIC HEALTH PROGRAM SPECIALIST','0688-SANITARIAN','0690-INDUSTRIAL HYGIENE','0696-CONSUMER SAFETY','0698-ENVIRONMENTAL HEALTH TECHNICIAN','0699-MEDICAL AND HEALTH STUDENT TRAINEE','0701-VETERINARY MEDICAL SCIENCE','0704-ANIMAL HEALTH TECHNICIAN','0799-VETERINARY STUDENT TRAINEE','0801-GENERAL ENGINEERING','0802-ENGINEERING TECHNICAL','0803-SAFETY ENGINEERING','0804-FIRE PROTECTION ENGINEERING','0806-MATERIALS ENGINEERING','0807-LANDSCAPE ARCHITECTURE','0808-ARCHITECTURE','0809-CONSTRUCTION CONTROL TECHNICAL','0810-CIVIL ENGINEERING','0817-SURVEY TECHNICAL','0819-ENVIRONMENTAL ENGINEERING','0828-CONSTRUCTION ANALYST','0830-MECHANICAL ENGINEERING','0840-NUCLEAR ENGINEERING','0850-ELECTRICAL ENGINEERING','0854-COMPUTER ENGINEERING','0855-ELECTRONICS ENGINEERING','0856-ELECTRONICS TECHNICAL','0858-BIOENGINEERING & BIOMEDICAL ENGINEERING','0861-AEROSPACE ENGINEERING','0871-NAVAL ARCHITECTURE','0873-MARINE SURVEY TECHNICAL','0880-MINING ENGINEERING','0881-PETROLEUM ENGINEERING','0890-AGRICULTURAL ENGINEERING','0893-CHEMICAL ENGINEERING','0895-INDUSTRIAL ENGINEERING TECHNICAL','0896-INDUSTRIAL ENGINEERING','0898-ENGINEERING TRAINEE','0899-ENGINEERING AND ARCHITECTURE STUDENT TRAINEE','0901-GENERAL LEGAL AND KINDRED ADMINISTRATION','0904-LAW CLERK','0905-GENERAL ATTORNEY','0930-HEARINGS AND APPEALS','0935-ADMINISTRATIVE LAW JUDGE','0950-PARALEGAL SPECIALIST','0958-EMPLOYEE BENEFITS LAW','0962-CONTACT REPRESENTATIVE','0963-LEGAL INSTRUMENTS EXAMINING','0965-LAND LAW EXAMINING','0967-PASSPORT AND VISA EXAMINING','0986-LEGAL ASSISTANCE','0987-TAX LAW SPECIALIST','0991-WORKERS COMPENSATION CLAIMS EXAMINING','0993-RAILROAD RETIREMENT CLAIMS EXAMINING','0996-VETERANS CLAIMS EXAMINING','0998-CLAIMS ASSISTANCE AND EXAMINING','0999-LEGAL OCCUPATIONS STUDENT TRAINEE','1001-GENERAL ARTS AND INFORMATION','1002-ARTS AND INFORMATION SUPPORT','1008-INTERIOR DESIGN','1010-EXHIBITS SPECIALIST','1015-MUSEUM CURATOR','1016-MUSEUM SPECIALIST AND TECHNICIAN','1020-ILLUSTRATING','1021-OFFICE DRAFTING','1035-PUBLIC AFFAIRS','1040-LANGUAGE SPECIALIST','1046-LANGUAGE CLERICAL','1051-MUSIC SPECIALIST','1054-THEATER SPECIALIST','1056-ART SPECIALIST','1060-PHOTOGRAPHY','1071-AUDIOVISUAL PRODUCTION','1082-WRITING AND EDITING','1083-TECHNICAL WRITING AND EDITING','1084-VISUAL INFORMATION','1087-EDITORIAL ASSISTANCE','1099-INFORMATION AND ARTS STUDENT TRAINEE','1101-GENERAL BUSINESS AND INDUSTRY','1102-CONTRACTING','1103-INDUSTRIAL PROPERTY MANAGEMENT','1104-PROPERTY DISPOSAL','1105-PURCHASING','1106-PROCUREMENT CLERICAL AND TECHNICIAN','1107-PROPERTY DISPOSAL CLERICAL AND TECHNICIAN','1108-BUSINESS SUPPORT','1109-GRANTS MANAGEMENT','1130-PUBLIC UTILITIES SPECIALIST','1140-TRADE SPECIALIST','1144-COMMISSARY MANAGEMENT','1145-AGRICULTURAL PROGRAM SPECIALIST','1146-AGRICULTURAL MARKETING','1147-AGRICULTURAL MARKET REPORTING','1150-INDUSTRIAL SPECIALIST','1152-PRODUCTION CONTROL','1160-FINANCIAL ANALYSIS','1163-INSURANCE EXAMINING','1165-LOAN SPECIALIST','1169-INTERNAL REVENUE OFFICER','1170-REALTY','1171-APPRAISING','1173-HOUSING MANAGEMENT','1176-BUILDING MANAGEMENT','1199-BUSINESS AND INDUSTRY STUDENT TRAINEE','1202-PATENT TECHNICIAN','1210-COPYRIGHT','1220-PATENT ADMINISTRATION','1221-PATENT ADVISER','1222-PATENT ATTORNEY','1223-PATENT CLASSIFYING','1224-PATENT EXAMINING','1226-DESIGN PATENT EXAMINING','1299-COPYRIGHT AND PATENT STUDENT TRAINEE','1301-GENERAL PHYSICAL SCIENCE','1306-HEALTH PHYSICS','1310-PHYSICS','1311-PHYSICAL SCIENCE TECHNICIAN','1313-GEOPHYSICS','1315-HYDROLOGY','1316-HYDROLOGIC TECHNICIAN','1320-CHEMISTRY','1321-METALLURGY','1330-ASTRONOMY AND SPACE SCIENCE','1340-METEOROLOGY','1341-METEOROLOGICAL TECHNICIAN','1350-GEOLOGY','1360-OCEANOGRAPHY','1361-NAVIGATIONAL INFORMATION','1370-CARTOGRAPHY','1371-CARTOGRAPHIC TECHNICIAN','1372-GEODESY','1373-LAND SURVEYING','1374-GEODETIC TECHNICIAN','1380-FOREST PRODUCTS TECHNOLOGY','1382-FOOD TECHNOLOGY','1384-TEXTILE TECHNOLOGY','1386-PHOTOGRAPHIC TECHNOLOGY','1397-DOCUMENT ANALYSIS','1398-PHYSICAL SCIENCE TRAINEE','1399-PHYSICAL SCIENCE STUDENT TRAINEE','1410-LIBRARIAN','1411-LIBRARY TECHNICIAN','1412-TECHNICAL INFORMATION SERVICES','1420-ARCHIVIST','1421-ARCHIVES TECHNICIAN','1499-LIBRARY AND ARCHIVES STUDENT TRAINEE','1501-GENERAL MATHEMATICS AND STATISTICS','1510-ACTUARIAL SCIENCE','1515-OPERATIONS RESEARCH','1520-MATHEMATICS','1521-MATHEMATICS TECHNICIAN','1529-MATHEMATICAL STATISTICS','1530-STATISTICS','1531-STATISTICAL ASSISTANT','1541-CRYPTANALYSIS','1550-COMPUTER SCIENCE','1598-MATHEMATICS OR COMPUTER SCIENCE TRAINEE','1599-MATHEMATICS AND STATISTICS STUDENT TRAINEE','1601-EQUIPMENT FACILITIES, AND SERVICES','1603-EQUIPMENT, FACILITIES, AND SERVICES ASSISTANCE','1630-CEMETERY ADMINISTRATION SERVICES','1640-FACILITY OPERATIONS SERVICES','1654-PRINTING SERVICES','1658-LAUNDRY OPERATIONS SERVICES','1667-FOOD SERVICES','1670-EQUIPMENT SERVICES','1699-EQUIPMENT AND FACILITIES MANAGEMENT STUDENT TRAINEE','1701-GENERAL EDUCATION AND TRAINING','1702-EDUCATION AND TRAINING TECHNICIAN','1710-EDUCATION AND VOCATIONAL TRAINING','1712-TRAINING INSTRUCTION','1715-VOCATIONAL REHABILITATION','1720-EDUCATION PROGRAM','1725-PUBLIC HEALTH EDUCATOR','1730-EDUCATION RESEARCH','1740-EDUCATION SERVICES','1750-INSTRUCTIONAL SYSTEMS','1799-EDUCATION STUDENT TRAINEE','1801-GENERAL INSPECTION, INVESTIGATION, ENFORCEMENT, AND COMPLIANCE SERIES','1802-COMPLIANCE INSPECTION AND SUPPORT','1805-INVESTIGATIVE ANALYSIS','1810-GENERAL INVESTIGATION','1811-CRIMINAL INVESTIGATION','1815-AIR SAFETY INVESTIGATING','1822-MINE SAFETY AND HEALTH INSPECTION SERIES','1825-AVIATION SAFETY','1831-SECURITIES COMPLIANCE EXAMINING','1849-WAGE AND HOUR INVESTIGATION SERIES','1850-AGRICULTURAL WAREHOUSE INSPECTION SERIES','1860-EQUAL OPPORTUNITY INVESTIGATION','1862-CONSUMER SAFETY INSPECTION','1863-FOOD INSPECTION','1881-CUSTOMS AND BORDER PROTECTION INTERDICTION','1889-IMPORT COMPLIANCE SERIES','1894-CUSTOMS ENTRY AND LIQUIDATING SERIES','1895-CUSTOMS AND BORDER PROTECTION','1896-BORDER PATROL ENFORCEMENT SERIES','1899-INVESTIGATION STUDENT TRAINEE','1910-QUALITY ASSURANCE','1980-AGRICULTURAL COMMODITY GRADING','1981-AGRICULTURAL COMMODITY AID','1999-QUALITY INSPECTION STUDENT TRAINEE','2001-GENERAL SUPPLY','2003-SUPPLY PROGRAM MANAGEMENT','2005-SUPPLY CLERICAL AND TECHNICIAN','2010-INVENTORY MANAGEMENT','2030-DISTRIBUTION FACILITIES & STORAGE MANAGEMENT','2032-PACKAGING','2091-SALES STORE CLERICAL','2099-SUPPLY STUDENT TRAINEE','2101-TRANSPORTATION SPECIALIST','2102-TRANSPORTATION CLERK AND ASSISTANT','2110-TRANSPORTATION INDUSTRY ANALYSIS','2121-RAILROAD SAFETY','2123-MOTOR CARRIER SAFETY','2125-HIGHWAY SAFETY','2130-TRAFFIC MANAGEMENT','2131-FREIGHT RATE','2135-TRANSPORTATION LOSS & DAMAGE CLAIMS EXAMINING','2144-CARGO SCHEDULING','2150-TRANSPORTATION OPERATIONS','2151-DISPATCHING','2152-AIR TRAFFIC CONTROL','2154-AIR TRAFFIC ASSISTANCE','2161-MARINE CARGO','2181-AIRCRAFT OPERATION','2183-AIR NAVIGATION','2185-AIRCREW TECHNICIAN','2186-TECHNICAL SYSTEMS PROGRAM MANAGER','2199-TRANSPORTATION STUDENT TRAINEE','2210-INFORMATION TECHNOLOGY MANAGEMENT','2299-INFORMATION TECHNOLOGY STUDENT TRAINEE']

#Set Background 
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background: linear-gradient(90deg, rgba(212,211,223,1) 0%, rgba(219,219,232,1) 31%, rgba(136,219,236,1) 100%);
background-size: cover;
background-position: center center;
background-repeat: no-repeat;
background-attachment: local;
}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

#Center Image
left_co, cent_co,last_co = st.columns(3)
with cent_co:
    st.image('job_search.gif')

#Header
st.header('Remote Federal Job Listings')

with st.container():
#InputBox
    job_search = st.text_input(label='Job Keywords:')

    #scraped from OPM website
    js_option = st.selectbox('What Job Series are you interested in?',(occ_series))

   
    if js_option is 'Any':
         job_code = ''
    else: 
    #get first 4 digits of the occupational series to eventually use for the BASE_URL
        job_code = f'JobCategoryCode={js_option[:4]}&'

    #Cut feature.. complexity with finding out the equivalent types: example GS-XX = NH-XX, etc.
    #Possibly add later
    #st.selectbox('What GS Series?', ('GS-1', 'GS-2', ))

    if st.button('Search'):
        #get data from text input, feed it to api

        host = 'data.usajobs.gov';  
        BASE_URL = f'https://data.usajobs.gov/api/search?{job_code}Keyword={job_search}&rmi=true&ResultsPerPage=500'
        API_KEY = open('api_key.txt', 'r').read()
        response = requests.get(BASE_URL, headers={"Host":host,  "Authorization-Key":API_KEY}).json()
        num_of_jobs = int(response['SearchResult']['SearchResultCount'])#All
        st.subheader( f'{num_of_jobs} Jobs Found ' )

        #Get Dictionary with job codes and count of each:
        thisdict = {}

        #Goes through all jobs                                                         
        for i in range(num_of_jobs):
            
            #new for loop
            for k in range(len(response['SearchResult']['SearchResultItems'][i]['MatchedObjectDescriptor']['JobCategory'])):
                jobseries = response['SearchResult']['SearchResultItems'][i]['MatchedObjectDescriptor']['JobCategory'][k]['Code']
                if jobseries in thisdict :
                    thisdict[jobseries] = thisdict[jobseries] + 1
                else: 
                    thisdict.update({jobseries : 1})
            
        #gets top 3 values from dict
        my_keys = sorted(thisdict, key=thisdict.get, reverse=True)[:3]

        if job_code != '':
            pass
            
        else:
            st.subheader('Top 3 Job Series found:')
            #create new list 
            my_labels = ['','','']
            #get name of occupational series from list
            for i in range(3):
                res = str([j for j in occ_series if str(my_keys[i]) in j])
                res_edited = res.partition("-")[2]
                res_edited = res_edited[:-2]
                my_labels[i] = my_keys[i] + ' - ' + res_edited


            pie_plot = go.Figure(go.Pie(
                labels=my_labels,            # Labels for the pie slices (has Occ Series numb + label)
                values=[thisdict[my_keys[0]], thisdict[my_keys[1]], thisdict[my_keys[2]]],            # Number of jobs found
                name='Pie Chart', 
                title='Top 3 Job Series:',
                pull=[0, 0, 0],         # Specify how much each slice should be pulled from the center (optional)
                textinfo='value', # Information to display on the pie slices
                hoverinfo='label',# Information to display on hover
                marker=dict(colors=['blue', 'green', 'red'], line=dict(color='white', width=0))  # Customize colors and borders
            ))

            st.plotly_chart(pie_plot)
   
        with st.container(border=False):
    
            
            #Creates individual containers withing the main container
            for i in range(num_of_jobs):

                #creates individual containers within the above container
                with st.container(border=True):
                

                        #Position Title
                        st.header(response['SearchResult']['SearchResultItems'][i]['MatchedObjectDescriptor']['PositionTitle'])

                        #Agency
                        st.subheader(response['SearchResult']['SearchResultItems'][i]['MatchedObjectDescriptor']['OrganizationName'])

                        #Job Grade and Level
                        clean_job = str(response['SearchResult']['SearchResultItems'][i]['MatchedObjectDescriptor']['JobGrade'][0])
                        low_grade = response['SearchResult']['SearchResultItems'][i]['MatchedObjectDescriptor']['UserArea']['Details']['LowGrade']
                        high_grade = response['SearchResult']['SearchResultItems'][i]['MatchedObjectDescriptor']['UserArea']['Details']['HighGrade']
                        
                                            
                        if low_grade == high_grade:
                            st.write( f'Pay Scale: {clean_job[10:12]}-{low_grade}')
                        else:
                            st.write( f'Pay Scale: {clean_job[10:12]}-{low_grade} - {clean_job[10:12]}-{high_grade}')


                        #Get number of job series
                        num_of_series = len(response['SearchResult']['SearchResultItems'][i]['MatchedObjectDescriptor']['JobCategory'])
                        series_str = ''

                        executed = 0
                        #Prints occupational series in container
                        for j in range(num_of_series):
                             series_str += f'{response['SearchResult']['SearchResultItems'][i]['MatchedObjectDescriptor']['JobCategory'][j]['Code']}'  
                             name =str([k for k in occ_series if response['SearchResult']['SearchResultItems'][i]['MatchedObjectDescriptor']['JobCategory'][j]['Code'] in k])
                             name_edit = name.partition("-")[2]
                             name_edit = name_edit[:-2]
                             series_str = series_str +  '-' + name_edit
                             
                             if num_of_series >= 2 and j != num_of_series -1: 
                                 series_str = series_str + ', '

                        st.write('Occupational Series: ' + series_str)

                        #URL for job posting
                        st.write('\n', response['SearchResult']['SearchResultItems'][i]['MatchedObjectDescriptor']['PositionURI'])

                        #Job description
                        st.write('\n', response['SearchResult']['SearchResultItems'][i]['MatchedObjectDescriptor']['UserArea']['Details']['JobSummary'])

#Footnote
st.caption('Developed by Shane Morgan', unsafe_allow_html=False, help=None)


