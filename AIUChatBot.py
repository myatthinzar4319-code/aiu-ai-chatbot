
from nltk.chat.util import Chat, reflections



pairs = [
    [
        r"(hi|hey|hello|hola|holla)(.*)",
        ["Hello", "Hey there","Hi Friend","Hi flok!","Hey! Who are you?",]
    ],
    
    [
        r"(.*)my name is(.*)",
        ["Hello %2, How are you today ?",]
    ],

    [
        r"(.*)nice to meet you too(.*)",
        ["Nice to hear that",]
    ],

    [
        r"(.*)help(.*) ",
        ["Sure! How can I help you? ", "Certainly! What is your problem?",]
    ],

    [
        r"(.*) your name ?",
        ["My name is Mr Albukhary, but I'm a chatbot and just call me AIU Chat box.",]
    ],

    [
        r"how are you?",
        ["I'm doing very well", "I am great !",]
    ],


    [
        r"(.*)purpose(.*)",
        ["My purpose is to make it easier for new applicants to get information about AIU",]
    ],

    [
        r"(.*)created(.*)",
        [" B-Positive Group Members from SCI created me ",]
    ],

    [
        r"(.*)your health(.*)",
        ['''Health is very important only for humans!, 
         I am an AI chat box and if your computer is healthy, I am also healthy!''',]
    ],

    [
        r"(.*)sorry (.*)",
        ["Its alright","Its OK, never mind that",]
    ],

    [
        r"(.*) (good|well|okay|ok)",
        ["Nice to hear that","Alright, great !",]
    ],
    
    [
        r"what can you do ?",
        ['''I do provide following infos:                                             \n
        1. Registration                                                                       \n
        2. Scholarship Details                                                           \n
        3. Details of Center of Foundation Studies (CFS)                \n
        4. Details of Language Center (LC)                                      \n
        5. Details of each Schools in AIU (SBSS, SEHS, SCI)        \n
        6. AIU location                                                                      \n
        7. Semester Details                                                                \n
        8. Name of AIU Founder, Chancellor and Vice Chancellor     \n
        9. GPA and CGPA Grading                                                       \n
        10. Background of AIU                            
        ''']
    ],

    [
        r"(.*)(background)(.*)",
        ['''Albukhary International University (AIU) is a private nonprofit education institution, a fully residential campus with state-of-the-art facilities.
            It provides conducive living and learning environment for self-discovery, nurturing relationships and building understanding on global issues.
            At AIU, students are exposed to holistic educational approach through combined academic and social engagement programme which is carried out throughout the study period.
        
            Mission; Provides opportunity to serve humanity through social business in redesigned learning environment.
        
            Vision; Innovating solutions that promote the convergence of ideas towards a sustainable world.''',]
    ],
    
    [
        r"(.*)(Scholarship)(.*)",
        ['''Scholarship Criteria : 
        
        1. Age between 18 – 22 years old.                                                \n
        2. Single marital status.                                                                 \n
        3. Household income below USD 300 for international applicant and 
           MYR 2,400 (Sabah and Sarawak), 
           MYR 5,300( W.P Kuala Lumpur, W.P Putrajaya & W.P Labuan) or 
           MYR 2,900 (Perlis, Kedah, Pulau Pinang, Perak, Kelantan, Terengganu, Johor, Melaka, Negeri Sembilan, Pahang).                                                                                      \n
           
        4. Failed to achieve CGPA of 2.8 for two consecutive semesters                    \n
        5. Serious disciplinary issues                                                                           \n
        6. Academic dishonesty such as being caught cheating during examinations, 
           providing false documents for admission etc.                                                          \n
        7. Specific for meal allowance - staying away from campus for more than 14 days.  \n
        
        If you want to apply Scholarship, https://apply.aiu.edu.my/?page=home

        ''',]
    ],
    [
        r"(.*)(Grading)(.*)",
        ['''GPA Grading system in AIU : 
        
              Grade   Mata grade
                A+      4.00
                A       3.75
                A-      3.67
                B+      3.33
                B       3.00
                C+      2.67
                C       2.33
                D       2.00
                E       1.67
                G       0.00   ''',]
    ],
    
    [
        r"(.*)(register|apply)(.*)",
        ['''Sure! We have the following programs in AIU :   \n
          1. Center for Foundation Studies (CFS)               \n
          2. Language Center (LC)                                      \n
          3. Degree Programs/Bachelor Program               \n
          Which one do you prefer?''',]
    ],
    [
        r"(.*)(Center for foundation studies|CFS)(.*)",
        ['''Details of CFS \n
            1. Credit in 5 subjects at SPM level including English and Mathematics. \n
            2. Minimum Grade Point Average of 2.67                                            \n
            3. Credit 4 hours subjects                                                                     \n
            4. 3 semesters for CFS and each semesters for 4 months                  \n
            5. 5 or 6 subjects for each semester                                                   \n
            
            
            
            The head of Centre for Foundation Studies is 
            Alia Hanim Zainal Abidin
            

            Lecturers of Centre for Foundation Studies :

            1. Aliaa Diyana Binti Zamri     \n
            2. Syaza Lyana Mahadzir       \n
            3. Alia Hanim Zainal Abidin    \n
            ''',]
    ],

    [
        r"(.*)(language center|LC)(.*)",
        ['''Details of LC \n
            1. Preparatory course for International English Language Testing System (IELTS) \n
            2. Preparatory course for Cambridge Linguaskill                                 \n 
            3. Preparatory course for International English Language Testing System (IELTS) \n
            4. Preparatory course for Cambridge Linguaskill                                 \n
            5. Business English / Professional English                                          \n
            6. English Camps and Creative Writing                                                \n 
            7. Buddy Programmes

            Head of Language Centre is
            Sherina Shahnaz Mohamed Fauzi
            
            
            Lecturers of Language Centre               \n
            1. Nurul Hamidah Mohd Hamdi              \n
            2. Nur Darina Ibrahim                             \n
            3. Rubini Radza                                      \n 
            4. Khairunnisha Binti Redzzuan             \n
            5. Marina Binti Nazrin                             \n 
            6. Fatin Nur Elleina Binti  Asmira Helmy \n
            7. Mubarak Ali Rakhir Mohamed''',]
    ],

    [
        r"(.*)(Bachelor|Degree)(.*)",
        ['''We have THREE schools in Degree program :              \n
            1. School of Business and Social Sciences (SBSS)      \n
            2. School of Education and Human Sciences                \n
            3. School of Computing and Informatics                          \n
            Which school do you want to apply to?''',]
    ],
    [
        r"(.*)(School of business and Social Sciences|SBSS)(.*)",
        ['''Programme offered by School of Business and Social Sciences(SBSS) 
        
            1. Bachelor of Business Administration (Honours)                                    \n
            2. Bachelor of Business Administration (Marketing)(Honours)                  \n 
            3. Bachelor of Business Administration (Human Resource Management) (Honours) \n
            4. Bachelor of Economics (Honours)                                                    \n 
            5. Bachelor of Social Development (Honours)                                      \n 
            6. Bachelor of Finance (Islamic Finance) (Honours)                             \n 
            7. Bachelor of Politics and International Relations (Honours)               \n 
            8. Master of Science in Business Management                                    \n 
            9. Doctor of Philosophy (PhD) in Business Management Tester
            The dean of School of Business and Social Sciences is 
            Associate Professor Dr. Suraya Hanim Mokhtar
            
            
            
            Lecturers of School of Business and Social Sciences :
        
            1. Associate Professor Dr. Suraya Hanim Mokhtar    \n
            2. Dr Siti Noorjannah Bt. Abd Halim                           \n
            3. Associate Professor Dr. Mustaffa Bin Omar           \n
            4. Dr. Reazul Islam                                                     \n 
            5. Noorasyikin Binti Mohd Noh                                   \n
            6. Dr. Hamid Abdulkhaleq Hassan Al-Wesabi            \n
            7. Osaid N.A. Abdaljawwad                                        \n
            8. Nurul Aina Johari                                                    \n 
            9. Dr. Wan ‘Aliaa Binti Wan Anis                                \n
            10. Hla Theingi Win                                                    \n
            11. Dr Bahiah Bt A Malek                                           \n
            
            
            
            Credit Hours for each programs in School of Business and Social Sciences :
            
            1. Bachelor of Business Administration (Honours)                       - 124 credit hours \n
            2. Bachelor of Business Administration (Marketing)(Honours)    - 124 credit hours \n
            3. Bachelor of Business Administration (Honours)                       - 124 credit hours \n
            4. Bachelor of Economics (Honours)                                            - 120 credit hours \n 
            5. Bachelor of Social Development (Honours)                              - 120 credit hours \n
            6. Bachelor of Finance (Islamic Finance) (Honours)                     - 120 credit hours \n
            7. Bachelor of Politics and International Relations (Honours)      - 132 credit hours \n 
            8. Master of Science in Business Management                              - 124 credit hours \n
            9. Doctor of Philosophy (PhD) in Business Managementester      - 132 credit hours \n
            ''',]
    ],

    [
        r"(.*)(School of education and human resources|SEHS)(.*)",
        ['''Programme offered by School of Education and Human Resources (SEHS)

            1. Bachelor of Elementary Education (Honours)                      \n
            2. Bachelor in Early Childhood Education (Honours)               \n
            3. Bachelor of Media and Communication (Honours)              \n
            
            
            The dean of School of Education and Human Resources is 
            Associate Professor Dr. Tengku Shahrom Bin Tengku Shahdan
            
             
             Lecturers of Education and Human Resources
        
            1. Associate Professor Dr. Tengku Shahrom Bin Tengku Shahdan     \n
            2. Associate Professor Dr. Bakare Kazeem Kayode                            \n
            3. Dr. Nooraida Binti Yakob                                                                 \n
            4. Dr. Siti Aishah Chu Bt Abdullah                                                      \n
            5. Dr. Sidra Shehzadi                                                                            \n
            6. Mohamad Nor Hisyam Bin Musa                                                     \n
            7. Ildefonso Halipa Jr.                                                                           \n
            8. Alia Hanim Zainal Abidin                                                                \n
            8. Aina Yasmin Bt Mohd Amin                                                            \n
            9. Adhara Ahmad                                                                                  \n
            10. Nurul Huda Bt Hassan Bakri                                                          \n
            11. Aini Syahira Jamaluddin                                                         \n
            12. Nur Faridatul Jamalia Binti Radzali                                       \n
            13. Siti Mukhlisa Binti Mohamad Khairul Adilah                       \n
            14. Samihah Bt Mahamud                                                            \n
            15. Norazly Bin Nordin                                                                \n
            
            Credit Hours for each programs in School of Education and Human Resources : 
            
            1. Bachelor of Elementary Education (Honours)             - 129 credit hours   \n
            2. Bachelor in Early Childhood Education (Honours)      - 120 credit hours  \n
            3. Bachelor of Media and Communication (Honours)     - 126 credit hours   \n
            ''',]
    ],

    [
        r"(.*)(School of computing and informatics|SCI)(.*)",
        ['''Programme offered by School of Computing and Informatics (SCI)

            1. Bachelor of Computer Science (Honours)
            
            
            Specializations in SCI : Data Science and Cyber Security
            
            
            
            Dean of School of Computing and Informatics :
            Dr. Basheer Riskhan.
            
            
            Lecturers of School of Computing and Informatics are:   \n
            Associate Professor Dr. Shahrinaz Bt Ismail                   \n
            Dr. Akibu Mahmoud Abdullahi                                         \n
            Halawati Binti Abd Jalil Safuan                                        \n
            Ts. Nor Azizah Binti Hitam                                               \n
            Nooremadinah Bt Alias. 
 
            Credit Hours for Computer Science in School of Computing and Informatics :
            
            Bachelor of Computer Science (Honours)   - 120 credit hours
            ''',]
    ],
    




    [
        r"(.*) (founder)",
        ['''
        Founder of Albukhary International University is Tan Sri Syed Mokhtar Shah bin Syed
        Nor Albukhary.
        ''']
    ],

    [
        r"(.*) (chancellor)",
        ['''
        Chancellor of Albukhary International University is Muhammad Yunus.
        ''']
    ],

    [
        r"(.*) (vice chancellor)",
        ['''
        Vice Chancellor of Albukhary International University is Muhammad Yunus.
        ''']
    ],

    [
        r"(.*) (semesters|UGP semesters|semesters in UGP)",
        ['''
        There are 3 semesters in a year.
        We have two kinds of semesters - long semester and short semester.
        For long semester - there is about 14 weeks.
        For short semester - there is only about 7 weeks.
        ''']
    ],
     








    [
        r"(.*) (AIU location|AIU located|location|city|located) ?",
        ['''Jln Tun Razak, Bandar Alor Setar, 05200 Alor Setar, Kedah
        
        Google Map link : 
        https://www.google.com/maps/place/Albukhary+International+University+(AIU)/@6.1336498,100.3863971,17z/data=!3m1!4b1!4m6!3m5!1s0x304b5ac489a998b9:0x3fa53e13f07fbb01!8m2!3d6.1336498!4d100.3863971!16s%2Fg%2F1216lnq4
        
        ''',]
    ]
    [
        r"quit",
        ["Bye for now. See you soon :) ","It was nice talking to you. See you soon :)"]
    ],

    [
        r"(.*)",
        ["Sorry, I don't understand",]
    ],
]



print(reflections)


chat = Chat(pairs, reflections)


chat.converse()
