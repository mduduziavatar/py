'''
    This is the team allocator project solution example project
'''


from traceback import print_tb


def student_list():
    return [
        'zakithikhDBN2022 - 4 April - Johannesburg Physical - seat 3'
        , 'ddhaalJHB2022 - 2 May - Cape Town Virtual'
        , 'thandohDBN2022 - 4 April - Phokeng Physical - seat 3'
        , 'zaneleJHB2022 - 2 May - Durban Virtual'
        , 'ntobekoDBN2022 - 4 April - Phokeng Physical - seat 2'
        , 'BusiJHB2022 - 2 May - Durban Virtual'
        , 'zinhlehDBN2022 - 4 April - Phokeng Physical - seat 1'
        , 'CebiJHB2022 - 2 May - Durban Virtual'
        , 'lukhona - 4 April - Phokeng Virtual'
        , 'ddhaalJHB2022 - 2 May - Durban Physical - seat 4',
    'gabiDBN2022 - 4 April - Phokeng Virtual', 'ngakithilJHB2022 - 2 May - Durban Physical - seat 5',
    'zimthembilehDBN2022 - 4 April - Phokeng Virtual', 'ngakuyelJHB2022 - 2 May - Durban Physical - seat 2',
    'zimlindilehDBN2022 - 4 April - Phokeng Virtual', 'yenzileJHB2022 - 2 May - Durban Physical - seat 3',
    'zimthandilehDBN2022 - 4 April - Johannesburg Virtual','kuhlengaweDBN2022 - 4 April - Durban Physical - seat 1',
    'zimkhonzileDBN2022 - 4 April - Johannesburg Virtual','hlelokuhlehDBN2022 - 4 April - Durban Physical - seat 3',
    'zizonkehDBN2022 - 4 April - Johannesburg Virtual','sibusisohDBN2022 - 4 April - Durban Physical - seat 2',
    'kholekileDBN2022 - 4 April - Johannesburg Virtual','vusiDBN2022 - 4 April - Durban Physical - seat 9',
    'kholelwahDBN2022 - 4 April - Johannesburg Virtual','zuzumuzihDBN2022 - 4 April - Durban Physical - seat 10',
    'thembelahDBN2022 - 4 April - Johannesburg Virtual','babazileDBN2022 - 4 April - Durban Physical - seat 11',
    'thembisileDBN2022 - 4 April - Johannesburg Virtual','owenkosiDBN2022 - 4 April - Durban Physical - seat 8',
    'thembisiweDBN2022 - 4 April - Johannesburg Physical - seat 5', 'nobuhleJHB2022 - 2 May - Cape Town physical',
    'thenjisiweDBN2022 - 4 April - Johannesburg Physical - seat 6', 'nonkonzoJHB2022 - 2 May - Cape Town Physical',
    'thethelelileDBN2022 - 4 April - Johannesburg Physical - seat 7', 'nombusoJHB2022 - 2 May - Cape Town Virtual',
    'thembiDBN2022 - 4 April - Johannesburg Physical - seat 4', 'nozizweJHB2022 - 2 May - Cape Town Virtual']


def dbn_campus_students(student_list):
    '''
    from the list of students above, fill in this function to return a list of all
    students in the Durban campus only.
    '''
    dbn_students = []

    for x in student_list:
        if "Durban" in x :
            dbn_students.append(x)
       
    return dbn_students

#print(dbn_campus_students(student_list()))


def cpt_campus_students(student_list):
    '''
    from the list of students above, fill in this function to return a list of all
    students in the Cape Town campus only.
    '''
    cpt_students = []

    for x in student_list:
        if "Cape Town" in x :
            cpt_students.append(x)


    return cpt_students

# print(cpt_campus_students(student_list()))

 
def jhb_campus_students(student_list):
    '''
    from the list of students above, fill in this function to return a list of all
    students in the Johannesburg campus only.
    '''
    jhb_students = []

    for x in student_list:
        if "Johannesburg" in x :
            jhb_students.append(x)

    return jhb_students

# print(jhb_campus_students(student_list()))


def nw_campus_students(student_list):
    '''
    from the list of students above, fill in this function to return a list of all
    students in the North West campus only.
    '''
    nw_students = []
    
    for x in student_list:
        if "Phokeng" in x:
            nw_students.append(x)

    return nw_students

#print(nw_campus_students(student_list()))


def dbn_physical_students(dbn_campus_students):
    '''
    from the list of dbn_campus_students, fill in this function to return a list of all
    students who will be attending physically on campus
    '''
    
    dbn_physical = []

    for x in dbn_campus_students:
        if "Durban Physical" in x:
            dbn_physical.append(x)

    return dbn_physical

#print(dbn_physical_students(dbn_campus_students(student_list())))

def dbn_physical_teams(dbn_physical_students):
    '''
    from the list of dbn_physical_students create list of 4 students per team, and add them to 
    one big list
    '''
    split_lists = [dbn_physical_students[x:x+4] for x in range(0, len(dbn_physical_students), 4)]

    return split_lists

# print(dbn_physical_teams(dbn_physical_students(dbn_campus_students(student_list()))))

def dbn_teams_file(durban_physical_teams):
    '''
    write and save the information in the dbn_physical_teams into a textfile
    '''
    file = open('dbn_teams.txt', 'w')
    file.writelines(durban_physical_teams)
    

def cpt_physical_students(cpt_campus_students):
    '''
    from the list of cpt_campus_students, fill in this function to return a list of all
    students who will be attending physically on campus
    '''
    cpt_physical = []

    for x in cpt_campus_students:
        if "Cape Town Physical" in x:
            cpt_physical.append(x)
    
    return cpt_physical

# print(cpt_physical_students(cpt_campus_students(student_list())))
def cpt_physical_teams(cpt_physical_students):
    '''
    from the list of cpt_physical_students create list of 4 students per team, and add them to 
    one big list
    '''
    split_lists = [cpt_physical_students[x:x+4] for x in range(0, len(cpt_physical_students), 4)]
    return split_lists

# print(cpt_physical_teams(cpt_physical_students(student_list())))
def cpt_teams_file(capetown_final_teams):
    '''
    write and save the information in the cpt_physical_teams into a textfile
    '''


def jhb_physical_students(jhb_campus_students):
    '''
    from the list of jhb_campus_students, fill in this function to return a list of all
    students who will be attending physically on campus
    '''
    jhb_physical = []

    for x in jhb_campus_students:
        if "Johannesburg Physical" in x:
            jhb_physical.append(x)

    return jhb_physical

# print(jhb_physical_students(jhb_campus_students(student_list())))
def jhb_physical_teams(jhb_physical_students):
    '''
    from the list of jhb_physical_students create list of 4 students per team, and add them to 
    one big list
    '''
    split_lists = [jhb_physical_students[x:x+4] for x in range(0, len(jhb_physical_students), 4)]
    return split_lists

# print(jhb_physical_teams(jhb_campus_students(student_list())))
def jhb_teams_file(jhb_final_teams):
    '''
    write and save the information in the jhb_physical_teams into a textfile
    '''
    


def nw_physical_students(nw_campus_students):
    '''
    from the list of nw_campus_students, fill in this function to return a list of all
    students who will be attending physically on campus
    '''
    nw_physical = []

    for x in nw_campus_students:
        if "Phokeng Physical" in x:
            nw_physical.append(x)

    return nw_physical

# print(nw_physical_students(nw_campus_students(student_list())))
def nw_physical_teams(nw_physical_students):
    '''
    from the list of nw_physical_students, create list of 4 students per team, and add them to 
    one big list
    '''
    split_lists = [nw_physical_students[x:x+4] for x in range(0, len(nw_physical_students), 4)]
    return split_lists


# print(nw_physical_teams(nw_campus_students(student_list())))
def nw_teams_file(nw_final_teams):
    '''
    write and save the information in the nw_physical_teams into a textfile
    '''


def get_virtual_students(student_list):
    '''
    from the list of students above, fill in this function to return a list of all
    students attending virtually.
    '''
    virtual_campus = []

    for x in student_list:
        if "Virtual" in x :
            virtual_campus.append(x)

    return virtual_campus

# print(get_virtual_students(student_list()))

def virtual_teams(get_virtual_students):
    '''
    from the list of virtual_students above,  create list of 4 students per team, and add them to 
        one big list
    '''
    split_lists = [get_virtual_students[x:x+4] for x in range(0, len(get_virtual_students), 4)]
    return split_lists

# print(virtual_teams(get_virtual_students(student_list())))
def virtual_teams_file(virtual_teams):
    '''
    write and save the information in the virtual_teams into a textfile
    '''


if __name__ == '__main__':
    '''
    call all your functions below to make your program execute    
    '''
    dbn_campus_students(student_list())
    cpt_campus_students(student_list())
    jhb_campus_students(student_list())
    nw_campus_students(student_list())
    dbn_physical_students(dbn_campus_students(student_list()))
    dbn_physical_teams(dbn_physical_students(dbn_campus_students(student_list())))
    cpt_physical_students(cpt_campus_students(student_list()))
    cpt_physical_teams(cpt_physical_students(student_list()))
    jhb_physical_students(jhb_campus_students(student_list()))
    jhb_physical_teams(jhb_campus_students(student_list()))
    nw_physical_students(nw_campus_students(student_list()))
    nw_physical_teams(nw_campus_students(student_list()))
    get_virtual_students(student_list())
    virtual_teams(get_virtual_students(student_list()))
    pass

